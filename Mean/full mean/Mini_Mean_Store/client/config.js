//configuration java script file

var app = angular.module("app", ['ngRoute']);

app.config(function($routeProvider){
  $routeProvider
  .when('/' {
    templateUrl: '/main.ejs',
    controller: 'userController'
  })
  //when statements
  .when('/dhashboard',{
    templateUrl: "/dashboard.ejs",
    controller: 'dashbordController'
  })
  .when("topic/:id",{
    templateUrl: '/topic.ejs',
    controller: 'topicController'
  })
  .when('/user/:id',{
    templateUrl: '/user.ejs',
    controller: 'userController'
  })
  //like an else statement
  .otherwise({
    redirectTo: '/'
  })
})
