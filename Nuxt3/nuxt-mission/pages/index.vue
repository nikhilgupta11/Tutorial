<template>
  <div>
    <Nuxt-link to="/about">About</Nuxt-link>
    <!-- <pre>{{ $data }}</pre> -->
    <!-- <h1>{{ planets }}</h1> -->
    <p v-if="$fetchState.prnding">Fetching Planets...</p>
    <p v-else-if="$fetchState.error">Error while fetching Planets</p>
    <ul v-else>
      <li v-for="planet in planets" :key="planet.slug">
        <NuxtLink :to="planet.slug">{{ planet.title }}</NuxtLink>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: "IndexPage",

  async fetch() {
    this.planets = await fetch("https://api.nuxtjs.dev/planets").then((res) =>
      res.json()
    );
  },

  data() {
    return {
      planets: [],
    };
  },
};
</script>
