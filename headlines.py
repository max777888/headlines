import feedparser
from flask import Flask
from flask import render_template

app = Flask(__name__)
BBC_FEED = "http://feeds.bbci.co.uk/news/rss.xml"
CNN_FEED = "http://rss.cnn.com/rss/edition_world.rss"

RSS_FEEDS = {'bbc': 'http://feeds.bbci.co.uk/news/rss.xml',
'cnn': 'http://rss.cnn.com/rss/edition.rss',
'fox': 'http://feeds.foxnews.com/foxnews/latest',
'iol': 'http://www.iol.co.za/cmlink/1.640',
'TechCrunch': 'https://techcrunch.com/rssfeeds'}

@app.route("/")

@app.route("/<publication>")


def get_news(publication="bbc"):
  feed = feedparser.parse(RSS_FEEDS[publication])
  first_article = feed['entries'][0]
  #return render_template("home.html",
  #        title=first_article.get("title"),
  #        published=first_article.get("published"),
  #        summary=first_article.get("summary"))
  return render_template("home.html", articles=feed['entries'])

if __name__ == "__main__":
  app.run(host='0.0.0.0', threaded=True, port=5000)