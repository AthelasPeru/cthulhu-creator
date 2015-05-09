;   var charData = {
		charBasicStats : {
			str: "",
			con: "",
			dex: "",
			app: "",
			pow: "",
			siz: "",
			_int: "",
			edu: "",
		},
		charSpecialStats : {			
			idea: "",
			know: "",
			luck: "",
			hp: "",
			san: "",
			db: ""
		},
		charExtra: {
			baseAge: "",
			profPoints: "",
			hobbyPoints: ""
		}

	};
	// var charDataTemp = JSON.parse(charData);

	var generate = {
		rollDice: function(number){
			return Math.floor(Math.random()*6) + 1;
		},
		basicStat: function(stat){
			var total = 0;
			for (var i = 0; i < 3; i++){
				total = total + generate.rollDice(6)
			}
			charData.charBasicStats[stat] = total;
		},
		secondStat: function(stat){
			var total = 0;
			for (var i = 0; i < 2; i++){
				total = total + generate.rollDice(6)
			} 
			total += 6;
			charData.charBasicStats[stat] = total;
		},
		eduStat: function(){
			var total = 0;
			for (var i = 0; i < 3; i++){
				total = total + generate.rollDice(6)
			}
			total += 3;
			charData.charBasicStats["edu"] = total;
		},
		specialStat: function(special, stat){
			charData.charSpecialStats[special] = charData.charBasicStats[stat] * 5;
		},
		hp: function(){
			charData.charSpecialStats["hp"] = Math.ceil((charData.charBasicStats["con"] + charData.charBasicStats["siz"]) / 2);
		},
		db: function(){
			var added = charData.charBasicStats["str"] + charData.charBasicStats["siz"]
			if (2 <= added <= 12 ){
				charData.charSpecialStats["db"] = "-1D6"
			} else if (13 <= added <= 16 ){
				charData.charSpecialStats["db"] = "-1D4"
			} else if (17 <= added <= 24 ){
				charData.charSpecialStats["db"] = "0"
			} else if (25 <= added <= 32 ){
				charData.charSpecialStats["db"] = "+1D4"
			} else if (33 <= added <= 40 ){
				charData.charSpecialStats["db"] = "+1D6"
			} else if (41 <= added <= 56 ){
				charData.charSpecialStats["db"] = "+2D6"
			} else if (57 <= added <= 72 ){
				charData.charSpecialStats["db"] = "+3D6"
			} else if (73 <= added <= 88 ){
				charData.charSpecialStats["db"] = "+4D6"
			}

		},
		allStats: function(){
			var stats = ["str", "dex", "con", "pow", "app"];
			var secStats = ["siz", "_int"];

			stats.map(this.basicStat);
			secStats.map(this.secondStat);
			this.eduStat();
			// I just got lazy
			this.specialStat("know", "edu");
			this.specialStat("luck", "pow");
			this.specialStat("san", "pow");
			this.specialStat("idea", "_int");
			this.hp();
			this.db();
			this.baseAge();
			this.profPoints();
			this.hobbyPoints();

		},
		baseAge: function(){
			charData.charExtra["baseAge"] = charData.charBasicStats["edu"] + 6;
		},
		profPoints: function(){
			charData.charExtra["profPoints"] = charData.charBasicStats.edu * 20;
		},
		hobbyPoints: function(){
			charData.charExtra["hobbyPoints"] = charData.charBasicStats._int * 10;
		},
		ageExtraPoints: function(age){
			charData.charExtra["profPoints"] = Math.floor(age - charData.charExtra["baseAge"]/10) * 20;
		},
		ageStatReduction: function(stat){
			charData.charBasicStats[stat] -= 1;
		},
		aging: function(age){
			return Math.floor((age - 40) /10 ); 
		}




	};
