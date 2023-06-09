"use strict";

var AllSum = 0;

function sum(x, y) {
    return x + y;
}


function cyfry(napis) {
    let s = 0;
    for (var i = 0; i < napis.length; i++) {
        var n = napis.charCodeAt(i);
        if (n >= 48 && n <= 57) {
            s += parseInt(napis.charAt(i))
        }
    }
    return s;
}

function litery(napis) {
    napis = napis.toLowerCase()
    let count = 0;
    for (var i = 0; i < napis.length; i++) {
        var n = napis.charCodeAt(i);
        if (n >= 97 && n <= 122) {
            count += 1;
        }
    }
    return count;
}

function suma(napis) {
    let number = parseInt(napis)
    if (isNaN(number))
        return AllSum;

    return AllSum + number;
}


function calculate(input) {
    let c = cyfry(input);
    let l = litery(input);
    AllSum = suma(input);
    return c + " " + l + " " + AllSum;
}

function GetInput() {
    let input;
    while (input = window.prompt()) {
        console.log(calculate(input));
    }
}

//GetInput();


describe('The sum() function', function () {
    it('Returns 4 for 2+2', function () {
        chai.expect(sum(2, 2)).to.equal(4);
    });
    it('Returns 0 for -2+2', function () {
        chai.expect(sum(-2, 2)).to.equal(0);
    });
});

describe('The cyfry(), litery() and suma() functions', function () {
    it('Same Cyfry', function () {
        var napis = "43125"
        chai.expect(calculate(napis)).to.equal("15 0 43125");
    });
    it('Same Litery', function () {
        var napis = "argkc"
        chai.expect(calculate(napis)).to.equal("0 5 43125");
    });
    it('Litery, a po nich cyfry', function () {
        var napis = "fsdm1234"
        chai.expect(calculate(napis)).to.equal("10 4 43125");
    });
    it('Cyfry, a po nich litery', function () {
        var napis = "123fsdsm"
        chai.expect(calculate(napis)).to.equal("6 5 43248");
    });
    it('Pusty napis', function () {
        var napis = ""
        chai.expect(calculate(napis)).to.equal("0 0 43248");
    });
});
