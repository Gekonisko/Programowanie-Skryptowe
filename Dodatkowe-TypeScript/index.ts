import express from "express";
import mongoose, { CallbackError } from "mongoose";
import dotenv from "dotenv";
import passport from "passport";
import session from "express-session";
import { loginCheck, loginFacebook } from "./auth/passport";
import acl from "express-acl";

const app = express();
dotenv.config();
loginCheck(passport);
const PORT = process.env.PORT || 4111;
loginFacebook(passport, PORT);

// Mongo DB conncetion
const database: string =
  process.env.MONGOLAB_URI ?? "mongodb://127.0.0.1:27017/app";

mongoose
  .connect(database)
  .then(() => console.log(`Connected to mongo: ${database}`))
  .catch((err) => console.log(err));

app.set("view engine", "ejs");

//BodyParsing
app.use(express.urlencoded({ extended: false }));
app.use(
  session({
    secret: "oneboy",
    saveUninitialized: true,
    resave: true,
  })
);
app.use(express.json());
app.use(passport.initialize());
app.use(passport.session());

app.use(function (req, res, next) {
  res.setHeader(
    "Content-Security-Policy",
    "default-src 'self' 'unsafe-inline'; style-src-elem 'self' 'unsafe-inline' https://cdn.jsdelivr.net; script-src-elem 'self' 'unsafe-inline' https://cdn.jsdelivr.net; img-src 'self' https://getbootstrap.com;"
  );
  res.setHeader("X-Frame-Options", "DENY");
  res.removeHeader("X-Powered-By");
  next();
});

//ACL
const configObject = {
  filename: "acl.json",
  baseUrl: "/",
  decodedObjectName: "user",
  roleSearchPath: "user.role",
};

let responseObject = {
  status: "Access Denied",
  message: "You are not authorized to access this resource",
};

acl.config(configObject, responseObject);
app.use(
  acl.authorize.unless({
    path: [
      "/login",
      "/register",
      "/logout",
      "/auth/facebook",
      "/auth/facebook/callback",
    ],
  })
);

//Routes
import("./routes/login").then((module) => app.use("/", module.router));

app.listen(PORT, () => console.log("Server has started at port " + PORT));
