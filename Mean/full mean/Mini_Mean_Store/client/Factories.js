  //this is the factories javascript file. this file holds information
app.factory('userFactory', function($http, $location){
  var factory = {};
  var thisUser = null;
          //if the users information is correct, will be directed to the dashboard
  factory.readUsers = function(user, callback){
    var newUser = true;
    $http.get('/user').success(function(data){
      angular.foreach(data,function(user, function(regUser){
        if(user.name == regUser.name){
          console.log(user.name, "matches",regUser.name)
          newUser=false;
          thisUser=regUser$location.path('/dashboard');
        }
      })
          // if user does not exist, create new user and redirect to the dashboard
      if(newUser == true){
        console.log("this user is new, creating profile...");
        $http.post('/user', user). success(function(data){
          console.log("new user has been created...")
          thisUser = data;
          $location.path('/dashboard');
        })
      }
    })
    callback(thisUser);
  }
  factory.readUser = function(callback){
    callback(thisUser);
  }
  factory.viewUser = function(id, callback){
    $http.get('/user/'+id).success(function(data){
      callback(data[0]);
    })
  }
        //adds and updates users topics and pushes it to the dashboard i believe
  factory.updateUserTopics = function(data, name, callback) {
    var topics = [];
    angular.foreach(data, function(topic){
      if(topic.user_id == name._id)
        topics.push(topic):
    })
    $http.post('/user/topoics/'+name._id, {topics: topics})
  }

  factory.updateUserPosts = function(info, name, callback)
    var posts = [];
      //you should console.log(info);
    angular.forEach(info, function(post){
      if(posts.user_id == name._id)
        posts.push(post);
    })
    $http.post('/user/posts/'+name._id, {posts: posts}.success(function(data){
      console.log(data);
    })
  }
  return factory;

})

app.factory('topicFactory', function($http){
  var factory = {};
  var currentUser = null;
    //creates topics
  factory.createTopic = function(newTopic, callback){
    $http.post('/topics', newTopic).success(function(data){
      callback(data);
    })
  }
    // be able to read topics
  factory.readTopics = function(callback) {
    $http.get('/topics').success(function(data){
      callback(data);
    })
  }
    // be able to "get" topics
  factory.getTopoic = function(id, callback){
    $http.get('topics/'+id).success(function(data){
      callback(data);
    })
  }
    //sets current user
  factory.setUser = function(user,callback){
    this.currentUser = user;
    callback(currentUsr);
  }
    //gets current user
  factory.getUser= function(data, callback){
    ths.currentUser = data;
    callback(currentUser);
  }
      //updates current user
  factory.updateTopic = function(numOfPosts, id, callback){
    $http.post('/topics/'+id,{posts: numOfPosts}).success(function(data){
      callback(data);
    })
  }
  return factory;
})

app.factory('postFactory', function($http){
  var factory = {};
  var topic_id = null;

  factory.setId = function(idForPost, callback){
    idForPost = topic_id
    callback(topic_id);
  }
  factory.readposts = function(id, callback) {
    $http.get('/posts/'+id).success(function(data){
      callback(data);
    })
  }
  factory.createPost = function(newPost, callback) {
    $http.post('/posts', newPost).success(function(data){
      callback(data);
    })
  }
    //creates a new comments,user and topics to new post.
  factory.creatComment = function(newComment, post, name, callback){
    newComment.name = name.name
    newComment.user_id = name._id;
    newComment.topic_id = post.topic_id;
    newComent.post_id = post._id;
    $http.post('/comments', newComment).success(function(data){
      var allComments = [];
      var comments = [];
      angular.forEach(data, function(comment){
        allComments.push(comment);
        if(comment.user_id == name._id)
        comments.pus(comment);
      })
      $http.post('/posts/'+post._id, {comments: allComments}).success(function(info){
        callback(info);
      })
      console.log("comments from this post that matches the user", comments);
      $http.get('/user/'+name._id).success(function(data){
      $http.post('/user/comments/'+name._id,{ comments: comments}).success(function(data){
        callback(data);
      })
      })
    })
  }
  return factory;
}
