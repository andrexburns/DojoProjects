var y = ["hello", "world", "JavaScript is Fun"];
var x = [3,5,"Dojo", "rocks", "Michael", "Sensei"];
function string(arr){
  for (var i = 0; i < arr.length; i++){;
    console.log(arr[i]);
  }
string(arr)
var x =  [1, 5, 90, 25, -3, 0]
function string(arr){
  arr.push(100);
  console.log(arr);
  arr.push(y);
  console.log(arr);
  }
}
string(x);
function sum(num){
  var sum = 0;
  for (var i = 0; i <num + 1 ; i++){
    sum = sum + i;
    console.log(sum);
  }
}
sum(500);
var arr =  [1, 5, 90, 25, -3, 0];
function min(arr){
  var min = arr[0];
  for (var i = 1; i < arr.length ; i++){
    if(arr[i]<min){
      min=arr[i];
    }
  }
  return min;
}
console.log(min(arr));
var sum = 0;
var arr = [1, 5, 90, 25, -3, 0];
function avg(){
  for (var i = 0 ; i < arr.length ; i++){
    var sum = sum + arr[i];
  }
}
console.log(sum/arr.length);

var new_ninja = {
  name: 'jessica',
  profession: 'coder',
  favorite_language: 'Javascript',
  dojo: 'the bay!!',
};
for (var key in new_ninja){
  console.log(key + " : " + new_ninja[key]);
}
