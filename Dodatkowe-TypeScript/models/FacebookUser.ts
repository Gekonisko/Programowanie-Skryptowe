import mongoose from "mongoose";

const FacebookUserSchema = new mongoose.Schema({
  facebookId: {
    type: String,
  },
  name: {
    type: String,
  },
  role: {
    type: String,
    default: "user",
  },
});

export interface FacebookUserDto {
  facebookId: string;
  name: string;
  role: string;
}

export const FacebookUser = mongoose.model<FacebookUserDto>(
  "FacebookUser",
  FacebookUserSchema
);
