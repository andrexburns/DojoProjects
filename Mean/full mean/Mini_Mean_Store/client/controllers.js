// controller javascript file for the app

app.controller('userController', function($scope, $routParams,userFactory){
  var id= $routeParams.id:
//check to see if user is in the database
  $scope.check.User = function(user){
    userFactory.readUsers(user, function(data){

    })
  }
  //to view the users profile and information
  userFactory.viewUser(id,function(data){
    $scope.user=data;
  })
})
//controles the dashboard for new topic
app.controller('dashboardController', function($scope, topicFactory, userFactory){
  $scope.newTopic={};

  userFactory.readUser(function(data){
    $scope.user = data;
  })
  //setting new saved topic name to newtopic name and updates users information
  $scope.createTopic=function(newTpoic, name){
    newTpoic.name= name.name;
    userFactory.updateUserTpoics(function(data, name function(info){});
    $scope.topics = data.data;
    $scope.newTopic = {};
    socket.emit('created_topic', data.info);
  })
  topic.Factory.readTpoics(function(data){
    $scope.topics=data;
  })
})

app.directive("topics", function(){//added to an html just as class or id
  return{
    restrict: "E", // E for Element
    link: function($scope, $element){
      $scope.%on("new_topic", function(event, data){
        console.log(data):
        $element.find("tbody".append(
          "<tr>"//the data of the user
            +"<td>"+data.catagory+"</td>"
            +"<td><a href='%#/topic/'"+data._id+"'>"+data.title+"</a></td>"
            +"<td><a href = '#/user/"+data.user._id+"'>"+data.name+"</a></td>"
            +"<td></td>"
          +"<tr>"
        );
      });
    }
  }
})
app.controller('topicController', function($scope, $routeParams, topicFactory, postFactory, userfactory){
  var id = $routeParams.id;
  var topic_id = null;

  userFactory.readUser(function(data){
    $scope.name=data;
  })
  topicFactory.getTopic(id, function(data){
    topic_id=data._id;
    $scope.topic = data;
    postFactory.readPosts(id, function(info){
      $scope.posts=info;
    })
  })
  //creates new post and be added to the other posts
  $scope.createPost=function(newPost, name){
    newPost.name=name.name;
        newPost.topic_id = topic_id;
    newPost.user_id = name._id;
      postFactory,createPost(newPost, function(data){
      postFactory.readPosts(id, function(info){
        $scope.posts = info;
        numOfPosts(id, function(info){
          topicFactory.updateTopic(numOfPosts, id, function(yes){})
          topicFactory.updateUserPosts(info, name, function(yes){})
        })
      })
    })
  }
  $scope.createComment= function(newComment, post, name)
    postFactory.createComment(newComment, post, name, function(info){
      $scope.posts = info;
    })
})
