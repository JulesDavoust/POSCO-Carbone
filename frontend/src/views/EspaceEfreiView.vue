<template>
    <div class="EspaceEfrei">
      <Navbar></Navbar>
      <div class="conteneur">  
        <FirstPageEEPage/>
      </div>
    </div>
</template>

<script>
import FirstPageEEPage from '../components/Questionnaire/FirstPageEEPage.vue'
import Navbar from '../components/Navbar.vue'


export default {
  name: 'EspaceEfrei',
  components: {
    Navbar,
    FirstPageEEPage
  }
}
</script>

<style scoped>
.conteneur{
  display: flex;
  justify-content: center; /* Centrage horizontal */
  align-items: center;     /* Centrage vertical */
  height: 100vh;           /* Utilise toute la hauteur de la fenêtre */
}
</style>
