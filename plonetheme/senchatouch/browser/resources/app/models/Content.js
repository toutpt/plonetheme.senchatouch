plone.models.Content = Ext.regModel("plone.models.Content", {
    fields: [
             {name: "title", type: "string"},
             {name: "id", type: "string"},
        {name: "description", type: "string"},
        {name: "url", type: "string"}
    ]
});
plone.stores.contents = new Ext.data.Store({
    model: "plone.models.Content",
    proxy: {
      type: 'ajax',
      url: 'sencha.model.content.json',
      reader: {
        type:'json',
        root:'content'
      }
    }
});