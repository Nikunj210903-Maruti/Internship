var express=require("express")
var path=require("path");
var app=express()

const publicPath = path.join(__dirname, '/public');

app.use(express.static(publicPath));


app.get("/",function(req,res){
res.sendFile("public/assignment_1.html",{root:__dirname});
});


app.listen(3000,()=>
{
	console.log("server is running at port : 3000")
})