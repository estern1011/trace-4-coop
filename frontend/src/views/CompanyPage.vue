<template>
  <div>
    <h2>{{this.name}}</h2>
    <p>
      Don't see your position? Add your position:
      <router-link
        :to="{ name: `positions`, params: {company_name: this.name, id: this.company_id}}"
      >here</router-link>.
    </p>
    <b-container class="bv-example-row">
      <b-row>
        <b-col>
          <h5>Position</h5>
        </b-col>
        <b-col>
          <h5>Location</h5>
        </b-col>
      </b-row>
      <b-row v-for="item in this.info" :key="item._id">
        <b-col>
          <p><router-link :to="{ name: `reviews`, params: {company_name: this.name, position_name: item.position_name, 
          company_id: this.company_id, position_id: item._id}}">
            {{item.position_name}}
            </router-link>
            </p>
        </b-col>
        <b-col>{{ item.location }}</b-col>
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
      company_id: "",
      info: {},
      name: ""
    };
  },
  mounted() {
    this.company_id = this.$route.params.id;
    console.log(this.company_id);

    axios
      .get(`http://localhost:5000/companies/${this.company_id}`)
      .then(response => (this.info = response.data.data));

    axios.get("http://localhost:5000/companies").then(response => {
      this.name = response.data.data.filter(company => {
        return company._id === this.company_id;
      })[0].company_name;
    });
  }
};
</script>

<style>
</style>