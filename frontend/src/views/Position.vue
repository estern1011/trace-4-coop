<template>
  <div>
    <h3>Reviews for {{ this.company_name }}'s {{ this.position_name }} position</h3>
    <!-- <input type="checkbox" id="interview" v-model="interview">
    <label for="interview">Interviews  </label>    
    |
    <input type="checkbox" id="coop" v-model="coop">
    <label for="coop">Co-op experiences</label>-->
    <b-container class="bv-example-row">
      <b-row>
        <b-col> <h5> Type of review </h5> </b-col>
        <b-col> <h5> Offer? </h5> </b-col>
        <b-col> <h5> Happy with offer? </h5> </b-col>
        <b-col> <h5> Review message </h5> </b-col>
      </b-row>
      <b-row v-for="item in this.info" :key="item._id">
        <b-col>{{ item.type }}</b-col>
        <b-col>
          <p>{{ item.offer }}</p>
        </b-col>
        <b-col>
          <p>{{ item.happy }}</p>
        </b-col>
        <b-col>{{ item.message }}</b-col>
      </b-row>
    </b-container>

    <!-- <pre><code>{{this.info}}</code></pre> -->
    <!-- <h2>{{ this.interview }} </h2>
    <h3>{{ this.coop }} </h3>-->
  </div>
</template>

<script>
import axios from "axios";

export default {
  props: ["company_id", "company_name", "position_id", "position_name"],
  name: "Position",
  data() {
    return {
      interview: true,
      coop: true,
      info: {}
    };
  },
  mounted() {
    this.company_id = this.$route.params.company_id;
    this.company_name = this.$route.params.company_name;
    this.position_id = this.$route.params.position_id;
    this.position_name = this.$route.params.position_name;

    axios
      .get(
        `http://localhost:5000/companies/${this.company_id}/position/${this.position_id}`
      )
      .then(response => (this.info = response.data.data));

    console.log(this.company_id);
    console.log(this.company_name);
    console.log(this.position_id);
    console.log(this.position_name);
  }
};
</script>

<style>
</style>