plone.controllers.contents = new Ext.Controller({
    index: function(options) {
    },
    show: function(options) {
       var id = parseInt(options.id),
        content = plone.stores.contents.getById(id);
      console.log(id);
      if (content) {
          console.log('content');
          plone.views.contentDetail.updateWithRecord(content);
          plone.views.viewport.setActiveItem(
              plone.views.contentDetail, options.animation
          );
      }
    },
    edit: function(options) {
    }
});