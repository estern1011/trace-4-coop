<template>
  <section id="app" class="section">
    <form>
      <h1 class="title is-1">{{form.formName}}</h1>

      <div class="field">
        <label class="label">What's the company name?</label>
        <div class="control">
          <input class="input" type="text" v-model="form.companyName" />
        </div>
      </div>

      <div class="field">
        <label class="label">Where is it located? (eg. Boston, MA)</label>
        <div class="control">
          <input class="input" type="text" v-model="form.location" />
        </div>
      </div>

      <div class="field">
        <label class="label">What position was this for?</label>
        <div class="control">
          <input class="input" type="text" v-model="form.position" />
        </div>
      </div>

      <div class="field">
        <label class="label">How difficult was the interview? (5 being most difficult)</label>
        <div class="control">
          <div class="select">
            <select v-model="form.interviewDifficulty">
              <option v-for="difficulty in [1,2,3,4,5]" :key="difficulty">{{difficulty}}</option>
            </select>
          </div>
        </div>
      </div>

      <div class="field">
        <label class="label">Types of Interview Questions</label>
        <div class="control">
          <label>
            <input type="checkbox" value="algo" v-model="form.questionType" />
            Algorithms
          </label>
          <br />
          <label>
            <input type="checkbox" value="behavioral" v-model="form.questionType" />
            Behavioral
          </label>
          <br />
          <label>
            <input type="checkbox" value="database" v-model="form.questionType" />
            Database Design
          </label>
          <br />
          <label>
            <input type="checkbox" value="systems" v-model="form.questionType" />
            System Design
          </label>
        </div>
      </div>

      <div class="field">
        <label class="label">How would you rate the interview? (10 being perfect)</label>
        <div class="control">
          <h4 class="title is-4">{{form.rating}} / 10</h4>
          <input type="range" min="0" max="10" v-model="form.rating" />
        </div>
      </div>

      <div class="field">
        <label class="label">Did you receive an offer?</label>
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
          <textarea v-model="message" placeholder="add multiple lines"></textarea>
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
export default {
  data() {
    return {
      form: {
        type: "interview",
        companyName: "",
        location: "",
        position: "",
        difficulty: "1",
        offer: "",
        questionType: [],
        rating: 0
      },
      showSubmitFeedback: false
    };
  },
  methods: {
    fakeSubmit() {
      this.showSubmitFeedback = true;
      setTimeout(() => {
        this.showSubmitFeedback = false;
      }, 3000);
    }
  }
};
</script>

<style>
</style>