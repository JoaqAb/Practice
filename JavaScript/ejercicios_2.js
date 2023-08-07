// Ejercicios javascript - Bucles
// Dificultad:  🟢

// 1- Escribir un programa que solicite la edad y si es mayor de 18 años mostrar un mensaje que ya puede conducir, si la edad ingresada no es un número válido indicarlo en un mensaje.
// let edad = prompt("Ingrese su edad: ")
// if (edad >= 18){
//     console.log("Puede conducir")
// } else if (edad < 18){
//     console.log("No puede conducir")
// } else {
//     console.log("No es un número válido")
// }

// Dificultad:  🟢🟡

// 2- Escribir un programa que solicite una nota (número) de 0  a 10. Luego mostrar la calificación en un alert según los siguientes rangos de nota:

// 0-2: Muy deficiente
// 3-4: Insuficiente
// 5-6: Suficiente
// 7: Bien
// 8-9: Notable
// 10: Sobresaliente

// Si ingreso un número que no esté dentro del rango de 0 a 10 mostrar un mensaje de “número erróneo”. Si el número ingresado no es válido mostrar el mensaje “Introduce un número válido”.

// Ejemplo:



// Input: 5
// Input: 50
// Input: hola10
// Output: Suficiente
// Output: Número erróneo
// Output: Introduce un número válido

// let nota;
// do{
//     nota = prompt("Ingrese su nota: ");   
    
//     if (!Number.isInteger(parseInt(nota))){
//         console.log("Introduce un número válido");
//     } else if (nota <= 0 || nota >= 10)
//     console.log("Número erróneo");
// } while (!Number.isInteger(parseInt(nota)) || nota <= 0 || nota >= 10);

// nota = parseInt(nota)

// switch (true){
//     case nota <= 2:
//         console.log("Muy deficiente");
//         break;
//     case nota === 3 || nota === 4:
//         console.log("Insuficiente");
//         break;
//     case nota === 5 || nota === 6:
//         console.log("Suficiente");
//         break;
//     case nota === 7:
//         console.log("Bien");
//         break;
//     case nota === 8 || nota === 9:
//         console.log("Notable");
//         break;
//     default:
//         console.log("Sobresaliente");
//         break;
// }


// Dificultad:  🟢🟡
 
// 3- Realiza un script que pida cadenas de texto  hasta que se pulse “cancelar”. Al salir con “cancelar” deben mostrarse todas las cadenas concatenadas con un guión -.
// Nota: usar confirm() https://www.w3schools.com/jsref/met_win_confirm.asp
// let text = [];
// do {
//     let ingreso = prompt("Ingrese un texto: ");
//     text.push(ingreso);
// } while (confirm("Quiere ingresar otro texto?") == true);

// console.log(text.join(" - "))


// Dificultad:  🟢🟡
// 4- Realiza un script que pida números hasta que se pulse “cancelar”. Si no es un número deberá indicarse con un «alert» y seguir pidiendo números. Al salir con “cancelar” deberá indicarse la suma total de los números introducidos.
// let nums = 0;
// let n;
// do { 
//     n = parseInt(prompt("Ingrese un número: "));
//     if (!isNaN(n)){
//         nums += n;
//     } else {
//         alert("Ingrese un número válido: ")
//     }
// } while (confirm("Quiere ingresar otro número?") == true);
// console.log(nums);

// Dificultad:  🟢🟡🔴
// 5- Realizar una página con un script que calcule el valor de la letra de un número de DNI (Documento nacional de identidad).

// El algoritmo para calcular la letra del dni es el siguiente :

// El número debe ser entre 0 y 99999999
// Debemos calcular el resto de la división entera entre el número y el número 23.
// Según el resultado, de 0 a 22, le corresponderá una letra de las siguientes:  (T, R, W, A, G, M, Y, F, P, D, X, B, N, J, Z, S, Q, V, H, L, C, K, E) 
// Si lo introducido no es un número deberá indicarse con un alert y volver a preguntar.
// Deberá de repetirse el proceso hasta que el usuario pulse «cancelar».
// Ejemplo: 
// Input:  40773821 
// Output: ‘L’

// let dni = 0;
// let letras = ['T', 'R', 'W', 'A', 'G', 'M', 'Y', 'F', 'P', 'D', 'X', 'B', 'N', 'J', 'Z', 'S', 'Q', 'V', 'H', 'L', 'C', 'K', 'E'];
// let letraDni;

// do { 
//     let n = parseInt(prompt("Ingrese su número de DNI: "));
//     if (!isNaN(n) && n >= 0 && n <= 99999999){
//         dni = n;
//     } else {
//         alert("Ingrese un número válido: ")
//     }
// } while (confirm("Quiere ingresar otro número?") == true);

// let tempo = Math.round(dni % 23);
// letraDni = letras[tempo];

// console.log(letraDni);


// Dificultad:  🟢🟡
// 6- Realiza un script que escriba una pirámide del 1 al 30 de la siguiente forma :

// 1
// 22
// 333
// 4444
// 55555
// 666666
// …….

// const H = 30;

// for (let i = 1; i < H + 1; i++){
//         let p = String(i).repeat(i);
//         console.log(p);
// }

// Dificultad:  🟢🟡
// 7- Haz un script que escriba una pirámide inversa de los números del 1 al número que indique el usuario (no mayor de 50)  de la siguiente forma : (suponiendo que indica 30).

// 303030303030303030303030303030303030303030303030303030303030
// 2929292929292929292929292929292929292929292929292929292929
// 28282828282828282828282828282828282828282828282828282828
// …..
// 333
// 22
// 1

// let h;

