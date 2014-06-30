# -*- coding: utf-8 -*-

#import logging
from Acquisition import aq_inner
from zope.i18nmessageid import MessageFactory
from Products.Five import BrowserView

from plone import api
from medialog.mobilethemeTwo.interfaces import IMobilethemeTwoSettings

import lxml.html
from lxml.cssselect import CSSSelector

import requests

class Scrape(BrowserView):
    """   lxml    """
    
    def repl(html, link):
        selector = api.portal.get_registry_record('medialog.mobilethemeTwo.interfaces.IMobilethemeTwoSettings.scrape_selector')
        scrape_external_base_url = api.portal.get_registry_record('medialog.mobilethemeTwo.interfaces.IMobilethemeTwoSettings.scrape_base_url')
        
        root_url = api.portal.get().absolute_url()

        if (not (link.startswith('http'))):
            link = scrape_external_base_url + link
        if link.endswith('.jpg') or link.endswith('.png') or link.endswith('.gif') or link.endswith('.jpeg') or link.endswith('.pdf'):
            return link
        link =   root_url + '/scrape?url=' + link
        

        return link
        
    @property
    def scraped(self):
        #get settings from control panel
        selector = api.portal.get_registry_record('medialog.mobilethemeTwo.interfaces.IMobilethemeTwoSettings.scrape_selector')
        scrape_external_base_url = api.portal.get_registry_record('medialog.mobilethemeTwo.interfaces.IMobilethemeTwoSettings.scrape_base_url')
        
        url=scrape_external_base_url
        if hasattr(self.request, 'url'):
            url = self.request.url
        
        #get html from the requested url
        r = requests.get(url)
        tree = lxml.html.fromstring(r.text)
        
        #the parsed DOM Tree
        lxml.html.tostring(tree)

        # construct a CSS Selector
        sel = CSSSelector(selector)
        
        # Apply the selector to the DOM tree.
        results = sel(tree)
        
        # the HTML for the first result.
        if results:
            match = results[0]
            #relink
            match.rewrite_links(self.repl)
        
            return lxml.html.tostring(match)
        return "Content can not be shown"
        