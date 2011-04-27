plone.controllers.contents = new Ext.Controller({
    index: function(options) {
		plone.views.viewport.setActiveItem(
		        plone.views.contentList, options.animation
		    );
    },
    show: function(options) {
      var id = options.id,
        content = plone.stores.contents.getById(id);
      console.log(options.id);
      if (content) {
          plone.views.contentDetail.updateWithRecord(content);
          plone.views.viewport.setActiveItem(
              plone.views.contentDetail, options.animation
          );
      }
    },
    edit: function(options) {
    }
});