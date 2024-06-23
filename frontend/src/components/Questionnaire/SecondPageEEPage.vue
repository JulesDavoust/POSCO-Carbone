<template>
    <div id="secondpage">
      <div v-if="index=='secondpage'">
        <div class="row mt-4 justify-content-center align-items-center">
          <div class="col-8 col-md-6">
            <div class="feature-card">
              <div class="text">Je réalise ce questionnaire pour simuler la consommation de :</div>
            </div>
          </div>
        </div>
        <div class="row mt-4 justify-content-center align-items-center">
          <div class="col-8 col-md-6 d-flex justify-content-center">
            <button type="button" class="btn text-btn" @click="SWIM()">Ma SWIM</button>
          </div>
        </div>
        <div class="row mt-4 justify-content-center align-items-center">
          <div class="col-8 col-md-6 d-flex justify-content-center">
            <button type="button" class="btn text-btn" @click="SEMESTRE()">Mon semestre à l'étranger</button>
          </div>
        </div>
      </div>
      <QuestionsSWIMVue v-if="index=='questionnaireSWIM'"/>
    </div>
  </template>
  
  <script>
import QuestionsSWIMVue from './QuestionsSWIM.vue';

  export default {
    name: 'SecondPageEEPage',
    components:{
      QuestionsSWIMVue
    },
    data(){
      return{
        index:'secondpage'
      }
    },
    methods: {
      SWIM() {
        console.log('swim loaded');
        this.index='questionnaireSWIM'
      },
      SEMESTRE() {
        console.log('semestre loaded');
      }
    }
  };
  </script>
  
<style scoped>
.feature-card {
  background-color: #C1E4C3;
  border-radius: 20px;
  padding: 20px;
  margin: 20px 0;
  height: 250px;
  display: flex;
  justify-content: center;
  align-items: center;
}

.text {
  font-size: xx-large;
}

.btn {
  background-color: #C1E4C3 !important;
  border-radius: 20px;
  margin: 20px 0;
}

.text-btn {
  font-size: medium;
  width: 20vw;
  height: 60px;
}

@media(max-width: 768px) {
    .text{
        font-size: large;
    }

    .text-btn {
        font-size: small;
        width: 30vw;
        height: 60px;
    }
}

@media(max-width: 375px) {
    .text{
        font-size: large;
    }

    .text-btn {
        font-size: small;
        width: 40vw;
        height: 60px;
    }
}
</style>