$(document).ready(function(){

// PAGINA 01 //////////////////////////////////////////

	$("#creation-mode").on("click", $("#random-creator"), function(){

		$("#stat-generator").removeClass("hide");
		$("#creation-mode").addClass("hide");
	});

// PAGINA 02 /////////////////////////////////////////

	$("#stat-generator ").on("click", $(".roll-dice"), function(){

// corre la funcion q asigna valores random a toda la pagina

	});


// NAVEGATION //////////////////////////////////////////

	$(".navegation").on("click", $("#back-button"), function(){

// le quita a la seccion anterior hide
// le da a ella misma hide 
	});

	$(".navegation").on("click", $("#next-button"), function(){

// le quita a la seccion siguiente hide
// le da a ella misma hide 
	});	

	$(".navegation").on("click", $("#cancel-button"), function(){

		$("#creation-mode").removeClass("hide");
// le da a ella misma hide 
	});		

//////////////////////////////////////////////////////////

});

