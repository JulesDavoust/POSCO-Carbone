<template>
  <div class="Conseils">
    <Navbar></Navbar>
    <!-- <div class="conteneur">  
      <test></test>
    </div> -->
  </div>
</template>

<script>
import Navbar from '../components/Navbar.vue'
import test from '../components/test.vue'

export default {
  name: 'Conseils',
  components: {
    Navbar,
    test
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
