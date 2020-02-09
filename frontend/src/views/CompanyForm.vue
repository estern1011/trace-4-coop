<template>
  <section id="app" class="section">
    <form>
      <h1 class="title is-1">{{form.formName}}</h1>

      <label class="label">What's the name of the company?</label>
      <div class="field">
        <div class="control">
          <b-form-textarea class="input" type="text" v-model="form.company_name" />
        </div>
      </div>

      <div class="field">
        <label class="label">Describe the company briefly</label>
        <div class="control">
          <b-form-textarea class="input" type="text" v-model="form.description" />
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
      form: {
        companyName: "",
        description: ""
      }
    };
  },
  methods: {
    onSubmit() {
      axios
        .post(
          "http://localhost:5000/companies",
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