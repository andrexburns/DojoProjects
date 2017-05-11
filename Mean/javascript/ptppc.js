function myOriginalFunction(){
  console.log('hello');
}

//myOriginalFunction();

function invokedFunction(callback){
  var x = setTimeout(function(){
    callback();
  }, 4000)
}
invokedFunction(myOriginalFunction);
invokedFunction(function(){console.log('world')});
