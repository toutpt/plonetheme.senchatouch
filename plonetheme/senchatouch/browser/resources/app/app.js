Ext.regApplication({
    name: 'plone',
    launch: function() {
        console.log('launch');
        this.views.viewport = new plone.views.Viewport();
    }
});