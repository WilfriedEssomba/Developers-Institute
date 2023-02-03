//Exercise 1
let language = prompt("Enter the language you speak")
let langue = language.length;
switch (language){
    case "english":
        console.log("Hello")
        break;
    case "french":
        console.log("Bonjour")
        break;
    case "beti":
        console.log("okok")
        break;
    default:
        console.log("01110011 01101111 01110010 01110010 01111001")
}
// Exercise 2
let x = parseInt(prompt("Enter your grade"));
switch (x){
    case x>90:
        console.log("A")
        break;
    case 90>=x>80:
        console.log("B")
        break;
    case 80>=x>=70:
        console.log("C")
        break;
    default:
        console.log("D")
}