#!/usr/bin/env python
"""
Monitor the Twitter stream API for certain key words

General Assembly Data Science
"""
import sys
import oauth2 as woof
import json
import urllib2 as urllib

from twitter_config import ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET


DEFAULT_KEYWORDS = "trump"
API_URL = "https://stream.twitter.com/1/statuses/filter.json"


# Global variables
oauth_token    = woof.Token(key=ACCESS_TOKEN_KEY, secret=ACCESS_TOKEN_SECRET)
oauth_consumer = woof.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
signature_method_hmac_sha1 = woof.SignatureMethod_HMAC_SHA1()

http_method = "GET"
http_handler  = urllib.HTTPHandler()
https_handler = urllib.HTTPSHandler()


def twitterreq(url, method, parameters):
    """Construct, sign, and open a twitter request
    using the hard-coded credentials above."""
    req = woof.Request.from_consumer_and_token(
        oauth_consumer, token=oauth_token, http_method="GET", http_url=url, parameters=parameters)

    req.sign_request(signature_method_hmac_sha1, oauth_consumer, oauth_token)
    headers = req.to_header()

    encoded_post_data = None
    if http_method == "POST":
        encoded_post_data = req.to_postdata()

    opener = urllib.OpenerDirector()
    opener.add_handler(http_handler)
    opener.add_handler(https_handler)

    return opener.open(req.to_url(), encoded_post_data)

def fetchsamples(key_words):
    parameters = {'track' : key_words}
    response = twitterreq(API_URL, "GET", parameters)
    for line in response: #Iterating over every related to topic

        text = json.loads(line.strip())['text']
        print text

def main():
    key_words = ' '.join(sys.argv[1:])
    if not key_words:
        print "You can specify keywords on the command line, e.g.", sys.argv[0], DEFAULT_KEYWORDS
        key_words = DEFAULT_KEYWORDS
    fetchsamples(key_words)

if __name__ == '__main__':
    main()

