"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.protectRoute = void 0;
function protectRoute(req, res, next) {
    if (req.isAuthenticated()) {
        console.log(req.user.role);
        return next();
    }
    console.log("Please log in to continue");
    res.redirect("/login");
}
exports.protectRoute = protectRoute;
