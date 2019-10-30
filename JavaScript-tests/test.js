let today = new Date();
let tomorrow = new Date();
let nextTwoDays = new Date();
let nextThreeDays = new Date();
let nextFourDays = new Date();
let nextFiveDays = new Date();

tomorrow.setDate(today.getDate()+1);
nextTwoDays.setDate(today.getDate()+2);
nextThreeDays.setDate(today.getDate()+3);
nextFourDays.setDate(today.getDate()+4);
nextFiveDays.setDate(today.getDate()+5);

console.log(today);
console.log(tomorrow);
console.log(nextTwoDays);
console.log(nextThreeDays);
console.log(nextFourDays);
console.log(nextFiveDays);

/*console.log(today);

console.log(today.getDate());
console.log(today.getMonth());
console.log(today.getFullYear());
console.log(today.getDay());*/