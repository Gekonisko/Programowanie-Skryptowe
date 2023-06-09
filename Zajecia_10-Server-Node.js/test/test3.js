//Source:  https://codeforgeek.com/unit-testing-nodejs-application-using-mocha/
var supertest = require("supertest");

// This agent refers to PORT where program is runninng.
var server = supertest.agent("http://localhost:8000");

// UNIT test begin
describe('GET /submit?name=John', function () {
    it('respond with "plik.txt"', function (done) {
        server
            .get('/submit?name=plik.txt')
            .expect('Content-Type', /text\/plain/)
            .expect(200, "plik.txt jest plikiem z zawartościa:\n      Ala ma kota", done);
    });

    it('respond with "Folder out"', function (done) {
        server
            .get('/submit?name=out')
            .expect('Content-Type', /text\/plain/)
            .expect(200, "out jest Katalogiem", done);
    });
});