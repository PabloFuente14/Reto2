document.getElementById("formulario_cliente").addEventListener('submit', validarFormulario);
document.getElementById("cp").addEventListener('blur', buscarCP);

function buscarCP(evento){
	//control código postal(cp): 3 tipos de errores
    var errores = false;
    var listaErrores = document.getElementById("errores");
    var error_cp_1 = !!document.getElementById("li_cp_1");
    var error_cp_2 = !!document.getElementById("li_cp_2");
    var error_cp_existe = !!document.getElementById("li_cp_existe");
    if(error_cp_1){
        var elemento_error_cp_1 = document.getElementById("li_cp_1");
        listaErrores.removeChild(elemento_error_cp_1);
    }

    if(error_cp_2){
        var elemento_error_cp_2 = document.getElementById("li_cp_2");
        listaErrores.removeChild(elemento_error_cp_2);
    }
	//eliminamos errores existentes antes de dar al botón
    if(error_cp_existe){
        var elemento_error_cp_existe = document.getElementById("li_cp_existe");
        listaErrores.removeChild(elemento_error_cp_existe);
    }
	// el cp sólo puede tener una longitud de 5 números
    var cp = document.getElementById('cp').value;
    if(cp.length != 5){
        errores = true;
        var li = document.createElement('li');
        li.id = "li_cp_1";
        li.innerHTML="El código postal debe de tener 5 números";
        listaErrores.appendChild(li);
    }
	//el cp solo puede tener números
    for(var i = 0; i < cp.length; i++){
        if(!Number.isInteger(parseInt(cp[i]))){
            errores = true;
            var li = document.createElement('li');
            li.id = "li_cp_2";
            li.innerHTML="El código postal solo puede tener números";
            listaErrores.appendChild(li);
            break;
        }
		//fin control cp
    }

    if(errores) return;
	//comprobamos si existe o no existe nuestra provincia y autocompletamos la misma en funión de sus dos primeros dígitos del cp
    var provincia = provincias.filter(function (provincia) { return provincia.id == cp.substr(0,2) });
    if(provincia.length > 0){
        document.getElementById('provincia').value = provincia[0].nm;
    }else{
        errores = true;
        var li = document.createElement('li');
        li.id = "li_cp_existe";
        li.innerHTML="El código postal no existe";
        listaErrores.appendChild(li);
    }

}

function validarFormulario(evento) {
    evento.preventDefault();
    var errores = false; // Por si tenemos errores 
    var listaErrores = document.getElementById("errores"); //Elemento donde publicaremos los errores
    while(listaErrores.firstChild) listaErrores.removeChild(listaErrores.firstChild); //Cuando presionemos el botón borramos si hay errores para mostrar los nuevos


    
    var abecedario = "abcdefghyjklmnopqrstuvwxyz"; // Variable con todas las letras del Abecedario
    var cif = document.getElementById('cif').value; // Elemtento cif
    cif = cif.toLowerCase(); // Ponemos todas las letras en minúscula para comprobar
    
    var ultima_posicion = cif.length - 1; // Obtenemos la Última posición del cif
    
    if((abecedario.indexOf(cif[0]) == -1 && abecedario.indexOf(cif[ultima_posicion]) == -1)){ // Si la primera posicion o la ultima no es letra mostramos errores
        errores = true;
        var li = document.createElement('li');
        li.innerHTML="El CIF debe comenzar o terminar con una letra";
        listaErrores.appendChild(li);
    }

	// Si el cif tiene algún espacio mostramos error
    for(var i = 0; i < cif.length; i++){
        if(cif.charAt(i) == ' '){
            errores = true;
            var li = document.createElement('li');
            li.innerHTML="El CIF no puede contener espacios";
            listaErrores.appendChild(li);
            break;
        }
    }
    //El nombre no puede contener números
    var nombre = document.getElementById('nombre').value;
    for(var i = 0; i < nombre.length; i++){
        if(Number.isInteger(parseInt(nombre[i]))){
            errores = true;
            var li = document.createElement('li');
            li.innerHTML="El nombre no puede contener números";
            listaErrores.appendChild(li);
            break;
        }
    }
    
	//la ciudad tampoco puede contener números
    var ciudad = document.getElementById('ciudad').value;
    for(var i = 0; i < ciudad.length; i++){
        if(Number.isInteger(parseInt(ciudad[i]))){
            errores = true;
            var li = document.createElement('li');
            li.innerHTML="La ciudad no puede contener números";
            listaErrores.appendChild(li);
            break;
        }
    }
    

    if(errores) return;

	document.querySelector("form").submit();

	
    
  }

