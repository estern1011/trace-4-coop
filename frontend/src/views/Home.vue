<template>
  <div id="app">
    <b-container class="bv-example-row">
      <b-row>
        <b-col> <h5> Company Name </h5> </b-col>
        <b-col> <h5> Location </h5> </b-col>
      </b-row>
      <b-row v-for="item in this.info" :key="item._id">
        <router-link :to="{ name: 'companies', params: {company_name: item.company_name, id: item._id}}">
          <b-col> {{ item.company_name }} </b-col>
          </router-link>
        <b-col> {{ item.location }} </b-col>
      </b-row>
    </b-container>
  </div>
</template>
<script>
import axios from "axios";

export default {
  name: "Home",
  data() {
    return {
      info: {}
    };
  },
  mounted() {
    axios
      .get("http://localhost:5000/companies")
      .then(response => (this.info = response.data.data));
  }
};
</script>
<style>
</style>