# imports
from bs4 import BeautifulSoup
import requests
import json
import unicodedata
import flask import Flask, jsonify

app = Flask(__name__)




@app.route('/', methods=['GET'])
def home():
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
  
  return jsonify(database)
