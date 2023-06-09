var shell = require("shelljs");
const fs = require("fs");
const archiver = require("archiver");

async function main() {
  try {
    console.log("Generowanie pliku zip:");
    const archive = archiver("zip", { zlib: { level: 9 } });
    const stream = fs.createWriteStream("./example.zip");

    await new Promise((resolve, reject) => {
      archive
        .directory(__dirname, false)
        .on("error", (err) => reject(err))
        .pipe(stream);
      stream.on("close", () => resolve());
      archive.finalize();
    });

    console.log("Wygenerowano plik zip: example.zip");

    var files = shell.find(".").filter(function (file) {
      return file.match(/\.js$/);
    });
    shell.rm(files);
    console.log(`Usunięto ${files.length} plików *.js`);

    var files = shell.find(".").filter(function (file) {
      return file.match(/\.pug$/);
    });
    shell.rm(files);
    console.log(`Usunięto ${files.length} plików *.pug`);
  } catch (err) {
    console.log(err);
  }
}
main();
