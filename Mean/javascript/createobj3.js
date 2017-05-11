function VehicleConstructor(name , wheels , passengers , speed){
  if (!(this instanceof VehicleConstructor)){
    return new VehicleConstructor(name,wheels,passengerNumber, speed);
  }
  var char = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ";
  this.distance_traveled = 0;
  this.speed = speed;
  this.name = name;
  this.wheels = wheels;
  this.passengers = passengers;
  this.vin = createVin();

  function createVin(){
    var vin = '';
    for (var i = 0; i < 17; i++){
      vin += char[Math.floor(Math.random()*35)];
    }
    return vin;
  }
}

VehicleConstructor.prototype.makeNoise = function(noise){
  var noise = noise || "BEEP BEEP!!!!!";
  console.log(noise);
  return this;
};

VehicleConstructor.prototype.move = function(){
  this.UpdateDistanceTraveled();
  this.makeNoise();
  return this;
};

VehicleConstructor.prototype.checkMiles = function(){
  console.log(this.distance_traveled);
  return this
};

VehicleConstructor.prototype.UpdateDistanceTraveled = function(){
  this.distance_traveled = this.distance_traveled + this.speed;
  console.log(this.distance_traveled);
}
var car = new VehicleConstructor("car" , 4 , 4 , 60);
