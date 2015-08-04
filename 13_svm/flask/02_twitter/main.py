"""Flask demo"""
from flask import Flask, render_template, request
import twitter
import json
from twitter_config import TWITTER_KEYS

# Init Flas app and Twitter api
app = Flask(__name__)
auth = twitter.oauth.OAuth(**TWITTER_KEYS)
twitter_api = twitter.Twitter(auth=auth, secure=True)


@app.route('/')
def index():
    return render_template('/index.html')


@app.route('/show', methods=['GET', 'POST'])
def show_tweets():
    user = request.form['screen_name'].encode('ascii', 'ignore').lower().strip()
    try:
        print "Calling Twitter, user:", user  # log to console
        raw_tweets = twitter_api.statuses.user_timeline(screen_name=user)
    except twitter.TwitterHTTPError as e:
        response_data = json.loads(e.response_data)
        print response_data  # log to console
        tweets = [response_data]  # print message on webpage as well (this is ugly)
    else:
        # Never a bad idea to save your data - you're a data scientist after all!
        with open('tweets/%s.json' % user, 'w') as f:
            json.dump(raw_tweets, f, indent=2)

        # parse raw tweets into something you want to display
        tweets = [
            tweet.get('user', {}).get('name', 'Unknown tweeter') + ': ' +
            tweet.get('text', '(no text)')
            for tweet in raw_tweets]

    return render_template('/index.html', tweets=tweets)


if __name__ == '__main__':
    app.run(debug=True)
    # app.run(host='0.0.0.0', debug=False)  # Never have debug = True when hosting a public website!
