import { Book } from "./Book";
import { TypeBookCover } from "./models";

export class BookDetails extends Book {
  public isbn: string;
  public typeBookCover: TypeBookCover;
  public description: string;
  public pages: number;
  public releaseData: Date;

  constructor(
    title: string,
    author: string,
    quantity: number,
    isbn: string,
    typeBookCover: TypeBookCover,
    description: string,
    pages: number,
    data: Date
  ) {
    super(title, author, quantity);
    this.isbn = isbn;
    this.typeBookCover = typeBookCover;
    this.description = description;
    this.pages = pages;
    this.releaseData = data;
  }
}
