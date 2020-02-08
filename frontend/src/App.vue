<template>
  <div id="app">
    <NavBar />
    <!-- {companies_page.map(company => <CompanyPage />)} -->
    <CompanyPage />
    <router-view></router-view>
  </div>
</template>

<script>
import Vue from "vue";
import NavBar from "./components/NavBar.vue";
import CompanyPage from "./components/CompanyPage.vue"
import { BootstrapVue, IconsPlugin } from "bootstrap-vue";
import "bootstrap/dist/css/bootstrap.css";
import "bootstrap-vue/dist/bootstrap-vue.css";
import companies_page from "./constants.js"

Vue.use(BootstrapVue);
Vue.use(IconsPlugin);

export default {
  name: "App",
  components: {
    NavBar,
    CompanyPage
  }
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
