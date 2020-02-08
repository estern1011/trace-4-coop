<template>
  <div id="app">
    <p>homepage</p>
    {{ this.info }}
  </div>
</template>
<script>
import axios from "axios";

export default {
  name: "Home",
  data() {
    return {
      info: {}
    }
  },
  mounted() {
    axios
      .get("http://localhost:5000/companies")
      .then(response => (this.info = response.data));
  }
};
</script>
<style>
</style>