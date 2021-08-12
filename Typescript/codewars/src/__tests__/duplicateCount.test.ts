// import { assert } from "react";

import { duplicateCount } from "../duplicateCount";

describe("Tests", function () {
  var lowers = "abcdefghijklmnopqrstuvwxyz",
    uppers = lowers.toUpperCase();
  it("Fixed tests", function () {
    expect(duplicateCount("")).toBe(0);
    expect(duplicateCount("abcde")).toBe(0);
    expect(duplicateCount("aabbcde")).toBe(2);
    expect(duplicateCount("aabBcde")).toBe(2);
    expect(duplicateCount("Indivisibility")).toBe(1);
    expect(duplicateCount("Indivisibilities")).toBe(2);
    expect(duplicateCount(lowers)).toBe(0);
    expect(duplicateCount(lowers + "baaAAB")).toBe(2);
    expect(duplicateCount(lowers + lowers)).toBe(26);
    expect(duplicateCount(lowers + uppers)).toBe(26);
  });
  it("Random tests", function () {
    var rnd = function (x: number): number {
      return Math.floor(Math.random() * x);
    };

    for (var t = 0; t < 100; t++) {
      var len = 3 + rnd(5),
        i = len + 1,
        str = lowers.slice(0, len * 2);
      if (rnd(100) < 70) {
        while (i-- > 0) str += [lowers, uppers][rnd(2)].slice(0, i);
      } else {
        str += lowers.slice(-len);
        len = 0;
      }
      expect(duplicateCount(str)).toBe(len);
    }
  });
});
