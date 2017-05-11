var mongoose = require('mongoose');
var comment = mongoose.model('comments');

module.exports = (function() {
  return{
    create: function(req, res){
      var newComment = new comment(reqbody);
      newComment.save(function(err, data){
        if(err)
          console.log("comment 10", err)
        else
          comment.find({post_id: data.post_id}, function(err, data){
            if(err)
              console.log("comment 14", err)
            else
              res.json(data);
          })
      })
    },
  }
})();
