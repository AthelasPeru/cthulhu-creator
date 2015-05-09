$(document).ready(function(){


// PAGINA 01 //////////////////////////////////////////


	$(".page01").on("click", $(".creator_buttom"), function(){

		$(".page02").removeClass("hide");
		$(".page01").addClass("hide");
		
	});

	// Al dar click sobre un pj creado se lee la data y se abre la pagina 'game-main' del personaje


/////////////////////////////////////////////////////////
// PAGINA 02 
/////////////////////////////////////////////////////////

	$(".page02 ").on("click", $(".stat-roller"), function(){




	});

	$(".page02 .selection_buttons .topage03").on("click", $(".topage03"), function(){

		$(".page03").removeClass("hide");
		$(".page02").addClass("hide");

// Al dar click tambien se deben grabar los stats producidos en 'new-character'

	});

	$(".page02 .selection_buttons .topage01").on("click", $(".topage01"), function(){

		$(".page01").removeClass("hide");
		$(".page02").addClass("hide");

// Al dar click tambien se deben borrar los stats producidos en 'new-character'

	});


//////////////////////////////////////////////////////////
// PAGINA 03
//////////////////////////////////////////////////////////

	$(".page03 .selection_buttons .topage04").on("click", $(".topage04"), function(){

		$(".page05").removeClass("hide");
		$(".page03").addClass("hide");

// Al dar click se agrega la profesion seleccionada a 'new-character'

	});

	$(".page03 .selection_buttons .topage02").on("click", $(".topage02"), function(){

		$(".page02").removeClass("hide");
		$(".page03").addClass("hide");

// Al dar click se deben borrar la profesion seleccionada de existir

	});

//////////////////////////////////////////////////////////
// PAGINA 04
//////////////////////////////////////////////////////////	




//////////////////////////////////////////////////////////
// PAGINA 05
//////////////////////////////////////////////////////////

	$(".page05").on("click", $(".topage06"), function(){

		$(".page05").removeClass("hide");
		$(".page03").addClass("hide");


	});



});

///////////////pagina de inicio//////////////////

// 1	al dar click al boton "create your investigator" se debe abrir la siguiente pagina: "core rolls"
// 2 al dar click al nombre de un personaje creado, se debe abrir la "pagina principal" de dicho personaje
// 3	moviendo a derecha (o izquierda) aparecen mas nombres de investigadores (si la cuenta tiene mas de 3).


///////////////////roll Calls////////////////



////////////ocupation///////////////////
// 1	al dar hover sobre el boton, aparece la lista de profesiones, al dar click sobre una, esta se selecciona(cambia de color x ejenmplo)
// 2	dar click sobre back te regresa a "roll calls"
// 3	dar click al boton "next" te lleva a la pagina "ocupational skills"


// ocupational skills //////////////////////////////////////




//////////////hobby skills/////////////////

// 1	se debe ver la lista completa de skills , en ella su porcentaje base y 2 botones para aumentar o disminuir puntaje
// 2	el total de "hobby points" es INT * 10
		// cuando se da click a los botones de adicionar o restar, se va modificando este numero base
// 3	cuando se selecciona un skill se puede editar en al cuadro de la derecha		
// 4	dar click sobre back te regresa a "ocupational skills"
// 5	dar click al boton "next" te lleva a la pagina "investigator data"

