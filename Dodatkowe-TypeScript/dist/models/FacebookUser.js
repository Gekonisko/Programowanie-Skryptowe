"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.FacebookUser = void 0;
const mongoose_1 = __importDefault(require("mongoose"));
const FacebookUserSchema = new mongoose_1.default.Schema({
    facebookId: {
        type: String,
    },
    name: {
        type: String,
    },
    role: {
        type: String,
        default: "user",
    },
});
exports.FacebookUser = mongoose_1.default.model("FacebookUser", FacebookUserSchema);
