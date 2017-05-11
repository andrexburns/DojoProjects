var mongoose = require('mongoose');
var Topic = mongoose.model('Topic');
module.export = (function(){
  create: function(req, res){
    var newTopic = new Topic(req.body);
    if(err);
    console.log("topic 10", err);
    else {
      topic.find({}, function(err, data){
        if(err);
        console.log("topic 4", err);
        else {
          var data = { data: data, info: info}
          res.json(data);
        }
      });
    }
  }
  read: function(req, res) {
    Topic.find({}, function(err, data){
      if(err)
      console.log("topic 25", err)
      else {
        res.json(data);
      }
    });
  }
  update: function(req, res){
    Topic.findByIdAndUpdate(
      req.params.id,{$set: {posts: req.body.posts}}, {new : true}, function(err, data){
        if(err);
        console.log("topic 47", err)
        else {
          ead,json(data);
        }
      }
    );
  }
})
