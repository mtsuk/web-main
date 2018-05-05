# -*- encoding: utf-8 -*-

import hashlib
from datetime import datetime

from flask import render_template, redirect, url_for

from emoji import app

@app.route('/')
def home():
    return redirect('https://emoji-gen.ninja', code=301)

@app.route('/sitemap.xml')
def sitemap_xml():
    return redirect(url_for('static', filename='sitemap.xml'))
