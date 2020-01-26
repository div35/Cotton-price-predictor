var express = require("express");
// var bodyParser = require('body-parser');
var {input} = require("./input");
var app = express();
app.use(express.json());
app.use(express.static("public"));
app.set("view engine","ejs");
app.use(express.urlencoded({extended : true}));


var viewinput = async (req , res) => {
    res.status(201).render("index");
}

let inputrouter = express.Router();
inputrouter.route("/input").post(input);
app.use("/api", inputrouter);

let viewrouter = express.Router();
viewrouter.route("/view").get(viewinput);
app.use("" , viewrouter);

app.listen(3000 , function(){
    console.log("Listening on port 3000");
})
