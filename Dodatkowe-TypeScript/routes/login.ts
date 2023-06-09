import express from "express";
import passport from "passport";
import { protectRoute } from "../auth/protect";
import { DashboardController } from "../controllers/dashboardController";
import { LoginController } from "../controllers/loginController";

export const router = express.Router();

const dashboardController = new DashboardController();
const loginController = new LoginController();

router.get("/register", loginController.registerView);
router.get("/login", loginController.loginView);

//Dashboard
router.get("/dashboard", protectRoute, dashboardController.dashboardView);
router.get("/dashboard/books", protectRoute, dashboardController.allBooksView);
router.get(
  "/dashboard/add-book",
  protectRoute,
  dashboardController.addBookView
);

router.post("/addBook", protectRoute, dashboardController.addBook);
router.post("/register", loginController.registerUser);
router.post("/login", loginController.loginUser);

router.get("/auth/facebook", passport.authenticate("facebook"));
router.get("/logout", loginController.logout);
router.get(
  "/auth/facebook/callback",
  passport.authenticate("facebook", { failureRedirect: "/login" }),
  loginController.facebookLogged
);
