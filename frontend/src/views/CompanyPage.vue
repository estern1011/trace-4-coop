<template>
  <div>
    <h2>{{this.company_name}}</h2>
    <p>
      Don't see your position? Add your position:
      <router-link
        :to="{ name: `positions`, params: {company_name: this.company_name, id: this.company_id}}"
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
        <b-col></b-col>
      </b-row>
      <b-row v-for="item in this.info" :key="item._id">
        <b-col>
          <p>
            <!-- <router-link :to="{ name: `reviews`, params: {company_name: this.company_name, position_name: item.position_name, 
            company_id: this.company_id, position_id: item._id}}">-->
            {{item.position_name}}
            <!-- </router-link> -->
          </p>
        </b-col>
        <b-col>{{ item.location }}</b-col>
        <b-col>
            <button v-on:click="goToReview(item.position_name, item._id)">Go to reviews</button>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
import axios from "axios";

export default {
  props: ["company_id", "company_name"],
  name: "Home",
  data() {
    return {
      info: {}
    };
  },
  methods: {
    goToReview(pos_name, pos_id) {
      this.$router.push({ name: 'reviews', params: {company_name: this.company_name, 
            company_id: this.company_id, position_name: pos_name, position_id: pos_id} })
    }
  },
  mounted() {
    this.company_id = this.$route.params.id;
    this.company_name = this.$route.params.company_name;
    console.log(this.company_id);

    axios
      .get(`http://localhost:5000/companies/${this.company_id}`)
      .then(response => (this.info = response.data.data));

    // axios.get("http://localhost:5000/companies").then(response => {
    //   this.name = response.data.data.filter(company => {
    //     return company._id === this.company_id;
    //   })[0].company_name;
    // // });
    // console.log(this.name)
    // console.log(this.company_id)
  }
};
</script>

<style>
</style>