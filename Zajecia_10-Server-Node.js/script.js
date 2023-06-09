

const myArgs = process.argv.slice(2);

const fs = require('fs');


class Path {
    constructor(path) {
        this.path = path;
    }

    SyncCheck() {
        const stats = fs.statSync(this.path);
        if (stats.isFile()) {
            console.log(`${this.path} jest plikiem, a jego zawartością jest:`);
            fs.readFile(this.path, (error, data) => {
                if (error) {
                    console.error(error);
                    return;
                }
                console.log(data.toString());
            });
            return "Plik"
        }
        if (stats.isDirectory()) {
            console.log(`${this.path} jest katalogiem`);
            return "Katalog"
        }
        return "Nie Wiadomo"
    }

    AsyncCheck() {
        const stats = fs.stat(this.path, (error, stats) => {
            if (error) {
                console.log(error);
            }
            else {
                if (stats.isFile()) {

                    console.log("Plik");
                }
                if (stats.isDirectory()) {
                    console.log("Katalog");
                }
            }
        });
    }

}

module.exports = Path;