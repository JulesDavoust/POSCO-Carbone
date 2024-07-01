<template>
    <div>
        <div class="container" v-if="indexpage === 'SuscribequestionnaireSEM'">
            <!-- Page d'accueil -->
            <div v-if="!started" class="text-center mt-5">
            <h3>Bienvenue sur le calculateur de bilan carbone pour la swim.<br>Quand vous cliquerez sur le bouton vous recevrez des questions hebdomadairement pour calculer votre bilan carbone tout au long de votre séjour.</h3>
            <button class="btn btn-primary mt-4" @click="startForm">S'inscrire pour le questionnaire du Semestre à l'étranger</button>
            </div>
        </div>
    </div>
</template>
  
  <script>
  import AuthService from '../../services/auth.service.js'
  export default {
    data(){
        return{
            API_URL: 'http://localhost:5000/',
            indexpage:'SuscribequestionnaireSEM'
        }
    },
    methods: {
      async startForm() {
        await fetch(this.API_URL + 'user/set_notification_semestre', {
          method: 'POST',
          headers: Object.assign({ 'Content-Type': 'application/json' }, AuthService.authHeader())
        })
          .then(response => response.json())
          .then(data => {console.log(data)})
          this.$router.push({'name':'Accueil'})
      },
    }
  };
  </script>
  
  
  <style scoped>
  
  </style>
  