#!/usr/bin/env python
# coding: utf-8

import sys

selector = "p" #@param {type:"string"}

url = sys.argv[1]

from requests_html import HTMLSession
session = HTMLSession()
with session.get(url) as r:
    paragraph = r.html.find(selector, first=False)
    text = " ".join([ p.text for p in paragraph])

from pipelines import pipeline
nlp = pipeline("multitask-qa-qg")

faqs = nlp(text)


print(faqs)
