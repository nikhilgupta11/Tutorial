import { createApp, h, provide } from "vue";
import "./style.css";
import App from "./App.vue";

import {
  ApolloClient,
  createHttpLink,
  InMemoryCache,
} from "@apollo/client/core";

// import gql from "graphql-tag";
import { DefaultApolloClient } from "@vue/apollo-composable";

const httpLink = new createHttpLink({
  uri: "http://localhost:4000/graphql",
});

const cache = new InMemoryCache();

const apolloClient = new ApolloClient({
  link: httpLink,
  cache,
});

// const AllBook = gql`
//   query allBooks {
//     allBooks {
//       id
//       title
//       rating
//     }
//   }
// `;

// apolloClient
//   .query({
//     query: AllBook,
//   })
//   .then((res) => {
//     console.log(res);
//   });

const app = createApp({
  setup() {
    provide(DefaultApolloClient, apolloClient);
  },
  render: () => h(App),
});
app.mount("#app");
