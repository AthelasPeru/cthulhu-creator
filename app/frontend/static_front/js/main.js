

var CharView = function(data){
	var self = this;
	self.ruleset;

	

	// Request
	var jqxhr = $.getJSON('/api/v1.0/creator/rules/6.0', function(data) {
					self.ruleset = data;
					console.log('the variable "ruleset" is done.');
				});
	 
	// Set a completion function for the request above
	jqxhr.complete(function() {
		self.setBindings(self.ruleset);
		ko.applyBindings(self.ruleset);
	});




	//Setting bindings
	self.setBindings = function(ruleset){
			
		}

};



















$(document).ready(function($) {
	new CharView();
});