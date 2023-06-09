"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.BookModel = exports.Book = void 0;
const mongoose_1 = __importDefault(require("mongoose"));
class Book {
    constructor(title, author, quantity) {
        this.title = title;
        this.author = author;
        this.quantity = quantity;
    }
}
exports.Book = Book;
const BookSchema = new mongoose_1.default.Schema({
    title: {
        type: String,
    },
    author: {
        type: String,
    },
    quantity: {
        type: Number,
    },
    isbn: {
        type: String,
    },
    typeBookCover: {
        type: String,
    },
    description: {
        type: String,
    },
    pages: {
        type: Number,
    },
    releaseData: {
        type: Date,
    },
});
exports.BookModel = mongoose_1.default.model("Book", BookSchema);
