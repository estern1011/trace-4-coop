<template>
  <div>
    <b-navbar toggleable="lg" type="dark" variant="info">
      <router-link to="/">
        <b-navbar-brand>Co-op Reviews</b-navbar-brand>
      </router-link>

      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav>
          <b-nav-item to="/about">About</b-nav-item>
          <b-nav-item to="/interview">Submit an Interview Review</b-nav-item>
          <b-nav-item to="/coop">Submit a Co-op Review</b-nav-item>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
  </div>
</template>

<script>
export default {};
</script>

<style>
</style>