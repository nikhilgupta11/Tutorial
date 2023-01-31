const mongoose = require("mongoose");

mongoose
  .connect("mongodb://127.0.0.1:27017/DBfirst", {
    useNewUrlParser: true,
    useUnifiedTopology: true,
  })
  .then(() => console.log("success"))
  .then((err) => console.log(err));

// create a schema
const firstschema = new mongoose.Schema({
  name: {
    type: String,
    required: true,
  },
  age: Number,
  active: Boolean,
  date: {
    type: Date,
    default: Date.now,
  },
});

// create collection
const FirstCollection = new mongoose.model("collectionFirst", firstschema);

// create document in this collection
// const firstDocument = new FirstCollection({
//   name: "Nikhil",
//   age: 23,
//   active: true,
// });

// save data into DB
// firstDocument.save();

// using Async await
// const firstDocument1 = async () => {
//   const firstDocument11 = new FirstCollection({
//     name: "vishal",
//     age: 23,
//     active: true,
//   });
//   const result = await firstDocument11.save();
//   console.log(result);
// };

// using try-catch
const firstDocument1 = async () => {
  try {
    const firstDocument11 = new FirstCollection({
      name: "shyam",
      age: 23,
      active: true,
    });
    const result = await firstDocument11.save();
    console.log(result);
  } catch (err) {
    console.log(err);
  }
};

// function call
firstDocument1();
