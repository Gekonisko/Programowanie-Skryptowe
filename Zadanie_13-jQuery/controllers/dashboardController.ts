import { Request, Response } from "express";
import { Book, BookModel } from "../models/Book";
import { TypeBookCover, Views } from "../models/models";

export class DashboardController {
  public dashboardView(req: Request, res: Response) {
    res.render(Views.DASHBOARD, {
      user: req.user,
    });
  }

  public addBookView(req: Request, res: Response) {
    res.render(Views.ADD_BOOK, {
      user: req.user,
      typeBookCover: Object.values(TypeBookCover),
    });
  }

  public async allBooksView(req: Request, res: Response) {
    const books = await BookModel.find({});
    res.render(Views.ALL_BOOKS, {
      user: req.user,
      books,
    });
  }

  public async addBook(req: Request, res: Response) {
    const book = req.body;

    if (isNaN(parseFloat(book.quantity))) {
      return res.send("Quantity must be a number");
    }

    const result = await BookModel.findOne({ title: book.title });
    if (result) {
      console.log("This book exist");
      return res.send("This title book exist");
    } else {
      await BookModel.insertMany(book);
      return res.send("Book added");
    }
  }
}
