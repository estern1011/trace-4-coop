<template>
  <section id="app" class="section">
    <form>
      <h1 class="title is-1">{{form.formName}}</h1>

      <label class="label">What's the name of the position?</label>
      <div class="field">
        <div class="control">
          <b-form-textarea class="input" type="text" v-model="form.position_name" />
        </div>
      </div>

      <div class="field">
        <label class="label">Where is the position located?</label>
        <div class="control">
          <b-form-textarea class="input" type="text" v-model="form.location" />
        </div>
      </div>

      <input class="button is-primary margin-bottom" type="submit" @click.prevent="onSubmit" />
    </form>

    <hr />
  </section>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      company_id: "",
      form: {
        position_name: "",
        location: ""
      }
    };
  },
  mounted() {
    this.company_id = this.$route.params.id;
    console.log(this.company_id);
  },

  methods: {
    onSubmit() {
      axios
        .post(
          `http://localhost:5000/companies/${this.company_id}`,
          this.form
        )
        .then(response => (this.result = response.status));
      this.$router.push("/");
    }
  }
};
</script>

<style>
</style>