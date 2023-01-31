const http = require("http");

const reponse = http.createServer((req, res) => {
  console.log(req.url);
  // res.end("hello nikhil is here");
  if (req.url == "/") {
    res.end("hello from home page");
  } else if (req.url == "/about") {
    res.end("hello from about page");
  } else if (req.url == "/contact") {
    res.end("hello from contact page");
  } else {
    // setting a error code and content type
    res.writeHead(404, { "Content-type": "text/html" });
    //

    res.end("page not found");
  }
});

reponse.listen(8000, "127.0.0.1", () => {
  console.log("port 8000");
});
