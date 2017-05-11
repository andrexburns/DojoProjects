function VehicleConstructor(name , wheels , passengers , speed){
  if (!(this instanceof VehicleConstructor)){
    return new VehicleConstructor(name,wheels,passengerNumber, speed);
  }
  var self = this;
  var distance_traveled = 0;

  function UpdateDistanceTraveled(){
    distance_traveled = distance_traveled + self.speed;
  }
  this.speed = speed;
  this.name = name;
  this.wheels = wheels;
  this.passengers = passengers;
  this.makeNoise = function(noise){
    var noise = noise || "BEEP BEEP!!!!!";
    console.log(noise);
  };
  this.move = function(){
  UpdateDistanceTraveled();
  this.makeNoise();
  };
  this.checkMiles = function(){
    return distance_traveled
  };
}
var car = new VehicleConstructor("Car" , 4 , 6 , 60);
console.log(car.checkMiles());
console.log(car.speed);
car.move();
console.log(car.checkMiles());
