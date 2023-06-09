"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.BookDetails = void 0;
const Book_1 = require("./Book");
class BookDetails extends Book_1.Book {
    constructor(title, author, quantity, isbn, typeBookCover, description, pages, data) {
        super(title, author, quantity);
        this.isbn = isbn;
        this.typeBookCover = typeBookCover;
        this.description = description;
        this.pages = pages;
        this.releaseData = data;
    }
}
exports.BookDetails = BookDetails;
