import os
import re
import random
from pathlib import Path
from flask import Flask
from flask import render_template, url_for, redirect
import markdown2

app = Flask(__name__)
CONTENT_DIR = Path('content')
STATIC_DIR = 'static/'

lang = 'en'

contents = {}

for md in CONTENT_DIR.glob('*'):
    with md.open() as f:
        contents[md.name] = markdown2.markdown(f.read())

def not_found():
    return '<h1>This page does not exist</h1>', 404

def get_quote(lang):
    quotes = STATIC_DIR + 'quotes_%s.txt' % lang

    if not os.path.isfile(quotes):
        quotes = STATIC_DIR + 'quotes_en.txt'

    with open(quotes, 'r') as f:
        quotes = f.read()
        quotes = quotes.splitlines()

        quote = quotes[random.randrange(0, len(quotes)-1)]

        m = re.search('^(.+)(\.|!|\?) ((\d )?\w+ (\(.*\))?\d+:\d+)$', quote)

        return m.group(1), m.group(3)

@app.route('/')
def index():
    quote, author = get_quote(lang)
    index = 'index_%s.html' % lang

    return render_template(index, quote=quote, author=author)

@app.route('/<page>')
def page(page):
    md = '%s_%s.md' % (page, lang)

    if md in contents:
        body = contents[md]

        html = 'page_%s.html' % lang

        return render_template(html, body=body, page=page.capitalize())
    else:
        return not_found()

if __name__ == '__main__':
    app.run(host='0.0.0.0')
