<template>
  <div>
    <h2> Reviews for {{ this.company_name }}'s {{ this.position_name }} position </h2>
    <pre><code>{{this.info}}</code></pre>
  </div>
</template>

<script>
import axios from "axios";

export default {
  props: ["company_id", "company_name", "position_id", "position_name"],
  name: "Position",
  data() {
    return {
      info: {}
    };
  },
  mounted() {
    this.company_id = this.$route.params.company_id;
    this.company_name = this.$route.params.company_name;
    this.position_id = this.$route.params.position_id;
    this.position_name = this.$route.params.position_name;

    axios
      .get(`http://localhost:5000/companies/${this.company_id}/position/${this.position_id}`)
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