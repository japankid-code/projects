export function duplicateCount(text: string): number {
  // ...
  const lowercase: string = text.toLowerCase();
  console.log("lowercase", lowercase);

  const lowerArr: string[] = Array.from(lowercase);
  console.log("lowerArr", lowerArr);

  // convert to lower and create set of unique vals
  const lowerSet: string[] = [...new Set(lowerArr)];
  // find the leftover elements after subtracting
  console.log("lowerSet", lowerSet);

  function leftoverCounter(): any {
    // const leftOverArray;
  }

  const leftovers = lowerArr.filter((val, i) => {
    // subtract only as many elements as there are in the lowerSet
    // return
    if (val === lowerSet[i]) {
      return false;
    }
    //     return i > lowerSet.length ? true : !lowerSet.includes(val)
  });
  console.log("leftovers", leftovers);

  const leftoverSet: string[] = [...new Set(leftovers)];
  // find the number of dupes
  const dupesNum: number = lowerArr.length - lowerSet.length;
  // find the number of unique letters
  const uniqueLetters: number = leftoverSet.length;
  console.log("leftoverSet", leftoverSet);

  console.log(dupesNum > uniqueLetters ? dupesNum : uniqueLetters);
  return dupesNum > uniqueLetters ? dupesNum : uniqueLetters;
}
