import json
from Products.Five import BrowserView
from Products.CMFCore.utils import getToolByName
from zope import component
from plonetheme.senchatouch import logger
from plone.app.layout.globals.interfaces import IViewView

class ContentJSON(BrowserView):
    """Search browserview used as proxy for model/Content"""
    
    def __init__(self, context, request):
        self.context = context
        self.request = request
    
    def __call__(self):
        catalog = getToolByName(self.context, 'portal_catalog')
        brains = catalog()
        res = []
        for brain in brains:
            ob = brain.getObject()
            try:
                view = component.getMultiAdapter((ob, self.request),name='senchatouch.html')
            except component.ComponentLookupError, e:
                logger.error('no senchatouch.html view for %s'%ob)
                continue
            try:
                html = view()
            except Exception, e:
                logger.error('rendering fails %s'%ob)
                continue
            bd = {'id':brain.UID,
                  'title':brain.Title,
                  'description':brain.Description,
                  'url':brain.getURL(),
                  'htmlcontent':html}
            res.append(bd)
        return json.dumps({'content':res})

class Document(BrowserView):
    """SenchaTouch html view for Document"""

    def __init__(self, context, request):
        self.context = context
        self.request = request

class Topic(BrowserView):
    """SenchaTouch html view for Topic"""


class Folder(BrowserView):
    """SenchaTouch html view for Folder"""

