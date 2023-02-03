//Exercise 1
const people = ["Greg", "Mary", "Devon", "James"];
people.shift();
people.splice(2,1,"Jason")
people.push("Wilfried")
console.log(people[0])
let peopleCopy = people.slice(1,3)
console.log(peopleCopy)
let last = people[3]
console.log(last)
for(let i=0;i<=people.length-1;i++){
    console.log(people[i])
}
for(let i=0;i<=people.length-1;i++){
    if (i === 3){
        break
    }
    console.log(people[i])
}
//Exercise 2
