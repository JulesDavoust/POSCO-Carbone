<template>
    <div v-if="valid">
        <Navbar></Navbar>
            <!-- <h1 v-if="type === 'swim'">SWIM Questionnaire</h1>
            <h1 v-else-if="type === 'semestre'">Semester Questionnaire</h1> -->
            <!-- Affichez le formulaire de questionnaire ici -->
            <!-- Formulaire pour SWIM -->
            <div class="conteneur">
            <div v-if="type === 'semestre'">
                <QuestionsSEMESTRE :token="token"/>
            </div>
            </div>
    </div>
    <div v-else>
        <Navbar></Navbar>
        <h1>Questionnaire hebdomadaire déjà réalisé</h1>
        <p v-if="error">{{ error }}</p>
        <p v-else>Tu n'as pas accès à ce questionnaire ou le lien a expiré.</p>
    </div>
</template>

<script>
import QuestionsSEMESTRE from '../components/Questionnaire/QuestionsSEMESTRE.vue'
import Navbar from '../components/Navbar.vue'

export default {
    components: {
        QuestionsSEMESTRE,
        Navbar
    },
    data() {
        return {
            valid: false,
            error: null,
            type: null,
            API_URL: 'http://localhost:5000/',
            token: null
        }
    },
    
    async created() {
        let token = localStorage.getItem('semestre');
        if (!token) {
            token = this.$route.query.token;
        }

        if (!token) {
            this.error = 'Token is missing';
            return;
        }
        this.token = token;

        try {
            const response = await fetch(`${this.API_URL}questionnaire?token=${this.token}`, {
                method: 'GET',
                headers: { 'Content-Type': 'application/json' }
            });

            const data = await response.json();
            if (data.message === 'Token is valid') {
                this.valid = true;
                this.type = data.type;
                localStorage.setItem("semestre", this.token);
            } else {
                this.error = data.message;
                localStorage.removeItem("semestre");  // Supprimer le token invalide
            }
        } catch (error) {
            console.error('An error occurred:', error);
            this.error = 'An error occurred';
        }
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