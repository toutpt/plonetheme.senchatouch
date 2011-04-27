from plone.browserlayer import layer as base
from zope import component
from zope import interface
from plone.registry.interfaces import IRegistry
from plonetheme.senchatouch import logger
from plonetheme.senchatouch import interfaces

def mark_layer(site, event):
    base.mark_layer(site, event)
    request = event.request
    registry = component.getUtility(IRegistry)
    settings = registry.forInterface(interfaces.IThemeSettings)
    if request.get('BASE1') == settings.domain:
        ifaces = [interfaces.IBrowserLayer] + list(interface.directlyProvidedBy(request))
        interface.directlyProvides(request, *ifaces)
