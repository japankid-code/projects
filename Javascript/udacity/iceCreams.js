// change the values of `flavor`, `vessel`, and `toppings` to test code
var flavor = "strawberry";
var vessel = "cone";
var toppings = "sprinkles";

if (flavor === "vanilla" || flavor === "chocolate") {
    if (vessel === "cone" || vessel === "bowl")
        if (toppings === "sprinkles" || toppings === "peanuts")
            console.log("I'd like two scoops of "+flavor+" ice cream in a "+vessel+" with "+toppings+".");
}
else {
    console.log("Your choices just did not make sense.");
}
