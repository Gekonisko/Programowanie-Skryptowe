// Application using the 'Pug' template system
var express = require("express"),
  logger = require("morgan");
var fs = require("fs");
const { MongoClient } = require("mongodb");
var app = express();
var x = 1;
var y = 2;

// Configuring the application
app.set("views", __dirname + "/views"); // Files with views can be found in the 'views' directory
app.set("view engine", "pug"); // Use the 'Pug' template system
app.locals.pretty = app.get("env") === "development"; // The resulting HTML code will be indented in the development environment

// Determining the contents of the middleware stack
app.use(logger("dev")); // Add an HTTP request recorder to the stack — every request will be logged in the console in the 'dev' format
// app.use(express.static(__dirname + '/public')); // Place the built-in middleware 'express.static' — static content (files .css, .js, .jpg, etc.) will be provided from the 'public' directory
const url = "mongodb://127.0.0.1:27017";

async function saveToMongo(operation) {
  const client = new MongoClient(url);
  await client.connect();
  const db = client.db("mongo");
  const collection = db.collection("operacje");
  const result = await collection.findOne(operation);
  if (result) {
    console.log("Operacja już istnieje", JSON.stringify(operation));
  } else {
    await collection.insertOne(operation);
    console.log("Insert Document", JSON.stringify(operation));
  }
  client.close();
}
// *** Route definitions ***

// The first route
app.get("/", function (req, res) {
  res.render("index", { x, y }); // Render the 'index' view
});

app.get("/json/:name", function (req, res) {
  try {
    var file = fs.readFileSync(`./resources/${req.params.name}.json`, "utf-8");
  } catch {
    res.send(`Not found file: ${req.params.name}.json`);
  }
  return res.render("operacje", { operations: JSON.parse(file) });
});

app.get("/calculate/:operation/:x/:y", function (req, res) {
  if (
    ["+", "-", "/", "*"].some((sign) => sign == req.params.operation) &&
    !isNaN(parseFloat(req.params.x)) &&
    !isNaN(parseFloat(req.params.y))
  ) {
    let operation = {
      operation: req.params.operation,
      x: parseFloat(req.params.x),
      y: parseFloat(req.params.y),
    };
    saveToMongo(operation);
    return res.render("mongo", {
      params: operation,
    });
  } else {
    res.send(
      `Operacja nieobługiwana: ${req.params.x} ${req.params.operation} ${req.params.y}`
    );
  }
});

app.get("/results", async function (req, res) {
  const client = new MongoClient(url);
  await client.connect();
  const db = client.db("mongo");
  const collection = db.collection("operacje");
  const results = await collection.find({}).toArray();

  return res.render("mongo_result", {
    results,
  });
});

// The application is to listen on port number 3000
app.listen(3000, function () {
  console.log("The application is available on port 3000");
});
