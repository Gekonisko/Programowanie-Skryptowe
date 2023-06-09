const express = require("express");
const logger = require("morgan");
/************* */
const app1 = express();
const app2 = express();
/************* */
app1.use(logger("dev"));
app2.use(logger("dev"));
/************* */

// Configuring the application
app1.set("views", __dirname + "/views");
app1.set("view engine", "pug");
app2.set("views", __dirname + "/views");
app2.set("view engine", "pug");

app1.listen(3000, function () {
  console.log("The application is available on port 3000");
});
app2.listen(3001, function () {
  console.log("The application is available on port 3001");
});
/************* */
app1.get("/", function (req, res) {
  res.render("time");
});

app2.get("/", function (req, res) {
  let date = new Date();
  const localDate = date.toLocaleDateString("pl-PL", {
    year: "numeric",
    month: "2-digit",
    day: "2-digit",
  });

  const localTime = date.toLocaleTimeString("pl-PL");
  res.setHeader("Access-Control-Allow-Origin", "*");
  res.send(`
  <?xml version="1.0" encoding="UTF-8"?>
  <div>
  <span id="date">${localDate}</span>
  <span id="time">${localTime}</span>
  </div>`);
});
/************* */
console.log("To stop the server, press 'CTRL + C'");
