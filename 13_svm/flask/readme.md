# Flask Demos

Flask is a library for Python to easily set up interactive websites. In their own words, Flask is a microframework for Python based on Werkzeug, Jinja 2 and good intentions. You can deploy Flask in your commercial products for free.

They have a great [Quickstart](http://flask.pocoo.org/docs/0.10/quickstart/#quickstart) tutorial to get you up to speed in no-time.

All you need to know is Python, HTML and Jinja 2, the latter being a scripting language to include variables in your html pages which communicate with your python code. It would definitely help if you'd know CSS as well, t make your website look pretty, and JavaScript, to add some basic front-end functionality to your page.

Just to be clear, Python (and Flask) operate at the 'back-end' of your website, which runs at the server's site, and HTML, CSS and JavaScript are all interpreted by the user's browser, which runs at the client's site and which is called your website's 'front-end'. When people say 'full-stack', they mean the full stack from front-end to back-end.

A great resource to learn all these technonologies is [W3Schools](http://www.w3schools.com/), which excellent tutorials on [HTML](http://www.w3schools.com/html/), [CSS](http://www.w3schools.com/css/),
[JavaScript](http://www.w3schools.com/js/), as well as [SQL](http://www.w3schools.com/sql) and [JSON](http://www.w3schools.com/json), which are technically not about websites but are commonly used.


### Installation

To install Flask, type

  ```sh
  pip install Flask
  ```


### Hello World

The first example is [hello_world.py](./01_hello_world/hello_world.py). It's only a few lines of code:

  ```python
  from flask import Flask
  app = Flask(__name__)

  @app.route("/")
  def hello():
      return "Hello World!"

  if __name__ == "__main__":
      app.run()
  ```

This script will output the following lines to the console:

  ```sh
  $ python hello_world.py
   * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
  ```

To see your website, open your browser and go to the stated address, or to `http://localhost:5000/`.

If you'd like to host your website publically later on, you need to give the `app.run()` method the argument `host='0.0.0.0'`. (You'll need to configure a ton more settings on your system before your website is actually reachable from external machines, though.)

Please refer to the [Quickstart](http://flask.pocoo.org/docs/0.10/quickstart/#quickstart) for a step-by-step explanation of the code.


### Displaying Tweets

The second example is a [website displaying tweets](./02_twitter/main.py). Please take your time going through the different files and the lines of code.

  ```sh
  main.py  # the python code using Flask
  twitter_config.py  # your private Twitter keys (never publish these!)
  static/  # folder containing static files such as images, scripts, static html webpages, etc.
    css/  # style sheets for your website's look & feel: fonts, color schemes, layout, etc.
      style_sheet.css
    html/  # static webpages (we have none of those)
    images/
      favicon.ico  # this will be the page's icon in your browser
      twitter_logo.png  # some other image
  templates/  # your dynamic webpages (pages that depend on your python code)
    index.html  # your homepagem, using HTML and Jinja2
  tweets/  # an empty folder to store the raw tweets in
  ```



