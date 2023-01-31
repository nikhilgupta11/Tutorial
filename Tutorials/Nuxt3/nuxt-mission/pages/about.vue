<template>
  <div>
    <Nuxt-link to="/">Home</Nuxt-link>
    <p>jenfjrewngfiure</p>
    <h1>kijoiwjfirw</h1>
    <button @click="getData(2, 3)">Buuton</button>
  </div>
</template>

<script>
export default {
  name: "IndexPage",
  Layout: "NewLayout",

  methods: {
    // getData() {
    //   // console.log("runnign");
    //   fetch(
    //     "http://cafe.addwebprojects.com:4007/api/v1/about/twilio-setting/"
    //   ).then((response) => console.log(response));
    // },

    getData(peraA, peraB) {
      const opera = peraA + peraB;
      console.log(opera);
    },
  },
};
</script>