//array provincias
var provincias = [{
	"id":"04",
	"nm":"Almería"
},{
	"id":"11",
	"nm":"Cádiz"
},{
	"id":"14",
	"nm":"Córdoba"
},{
	"id":"18",
	"nm":"Granada"
},{
	"id":"21",
	"nm":"Huelva"
},{
	"id":"23",
	"nm":"Jaén"
},{
	"id":"29",
	"nm":"Málaga"
},{
	"id":"41",
	"nm":"Sevilla"
},{
	"id":"22",
	"nm":"Huesca"
},{
	"id":"44",
	"nm":"Teruel"
},{
	"id":"50",
	"nm":"Zaragoza"
},{
	"id":"33",
	"nm":"Asturias"
},{
	"id":"07",
	"nm":"Balears,Illes"
},{
	"id":"35",
	"nm":"Palmas,Las"
},{
	"id":"38",
	"nm":"SantaCruzdeTenerife"
},{
	"id":"39",
	"nm":"Cantabria"
},{
	"id":"05",
	"nm":"Ávila"
},{
	"id":"09",
	"nm":"Burgos"
},{
	"id":"24",
	"nm":"León"
},{
	"id":"34",
	"nm":"Palencia"
},{
	"id":"37",
	"nm":"Salamanca"
},{
	"id":"40",
	"nm":"Segovia"
},{
	"id":"42",
	"nm":"Soria"
},{
	"id":"47",
	"nm":"Valladolid"
},{
	"id":"49",
	"nm":"Zamora"
},{
	"id":"02",
	"nm":"Albacete"
},{
	"id":"13",
	"nm":"CiudadReal"
},{
	"id":"16",
	"nm":"Cuenca"
},{
	"id":"19",
	"nm":"Guadalajara"
},{
	"id":"45",
	"nm":"Toledo"
},{
	"id":"08",
	"nm":"Barcelona"
},{
	"id":"17",
	"nm":"Girona"
},{
	"id":"25",
	"nm":"Lleida"
},{
	"id":"43",
	"nm":"Tarragona"
},{
	"id":"03",
	"nm":"Alicante/Alacant"
},{
	"id":"12",
	"nm":"Castellón/Castelló"
},{
	"id":"46",
	"nm":"Valencia/València"
},{
	"id":"06",
	"nm":"Badajoz"
},{
	"id":"10",
	"nm":"Cáceres"
},{
	"id":"15",
	"nm":"Coruña,A"
},{
	"id":"27",
	"nm":"Lugo"
},{
	"id":"32",
	"nm":"Ourense"
},{
	"id":"36",
	"nm":"Pontevedra"
},{
	"id":"28",
	"nm":"Madrid"
},{
	"id":"30",
	"nm":"Murcia"
},{
	"id":"31",
	"nm":"Navarra"
},{
	"id":"01",
	"nm":"Araba/Álava"
},{
	"id":"48",
	"nm":"Bizkaia"
},{
	"id":"20",
	"nm":"Gipuzkoa"
},{
	"id":"26",
	"nm":"Rioja,La"
},{
	"id":"51",
	"nm":"Ceuta"
},{
	"id":"52",
	"nm":"Melilla"
}];