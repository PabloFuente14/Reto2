// definimo las clases de css  que son tamaño
var clases = ["f0", "f1", "f2", "f3", "f4"];

// definimos en que posicion vamos a empezar
var inicioClase = 2;

//funcion del boton de aumentar
document.getElementById('aumentar').addEventListener('click', function () {
    let clasePrevia = inicioClase; // inicia con la clase =2
    inicioClase++; // aumentamos la posicion al inicioClase= 3
    inicioClase = (inicioClase == clases.length) ? clases.length - 1 : inicioClase; //le resto uno si esta en la ultima pos. del array
    cambiarClases(clasePrevia, inicioClase);
});

//funcion del boton de disminuir
document.getElementById('disminuir').addEventListener('click', function () {
    let clasePrevia = inicioClase; // inicia con la clase =2
    inicioClase--; // restamos la posicion al inicioClase= 1
    inicioClase = (inicioClase < 0) ? 0 : inicioClase; //si es cero se queda en cero
    cambiarClases(clasePrevia, inicioClase);
});

// le dicimos la clase previa y la que vamos a pasar
function cambiarClases(previa, siguiente) {
    if (previa != siguiente) {
        var elemento = document.querySelector('html') // cogemos todos los elementos html
        elemento.classList.remove(clases[previa]);//quitamos la clases previa
        elemento.classList.add(clases[siguiente]);//añadimos la clases siguiente
    }
}