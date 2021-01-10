/*
 * Programming Quiz: What do I Wear? (3-7)
 *
 * Using if/else statements, create a series of logical expressions that logs the size of a t-shirt based on the measurements of:
 *   - shirtWidth
 *   - shirtLength
 *   - shirtSleeve
 *
 * Use the chart above to print out one of the following correct values:
 *   - S, M, L, XL, 2XL, or 3XL
 */

/*
 * QUIZ REQUIREMENTS
 * 1. Your code should have the variables `shirtWidth`, `shirtLength`, and `shirtSleeve`
 * 2. Your code should include an `if...else` conditional statement
 * 3. Your code should use logical expressions
 * 4. Your code should produce the expected output
 * 6. Your code should not be empty
 * 7. BE CAREFUL ABOUT THE EXACT CHARACTERS TO BE PRINTED.
 */
 


// change the values of `shirtWidth`, `shirtLength`, and `shirtSleeve` to test your code
var shirtWidth = 23;
var shirtLength = 30;
var shirtSleeve = 8.71;

/*
 * To gain confidence, check your code for the following combination of [shirtWidth, shirtLength, shirtSleeve, expectedSize]:
 * [18, 28, 8.13, 'S']
 * [19.99, 28.99, 8.379, 'S']
 * [20, 29, 8.38, 'M']
 * [22, 30, 8.63, 'L']
 * [24, 31, 8.88, 'XL']
 * [26, 33, 9.63, '2XL']
 * [27.99, 33.99, 10.129, '2XL']
 * [28, 34, 10.13, '3XL']
 * [18, 29, 8.47, 'NA']
*/

// WRITE YOUR CODE HERE

[shirtWidth, shirtLength, shirtSleeve, expectedSize]

if ((shirtWidth>=18) && (shirtWidth<20) && (shirtLength>=28) && (shirtLength<29) && (shirtSleeve>=7) && (shirtSleeve<8.13)) {
    console.log("S")
}
if ((shirtWidth>=20) && (shirtWidth<22) && (shirtLength>=29) && (shirtLength<30) && (shirtSleeve>=8.38) && (shirtSleeve<8.63)) {
    console.log("M")
}
if ((shirtWidth>=22) && (shirtWidth<24) && (shirtLength>=31) && (shirtLength<32) && (shirtSleeve>=8.63) && (shirtSleeve<8.88)) {
    console.log("L")
}
if ((shirtWidth>=24) && (shirtWidth<26) && (shirtLength>=32) && (shirtLength<33) && (shirtSleeve>=8.88) && (shirtSleeve<9.63)) {
    console.log("XL")
}
if ((shirtWidth>=26) && (shirtWidth<28) && (shirtLength>=33) && (shirtLength<34) && (shirtSleeve>=8.13) && (shirtSleeve<9.63)) {
    console.log("2XL")
}
if ((shirtWidth>=28) && (shirtWidth<32) && (shirtLength>=34) && (shirtLength<35) && (shirtSleeve>=10.13) && (shirtSleeve<11)) {
    console.log("3XL")
}