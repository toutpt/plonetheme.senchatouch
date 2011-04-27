var panel;
Ext.setup({
    tabletStartupScreen: plonemobile['app']['tabletStartupScreen'],
    phoneStartupScreen: plonemobile['app']['phoneStartupScreen'],
    icon: plonemobile['app']['icon'],
    glossOnIcon: plonemobile['app']['glossOnIcon'],
    onReady: function() {

    /*
     * Define the global panel
     */
    panel = new Ext.Panel({
        fullscreen: true,
    });
    /*
     * Define first title panel
     */
    var header = new Ext.Panel({});
    var titleBar = new Ext.Toolbar({
        dock : 'top',
        title : plonemobile['site']['title'],
        items:[]
    });
    header.addDocked(titleBar);

    var content = new Ext.Panel({
      title:'Content',
      scroll: 'vertical',
      tpl: [
                '<tpl for=".">',
                '<div class="#contentitem">',
                '<h1>{title}</h1>',
                '{content}',
                '</div>',
                '</tpl>'
            ]
    });
    /*
     * Define Footer
     */
    var tabHandler = function(b, e){
      alert('test');
    };
    var footer = new Ext.TabPanel({
        dock:'bottom',
        cardSwitchAnimation: 'slide',
        defaults: {
            cls: 'card card3',
            iconCls: 'section',
        },
        items: [
        {
            title: 'Section 1',
            html:'<h1>toto</h1><h2>titi</h2><p>ttt</p><p>toto</p>'
        },{
            title: 'Section 2'
        },{
            title: 'Section 3'
        },{
            iconCls: 'more',
            title: 'More',
            html: 'more sections'
        },{
            iconCls: 'info',
            title: 'About',
            html: 'Pressed Info'
        }, {
            iconCls: 'team',
            title: 'Contact',
            html: 'Pressed Team'
        }, {
            iconCls: 'search',
            title: 'Search',
            html: 'Search'
        }],
        tabBar: {
            dock: 'bottom', //change the way buttons are rendered
            scroll: {
                direction: 'horizontal',
                useIndicators: false
            },
            layout: {
                pack: 'center'
            }
        }
    });
    panel.addDocked(header);
    panel.addDocked(content);
    panel.addDocked(footer);
    panel.doComponentLayout();
    content.update(plonemobile['content'])
}
});