export function duplicateCount(text: string): number {
  const lowercase: string = text.toLowerCase();
  const lowerArr: string[] = Array.from(lowercase).sort();
  // convert to lower and create set of unique vals
  const lowerSetPre: string[] = [...new Set(lowerArr)];
  const lowerSet: string[] = lowerSetPre.sort();
  // find the leftover elements after subtracting
  console.log("lower set", lowerSet);

  function leftoverCounter(): number {
    // this function is designed to produce an array that is the difference
    // of the lowerArr and lowerSet

    // create a temporary array from which to splice
    const tempSet: string[] = lowerSet;

    const leftovers = lowerArr.filter((val, i) => {
      // if the temporary set contains the character,
      if (tempSet.includes(val)) {
        // filter it out but also remove that character from the temp set.
        tempSet.splice(0, 1);
        return false;
      } else {
        return true;
      }
    });
    const leftoverSet: string[] = [...new Set(leftovers)];
    return leftoverSet.length;
  }

  // find the number of dupes
  const dupesNum: number = lowerArr.length - lowerSet.length;
  // find the number of unique letters
  const uniqueLetters: number = leftoverCounter();

  return uniqueLetters;
}
