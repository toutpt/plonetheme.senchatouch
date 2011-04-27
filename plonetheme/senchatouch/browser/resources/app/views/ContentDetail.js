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
                        Ext.dispatch({
                            controller: plone.controllers.contents,
                            action: 'index',
                            animation: {type:'slide', direction:'right'}
                        });
                    }
                }
            },
            {xtype:'spacer'}
        ]
    }],
    updateWithRecord: function(record) {
    	Ext.each(this.items.items, function(item) {
            item.update(record.data);
        });
    	var toolbar = this.getDockedItems()[0];
      toolbar.setTitle(record.get('title'));
    },
    styleHtmlContent:true,
    scroll: 'vertical',
    items: [
	  {xtype:'panel',tpl:[
	      '<h4>Description</h4>',
          '<div class="field">{htmlcontent}</div>'
	  ]}
    ]
});