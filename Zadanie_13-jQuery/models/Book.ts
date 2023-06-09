import mongoose from "mongoose";

export class Book {
  public title: string;
  public author: string;
  public quantity: number;

  constructor(title: string, author: string, quantity: number) {
    this.title = title;
    this.author = author;
    this.quantity = quantity;
  }
}

const BookSchema = new mongoose.Schema({
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

export const BookModel = mongoose.model<Book>("Book", BookSchema);
