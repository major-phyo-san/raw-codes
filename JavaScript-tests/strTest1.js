
function numStringToTotal(numTxt){
strLen = numTxt.length;
var firstSum = 0;
var secondSum = 0;
var final=0;
for(i=0;i<strLen;i++){
firstSum += parseInt(numTxt[i]);
}

console.log(firstSum);

if(firstSum>9){
	firstSumStr = firstSum.toString();
	for(i=0;i<firstSumStr.length;i++){
		secondSum += parseInt(firstSumStr[i]);
	}
	console.log(secondSum);
	final = secondSum;
}
else
	final = firstSum;
return final;

}

console.log(numStringToTotal("34221"));