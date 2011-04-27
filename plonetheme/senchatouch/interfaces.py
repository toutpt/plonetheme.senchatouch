from zope import interface
from zope import schema
from plonetheme.senchatouch import i18n

class IBrowserLayer(interface.Interface):
    """Browser layer"""

class IThemeSettings(interface.Interface):
    """Settings for jquerymobile theme"""

    domain = schema.URI(
        title=i18n.label_domain,
        description=i18n.desc_domain,
        required=False,
        )

class IMobileView(interface.Interface):
    """The view for mobile site"""

    def apply_to_context():
        """Return true if you are suppose to apply this view on the context
        
        This is the entry point for integrator wants to support other add-ons"""

