// Exercise 1
5 >= 1//true
0 === 1//false
4 <= 1//false
1 != 1//false
"A" > "B"//false
"B" < "C"//false
"a" > "A"//false
"b" < "A"//false
true === false//false
true != true//false
// Exercise 2
let num1 = parseInt(prompt("Enter the first number"));
let num2 = parseInt(prompt("Enter the second number"));
let sum = num1+num2; // To perfom other operations we just have to change the math sign(-,*,/)
alert( sum);
// Exercise 3
let sentence = prompt("Enter a sentence containing the word 'Nemo'");
let word = sentence.indexOf("Nemo");
console.log("i found Nemo at " + word);
// Exercise 4
let n = parseInt(prompt("Enter a number"));
