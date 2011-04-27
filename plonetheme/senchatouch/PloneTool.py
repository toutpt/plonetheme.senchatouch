from collective.monkeypatcher import meta
from zope import component
from zope import interface
from plonetheme.senchatouch import interfaces
from plonetheme.senchatouch import logger
from plone.app.layout.globals.interfaces import IViewView

def browserDefault(self, obj):
    """We monkey patch this method. We want to control html rendering
    throw @@senchatouch view"""
    request = getattr(self, 'REQUEST', None)

    if interfaces.IBrowserLayer.providedBy(request):
        if obj.isPrincipiaFolderish:
            defaultPage = self.getDefaultPage(obj)
            if defaultPage is not None:
                logger.info('apply original browserDefault with defaultpage')
                return self._old_browserDefault(obj)

        try:
            view = component.getMultiAdapter((obj, request), name='senchatouch')
            if view.apply_to_context():
                logger.info('apply senchatouch view')
                return obj, ['@@senchatouch']
        except component.ComponentLookupError, e:
            logger.info('can t find senchatouch view on %s'%obj)
        except AttributeError, e:
            logger.info('attribute error on view %s for %s. trace: %s'%(view, obj,e))

    logger.info('apply original browserDefault')
    return self._old_browserDefault(obj)
