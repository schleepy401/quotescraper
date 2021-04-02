# quotescraper: A basic web scraper API

## Features
- **Language:** [Python 3.8.5](https://docs.python.org/3.8/)
- **Technologies used:**
  - [BeautifulSoup 4](https://pypi.org/project/beautifulsoup4/)
  - [Flask 1.1.2](https://flask.palletsprojects.com/en/1.1.x/)
- **Website being scraped:** [Quotes To Scrape](https://quotes.toscrape.com)
- **API is live at** [this link](https://w0lfw1tz.herokuapp.com)
- The data is returned in JSON format. Feel free to use this in your apps or projects.

## Using the API
- Just call the link [https://w0lfw1tz.herokuapp.com](https://w0lfw1tz.herokuapp.com). The data is returned in a JSON array format like this:
```
[
  {
      "author": <String>,
      "quote": <String>
  },
  {
      "author": <String>,
      "quote": <String>
  }, ...  
]
```
- **Datapoints:**
  - Every element/index of the JSON array contains a JSON file of the following format:
  ```
    {
      "author": <String>,
      "quote": <String>
    }
  ```
  - The ```author``` key returns the name of the author of the quote. The returned data is in string format.
  - The ```quote``` key returns the writing. The returned data is in string format.

## Changelog
- **Version 1.0:**
  - *Date of release:* 2nd April, 2021
  - First version of Quotes API.
  - <span style="color:red">some *Bugs with the current version: * text.</span>
    - The data isn't updated since the source of data being scraped is static currently.
    - Some special characters (such as é etc.) are not supported due to being interconverted between Unicode UTF8 and ASCII for being supported even somewhat properly by the textIOwrapper class which converts the raw html strings into proper JSON.
## Contributors
- [Tanmoy Sarkar](https://github.com/tanmoyio) for helping me with debugging and basic python skills irl

## Acknowledgments
- Documentations of the above linked technologies for being my source of learning.
- My friends for shamelessly having my back.
