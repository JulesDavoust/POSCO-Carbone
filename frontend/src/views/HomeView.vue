<template>
  <div class="home">
    <Navbar></Navbar>
    <HeaderHomePage></HeaderHomePage>
    <BodyHomePage></BodyHomePage>
  </div>
</template>

<script>
import BodyHomePage from '../components/BodyHomePage.vue'
import HeaderHomePage from '../components/HeaderHomePage.vue'
import Navbar from '../components/Navbar.vue'

export default {
  name: 'HomeView',
  components: {
    Navbar,
    HeaderHomePage,
    BodyHomePage
  }
}
</script>
