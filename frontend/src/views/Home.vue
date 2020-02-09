<template>
  <div id="app">
    <autocomplete
      :search="companySearch"
      :get-result-value="getCompanyResultValue"
      @submit="handleCompanySubmit"
      placeholder="Search for a company"
      aria-label="Search for a company"
    >
      <template #result="{ result, props }">
        <li v-bind="props" class="autocomplete-result wiki-result">
          <div class="wiki-title">{{ result.company_name }}</div>
        </li>
      </template>
    </autocomplete>
    <h4>
      Don't see your company? Add your company
      <a href="/company">here</a>.
    </h4>
    <b-container class="bv-example-row">
      <b-row>
        <b-col><h5>Logo</h5></b-col>
        <b-col>
          <h5>Company Name</h5>
        </b-col>
        <b-col>
          <h5>Link to Company</h5>
        </b-col>
      </b-row>
      <b-row v-for="item in this.companies" :key="item._id">
        <b-col>
          <img :src="item.logo" />
        </b-col>
        <b-col>
          <router-link
            :to="{ name: 'companies', params: {company_name: item.company_name, id: item._id}}"
          >{{ item.company_name }}</router-link>
        </b-col>

        <b-col>
          <a :href="item.domain">{{ item.domain }}</a>
        </b-col>
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
      companies: {}
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
      this.form.company_id = this.companies.filter(item => {
        return item.company_name === input.company_name;
      })[0]._id;
      console.log(this.form.company_id);
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