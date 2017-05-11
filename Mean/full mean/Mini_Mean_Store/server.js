var express = require('express');
var path = require('path');
var bodyParser = require('body-Parser');
var app = express();

var server = app.listen(800, function(){
  console.log("listening on port 8000");
});
app.use(express.static(path.join(__dirname, '.client')));
app.use(bodyParser.urlencoded({extended: true}));
app.use(bodyParser.json());

app.set('views',path.join(__dirname, './client'));
app.set('view engine', 'ejs');

require("./config/mongoose.js");
io=require('socket.io').listen(server);

io.sockets.on('connection', function(socket){
    //when (Listener) On connection
  console.log("connected - Socket ID: ", socket.id);
    //when (Listener) On disconnection
  socket.on('disconnect', function() {
    console.log("Disconnected - Socket ID: ", socket.id);
  })
    //when (listener) topic being added
  socket.on('created_topic', function(data){
    socket.broadcast.emit('topic_added', data);
  })
});

require("./config/routes.js")(app);
