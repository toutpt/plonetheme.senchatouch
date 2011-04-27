plone.views.ContentDetail = Ext.extend(Ext.Panel, {
    dockedItems: [{
        xtype: 'toolbar',
        title: 'View content',
        items: [
            {
                text: 'Back',
                ui: 'back',
                listeners: {
                    'tap': function () {
                        //Ext.dispatch({
                        //    controller: app.controllers.contacts,
                        //    action: 'index',
                        //    animation: {type:'slide', direction:'right'}
                        //});
                    }
                }
            },
            {xtype:'spacer'},
            {
                id: 'edit',
                text: 'Edit',
                ui: 'action',
                listeners: {
                    'tap': function () {
                        //Ext.dispatch({
                        //    controller: app.controllers.contacts,
                        //    action: 'edit',
                        //    id: this.record.getId()
                        //});
                    }
                }
            }
        ]
    }],
    updateWithRecord: function(record) {
      var toolbar = this.getDockedItems()[0];
      toolbar.setTitle(record.get('title'));
      toolbar.getComponent('edit').record = record;
    },
    styleHtmlContent:true,
    scroll: 'vertical',
    items: []
});