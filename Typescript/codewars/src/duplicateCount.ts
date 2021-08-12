// export function duplicateCount(text: string): number {
//   const lowercase: string = text.toLowerCase();
//   const lowerArrPre: string[] = Object.assign([], lowercase);
//   const lowerArr: string[] = lowerArrPre.sort();
//   // convert to lower and create set of unique vals
//   const lowerSetPre: string[] = [...new Set(lowerArr)];
//   const lowerSet: string[] = lowerSetPre.sort();
//   // find the leftover elements after subtracting

//   function leftoverCounter(): number {
//     // this function is designed to produce an array that is the difference of the lowerArr and lowerSet

//     // create a temporary array from which to splice
//     const tempSet: string[] = lowerSet;

//     const leftovers = lowerArr.filter((val: string) => {
//       // if the temporary set contains the character,
//       if (tempSet.includes(val)) {
//         // filter it out but also remove that character from the temp set.
//         tempSet.splice(0, 1);
//         return false;
//       } else {
//         return true;
//       }
//     });
//     const leftoverSet: string[] = [...new Set(leftovers)];
//     return leftoverSet.length;
//   }
//   // find the number of unique letters
//   const count: number = leftoverCounter();

//   return count;
// }

export function duplicateCount(text: string): number {
  let map: any = {};
  for (const t of Array.from(text.toLowerCase())) {
    // if there is a letter in the map, increment its value, else add it
    map[t] ? (map[t] += 1) : (map[t] = 1);
  }
  // make a list of the object vals, any value over 1 is a duplicate
  // removing the ones, we are left the number of unique letters
  return Object.values(map).filter((count: any) => count > 1).length;
}
