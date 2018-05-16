var express = require('express');
var app = express();
var mongoose = require('mongoose');

var routingController = require('./controllers/routingController');

/*var PythonShell = require('python-shell');

var pyshell = new PythonShell('python/chatbot.py');
pyshell.send('Hey there');
pyshell.on('message', function (message) {
  // received a message sent from the Python script (a simple "print" statement)
  console.log(message);
});*/


var http = require('http').Server(express);

    

var port = 3000;

app.use('/assets', express.static(__dirname + '/public') );
app.use('/', express.static(__dirname + '/public'));

app.set('view engine', 'ejs');

routingController(app);

var server = app.listen(port,function(){
  console.log('listening on *:3000');
});

var io = require('socket.io')(http).listen(server);

io.on('connection', function(socket){
  console.log('a user connected');
  socket.on('request', function(msg){
    socket.emit('response', 'Response is:'+msg);
    console.log('message: ' + msg);
  });
  socket.on('disconnect', function(){
    console.log('user disconnected');
  });
});