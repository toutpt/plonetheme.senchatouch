from plone.z3cform import layout

from plone.app.registry.browser.controlpanel import RegistryEditForm
from plone.app.registry.browser.controlpanel import ControlPanelFormWrapper

from plonetheme.senchatouch.interfaces import IThemeSettings
from plonetheme.senchatouch import i18n

class ThemeSettingsControlPanelForm(RegistryEditForm):
    schema = IThemeSettings

ThemeSettingsControlPanelView = layout.wrap_form(ThemeSettingsControlPanelForm,
                                                 ControlPanelFormWrapper)
ThemeSettingsControlPanelView.label = i18n.label_controlpanel

