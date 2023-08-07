// Dificultad:  🟢
// 1.- Escribe un programa de una sola línea que haga que aparezca en la pantalla un alert que diga “un mensaje”.
    // console.warn("Un mensaje");

// Dificultad:  🟢
// 2.- Escribe un programa de una sola línea que escriba en la pantalla un texto que diga «Hello World» (document.write).
    // document.write("¡Hola, mundo!");


// Dificultad:  🟢
// 3.- Escribe un programa de una sola línea que escriba en la pantalla el resultado de sumar 3 + 5.
    // console.log(`El resultado de 3 + 5 es ${3 + 5}`);

// Dificultad:  🟢
// 4.- Escribe un programa de dos líneas que pida el nombre del usuario con un prompt y escriba un texto que diga «Hola nombreUsuario»
// Ejemplo: 

// input: Coder 
// Output: Hola Coder
    // let nombre = prompt("Ingrese su nombre: ");
    // console.log (`Hola ${nombre}`)

// Dificultad:  🟢
// 5.- Escribe un programa de tres líneas que pida un número, pida otro número y escriba el resultado de sumar estos dos números.
// Nota: Tener en cuenta la siguiente función: parseInt
// https://developer.mozilla.org/es/docs/Web/JavaScript/Referencia/Objetos_globales/parseInt

    // let num1 = parseInt(prompt("Ingrese primer numero: "))
    // let num2 = parseInt(prompt("Ingrese segundo numero: "))

    // console.log(`El resultado de ${num1} + ${num2} es ${num1 + num2}`)

// Dificultad:  🟢
// 6.- Escribe un programa que pida dos números y escriba en la pantalla cual es el mayor.
// Ejemplo: 

// input: 15 , 3

// Output: El 15 es el número más grande

    // let num1 = parseInt(prompt("Ingrese primer numero: "))
    // let num2 = parseInt(prompt("Ingrese segundo numero: "))

    // if (num1 > num2){
    //     console.log(`El número ${num1} es mayor`)
    // } else {
        //     console.log(`El número ${num2} es mayor`)
        // }
        
        // Dificultad:  🟢
        // 7.- Escribe un programa que pida 3 números y escriba en la pantalla el mayor de los tres.
        // Ejemplo: 
        
        // input: 15 , 3, 9
        

        // Output: El 15 es el número más grande

        // let num1 = parseInt(prompt("Ingrese primer número: "))
        // let num2 = parseInt(prompt("Ingrese segundo número: "))
        // let num3 = parseInt(prompt("Ingrese segundo número: "))
        
        // if (num1 > num2 && num1 > num3) {
        //     console.log(`El número ${num1} es mayor`)
        // } else if (num2 > num3 && num2 > num3) {
        //     console.log(`El número ${num2} es mayor`)
        // } else {
        //     console.log(`El número ${num3} es mayor`)
        // }
        
        // Dificultad:  🟢
        // 8.- Escribe un programa que pida un número y diga si es divisible por 2
        // Ejemplo: 

        // input: 10
        // input: 15
        // Output: El 10 es divisible por 2.
        // Output: El 15 no es divisible por 2.
        
        // let num1 = parseInt(prompt("Ingrese un número: "))
        
        // if (num1 % 2 === 0){
        //     console.log(`El número ${num1} es divisible por 2`)
        // } else {
        //     console.log(`El número ${num1} no es divisible por 2`)
        // }


// Dificultad:  🟢🟡 
// 9.- Escribe un programa que pida una frase y escriba las vocales que aparecen
// Nota: Tener en cuenta la función length y substring o charAt (developer mozilla)
// Ejemplo:

// input: Hola mundo
// Output: oauo

    // let frase = prompt("Ingrese una frase: ");
    // for (let i = 0; i < frase.length; i++){
    //     let letter = frase[i].toLowerCase();
    //     if (letter === 'a' || letter === 'e' || letter === 'i' || letter === 'o' || letter === 'u'){
    //         console.log(letter);
    //     }
    // }

// Dificultad:  🟢🟡
// 10.- Escribe un programa que pida un número y nos diga si es divisible por 2, 3, 5 o 7 (sólo hay que comprobar si lo es por uno de los cuatro)
// Ejemplo: 

// input: 20
// Output: El 20 es divisible por 2.

// let num = prompt("Ingrese un número: ")
// num = parseInt(num);

// switch (true){
//     case num % 2 === 0:
//         console.log(`El número ${num} es divisible por 2`)
//         break;
//     case num % 3 === 0:
//         console.log(`El número ${num} es divisible por 3`)
//         break;
//     case num % 5 === 0:
//         console.log(`El número ${num} es divisible por 5`)
//         break;
//     case num % 7 === 0:
//         console.log(`El número ${num} es divisible por 7`)
//         break;
//     default:
//         console.log(`El número ${num} no es divisible por 2, 3, 5 ni 7`);
//         break;    
// }



// Dificultad:  🟢🟡
// 11.- Añadir al ejercicio anterior que nos diga por cuál de los cuatro es divisible (hay que decir todos por los que es divisible)
// Ejemplo: 

// input: 20
// input: 210

// Output: El 20 es divisible por 2 y por 5.
// Output: El 210 es divisible por 2, por 3, por 5 y por 7.

let num = prompt("Ingrese un número: ");
num = parseInt(num);

let div = [];

if (num % 2 === 0) {
    div.push(" por 2");
}
if (num % 3 === 0) {
    div.push(" por 3");
}
if (num % 5 === 0) {
    div.push(" por 5");
}
if (num % 7 === 0) {
    div.push(" por 7");
}

if (div.length > 0){
    console.log(`El número ${num} es divisible${div}`)
} else {
    console.log(`El número ${num} no es divisible por 2, 3, 5 ni 7`);
}