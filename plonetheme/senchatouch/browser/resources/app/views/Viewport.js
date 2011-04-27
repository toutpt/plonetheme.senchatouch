plone.views.Viewport = Ext.extend(Ext.Panel, {
    fullscreen: true,
    layout: 'card',
    cardSwitchAnimation: 'slide',
    initComponent: function() {
        //put instances of cards into app.views namespace
        Ext.apply(plone.views, {
            contentList: new plone.views.ContentList(),
            contentDetail: new plone.views.ContentDetail()
            //contactForm: new app.views.ContactForm()
        });
        //put instances of cards into viewport
        Ext.apply(this, {
            items: [
                plone.views.contentList,
                //app.views.contactsList,
                plone.views.ContentDetail
                //app.views.contactForm,
            ]
        });
        plone.views.Viewport.superclass.initComponent.apply(this, arguments);
    }
});