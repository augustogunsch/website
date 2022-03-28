import os
import re
import random
from flask import Flask
from flask import render_template, url_for, redirect
import markdown2

app = Flask(__name__)
CONTENT_DIR = 'content/'
STATIC_DIR = 'static/'

def not_found():
    return '<h1>This page does not exist</h1>', 404

def read_md(fname):
    with open(fname, 'r') as f:
        return markdown2.markdown(f.read())

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
    return redirect(url_for('index_lang', lang='en'))

@app.route('/<lang>')
def index_lang(lang):
    md = CONTENT_DIR + 'index_%s.md' % lang

    if os.path.isfile(md):
        body = read_md(md)
        quote, author = get_quote(lang)

        return render_template('index.html', body=body, quote=quote, author=author)
    else:
        return not_found()

@app.route('/<lang>/<page>')
def page_lang(lang, page):
    md = CONTENT_DIR + '%s_%s.md' % (page, lang)

    if os.path.isfile(md):
        body = read_md(md)

        return body
    else:
        return not_found()

if __name__ == '__main__':
    app.run(host='0.0.0.0')
