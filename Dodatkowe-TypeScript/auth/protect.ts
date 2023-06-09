import { Request, Response, NextFunction } from "express";

export function protectRoute(
  req: Request,
  res: Response,
  next: NextFunction
): void {
  if (req.isAuthenticated()) {
    console.log((req.user as any).role);
    return next();
  }
  console.log("Please log in to continue");
  res.redirect("/login");
}
