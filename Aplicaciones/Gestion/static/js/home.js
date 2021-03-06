// definimo las clases de css  que son tamaño
var clases = ["tamano0" ,  "tamano1"  , "tamano2" , "tamano3" , "tamano4"];
//var clases = ["display-1", "display-2", "display-3", "display-4"]

// definimos en que posicion vamos a empezar
var inicioClase = 2;

//funcion del boton de aumentar
let aumento = document.getElementById('aumentar');
aumento.addEventListener('click', aumentar);
function aumentar() {
    let clasePrevia = inicioClase; // inici)a con la clase =2
    inicioClase++; // aumentamos la posicion al inicioClase= 3
    inicioClase = (inicioClase == clases.length) ? clases.length - 1 : inicioClase; //le resto uno si esta en la ultima pos. del array
    cambiarClases(clasePrevia, inicioClase);
}

//funcion del boton de disminuir

let reducir=document.getElementById('disminuir');
reducir.addEventListener('click',disminuir);
function disminuir(){
    let clasePrevia = inicioClase; // inicia con la clase =2
    inicioClase--; // restamos la posicion al inicioClase= 1
    inicioClase = (inicioClase < 0) ? 0 : inicioClase; //si es cero se queda en cero
    cambiarClases(clasePrevia, inicioClase);
}


// le dicimos la clase previa y la que vamos a pasar
function cambiarClases(previa, siguiente) {
    if (previa != siguiente) {
        var elemento = document.querySelector('#titulo') // cogemos id titulo
        elemento.classList.remove(clases[previa]);//quitamos la clases previa
        elemento.classList.add(clases[siguiente]);//añadimos la clases siguiente

        var elemento1 = document.querySelector('#navbarNav') // cogemos id navbarNav
        elemento1.classList.remove(clases[previa]);//quitamos la clases previa
        elemento1.classList.add(clases[siguiente]);//añadimos la clases 

        var elemento2 = document.querySelector('#texto2') // cogemos id texto2
        elemento2.classList.remove(clases[previa]);//quitamos la clases previa
        elemento2.classList.add(clases[siguiente]);//añadimos la clases siguiente

        var elemento3 = document.querySelector('#texto') // cogemos id  texto
        elemento3.classList.remove(clases[previa]);//quitamos la clases previa
        elemento3.classList.add(clases[siguiente]);//añadimos la clases siguiente
    }
}


