"use strict";
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.LoginController = void 0;
const bcryptjs_1 = __importDefault(require("bcryptjs"));
const passport_1 = __importDefault(require("passport"));
const User_1 = require("../models/User");
class LoginController {
    registerView(req, res) {
        res.render("register", {});
    }
    registerUser(req, res) {
        return __awaiter(this, void 0, void 0, function* () {
            const { name, email, location, password, confirm } = req.body;
            if (!name || !email || !password || !confirm) {
                console.log("Fill empty fields");
            }
            if (password !== confirm) {
                console.log("Password must match");
            }
            else {
                const user = yield User_1.User.findOne({ email: email });
                if (user) {
                    console.log("email exists");
                    res.render("register", {
                        name,
                        email,
                        password,
                        confirm,
                    });
                }
                else {
                    const newUser = new User_1.User({
                        name,
                        email,
                        location,
                        password,
                    });
                    bcryptjs_1.default.genSalt(10, (err, salt) => bcryptjs_1.default.hash(newUser.password, salt, (err, hash) => __awaiter(this, void 0, void 0, function* () {
                        if (err)
                            throw err;
                        newUser.password = hash;
                        yield newUser.save().catch((err) => console.log(err));
                        res.redirect("/login");
                    })));
                }
            }
        });
    }
    loginView(req, res) {
        res.render("login", {});
    }
    loginUser(req, res) {
        const { email, password } = req.body;
        console.log(req.body);
        if (!email || !password) {
            console.log("Please fill in all the fields");
            res.render("login", {
                email,
                password,
            });
        }
        else {
            passport_1.default.authenticate("local", {
                successRedirect: "/dashboard",
                failureRedirect: "/login",
                failureFlash: true,
            })(req, res);
        }
    }
    logout(req, res) {
        req.logout(() => {
            res.redirect("/login");
        });
    }
    facebookLogged(req, res) {
        res.redirect("/dashboard");
    }
}
exports.LoginController = LoginController;
