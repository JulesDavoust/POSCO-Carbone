<template>
  <div id="secondpage">
    <div class="cadre" v-if="index === 'secondpage'">
      <div class="row mt-4 justify-content-center align-items-center">
        <div class="col-12 col-md-8">
          <div class="feature-card">
            <div class="text">Je réalise ce questionnaire pour simuler la consommation de :</div>
          </div>
        </div>
      </div>
      <div class="row mt-4 justify-content-center align-items-center">
        <div class="col-12 col-md-8 d-flex justify-content-center">
          <button type="button" class="btn text-btn" @click="SWIM()">Ma SWIM</button>
        </div>
      </div>
      <div class="row mt-4 justify-content-center align-items-center">
        <div class="col-12 col-md-8 d-flex justify-content-center">
          <button type="button" class="btn text-btn" @click="SEMESTRE()">Mon semestre à l'étranger</button>
        </div>
      </div>
      <div class="row mt-4 justify-content-center align-items-center">
        <div class="col-12 col-md-8 d-flex justify-content-center">
          <button type="button" class="btn text-btn" @click="PERSO()">Activité EFREI</button>
        </div>
      </div>
    </div>
    <suscribeQuestionnaireSWIM v-if="index === 'SuscribequestionnaireSWIM'" />
    <suscribeQuestionnaireSEM v-if="index === 'SuscribequestionnaireSEM'" />
  </div>
</template>

  
<script>
import suscribeQuestionnaireSEM from './suscribeQuestionnaireSEM.vue';
import suscribeQuestionnaireSWIM from './suscribeQuestionnaireSWIM.vue';

export default {
  name: 'SecondPageEEPage',
  components: {
    suscribeQuestionnaireSWIM,
    suscribeQuestionnaireSEM
  },
  data() {
    return {
      index: 'secondpage'
    };
  },
  methods: {
    SWIM() {
      console.log('swim loaded');
      this.index = 'SuscribequestionnaireSWIM';
    },
    SEMESTRE() {
      console.log('semestre loaded');
      this.index = 'SuscribequestionnaireSEM';
    },
    PERSO() {
      console.log('personnel loaded');
    }
  }
};
</script>

  
<style scoped>
/* .cadre{
  border: 3px solid #48b14f;
  padding: 5%;
  width: 90vh;
} */

.feature-card {
  background-color: #C1E4C3;
  border-radius: 20px;
  padding: 20px;
  margin: 20px 0;
  height: auto; /* Updated to auto for better responsiveness */
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center; /* Ensure text is centered */
}

.text {
  font-size: 1.5rem; /* Adjust base font size */
}

.btn {
  background-color: #C1E4C3 !important;
  border-radius: 20px;
  margin: 5px 0;
}

.text-btn {
  font-size: 0.8rem;
  width: 50vw;
  height: 40px;
}

@media (max-width: 768px) {
  .text {
    font-size: 1rem; /* Adjust font size for smaller screens */
  }

  .text-btn {
    font-size: 0.9rem;
    width: 60vw;
    height: 40px;
  }
}

@media (max-width: 375px) {
  .text {
    font-size: 0.9rem; /* Further adjust font size for very small screens */
  }

  .text-btn {
    font-size: 0.7rem;
    width: 60vw;
    height: 40px;
  }
}
</style>
