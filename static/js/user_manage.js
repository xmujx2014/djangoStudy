(function($){
	$(document).ready(function(){
		var AddUserView = Backbone.View.extend({
			el: $("div.main"),
			initialize:function(){
				_.bindAll(this, 'render')
				this.render();
			},
			render: function(){
				$(this.el).append($.tpl['add_person']())
			}
		});

		var indexView = new AddUserView();
	})
})(jQuery);