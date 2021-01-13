var x = 1;

while (x <= 20) {
    if (x % 3 === 0) {
        console.log("fizz");
        if (x % 5 === 0) {console.log("fizzbuzz")}
    } else if (x % 5 === 0) {
        console.log("fizz");
    }
    else {
        console.log(x);
    }
    x += 1
}