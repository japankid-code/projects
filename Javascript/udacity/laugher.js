var laugh = function(laffs) {
    printout = "";
    length = laffs;
    for (var laffs = 0; laffs<length; laffs++) {
        printout += "ha";
    }
    printout += "!";
    return printout;
}

console.log(laugh(10));