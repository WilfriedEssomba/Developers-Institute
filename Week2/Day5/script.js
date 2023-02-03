function playTheGame(){
    let will = confirm("Do you want to play?")
    if (will == false){
        alert("No problem, Goodbye")
    }else{
        let num = parseInt(prompt("Enter a number between 0 and 10"))
        if (isNaN(num) == true){
            alert("Sorry not a number")
        }else{
            
        }
    }
}