// do {
//     h = parseInt(prompt("Ingrese altura: "));
// } while (isNaN(h) || h < 1 || h > 50);

// for (let i = h; i > 0; i--) {
//     let p = String(i).repeat(i);
//     console.log(p);
// }




// Dificultad:  🟢🟡
// 8- Crea script para generar pirámide siguiente con los números del 1 al número que indique el usuario (no mayor de 50) 

// 1
// 12
// 123
// 1234
// 12345
// 123456
// ……

// let h;

// do {
//     h = parseInt(prompt("Ingrese altura: "));
// } while (isNaN(h) || h < 1 || h > 50);

// for (let i = 0; i <= h; i ++){
//     let row = "";

//     for (let j = 1; j <= i; j++){
//         row += j;
//     }
//     console.log(row);
// }



// Dificultad:  🟢🟡🔴
// 9- Crea un script que escriba los números del 1 al 500, que indique cuáles son múltiplos de 4 y de 9 y que cada 5 líneas muestre una línea horizontal. Por ejemplo :

// 1
// 2
// 3
// 4 (Múltiplo de 4)
// 5-
// ————————————————————-

// 6
// 7
// 8 (Múltiplo de 4)
// 9 (Múltiplo de 9)
// 10


// const TOP = 500;
// for (let i = 1; i <= TOP; i++) {
//     if (i % 4 === 0 && i % 9 ===0) {
//         console.log(i + " (Múltiplo de 4 y 9)");
//     } else if (i % 9 === 0) {
//         console.log(i + " (Múltiplo de 9)");
//     } else if (i % 5 === 0) {
//         console.log(i);
//         console.log("---------------------");
//     } else if 
//         (i % 4 === 0){
//             console.log(i + " (Múltiplo de 4)");
//     } else {
//         console.log(i);
//     }
// }

// Dificultad:  🟢🟡🔴
// 10- Realiza un script que pida número de filas y columnas y escriba una tabla. Dentro de cada una de las celdas deberá escribirse un número consecutivo en orden descendente. Si, por ejemplo, la tabla es de 7×5 los números irán del 35 al 1.

// let x;
// let y;
// let tot;

// do { 
//     x = parseInt(prompt("Ingrese número de columnas: "));
// } while (isNaN(x) || x < 1 || x > 10);
// do { 
//     y = parseInt(prompt("Ingrese número de filas: "));
// } while (isNaN(y) || y < 1 || y > 10);

// tot = x * y;

// for (let i = 0; i < x; i++){
//     let fila = "";
//     for (let j = 0; j < y; j++){
//         fila += tot + " ";
//         tot--;
//     }
//     console.log(fila);
// }

// Ejercicios con Math

// Dificultad:  🟢🟡
// 11- Realiza un script que pida por teclado 3 edades y 3 nombres e indique el nombre del mayor. *
// let edad = [];
// let nombre = [];

// do {
//     let h = parseInt(prompt("Ingrese edad: "));

//     if (!isNaN(h) && h >= 1 && h <= 100) {
//         edad.push(h);
//     } else {
//         alert("Ingrese edad válida.")
//     }

//     let n = prompt("Ingrese nombre: ");
//         nombre.push(n);
// } while (edad.length < 3);

// let max = Math.max(...edad);
// let maxIndex = edad.indexOf(max);
// console.log(nombre[maxIndex]);



// Nota: ver funcion Math() https://www.w3schools.com/js/js_math.asp

// Dificultad:  🟢🟡
// 12- Realiza un script que genere un número aleatorio entre 1 y 99
// let numRandom = Math.round(Math.random() * 100)
// console.log(numRandom);

// Ejercicios con String
// Dificultad:  🟢🟡
// 13- Realiza un script que pida un texto y lo muestre en mayúsculas.
// let s = prompt("Ingrese un texto: ");
// console.log(s.toUpperCase());

// Dificultad:  🟢🟡
// 14- Realiza un script que pida una cadena de texto y lo muestre poniendo el signo – entre cada carácter sin usar el método replace. Por ejemplo, si tecleo “hola qué tal”, deberá salir “h-o-l-a- -q-u-e- -t-a-l”.
// let s = prompt("Ingrese un texto: ");
// let n = s.split("").join("-")
// console.log(n)

// Dificultad:  🟢🟡
// 15- Realiza un script que cuente el número de vocales que tiene un texto.
// let s = prompt("Ingrese un texto: ");
// let vocales = ['a', 'e', 'i', 'o', 'u']
// let counter = 0;

// for (let i = 0; i < s.length; i++) {
//     if (vocales.includes(s[i])) {
//         counter++;
//     }
// }
// console.log(counter);


// Dificultad:  🟢🟡
// 16- Realiza un script que pida una cadena de texto y la devuelva al revés. Es decir, si tecleo “hola que tal” deberá mostrar “lat euq aloh”.
// let s = prompt("Ingrese un texto: ");
// let lenS = s.length;
// let invertS = "";

// for (let i = lenS - 1; i >= 0; i--) {
//     invertS += s[i]; 
// }
// console.log(invertS);



// Dificultad:  🟢
// 17- Realiza un script que muestre la posición de la primera vocal de un texto introducido por teclado.
// Ejemplo:
// Input: Hola mundo
// Output: la vocal ‘o’ está en la posición 1

// let s = prompt("Ingrese un texto: ");
// let vocales = ['a', 'e', 'i', 'o', 'u']
// let pos;
// let vocal;

// for (let i = 0; i < s.length; i++) {
//     if (vocales.includes(s[i])) {
//         vocal = s[i];
//         pos = i;
//         break;
//     }    
// }
// console.log(`La vocal '${vocal}' está en la posición ${pos}`)