const mongoose = require("mongoose");

const schema = new mongoose.Schema({
  name: {
    type: String,
    required: true,
    minlength: 2,
  },
  fName: {
    type: String,
    required: true,
    minlength: 2,
  },
  mName: {
    type: String,
    required: true,
    minlength: 2,
  },
  mobile: {
    type: String,
    required: true,
    unique: [true, "Mobile Number must be unique."],
  },
  address: {
    type: String,
    required: true,
  },
});

module.exports(schema);
