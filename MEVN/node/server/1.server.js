const http = require("http");

const reponse = http.createServer((req, res) => {
  res.end("hello nikhil is here");
});

reponse.listen(8000, "127.0.0.1", () => {
  console.log("port 8000");
});
