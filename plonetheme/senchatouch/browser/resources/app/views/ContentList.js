plone.views.ContentList = Ext.extend(Ext.Panel, {
    dockedItems: [{
        xtype: 'toolbar',
        title: 'Content'
    }],
    items: [{
        xtype: 'list',
        store: plone.stores.contents,
        itemTpl: '{title} {id}',
        onItemDisclosure: function (record) {
            Ext.dispatch({
                controller: plone.controllers.contents,
                action: 'show',
                id: record.getId()
            });
        }
    }],
    initComponent: function() {
        plone.stores.contents.load();
        plone.views.ContentList.superclass.initComponent.apply(this, arguments);
    }
});