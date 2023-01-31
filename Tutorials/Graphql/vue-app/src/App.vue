<template>
  <div>
    <a href="https://vitejs.dev" target="_blank">
      <img src="/vite.svg" class="logo" alt="Vite logo" />
    </a>
    <a href="https://vuejs.org/" target="_blank">
      <img src="./assets/vue.svg" class="logo vue" alt="Vue logo" />
    </a>

    <div>
      <input type="text" v-model="searchTerm" />
      <p v-if="loading">Loading......</p>
      <p v-else-if="error">something went wrong.....</p>
      <template v-else>
        <p v-if="activeBook">
          Update "{{ activeBook.title }}" rating:
          <EditRating
            :initial-rating="activeBook.rating"
            :book-id="activeBook.id"
            @closeForm="activeBook = null"
          />
        </p>
        <template v-else>
          <p v-for="data in result.allBooks" :key="data.id">
            {{ data.title }} - {{ data.rating }}
            <button @click="activeBook = data">Edit</button>
          </p>
          <!-- <p v-for="data in books" :key="data.id">
          {{ data.title }} - {{ data.rating }}
        </p> -->
        </template>
      </template>
    </div>
  </div>
</template>

<script>
import { useQuery } from "@vue/apollo-composable";
import { useMutation } from "@vue/apollo-composable";
import AllBook from "./graphql/allbooks.query.gql";
import updateBook from "./graphql/updateBook.mutation.gql";
// import { useResult } from "@vue/apollo-composable";

import EditRating from "./components/EditRating.vue";

import { ref } from "vue";
export default {
  name: "App",
  components: {
    EditRating,
  },
  setup() {
    const searchTerm = ref("");

    const activeBook = ref("null");

    const { result, loading, error } = useQuery(
      AllBook,
      () => ({ search: searchTerm.value }),
      () => ({
        debounce: 2000,
        // enabled: searchTerm.value.length > 2,
      })
    );
    // console.log(result);

    // const books = useResult(result, [], (data) => data.allBooks);

    const { mutate } = useMutation(updateBook);
    return {
      result,
      searchTerm,
      loading,
      error,
      // books,
      activeBook,
    };
  },
};
</script>

<style scoped>
.logo {
  height: 6em;
  padding: 1.5em;
  will-change: filter;
}
.logo:hover {
  filter: drop-shadow(0 0 2em #646cffaa);
}
.logo.vue:hover {
  filter: drop-shadow(0 0 2em #42b883aa);
}
</style>
