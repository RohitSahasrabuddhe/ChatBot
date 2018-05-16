var fs = require('fs');



module.exports = function(app){
    
    //app.use(bodyParser.json());
    //app.use(bodyParser.urlencoded({ extended: true}));
    
    /* app.get('/signUp', function(req,res){
         res.render('signup');   
              
     });*/
    
    app.get('/', function(req,res){
         res.render('index');              
     });
    
    
    
    /*app.get('/logIn', function(req,res){
         res.render('login');   
              
     });*/
    
};