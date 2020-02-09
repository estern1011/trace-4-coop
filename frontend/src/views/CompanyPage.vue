<template>
  <div>
    <p>{{ $route.params.id }}</p>
    <b-card
      title="Card Title"
      img-src="https://picsum.photos/600/300/?image=25"
      img-alt="Image"
      img-top
      tag="article"
      class="mb-2"
    >
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
    </b-card>
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

    const company_id = this.$route.params.id;
    console.log(company_id);

    axios
      .get(`http://localhost:5000/companies/${company_id}`)
      .then(response => (this.info = response.data.data));
  }
};

</script>

<style>
</style>