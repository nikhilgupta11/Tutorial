const fs = require("fs");

// creating a file if not exists
// override the data if file exists
fs.writeFileSync("first.txt", "welcome to node.");

// append the data
fs.appendFileSync("first.txt", "m hu nikhil");

// read
const read = fs.readFileSync("first.txt");
console.log(read.toString());

// read with utf8 to convert the data into string
const read2 = fs.readFileSync("first.txt", "UTF-8");
console.log(read2);

// Rename a file

fs.renameSync("first.txt", "renamedFirst.txt");

// unlink or delete this text file
fs.unlinkSync("renamedFirst.txt");
