/** Operation - Klasa zajmujaca się Operacjami */
class Operation {
    /**
     * Repezentuje operacje
     * @constructor
     * @param {Number} x - zmienna x
     * @param {Number} y - zmienna y
    */
    constructor(x, y) {
        this.x = x;
        this.y = y;
    }

    /** sum - ooperacja sumowania na zdefiniowanych wartościach x i y */
    sum() {
        return this.x + this.y;
    }
}

module.exports = Operation;