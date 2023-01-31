<template>
  <div>
    <h1>Hello this is dynamic page created by Slug.</h1>
    <h1>Dynamic Route:-{{ $route.params.slug }}</h1>
    <h1>{{ planet.title }}</h1>
    <img :src="planet.image" alt="" />
    <pre>{{ $data }}</pre>
  </div>
</template>

<script>
export default {
  name: "DynamicPage",

  async asyncData({ params }) {
    const planet = await fetch(`https://api.nuxtjs.dev/planets/${params}`).then(
      (res) => res.json()
    );

    return { planet };
  },
};
</script>

<style scoped>
img {
  width: 200px;
  height: 200px;
}
</style>
