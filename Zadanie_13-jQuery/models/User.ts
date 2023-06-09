import mongoose from "mongoose";

const UserSchema = new mongoose.Schema({
  name: {
    type: String,
    required: true,
  },
  email: {
    type: String,
    required: true,
  },
  password: {
    type: String,
    required: true,
  },
  location: {
    type: String,
    default: "Kraków",
  },
  date: {
    type: Date,
    default: Date.now,
  },
});

export interface UserDto {
  name: string;
  email: string;
  password: string;
  location: string;
  date: string;
}

export const User = mongoose.model<UserDto>("User", UserSchema);
