var http = require('http');
var fs = require('fs');
var server = http.createServer(function (request, response){

  if(request.url === '/views/cars.html'){
    fs.readFile('./views/cars.html', 'utf8', function(error, contents){
      response.writeHead(200, {'Content-Type': 'text/html'});
      response.write(contents);
      response.end();
    });
  }
  if(request.url == '/images/mystmach.jpg'){
    fs.readFile('./images/mystmach.jpg', function(error, contents){
      response.writeHead(200, {'Content-Type': 'image/jpg'});
      response.write(contents);
      response.end();
    })
  }
})
server.listen(6789);
