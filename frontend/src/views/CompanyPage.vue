<template>
  <div>
    <p>{{ $route.params.id }} </p>
    <b-card
      title="Card Title"
      img-src="https://picsum.photos/600/300/?image=25"
      img-alt="Image"
      img-top
      tag="article"
      class="mb-2"
    >
      <b-card-text>
        <b-table striped hover :items="items"></b-table>
      </b-card-text>

      <!-- <b-button href="#" variant="primary">Go somewhere</b-button> -->
    </b-card>
  </div>
</template>

<script>
export default {
  data() {
    return {
      items: [
        { position: "Software Developer", rating: "5/5" },
        { position: "Data Scientist", rating: "5/5" },
        { position: "UI/UX", rating: "5/5" }
      ]
    };
  }
};
</script>

<style>
</style>