<template>
    <div class="EspaceEfrei">
        <NavbarVue></NavbarVue>
        <FirstPageEEPageVue></FirstPageEEPageVue>
    </div>
</template>

<script>
import FirstPageEEPageVue from '../components/Questionnaire/FirstPageEEPage.vue'
import NavbarVue from '../components/Navbar.vue'


export default {
  name: 'EspaceEfrei',
  components: {
    NavbarVue,
    FirstPageEEPageVue
  }
}
</script>

<style>

</style>
