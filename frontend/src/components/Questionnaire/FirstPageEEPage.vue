<template>
    <div class="firstpage">
      <div v-if="currentpage === 'first'">
        <div class="row mt-4 justify-content-center align-items-center">
          <div class="col-10 col-md-8 text-center">
            <div class="feature-card">
              <h2>Bienvenue dans l'espace EFREI</h2>
              <p>
                Cet espace est dédié à la sensibilisation de la consommation pour le climat. Nous prenons en compte l’effet rebond dans le calcul de l’empreinte carbone pour la SWIM et la Mobilité Internationale L3.
              </p>
              <p>
                L’effet rebond inclut les déplacements secondaires/supplémentaires, les nouveaux choix alimentaires et la consommation énergétique inhabituelle durant un séjour à l’étranger.
              </p>
            </div>
            <button type="button" class="btn" @click="Start()">Explorez votre empreinte carbone</button>
          </div>
        </div>
        <img src="../../assets/image.png" class="background-image">
      </div>
      <SecondPageEEPage v-if="currentpage === 'second'" />
    </div>
  </template>
  
  <script>
  import SecondPageEEPage from './SecondPageEEPage.vue'
  
  export default {
    components: {
      SecondPageEEPage
    },
    data() {
      return {
        currentpage: 'first'
      }
    },
    methods: {
      Start() {
        this.currentpage = 'second'
      }
    }
  }
  </script>
  
  <style scoped>
  .firstpage {
    position: relative;
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
  }
  
  .feature-card {
    background-color: #C1E4C3;
    border-radius: 20px;
    padding: 20px;
    margin: 20px 0;
    display: inline-block;
    text-align: center;
  }
  
  .btn {
    background-color: #C1E4C3 !important; 
    margin-top: 20px;
    border-radius: 30px !important; 
  }
  
  .background-image {
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
    width: 100%;
    height: auto;
    z-index: -1;
  }
  </style>
  