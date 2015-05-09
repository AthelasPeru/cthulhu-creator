$(document).ready(function(){
	var rollDice = $(".roll-dice").on('click', function(){
		generate.allStats();
		var stats = $("[data-stat]");

		for (var i = 0; i < stats.length; i++){
			var stat = $(stats[i]).attr("data-stat");
			if(stat == "str"){
				$(stats[i]).find("input").attr("value", charData.charBasicStats[stat])
			} 
			else if (stat == "dex"){
				$(stats[i]).find("input").attr("value", charData.charBasicStats[stat])
			}
			else if (stat == "con"){
				$(stats[i]).find("input").attr("value", charData.charBasicStats[stat])
			}
			else if (stat == "_int"){
				$(stats[i]).find("input").attr("value", charData.charBasicStats[stat])
			}
			else if (stat == "siz"){
				$(stats[i]).find("input").attr("value", charData.charBasicStats[stat])
			}
			else if (stat == "pow"){
				$(stats[i]).find("input").attr("value", charData.charBasicStats[stat])
			}
			else if (stat == "app" ){
				$(stats[i]).find("input").attr("value", charData.charBasicStats[stat])
			}
			else if (stat == "edu" ){
				$(stats[i]).find("input").attr("value", charData.charBasicStats[stat])
			}
			else if (stat == "idea" ){
				$(stats[i]).find("input").attr("value", charData.charSpecialStats[stat])
			}
			else if (stat == "know" ){
				$(stats[i]).find("input").attr("value", charData.charSpecialStats[stat])
			}
			else if (stat == "luck" ){
				$(stats[i]).find("input").attr("value", charData.charSpecialStats[stat])
			}
			else if (stat == "hp" ){
				$(stats[i]).find("input").attr("value", charData.charSpecialStats[stat])
			}
			else if (stat == "san" ){
				$(stats[i]).find("input").attr("value", charData.charSpecialStats[stat])
			}
			else if (stat == "db" ){
				$(stats[i]).find("input").attr("value", charData.charSpecialStats[stat])
			}
			else if (stat == "baseAge" ){
				$(stats[i]).find("input").attr("value", charData.charExtra[stat])
			}
			else if (stat == "profPoints" ){
				$(stats[i]).find("input").attr("value", charData.charExtra[stat])
			}
			else if (stat == "hobbyPoints" ){
				$(stats[i]).find("input").attr("value", charData.charExtra[stat])
			}

		}
			
	});
});