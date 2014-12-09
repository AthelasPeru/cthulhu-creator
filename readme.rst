Chtulhu Character creator
==========================

API Routes
-------------

Get the rules set
+++++++++++++++++++++++++++++++++++++++

*route*: /api/v1.0/character/rules/<string:rules>

methods=['GET']

Esta ruta provee a la aplicación del set de reglas a utilizar, si se solicita un set de reglas que no existe retorna un 404.

**curl** : curl -i http://localhost:5000/api/v1.0/character/rules/<string:rules>

El string rules debe ser reemplazado por la versión del manual a utilizar, 5.0, 5.5, 6.0


Get all the user characters
+++++++++++++++++++++++++++++++++++

*route*: /api/v1.0/character/<int:user_id>

methods=['GET']

Esta ruta devuelve todos los personajes asociados con el id del usuario logeado, de esta manera se pueden utilizar en el frontend.

**curl** :  curl -i http://localhost:5000/api/v1.0/character/<int:user_id>

el int debe ser reemplazado por el id del usuario, por ahora devuelve la lista de todos los personajes que este usuario tenga



Get a specific character for a user
+++++++++++++++++++++++++++++++++++++

*route* : /api/v1.0/character/<int:user_id>/<int:character_id>

methods=['GET']

Esta ruta devuelve todos los datos del personaje específico

**curl**: curl -i http://localhost:5000/api/v1.0/character/<int:user_id>/<int:character_id>

el contador de in de character_id comienza en 0


Add a new character to a user
+++++++++++++++++++++++++++++++

*route* : /api/v1.0/character/<int:user_id>

methods=['POST']

Esta ruta agrega un personaje enviado mediante POST a la ruta del jugador.

**curl**: curl -i -H "Content-Type: application/json" -X POST -d '{"character": {"id": 1, "general_data":{"complete_name": "Incio","profession": "Photographer","degree": "Expert","birthplace": "Peru","mental_disorde": "All of them","gender": "male","age": "14" }}}' http://localhost:5000/api/v1.0/character/1

El JSON debe enviarse sin comas sobrantes, o dará error Bad Request.


Update a character data 
++++++++++++++++++++++++

*route* : /api/v1.0/character/<int:user_id>/<int:character_id>

methods=['PUT']

Esta ruta actualiza la data de un personaje, requeire que se le envíe un data JSON

**curl**: curl -i -H "Content-Type: application/json" -X PUT -d '{"character": {"general_data":{"complete_name": "Nombre Nuevo"}}}' http://localhost:5000/api/v1.0/character/1/0

El id tiene que ser un elemento del mismo level que el general_data, si no no encontrará el elemento dentro del array de PJ'si


Delete a character
+++++++++++++++++++++

*route* : /api/v1.0/character/<int:user_id>/<int:character_id>

methods=['DELETE']

Esta ruta elimina un personaje para el jugador seleccionado.

**curl** : curl -i -X DELETE http://localhost:5000/api/v1.0/character/1/0





Importante
---------------

El API por ahora no tiene una estructura fija, los usuarios tienen la siguiente estructura en JSON

.. code-block:: json

	{ 
	"_id" : {
		 "$oid" : "valor automatico que asigna mongo"
	  } , 
		"user_id" : 1 , 
		"characters" : [ 
			{ "general_data" : { "birthplace" : "" , "degree" : "" , "gender" : "" , "age" : "" , "profession" : "" , "complete_name" : "" , "mental_disorders" : ""} , "id" : int} , 
			{ "general_data" : { "birthplace" : "" , "degree" : "" , "gender" : "" , "age" : "" , "profession" : "" , "complete_name" : "" , "mental_disorde" : " "} , "id" : int}
		]
	}



