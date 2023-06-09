import bcrypt from "bcryptjs";
import { PassportStatic } from "passport";
import { Strategy } from "passport-facebook";
import { Strategy as LocalStrategy } from "passport-local";
import { FacebookUser, FacebookUserDto } from "../models/FacebookUser";
import { User, UserDto } from "../models/User";

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
    done(null, user);
  });

  passport.deserializeUser((id: UserDto | FacebookUserDto, done) => {
    if ((id as FacebookUserDto).facebookId) {
      FacebookUser.findById(id, null, null, (error, user) => {
        done(error, user);
      });
    } else {
      User.findById(id, null, null, (error, user) => {
        done(error, user);
      });
    }
  });
}

export function loginFacebook(passport: PassportStatic, PORT: string | number) {
  passport.use(
    new Strategy(
      {
        clientID: "894274098379880",
        clientSecret: "e7f00bbaa98a9d720823b9ff89435fbc",
        callbackURL: `http://localhost:${PORT}/auth/facebook/callback`,
      },
      async function (accessToken, refreshToken, profile, done) {
        let user = await FacebookUser.findOne({
          facebookId: profile.id,
        });

        if (user == undefined) {
          done(
            null,
            await FacebookUser.create({
              facebookId: profile.id,
              name: profile.displayName,
            })
          );
        } else {
          done(null, user);
        }
      }
    )
  );
}
