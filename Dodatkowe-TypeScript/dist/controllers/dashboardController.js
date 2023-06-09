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
Object.defineProperty(exports, "__esModule", { value: true });
exports.DashboardController = void 0;
const Book_1 = require("../models/Book");
const models_1 = require("../models/models");
class DashboardController {
    dashboardView(req, res) {
        res.render(models_1.Views.DASHBOARD, {
            user: req.user,
        });
    }
    addBookView(req, res) {
        res.render(models_1.Views.ADD_BOOK, {
            user: req.user,
            typeBookCover: Object.values(models_1.TypeBookCover),
        });
    }
    allBooksView(req, res) {
        return __awaiter(this, void 0, void 0, function* () {
            const books = yield Book_1.BookModel.find({});
            res.render(models_1.Views.ALL_BOOKS, {
                user: req.user,
                books,
            });
        });
    }
    addBook(req, res) {
        return __awaiter(this, void 0, void 0, function* () {
            const book = req.body;
            if (isNaN(parseFloat(book.quantity))) {
                return res.send("Quantity must be a number");
            }
            const result = yield Book_1.BookModel.findOne({ title: book.title });
            if (result) {
                console.log("This book exist");
                return res.send("This title book exist");
            }
            else {
                yield Book_1.BookModel.insertMany(book);
                return res.send("Book added");
            }
        });
    }
}
exports.DashboardController = DashboardController;
