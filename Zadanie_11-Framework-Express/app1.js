// No use of any template system
var express = require("express"),
  logger = require("morgan");
const { MongoClient } = require("mongodb");
var fs = require("fs");
var app = express();
var x = 1;
var y = 2;

// Determining the contents of the middleware stack
app.use(logger("dev")); // Place an HTTP request recorder on the stack — each request will be logged in the console in 'dev' format
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

let operationResult = (operation) => {
  switch (operation.sign) {
    case "+":
      return operation.x + operation.y;
    case "-":
      return operation.x - operation.y;
    case "*":
      return operation.x * operation.y;
    case "/":
      return operation.x / operation.y;
  }
};
// *** Route definitions ***

// The first route
app.get("/", function (req, res) {
  res.send(`
<!DOCTYPE html>
<html lang="en" data-bs-theme="dark">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link
      href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css"
      rel="stylesheet"
      integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD"
      crossorigin="anonymous">
    <title>Your first page</title>
  </head>
  <body>
    <main class="container">
      <h1>Hello World</h1>
      <div>${x} + ${y} = ${x + y}</div>
    </main>
    <script
      src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js"
      integrity="sha384-w76AqPfDkMBDXo30jS1Sgez6pr3x5MlQ1ZAGC+nuZB+EYdgRZgiwxhTBTkF7CXvN"
      crossorigin="anonymous">
    </script>
  </body>
</html>
`); // Send a response to the browser
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
    res.send(
      `Operacja: <div>${req.params.x} ${req.params.operation} ${req.params.y
      } = <span>${operationResult({
        sign: req.params.operation,
        x: parseFloat(req.params.x),
        y: parseFloat(req.params.y),
      })}</span>`
    );
  } else {
    res.send(
      `Operacja nieobługiwana: ${req.params.x} ${req.params.operation} ${req.params.y}`
    );
  }
});

app.get("/json/:name", function (req, res) {
  try {
    var file = fs.readFileSync(`./resources/${req.params.name}.json`, "utf-8");
  } catch {
    res.send(`Not found file: ${req.params.name}.json`);
  }

  let operations = JSON.parse(file);

  let operationTable = "";
  for (const operation of operations) {
    operationTable += `
      <tr>
          <td>${operation.x}</td>
          <td>${operation.znak}</td>
          <td>${operation.y}</td>
          <td>${operationResult({
      sign: operation.znak,
      x: operation.x,
      y: operation.y,
    })}</td>
      </tr>
    `;
  }

  res.send(`
<!DOCTYPE html>
<html lang="en" data-bs-theme="dark">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link
      href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css"
      rel="stylesheet"
      integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD"
      crossorigin="anonymous">
    <title>Your first page</title>
  </head>
  <body>
    <main class="container">
      <h1>Hello World</h1>
      <table class="table">
        <tr>
          <th>x</th>
          <th>Operation</th>
          <th>y</th>
          <th>Result</th>
        </tr>
        ${operationTable}
      </table>
    </main>
    <script
      src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js"
      integrity="sha384-w76AqPfDkMBDXo30jS1Sgez6pr3x5MlQ1ZAGC+nuZB+EYdgRZgiwxhTBTkF7CXvN"
      crossorigin="anonymous">
    </script>
  </body>
</html>
`);
});

app.get("/results", async function (req, res) {
  const client = new MongoClient(url);
  await client.connect();
  const db = client.db("mongo");
  const collection = db.collection("operacje");
  const results = await collection.find({}).toArray();

  let operationTable = "";
  for (const result of results) {
    operationTable += `
      <tr>
          <td>${result.x}</td>
          <td>${result.operation}</td>
          <td>${result.y}</td>
          <td>${operationResult({
      sign: result.operation,
      x: result.x,
      y: result.y,
    })}</td>
      </tr>
    `;
  }
  res.send(`
<!DOCTYPE html>
<html lang="en" data-bs-theme="dark">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link
      href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css"
      rel="stylesheet"
      integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD"
      crossorigin="anonymous">
    <title>Your first page</title>
  </head>
  <body>
    <main class="container">
      <h1>Hello World</h1>
      <table class="table">
        <tr>
          <th>x</th>
          <th>Operation</th>
          <th>y</th>
          <th>Result</th>
        </tr>
        ${operationTable}
      </table>
    </main>
    <script
      src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js"
      integrity="sha384-w76AqPfDkMBDXo30jS1Sgez6pr3x5MlQ1ZAGC+nuZB+EYdgRZgiwxhTBTkF7CXvN"
      crossorigin="anonymous">
    </script>
  </body>
</html>
`);
});

// The application is to listen on port number 3000
app.listen(3000, function () {
  console.log("The application is available on port 3000");
});
