import json
from Products.Five import BrowserView
from plonetheme.senchatouch import logger

from zope import component
from zope import interface
from Acquisition import aq_inner
from Products.CMFCore.utils import getToolByName

class SenchaTouch(BrowserView):
    """SenchaTouch view for every content is the same"""
    def __init__(self, context, request):
        self.context = context
        self.request = request
    
    def apply_to_context(self):
        return True
    
    def title(self):
        #TODO: return the site tit
        return self.portal_state.portal_title()

    @property
    def portal_state(self):
        portal_state = component.getMultiAdapter((self.context, self.request),
                                                 name=u"plone_portal_state")
        return portal_state
    
    def portal_url(self):
        return self.portal_state.portal_url()

RESPONSE = {'site':{'title':'Plone on Sencha Touch',
                    'description':'A demo Plone web site on sencha touch framework',
                    'url':'http://mobile.makina-corpus.org',
                    'logo':'http://plone.org/logo.png'},
            'app':{'tabletStartupScreen':'tablet_startup.png',
                   'phoneStartupScreen':'phone_startup.png',
                   'icon':'icon.png',
                   'glossOnIcon':False},
            'sections':[{}],
            'content':{}}

class PloneSiteRoot(BrowserView):
    """A base default view returning json content formated for the sencha
    touch app"""
    def __init__(self, context, request):
        self.context = context
        self.request = request
    
    def __call__(self):
        self.request.response.setHeader("Content-type", "text/javascript")
        response = RESPONSE.copy()
        self.update(response)
        js = "plonemobile = "+json.dumps(response)+';'
        logger.info(js)
        return js
    
    def title(self):
        return self.context.Title()

    def update(self, response):
        self.update_site(response)
        self.update_app(response)
        self.update_sections(response)
        self.update_content(response)

    def update_site(self, response):
        portal_state = self.portal_state
        response['site']['title'] = portal_state.portal_title()
        response['site']['description'] = 'My site title'
        response['site']['url'] = portal_state.portal_url()
        response['site']['logo'] = 'My site title'
        response['site']['language'] = portal_state.language()

    def update_app(self, response):
        #TODO: use plone.app.registry to make this configurable per site
        pass
    
    def update_sections(self, response):
        context = aq_inner(self.context)
        portal_tabs_view = component.getMultiAdapter((context, self.request),
                                           name='portal_tabs_view')
        tabs = portal_tabs_view.topLevelTabs()
        sections = response['sections']
        for tab in tabs:
            sections.append({'id':tab['id'],
                         'title':tab['name'],
                         'description':tab['description'],
                         'url':tab['url']})

    def update_content(self, response):
        response['content']['title'] = self.context.Title()
        response['content']['content'] = "<h1>Hello world</h1>"

    @property
    def portal_state(self):
        portal_state = component.getMultiAdapter((self.context, self.request),
                                                 name=u"plone_portal_state")
        return portal_state

class ATDocument(PloneSiteRoot):
    """A base default view returning json content formated for the sencha
    touch app"""
