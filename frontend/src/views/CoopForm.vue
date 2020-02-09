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
      <input class="button is-primary margin-bottom" type="submit" @click.prevent="onSubmit" />
    </form>


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
        company_id: "",
        position_id: "",
        message: "",
        offer:"false"
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
      this.form.company_id = this.companies.filter(item => {
        return item.company_name === input.company_name;
      })[0]._id;
      console.log(this.form.company_id);
      this.positions = axios
        .get("http://localhost:5000/companies/" + this.form.company_id)
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
      this.form.position_id = this.positions.filter(item => {
        return item.position_name === input.position_name;
      })[0]._id;
      console.log(this.form.poisition_id);
    },
    onSubmit() {
      axios.post(`http://localhost:5000/companies/${this.form.company_id}/position/${this.form.position_id}`, this.form)
      .then(response => (this.result = response.status));
      this.$router.push("/thanks");

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