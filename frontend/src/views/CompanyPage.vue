<template>
  <div>
    <p>{{ $route.params.id }}</p>
    <p>{{this.name}}</p>
    <p>
      Don't see your position? Add your position
      <router-link
        :to="{ name: `companies/${$route.params.id}`, params: {company_name: this.name, id: $route.params.id}}"
      >here</router-link>.
    </p>
    <b-container class="bv-example-row">
      <b-row>
        <b-col>
          <h5>Position</h5>
        </b-col>
        <b-col>
          <h5>id</h5>
        </b-col>
      </b-row>
      <b-row v-for="item in this.info" :key="item._id">
        <b-col>
          <p>{{item.position}}</p>
        </b-col>
        <b-col>{{ item._id }}</b-col>
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
      info: {},
      name: ""
    };
  },
  mounted() {
    const company_id = this.$route.params.id;
    console.log(company_id);

    axios
      .get(`http://localhost:5000/companies/${company_id}`)
      .then(response => (this.info = response.data.data));

    axios.get("http://localhost:5000/companies").then(response => {
      this.name = response.data.data.filter(company => {
        return company._id === company_id;
      })[0].company_name;
    });
  }
};
</script>

<style>
</style>