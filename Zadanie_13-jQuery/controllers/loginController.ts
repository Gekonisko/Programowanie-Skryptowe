import bcrypt from "bcryptjs";
import passport from "passport";
import { Request, Response } from "express";
import { User } from "../models/User";

export class LoginController {
  public registerView(req: Request, res: Response): void {
    res.render("register", {});
  }

  public async registerUser(req: Request, res: Response): Promise<void> {
    const { name, email, location, password, confirm } = req.body;

    if (!name || !email || !password || !confirm) {
      console.log("Fill empty fields");
    }

    if (password !== confirm) {
      console.log("Password must match");
    } else {
      const user = await User.findOne({ email: email });
      if (user) {
        console.log("email exists");
        res.render("register", {
          name,
          email,
          password,
          confirm,
        });
      } else {
        const newUser = new User({
          name,
          email,
          location,
          password,
        });
        bcrypt.genSalt(10, (err, salt) =>
          bcrypt.hash(newUser.password, salt, async (err, hash) => {
            if (err) throw err;

            newUser.password = hash;
            await newUser.save().catch((err) => console.log(err));
            res.redirect("/login");
          })
        );
      }
    }
  }

  public loginView(req: Request, res: Response): void {
    res.render("login", {});
  }

  public loginUser(req: Request, res: Response): void {
    const { email, password } = req.body;

    if (!email || !password) {
      console.log("Please fill in all the fields");
      res.render("login", {
        email,
        password,
      });
    } else {
      passport.authenticate("local", {
        successRedirect: "/dashboard",
        failureRedirect: "/login",
        failureFlash: true,
      })(req, res);
    }
  }
}
