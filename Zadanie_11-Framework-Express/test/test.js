//Source:  https://codeforgeek.com/unit-testing-nodejs-application-using-mocha/
const { assert, expect } = require("chai");
var supertest = require("supertest");
var chai = require("chai");
chai.use(require("chai-json"));

// This agent refers to PORT where program is runninng.
var server = supertest.agent("http://localhost:3000");

// UNIT test begin
describe("GET /", function () {
  it("respond with html", function (done) {
    server.get("/").expect("Content-Type", /html/).expect(200, done);
  });

  it("sum 1 + 2", function (done) {
    server.get("/").end((err, res) => {
      expect(res.text).to.be.contain("<div>1 + 2 = 3</div>");
      return done();
    });
  });
});

describe("GET /json/:name", function () {
  it("operations: test.json", function (done) {
    server.get("/json/test").end((err, res) => {
      expect(res.text).to.be.contain(
        `<td>2</td>\n          <td>*</td>\n          <td>2</td>\n          <td>4</td>`
      );
      expect(res.text).to.be.contain(
        `<td>1</td>\n          <td>+</td>\n          <td>2</td>\n          <td>3</td>`
      );
      expect(res.text).to.be.contain(
        `<td>3</td>\n          <td>-</td>\n          <td>2</td>\n          <td>1</td>`
      );
      expect(res.text).to.be.contain(
        `<td>6</td>\n          <td>/</td>\n          <td>2</td>\n          <td>3</td>`
      );

      expect(`./resources/test.json`)
        .to.be.a.jsonFile()
        .and.contain.jsonWithProps({
          znak: "+",
          x: 1,
          y: 2,
        })
        .and.contain.jsonWithProps({
          znak: "-",
          x: 3,
          y: 2,
        })
        .and.contain.jsonWithProps({
          znak: "*",
          x: 2,
          y: 2,
        })
        .and.contain.jsonWithProps({
          znak: "/",
          x: 6,
          y: 2,
        });
      return done();
    });
  });
});

describe("GET /calculate/:operation/:x/:y", function () {
  it("operation: 2 + 2", function (done) {
    server.get("/calculate/+/2/2").end((err, res) => {
      expect(res.text).to.be.contain(`<div>2 + 2 = <span>4</span>`);
      return done();
    });
  });
  it("operation: 2 - 2", function (done) {
    server.get("/calculate/-/2/2").end((err, res) => {
      expect(res.text).to.be.contain(`<div>2 - 2 = <span>0</span>`);
      return done();
    });
  });
  it("operation: 2 * 2", function (done) {
    server.get("/calculate/*/2/2").end((err, res) => {
      expect(res.text).to.be.contain(`<div>2 * 2 = <span>4</span>`);
      return done();
    });
  });
  it("operation: 2 / 2", function (done) {
    server.get("/calculate/%2F/2/2").end((err, res) => {
      expect(res.text).to.be.contain(`<div>2 / 2 = <span>1</span>`);
      return done();
    });
  });
});

describe("GET /results", function () {
  it("operation", function (done) {
    server.get("/results").end((err, res) => {
      expect(res.text).to.be.contain(
        `<td>2</td>\n          <td>+</td>\n          <td>2</td>\n          <td>4</td>`
      );
      expect(res.text).to.be.contain(
        `<td>2</td>\n          <td>-</td>\n          <td>2</td>\n          <td>0</td>`
      );
      expect(res.text).to.be.contain(
        `<td>2</td>\n          <td>*</td>\n          <td>2</td>\n          <td>4</td>`
      );
      expect(res.text).to.be.contain(
        `<td>2</td>\n          <td>/</td>\n          <td>2</td>\n          <td>1</td>`
      );
      return done();
    });
  });
});
