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
exports.loginFacebook = exports.loginCheck = void 0;
const bcryptjs_1 = __importDefault(require("bcryptjs"));
const passport_facebook_1 = require("passport-facebook");
const passport_local_1 = require("passport-local");
const FacebookUser_1 = require("../models/FacebookUser");
const User_1 = require("../models/User");
//Load model
function loginCheck(passport) {
    passport.use(new passport_local_1.Strategy({ usernameField: "email" }, (email, password, done) => __awaiter(this, void 0, void 0, function* () {
        const user = yield User_1.User.findOne({ email: email }).catch((error) => console.log(error));
        if (!user) {
            console.log("wrong email");
            return done("wrong email");
        }
        //Match Password
        bcryptjs_1.default.compare(password, user.password, (error, isMatch) => {
            if (error)
                throw error;
            if (isMatch) {
                return done(null, user);
            }
            else {
                console.log("Wrong password");
                return done("Wrong password");
            }
        });
    })));
    passport.serializeUser((user, done) => {
        done(null, user);
    });
    passport.deserializeUser((id, done) => {
        if (id.facebookId) {
            FacebookUser_1.FacebookUser.findById(id, null, null, (error, user) => {
                done(error, user);
            });
        }
        else {
            User_1.User.findById(id, null, null, (error, user) => {
                done(error, user);
            });
        }
    });
}
exports.loginCheck = loginCheck;
function loginFacebook(passport, PORT) {
    passport.use(new passport_facebook_1.Strategy({
        clientID: "894274098379880",
        clientSecret: "e7f00bbaa98a9d720823b9ff89435fbc",
        callbackURL: `http://localhost:${PORT}/auth/facebook/callback`,
    }, function (accessToken, refreshToken, profile, done) {
        return __awaiter(this, void 0, void 0, function* () {
            let user = yield FacebookUser_1.FacebookUser.findOne({
                facebookId: profile.id,
            });
            if (user == undefined) {
                done(null, yield FacebookUser_1.FacebookUser.create({
                    facebookId: profile.id,
                    name: profile.displayName,
                }));
            }
            else {
                done(null, user);
            }
        });
    }));
}
exports.loginFacebook = loginFacebook;
