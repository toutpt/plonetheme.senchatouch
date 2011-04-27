from zope import interface
from plone.memoize.instance import memoize
from plonetheme.senchatouch import interfaces

def getDefaultSkin(self):
    request = self.REQUEST #better way ?

    if interfaces.IBrowserLayer.providedBy(request):
        return 'Sencha Touch Theme'

    return self.default_skin
