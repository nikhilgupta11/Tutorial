const fs = require("fs");

// creating a file if not exists
// override the data if file exists
fs.writeFile("first.txt", "welcome to node.", (err) => {
  console.log("done");
});

// append the data
fs.appendFile("first.txt", "m hu nikhil", (err) => {
  console.log("appended");
});

// read
const read = fs.readFile("first.txt", "UTF-8", (err, data) => {
  console.log(data);
});

console.log(read);

//unlink or delete this text file
fs.unlink("renamedFirst.txt", () => {
  console.log("ho gya");
});
