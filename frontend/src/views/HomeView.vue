<template>
  <div class="home">
    <NavbarVue></NavbarVue>
    <HeaderHomePageVue></HeaderHomePageVue>
    <BodyHomePageVue></BodyHomePageVue>
  </div>
</template>

<script>
import BodyHomePageVue from '../components/BodyHomePage.vue'
import HeaderHomePageVue from '../components/HeaderHomePage.vue'
import NavbarVue from '../components/Navbar.vue'

export default {
  name: 'HomeView',
  components: {
    NavbarVue,
    HeaderHomePageVue,
    BodyHomePageVue
  }
}
</script>
