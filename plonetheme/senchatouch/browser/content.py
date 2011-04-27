import json
from Products.Five import BrowserView
from Products.CMFCore.utils import getToolByName
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
            bd = {'id':brain.UID,
                  'title':brain.Title,
                  'description':brain.Description,
                  'url':brain.getURL()}
            res.append(bd)
            self.context.plone_log(bd)
        return json.dumps({'content':res})
