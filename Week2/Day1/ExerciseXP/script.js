// Exercisse 1
let Favfood =  "Okok ";
let Favmeal = "Lunch ";
let Eating = " i eat " + Favfood + " at every " + Favmeal;
console.log(Eating);
// Exercise 2 part 1
const myWatchedSeries =  [ "Avengers", "One piece", "jjk0"];
let myWatchedSerieslength = myWatchedSeries.length;
let myWatchedSeriessentence = "Avengers, One piece and jjk0";
let Fullsentence = " i watched " + myWatchedSerieslength + " series : " + myWatchedSeriessentence;
console.log(Fullsentence);
// part 2
myWatchedSeries[0] = "Naruto";
myWatchedSeries.push("FMA");
myWatchedSeries.splice(0,0,"MHA");
myWatchedSeries.splice(1,1);
console.log(myWatchedSeries[1][2]);
console.log(myWatchedSeries);
// Exercise 3
let temperatureC = 10;
let temperatureF = (((temperatureC/5)*9)+32);
console.log(temperatureC + "°C is equal to " + temperatureF + "°F");
// Exercise 4
let c;
let a = 34;
let b = 21;

console.log(a+b); //first expression
    // Prediction:it will output 55 because 34 and 21 are numbers
    // Actual:55

a = 2;

console.log(a+b); //second expression
    // Prediction:it will output 23 because 2 and 21 are numbers
    // Actual:23

    // c is undefined since it has not been assigned any value

//Exercise 5
typeof(15)
// Prediction:number
// Actual:

typeof(5.5)
// Prediction:number
// Actual:

typeof(NaN)
// Prediction:number
// Actual:

typeof("hello")
// Prediction:string
// Actual:

typeof(true)
// Prediction:boolean
// Actual:

typeof(1 != 2)
// Prediction:boolean
// Actual:

"hamburger" + "s"
// Prediction:hamburgers
// Actual:

"hamburgers" - "s"
// Prediction:NaN
// Actual:

"1" + "3"
// Prediction:13
// Actual:

"1" - "3"
// Prediction:NaN
// Actual:

"johnny" + 5
// Prediction:johnny5
// Actual:

"johnny" - 5
// Prediction:NaN
// Actual:

99 * "hello"
// Prediction:NaN
// Actual:

1 != 1
// Prediction:false
// Actual:

1 == "1"
// Prediction:true
// Actual:

1 === "1"
// Prediction:false
// Actual:

//Exercise 6
5 + "34"
// Prediction:534
// Actual:

5 - "4"
// Prediction:NaN
// Actual:

10 % 5
// Prediction:0
// Actual:

5 % 10
// Prediction:5
// Actual:

"Java" + "Script"
// Prediction:JavaScript
// Actual:

" " + " "
// Prediction:  
// Actual:

" " + 0
// Prediction: 0
// Actual:

true + true
// Prediction:2
// Actual:

true + false
// Prediction:1
// Actual:

false + true
// Prediction:1
// Actual:

false - true
// Prediction:-1
// Actual:

!true
// Prediction:false
// Actual:

3 - 4
// Prediction:1
// Actual:

"Bob" - "bill"
// Prediction:NaN
// Actual: