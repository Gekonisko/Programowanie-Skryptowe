"use strict";
var __createBinding = (this && this.__createBinding) || (Object.create ? (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    var desc = Object.getOwnPropertyDescriptor(m, k);
    if (!desc || ("get" in desc ? !m.__esModule : desc.writable || desc.configurable)) {
      desc = { enumerable: true, get: function() { return m[k]; } };
    }
    Object.defineProperty(o, k2, desc);
}) : (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    o[k2] = m[k];
}));
var __setModuleDefault = (this && this.__setModuleDefault) || (Object.create ? (function(o, v) {
    Object.defineProperty(o, "default", { enumerable: true, value: v });
}) : function(o, v) {
    o["default"] = v;
});
var __importStar = (this && this.__importStar) || function (mod) {
    if (mod && mod.__esModule) return mod;
    var result = {};
    if (mod != null) for (var k in mod) if (k !== "default" && Object.prototype.hasOwnProperty.call(mod, k)) __createBinding(result, mod, k);
    __setModuleDefault(result, mod);
    return result;
};
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
var _a;
Object.defineProperty(exports, "__esModule", { value: true });
const express_1 = __importDefault(require("express"));
const mongoose_1 = __importDefault(require("mongoose"));
const dotenv_1 = __importDefault(require("dotenv"));
const passport_1 = __importDefault(require("passport"));
const express_session_1 = __importDefault(require("express-session"));
const passport_2 = require("./auth/passport");
const express_acl_1 = __importDefault(require("express-acl"));
const app = (0, express_1.default)();
dotenv_1.default.config();
(0, passport_2.loginCheck)(passport_1.default);
const PORT = process.env.PORT || 4111;
(0, passport_2.loginFacebook)(passport_1.default, PORT);
// Mongo DB conncetion
const database = (_a = process.env.MONGOLAB_URI) !== null && _a !== void 0 ? _a : "mongodb://127.0.0.1:27017/app";
mongoose_1.default
    .connect(database)
    .then(() => console.log(`Connected to mongo: ${database}`))
    .catch((err) => console.log(err));
app.set("view engine", "ejs");
//BodyParsing
app.use(express_1.default.urlencoded({ extended: false }));
app.use((0, express_session_1.default)({
    secret: "oneboy",
    saveUninitialized: true,
    resave: true,
}));
app.use(express_1.default.json());
app.use(passport_1.default.initialize());
app.use(passport_1.default.session());
app.use(function (req, res, next) {
    res.setHeader("Content-Security-Policy", "default-src 'self' 'unsafe-inline'; style-src-elem 'self' 'unsafe-inline' https://cdn.jsdelivr.net; script-src-elem 'self' 'unsafe-inline' https://cdn.jsdelivr.net; img-src 'self' https://getbootstrap.com;");
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
express_acl_1.default.config(configObject, responseObject);
app.use(express_acl_1.default.authorize.unless({
    path: [
        "/login",
        "/register",
        "/logout",
        "/auth/facebook",
        "/auth/facebook/callback",
    ],
}));
//Routes
Promise.resolve().then(() => __importStar(require("./routes/login"))).then((module) => app.use("/", module.router));
app.listen(PORT, () => console.log("Server has started at port " + PORT));
