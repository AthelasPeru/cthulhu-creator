function CharCreationView() {
	var self = this;
	
	// Configuration Variables
	self.template = 'create.html';
	self.screens = [
		'initial-screen', 
		'core-rolls-screen', 
		'occupation-screen', 
		'occupational-screen', 
		'hobby-screen', 
		'investigator-data-screen'
	];

	// Main Rules object with all the data we need to create the char
	
	self.ruleset = getRules('/api/v1.0/creator/rules/6.0');
	console.dir(self.ruleset);
	// Main Methods

	// Main Utilities
	self.goBack = function(){};
	self.saveState = function(){};
	self.rollDices = function(){};


	self.getRules = function(url){
		$.getJSON(url, function(data) {
			var parsedData = JSON.parse(data);
			return ko.mapping.fromJS(parsedData);;
		}

	};
	self.finalSave = function(finalCharData){
		$.post("/some/url", finalCharData, function(returnedData) {
		    console.log('everything went well?');  
		})
	};
		



}; // End of CharCreationView

//Apply Bindings for Knockout to Work
window.onload = function(){	
	ko.applyBindings(new CharCreationView());
};


