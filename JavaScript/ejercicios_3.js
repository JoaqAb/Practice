
// Ejercicios javascript
// Prácticas con arreglos y funciones


// Arrays
// Dificultad:  🟢
// 1- Crear un array llamado meses y que almacene el nombre de los doce meses del año. Mostrar por pantalla en forma de lista los doce nombres del arreglo.
// Output:
// const months = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'];

// for (let i = 0; i < months.length; i++) {
//     console.log(months[i]);    
// }

// Dificultad:  🟢🟡
// 2-  Crear un script que solicite al usuario mediante un prompt el nombre de ciudades y almacenarlas en un arreglo, cuando el usuario selecciona cancelar se debe mostrar el arreglo generado, luego realizar las siguientes acciones:

// Mostrar la longitud del arreglo.
// Mostrar en el documento web los ítems de las posiciones primera, tercera y última.
// Añade en última posición la ciudad de París.
// Escribe por pantalla el elemento que ocupa la segunda posición.
// Sustituye el elemento que ocupa la segunda posición por la ciudad de 'Barcelona'.

// Ejemplo:
// Input:
// [‘Nueva York, Estados Unidos’, ‘Barcelona, España’, ‘Tokio, Japón’, ‘Londres, Reino Unido’, ‘Roma, Italia’, ‘Pekín, China’, ‘Río de Janeiro, Brasil’, ‘Ámsterdam, Países Bajos’, ‘Sídney, Australia’, ‘El Cairo, Egipto’]

// Output:

// let ciudades = [];
// do {
//     let ciudad = prompt("Ingrese una ciudad: ");
//     ciudades.push(ciudad);
// } while (confirm("Quiere ingresar otro ciudad?") == true);

// console.log(`El array contiene ${ciudades.length} ciudades`);
// console.log(`Primer elemento ${ciudades[0]}`);
// console.log(`Tercer elemento ${ciudades[2]}`);
// console.log(`Ultimo elemento ${ciudades[ciudades.length - 1]}`);
// ciudades.push("Paris");
// console.log(`Segundo elemento ${ciudades[1]}`);
// ciudades[1] = "Barcelona"

// for (let i = 0; i < ciudades.length; i++) {
//     console.log(`Elemento: ${ciudades[i]}`);    
// }

// Dificultad:  🟢🟡🔴

// 3- Escribir un script que simule el lanzamiento de dos dados. Hacer uso de la función Math.random para obtener números aleatorios entre 1 y 6 para cada uno de los lanzamientos de los dados. Sumar el resultado de lanzar dos dados y anotar en un array el número de apariciones de dicha suma, repitiendo 50 veces esta operación.

// Ejemplo de salida:

// let suma = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];

// for (let i = 0; i < 50; i++) {
//     let dado1 = Math.floor(Math.random() * 6) + 1;
//     let dado2 = Math.floor(Math.random() * 6) + 1;
//     let result = dado1 + dado2;    
//     suma[result - 2]++;
// }

// let num = 2;
// for (let j = 0; j < suma.length; j++, num++) {
//     console.log(`${num}:  ${suma[j]}`);        
// }


// Funciones
// Dificultad:  🟢
// 4- Escribir el código de una función a la que se pasa como parámetro un número entero y devuelve como resultado una cadena de texto que indica si el número es par o impar. Mostrar por pantalla el resultado devuelto por la función.
function esPar(num) {
    
}

// Dificultad:  🟢🟡
// 5- Definir una función que muestre información sobre una cadena de texto que se le pasa como argumento. A partir de la cadena que se le pasa, la función determina si esa cadena está formada sólo por mayúsculas, sólo por minúsculas o por una mezcla de ambas.
// Dificultad:  🟢🟡
// 6- Solicitar por pantalla al usuario ingresar el valor de los lados de un rectángulo, luego crear una función para calcular su perímetro y mostrarlo por pantalla.

// La fórmula del perímetro  es p = 2*(a +b)

// Ejemplo:




// Input:
// lado A = 24
// lado B = 5

// Output: 58

// Dificultad:  🟢🟡
// 7- Escriba un script que muestre la tabla de multiplicar de un número ingresado por pantalla, la creación de la tabla debe ser realizada con una función y mostrar solo los resultados del 1 al 10 del número elegido por el usuario.

