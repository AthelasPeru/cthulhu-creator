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

		$(this).parent().prev().removeClass("hide");

		$(this).parent().addClass("hide");

	});

	$(".navegation").on("click", $("#next-button"), function(){

		$(this).parent().next().removeClass("hide");
		
		$(this).parent().addClass("hide");

	});	

	$(".navegation").on("click", $("#cancel-button"), function(){

		$("#creation-mode").removeClass("hide");
		$(this).parent().addClass("hide");		
// le da a ella misma hide 
	});		

//////////////////////////////////////////////////////////

});

