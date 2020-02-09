<template>
  <section id="app" class="section">
    <form>
      <h1 class="title is-1">{{form.formName}}</h1>

      <label class="label">What's the company name?</label>
      <autocomplete
        :search="companySearch"
        :get-result-value="getCompanyResultValue"
        @submit="handleCompanySubmit"
        placeholder="Search for a company"
        aria-label="Search for a company"
        :v-model="form.companyName"
      >
        <template #result="{ result, props }">
          <li v-bind="props" class="autocomplete-result wiki-result">
            <div class="wiki-title">{{ result.company_name }}</div>
          </li>
        </template>
      </autocomplete>

      <div class="field">
        <label class="label">Describe the company briefly</label>
        <div class="control">
          <b-form-textarea class="input" type="text" v-model="form.position" />
        </div>
      </div>

      <input class="button is-primary margin-bottom" type="submit" @click.prevent="fakeSubmit" />
    </form>

    <transition name="fade" mode="out-in">
      <article class="message is-primary" v-show="showSubmitFeedback">
        <div class="message-header">
          <p>Fake Send Status:</p>
        </div>
        <div class="message-body">Successfully Submitted!</div>
      </article>
    </transition>

    <hr />

    <h5>JSON</h5>
    <pre><code>{{form}}</code></pre>
  </section>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      companies: {},
      form: {
        type: "co-op",
        companyName: "",
        location: "",
        position: "",
        rating: 0,
        message: ""
      },
      showSubmitFeedback: false
    };
  },
  methods: {
    companySearch(input) {
      if (input.length < 1) {
        return [];
      }
      return this.companies.filter(company => {
        return company.company_name
          .toLowerCase()
          .startsWith(input.toLowerCase());
      });
    },
    getCompanyResultValue(result) {
      return result.company_name;
    },
    handleCompanySubmit(input) {
      this.company_id = this.companies.filter(item => {
        return item.company_name === input.company_name;
      })[0]._id;
      console.log(this.company_id);
    },
    positionSearch(input) {
      if (input.length < 1) {
        return [];
      }
      return this.companies.filter(company => {
        return company.company_name
          .toLowerCase()
          .startsWith(input.toLowerCase());
      });
    },
    getPositionResultValue(result) {
      return result.company_name;
    },
    handlePositionSubmit(input) {
      this.company_id = this.companies.filter(item => {
        return item.company_name === input.company_name;
      })[0]._id;
      console.log(this.company_id);
    },
    fakeSubmit() {
      this.showSubmitFeedback = true;
      setTimeout(() => {
        this.showSubmitFeedback = false;
      }, 3000);
    }
  },
  mounted() {
    axios
      .get("http://localhost:5000/companies")
      .then(response => (this.companies = response.data.data));
  }
};
</script>

<style>
</style>