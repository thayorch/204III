window.numberToWords = function (num) {
    if (num === 0) return "zero";
    const belowTwenty = [
      "",
      "one",
      "two",
      "three",
      "four",
      "five",
      "six",
      "seven",
      "eight",
      "nine",
      "ten",
      "eleven",
      "twelve",
      "thirteen",
      "fourteen",
      "fifteen",
      "sixteen",
      "seventeen",
      "eighteen",
      "nineteen",
    ];
    const tens = [
      "",
      "",
      "twenty",
      "thirty",
      "forty",
      "fifty",
      "sixty",
      "seventy",
      "eighty",
      "ninety",
    ];
    const hundreds = [
      "",
      "one hundred",
      "two hundred",
      "three hundred",
      "four hundred",
      "five hundred",
      "six hundred",
      "seven hundred",
      "eight hundred",
      "nine hundred",
    ];

    
    let chunks = [];
    let currentNum = BigInt(Math.floor(num));
    while (currentNum > 0n) {
      chunks.unshift(currentNum % 1000n);
      currentNum = currentNum / 1000n;
    }
    if (chunks.length === 0) chunks.push(0n);
    let integerWords = chunks
      .map((chunk, index) => {
        chunk = Number(chunk);
        if (chunk === 0) return "";
        const hundred = Math.floor(chunk / 100);
        const tenUnit = chunk % 100;
        const ten = Math.floor(tenUnit / 10);
        const unit = tenUnit % 10;
        let chunkText = "";
        if (hundred > 0) chunkText += hundreds[hundred] + " ";
        if (tenUnit >= 20) {
          chunkText += tens[ten] + " ";
          if (unit > 0) chunkText += belowTwenty[unit];
        } else if (tenUnit > 0) {
          chunkText += belowTwenty[tenUnit];
        }
        if (chunk > 0 && index < chunks.length - 1) {
          let scale = integerScales[chunks.length - index - 2];
          return (
            chunkText.trim() + " " + plural(chunk, scale, { showNumber: false })
          );
        }
        return chunkText.trim();
      })
      .join(" ")
      .trim();
    let decimalPart = (num - Math.floor(num))
      .toFixed(num.toString().split(".")?.[1]?.length)
      .toString()
      .slice(2);
    let decimalLength =
      decimalPart > 0 ? decimalPart.toString().replace("-", "").length : 0;
    return (
      (integerWords.length > 0 ? integerWords : "zero") +
      (decimalLength > 0
        ? " point " +
          numberToWords(decimalPart) +
          " " +
          plural(decimalPart, decimalScales[decimalLength - 1], {
            showNumber: false,
          })
        : "")
    );
  };