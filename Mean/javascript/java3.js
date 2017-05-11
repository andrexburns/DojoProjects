var run;
function runlogger(){
  var run;
  run = " run!!!";
  return run;
}
var run;
runlogger();
run = "I am Running !! ";
console.log(run);
function runningLogger(){
  console.log("I am running");
}
function Multiplyby10(numb){
  if(typeof(numb) == "number"){
    return numb * 10;
  }
}
var cat;
function stringReturnOne(){
  var cat;
  cat = "kitten";
  return cat;
}
var dog;
function stringReturnTwo(){
  var dog;
  dog = "spike"
  return dog;
}
function myFunctionRunner(parameter){
  if (typeof(parameter) == "function"){
    parameter();
  }
}
myFunctionRunner(stringReturnOne);

function doubleConsoleLog(parameter1, parameter2){
  if (typeof(parameter1) == "function" && typeof (paramter2) == "function"){
    console.log(parameter1(), parameter2());
  }
}
doubleConsoleLog(stringReturnOne, stringReturnTwo);

function caller2(parameter){
  console.log('starting');
  var x = setTimeout(function(){
    if (typeof(parameter) == "function"){
      parameter(stringReturnOne, stringReturnTwo);
    }
  }, 4500);
  console.log('fin');
  return "Riveting";
}
caller2(doubleConsoleLog);
