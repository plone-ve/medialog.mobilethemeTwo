# -*- coding: utf-8 -*-

#import logging
#from Acquisition import aq_inner
from zope.i18nmessageid import MessageFactory
from Products.Five import BrowserView

from plone import api
from medialog.mobilethemeTwo.interfaces import IMobilethemeTwoSettings

import lxml.html
from lxml.cssselect import CSSSelector
from lxml.html.clean import Cleaner



import requests

class Scrape(BrowserView):
    """   A View that uses lxml to embed external content    """
    
    def repl(html, link):
        selector = api.portal.get_registry_record('medialog.mobilethemeTwo.interfaces.IMobilethemeTwoSettings.scrape_selector')
        scrape_base_url = api.portal.get_registry_record('medialog.mobilethemeTwo.interfaces.IMobilethemeTwoSettings.scrape_base_url')
        root_url = api.portal.get().absolute_url()
        
        #if link.startswidth('/'):
        #    link = scrape_base_url + link
        
        #open pages from other sites in its own window.
        if (not (link.startswith(scrape_base_url))):
            return link
        #dont modyfy image links
        if link.endswith('.jpg') or link.endswith('.png') or link.endswith('.gif') or link.endswith('.js') or link.endswith('.jpeg') or link.endswith('.pdf'):
            return link
        #point other pages from same site to embedded view
        link =   root_url + '/scrape?url=' + link
        return link
        
    def scraped(self):
        #get settings from control panel
        selector = api.portal.get_registry_record('medialog.mobilethemeTwo.interfaces.IMobilethemeTwoSettings.scrape_selector')
        scrape_base_url = api.portal.get_registry_record('medialog.mobilethemeTwo.interfaces.IMobilethemeTwoSettings.scrape_base_url')
        
        url = api.portal.get_registry_record('medialog.mobilethemeTwo.interfaces.IMobilethemeTwoSettings.scrape_url')
        
        if hasattr(self.request, 'url'):
            parts = url.split('//', 1)
            scrape_base_url = parts[0]+'//'+parts[1].split('/', 1)[0]
        
            url = self.request.url
        
        
        #get html from the requested url
        r = requests.get(url)
        tree = lxml.html.fromstring(r.text)
        
                
        #clean evil stuff
        cleaner = Cleaner(javascript = True , style = True )
        cleaner(tree)
        
        #the parsed DOM Tree
        lxml.html.tostring(tree)

        #relink
        tree.make_links_absolute(scrape_base_url, resolve_base_href=True)
        tree.rewrite_links(self.repl)
        
        # construct a CSS Selector
        sel = CSSSelector(selector)
        
        
        # Apply the selector to the DOM tree.
        results = sel(tree)
        
        # the HTML for the first result.
        if results:
            match = results[0]
            return lxml.html.tostring(match)

        #return "Content can not be filtered, we are returning whole page"
        return lxml.html.tostring(tree)


class ScrapeView(BrowserView):
    """   A Dexterity Content View that uses lxml to embed external content    """
    
    def repl(html, link):
        selector = api.portal.get_registry_record('medialog.mobilethemeTwo.interfaces.IMobilethemeTwoSettings.scrape_selector')
        scrape_base_url = api.portal.get_registry_record('medialog.mobilethemeTwo.interfaces.IMobilethemeTwoSettings.scrape_base_url')
        root_url = api.portal.get().absolute_url()

        if link.startswidth('/'):
            link = scrape_base_url + link
            
        if (not (link.startswith(scrape_base_url))):
            return link
        if link.endswith('.jpg') or link.endswith('.png') or link.endswith('.gif') or link.endswith('.js') or link.endswith('.jpeg') or link.endswith('.pdf'):
            return link
        if link.startswidth(scrape_base_url):
            link =   root_url + '/scrape?url=' + link

        
        return link
    
    @property
    def scraped(self):
        url = str(self.context.scrape_url)
        selector = str(self.context.scrape_selector)
        #parts = url.split('//', 1)
        #scrape_base_url = str(parts[0]+'//'+parts[1].split('/', 1)[0])
        
        scrape_base_url = api.portal.get_registry_record('medialog.mobilethemeTwo.interfaces.IMobilethemeTwoSettings.scrape_base_url')
         
        #get html from the requested url
        r = requests.get(url)
        tree = lxml.html.fromstring(r.text)
        
                
        #clean evil stuff
        cleaner = Cleaner(javascript = True , style = True )
        cleaner(tree)
        
        #the parsed DOM Tree
        lxml.html.tostring(tree)

        #relink
        tree.make_links_absolute(scrape_base_url, resolve_base_href=True)
        tree.rewrite_links(self.repl)
        
        # construct a CSS Selector
        sel = CSSSelector(selector)
        
        
        # Apply the selector to the DOM tree.
        results = sel(tree)
        
        # the HTML for the first result.
        if results:
            match = results[0]
            return lxml.html.tostring(match)

        #return "Content can not be filtered, we are returning whole page"
        return lxml.html.tostring(tree)

