function VehicleConstructor(name , wheels , passengers){
  var vehicle = {};
  vehicle.name = name;
  vehicle.wheels = wheels;
  vehicle.passengers = passengers;
  vehicle.makeNoise = function(){
    console.log("noise maker 5000");
  }
  return vehicle;
}

var Bike = VehicleConstructor("Bike" , 2 , 1);
console.log(Bike);
Bike.makeNoise = function(){
  console.log("RING RING!!!")
}

Bike.makeNoise();

var Sedan = VehicleConstructor("Sedan" , 4 , 4);
console.log(Sedan);
Sedan.makeNoise = function(){
  console.log("HONK HONK!!!")
}

Sedan.makeNoise();

var Bus = VehicleConstructor("Bus" , 8 , 2);
Bus.morePassengers = function(passengers){
  Bus.passengers = Bus.passengers + passengers;
}
Bus.makeNoise = function(){
  console.log("WHEELS ON THE BUSS!!!!!")
}
Bus.makeNoise();
console.log(Bus.passengers)
Bus.morePassengers(16);
console.log(Bus.passengers)
console.log(Bus);
