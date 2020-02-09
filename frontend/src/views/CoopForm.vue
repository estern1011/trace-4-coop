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

      <label class="label">What position was this for?</label>
      <autocomplete
        :search="positionSearch"
        :get-result-value="getPositionResultValue"
        @submit="handlePositionSubmit"
        placeholder="Search for a position"
        aria-label="Search for a position"
        :v-model="form.positionName"
      >
        <template #result="{ result, props }">
          <li v-bind="props" class="autocomplete-result wiki-result">
            <div class="wiki-title">{{ result.position_name }}</div>
          </li>
        </template>
      </autocomplete>

      <!-- <div class="field">
      <label class="label">What position was this for?</label>-->
      <!-- <div class="control">
          <input class="input" type="text" v-model="form.position" />
      </div>-->
      <!-- </div> -->

      <div class="field">
        <label class="label">Does this company offer full-time return positions?</label>
        <div class="control">
          <label>
            <input type="radio" value="true" v-model="form.offer" />
            Yes
          </label>
          <br />
          <label>
            <input type="radio" value="false" v-model="form.offer" />
            No
          </label>
        </div>
      </div>

      <div class="field">
        <label class="label">Please describe a regular day on the job</label>
        <div class="control">
          <textarea v-model="form.message" placeholder="add multiple lines"></textarea>
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
      positions: {},
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
      this.positions = axios
        .get("http://localhost:5000/companies/" + this.company_id)
        .then(response => (this.positions = response.data.data));
    },
    positionSearch(input) {
      if (input.length < 1) {
        return [];
      }
      return this.positions.filter(position => {
        return position.position_name
          .toLowerCase()
          .startsWith(input.toLowerCase());
      });
    },
    getPositionResultValue(result) {
      return result.position_name;
    },
    handlePositionSubmit(input) {
      this.position_id = this.position.filter(item => {
        return item.position_name === input.position_name;
      })[0]._id;
      console.log(this.position_id);
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