
var suspect = "Mr. Parkes"; 


var weapon = "";
var solved = false;

if (room === "billiards room") {
    weapon = "poison";
    if (suspect === "Mr. Parkes")
        solved = true;
} 

/* ****************************************** */
// The code below will run only when `solved` is true
if (solved) {
    console.log(suspect +" did it in the "+ room +" with the "+ weapon +"!");
}
/* ****************************************** */