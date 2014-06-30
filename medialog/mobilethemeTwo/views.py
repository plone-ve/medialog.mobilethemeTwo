# -*- coding: utf-8 -*-

import logging
from Acquisition import aq_inner
from zope.component import getMultiAdapter
from zope.i18nmessageid import MessageFactory
from Products.Five import BrowserView
from zope.component import getUtility
from plone.registry.interfaces import IRegistry
from medialog.mobilethemeTwo.interfaces import IMobilethemeTwoSettings
import lxml.html
from lxml.cssselect import CSSSelector

import requests

class Scrape(BrowserView):
    """   lxml    """
    
    
    def repl(html, link):

        settings = getUtility(IRegistry).forInterface(IMobilethemeTwoSettings)
        selector = settings.scrape_selector
        scrape_external_base_url = settings.scrape_base_url
        scrape_url = settings.scrape_url

        if link.startswith(scrape_external_base_url):
            link =   'scrape?url=' + link
            return link
        if link.startswith('/'):
            link = scrape_url + link
            return link
        return link
        
    @property
    def scraped(self):
        url = self.request.url
        #finally:
        #   return "Error No URL included"
        
        
        settings = getUtility(IRegistry).forInterface(IMobilethemeTwoSettings)
        selector = str(settings.scrape_selector)
        scrape_external_base_url = str(settings.scrape_base_url)
        
        r = requests.get(url)
        tree = lxml.html.fromstring(r.text)
        
        tree.make_links_absolute(base_url=scrape_external_base_url, resolve_base_href=True)
        tree.rewrite_links(self.repl)
        
        #the parsed DOM Tree
        lxml.html.tostring(tree)

        # construct a CSS Selector
        sel = CSSSelector(selector)
        
        # Apply the selector to the DOM tree.
        results = sel(tree)
        
        # the HTML for the first result.
        match = results[0]
        return lxml.html.tostring(match)

        