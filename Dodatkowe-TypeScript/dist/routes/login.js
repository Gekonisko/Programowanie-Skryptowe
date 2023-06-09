"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.router = void 0;
const express_1 = __importDefault(require("express"));
const passport_1 = __importDefault(require("passport"));
const protect_1 = require("../auth/protect");
const dashboardController_1 = require("../controllers/dashboardController");
const loginController_1 = require("../controllers/loginController");
exports.router = express_1.default.Router();
const dashboardController = new dashboardController_1.DashboardController();
const loginController = new loginController_1.LoginController();
exports.router.get("/register", loginController.registerView);
exports.router.get("/login", loginController.loginView);
//Dashboard
exports.router.get("/dashboard", protect_1.protectRoute, dashboardController.dashboardView);
exports.router.get("/dashboard/books", protect_1.protectRoute, dashboardController.allBooksView);
exports.router.get("/dashboard/add-book", protect_1.protectRoute, dashboardController.addBookView);
exports.router.post("/addBook", protect_1.protectRoute, dashboardController.addBook);
exports.router.post("/register", loginController.registerUser);
exports.router.post("/login", loginController.loginUser);
exports.router.get("/auth/facebook", passport_1.default.authenticate("facebook"));
exports.router.get("/logout", loginController.logout);
exports.router.get("/auth/facebook/callback", passport_1.default.authenticate("facebook", { failureRedirect: "/login" }), loginController.facebookLogged);
