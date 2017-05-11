// ge the http module:
var http = require('http');
//fs module allows us to read and write content for our responses!!
var fs = require('fs');
//creating a server ising the htpp module:
var server = http.createServer(function (request, response){
  //see what URL the clients are requesting:
  console.log('client request  URL:', request.url);
  //this is how we do routing:
  var file;
  console.log("URL:", request.url)
  switch (request.url) {
    case "/":
      file = "index.html"
      break;
    case "/ninjas":
      file = "ninjas.html"
      break;
    case "/dojo/new":
      file = "dojo.html"
      break;
    default:
      file = null;
          break;
  }
  //`static/${file}` === 'static/' + file
  //  send file or error to browser
  if (file!== null){
    fs.readFile(`static/${file}`, 'utf8', function(error, contents){
      if (error) {  console.log(error);  }
      response.writeHead(200, {'Content-Type': 'text/html'});
      response.write(contents);
      response.end()
    });
  } else{ //if file is null or not found
    response.writeHead(404);
    response.end("file aint` found!!!!!!");
  }
});

//tell your server wich port to run on
server.listen(6789);
//presponserint to terminal window
console.log("Running in localhost at port 6789");
