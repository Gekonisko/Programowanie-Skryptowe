var expect = require('chai').expect;
var assert = require('assert');
var Path = require('../script');

describe('Script.js', function () {
    it('plik.txt', function () {
        var op = new Path("plik.txt");
        assert.strictEqual(op.SyncCheck(), "Plik")
    });
    it('Katalog out', function () {
        var op = new Path("out");
        assert.strictEqual(op.SyncCheck(), "Katalog")
    });
});