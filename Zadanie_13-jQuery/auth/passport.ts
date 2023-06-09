import bcrypt from "bcryptjs";
import { PassportStatic } from "passport";
import { Strategy as LocalStrategy } from "passport-local";
import { User } from "../models/User";

//Load model
export function loginCheck(passport: PassportStatic): void {
  passport.use(
    new LocalStrategy(
      { usernameField: "email" },
      async (email, password, done) => {
        const user = await User.findOne({ email: email }).catch((error) =>
          console.log(error)
        );

        if (!user) {
          console.log("wrong email");
          return done("wrong email");
        }

        //Match Password
        bcrypt.compare(password, user.password, (error, isMatch) => {
          if (error) throw error;
          if (isMatch) {
            return done(null, user);
          } else {
            console.log("Wrong password");
            return done("Wrong password");
          }
        });
      }
    )
  );

  passport.serializeUser((user, done) => {
    console.log("serializeUser");
    done(null, user);
  });

  passport.deserializeUser((id, done) => {
    User.findById(id, null, null, (error, user) => {
      console.log("deserializeUser");
      done(error, user);
    });
  });
}
