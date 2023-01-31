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

const firstDocument1 = async () => {
  try {
    const first = new FirstCollection({
      name: "shyam",
      age: 23,
      active: true,
    });
    const second = new FirstCollection({
      name: "shyam",
      age: 23,
      active: true,
    });
    const third = new FirstCollection({
      name: "shyam",
      age: 23,
      active: true,
    });
    const fourth = new FirstCollection({
      name: "shyam",
      age: 23,
      active: true,
    });
    const result = await FirstCollection.insertMany([
      first,
      second,
      third,
      fourth,
    ]);
    console.log(result);
  } catch (err) {
    console.log(err);
  }
};

// function call
firstDocument1();
