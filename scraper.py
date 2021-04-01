# imports
from bs4 import BeautifulSoup
import requests
import json
import unicodedata
import flask

res = requests.get('https://quotes.toscrape.com/tag/life')

soup = BeautifulSoup(res.content, 'html.parser')
quotes = soup.find_all("div", class_ = "quote")

myQuotes = []
entry = {}
database = []

for quote in quotes:
  author = quote.select('small.author')[0].text
  text = quote.select('span.text')[0].text
  entry['author']=unicodedata.normalize('NFKD', author).encode('ascii', 'ignore').decode('utf-8')
  entry['quote']=unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('utf-8')
  database.append(entry)
  entry = {}

with open('database.json','w', encoding='utf8') as f:
  json.dump(database,f)

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return jsonify(str(database))

app.run()
