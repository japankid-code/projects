"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.duplicateCount = void 0;
function duplicateCount(text) {
    const lowercase = text.toLowerCase();
    const lowerArr = new Array(lowercase).sort();
    // convert to lower and create set of unique vals
    const lowerSetPre = [...new Set(lowerArr)];
    const lowerSet = lowerSetPre.sort();
    // find the leftover elements after subtracting
    function leftoverCounter() {
        // this function is designed to produce an array that is the difference
        // of the lowerArr and lowerSet
        // create a temporary array from which to splice
        const tempSet = lowerSet;
        const leftovers = lowerArr.filter((val, i) => {
            // if the temporary set contains the character,
            if (tempSet.includes(val)) {
                // filter it out but also remove that character from the temp set.
                tempSet.splice(0, 1);
                return false;
            }
            else {
                return true;
            }
        });
        const leftoverSet = [...new Set(leftovers)];
        return leftoverSet.length;
    }
    // find the number of dupes
    const dupesNum = lowerArr.length - lowerSet.length;
    // find the number of unique letters
    const uniqueLetters = leftoverCounter();
    return uniqueLetters;
}
exports.duplicateCount = duplicateCount;
