    # -*- coding: utf-8 -*-

import logging
from Acquisition import aq_inner
from zope.component import getMultiAdapter
from zope.i18nmessageid import MessageFactory
from Products.Five import BrowserView
from zope.component import getUtility

import lxml.html
from lxml.cssselect import CSSSelector

import requests

class Scrape(BrowserView):
    """   lxml    """

        
    @property
    def scraped(self):
        r = requests.get('https://www.bergen.kommune.no/omkommunen/avdelinger/bergenhus-og-arstad-kulturkontor/9353')
        tree = lxml.html.fromstring(r.text)

        #the parsed DOM Tree
        lxml.html.tostring(tree)

        # construct a CSS Selector
        sel = CSSSelector('#rg7726')
        
        # Apply the selector to the DOM tree.
        results = sel(tree)
        
        # the HTML for the first result.
        match = results[0]
        return lxml.html.tostring(match)

        # get the href attribute of the first result
        #print match.get('href')

        # print the text of the first result.
        #print match.text

        # get the text out of all the results
        #return [result.text for result in results]