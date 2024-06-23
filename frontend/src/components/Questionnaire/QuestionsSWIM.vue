<template>
  <div id="secondpage">
    <div v-if="indexpage=='secondpage'">
      <div class="row mt-4 justify-content-center align-items-center">
        <div class="col-12 col-md-10">
          <div class="progress-container">
            <h4>Bilan Carbone Moyen</h4>
            <div class="progress mb-4">
              <div class="progress-bar" role="progressbar" :style="{ width: moyBilanCO2 + '%' }" :aria-valuenow="moyBilanCO2" aria-valuemin="0" aria-valuemax="100">{{ moyBilanCO2 }}</div>
            </div>
            <h4>Votre Bilan Carbone</h4>
            <div class="progress">
              <div class="progress-bar bg-success" role="progressbar" :style="{ width: bilanCO2 + '%' }" :aria-valuenow="bilanCO2" aria-valuemin="0" aria-valuemax="100">{{ bilanCO2 }}</div>
            </div>
          </div>
        </div>
      </div>

      <div class="row mt-4 justify-content-center align-items-center">
        <div class="col-8 col-md-6">
          <div :class="['feature-card', getCategoryClass(questions[index].categorie)]">
            <div class="text">{{ questions[index].question }}</div>
          </div>
        </div>
      </div>
      <div class="row mt-4 justify-content-center align-items-center" v-if="questions[index].type === 'text'">
        <div class="col-8 col-md-6">
          <div :class="['feature-card-reponse',getCategoryClass(questions[index].categorie)]" >
            <input type="number" :class="['form-control']" placeholder="Votre réponse" v-model="textReponse" min="0">
          </div>
        </div>
      </div>

      <div class="row mt-4 justify-content-center align-items-center" v-if="questions[index].type === 'multiple'">
        <div class="col-12 d-flex justify-content-center flex-wrap">
          <div v-for="(reponse, idx) in questions[index].reponses" :key="idx" class="p-2">
            <button v-if="questions[index].id == 0" type="button" :class="['btn-response', 'text-btn', getCategoryClass(questions[index].categorie)]" @click="getAnswer(idx)">{{ Object.keys(reponse)[0]}}</button>
            <button v-else-if="questions[index].id == 3" type="button" :class="['btn-response', 'text-btn', getCategoryClass(questions[index].categorie)]" @click="getAnswer(idx)">{{ Object.keys(reponse)[0]}}</button>
            <button v-else type="button" :class="['btn-response', 'text-btn', getCategoryClass(questions[index].categorie)]" @click="getAnswer(reponse)">{{ reponse }}</button>
          </div>
        </div>
      </div>

      <div class="row mt-4 justify-content-center align-items-center">
        <div class="col-8 col-md-6 d-flex justify-content-center">
          <button v-if="this.index < (this.questions.length - 1)" type="button" class="btn text-btn" @click="suivante()">Question suivante</button>
          <button v-else type="button" class="btn text-btn" @click="finir()">Finir le questionnaire</button>
        </div>
      </div>
    </div>
    <BilanEEPageVue v-if="indexpage=='bilanpage'" :bilan-moy_prop="moyBilanCO2" :bilan_prop="bilanCO2" :emission="saveEmission"></BilanEEPageVue>
  </div>
</template>

<script>
import BilanEEPageVue from './BilanEEPage.vue';

export default {
  name: 'SWIMEEPage',
  components:{
    BilanEEPageVue
  },
  data() {
    return {
      questions: [
        {id:0, question: "Comment vous êtes-vous rendus à votre destination ?", type: 'multiple', reponses: [{'Avion':100}, {'Train':20}, {'Voiture':40}, {'Bus':30}], categorie:'transport' },
        {id:1, question: "Quelle est votre consommation de viande rouge par semaine ?", type: 'text', categorie:'nourriture' },
        {id:2, question: "Combien de fois avez-vous pris les transports ?", type: 'text', categorie:'transport' },
        {id:3, question: "Votre chauffage était alimenté par quelle énergie ?", type: 'multiple', reponses: [{'Electricité':9}, {'Gaz':20}], categorie:'energie' }
      ],
      index: 0,
      textReponse:'',
      multipleReponse:'',

      saveMultipleReponse: {},
      saveTextReponse: {},

      saveEmission: [{name:'transport', amount:0, color:'bg-blue'}, {name:'nourriture', amount:0, color:'bg-red'}, {name:'energie', amount:0, color:'bg-yellow'}],

      bilanCO2:0,
      moyBilanCO2:4.6,

      indexpage: 'secondpage'

    };
  },
  methods: {
    precedente() {
      if (this.index > 0) {
        console.log('précédente');
        this.index--;
        console.log(this.index);
      }
    },
    suivante() {
      if (this.index < (this.questions.length - 1)) {
        console.log('suivante');
        console.log(this.textReponse)
        console.log(this.multipleReponse)
        this.calculBilanCO2()
        this.index++;
        console.log(this.index);
        
      }
    },
    calculBilanCO2() {
      switch (this.questions[this.index].id) {
        case 0:
          console.log(Object.values(this.questions[this.index].reponses[this.multipleReponse]))
          this.bilanCO2 = Object.values(this.questions[this.index].reponses[this.multipleReponse]) * 0.2 + this.bilanCO2
          this.saveEmissionFunction((Object.values(this.questions[this.index].reponses[this.multipleReponse]) * 0.2))
          break;
        case 1:
          this.bilanCO2 = this.textReponse * 0.1 + this.bilanCO2
          this.saveEmissionFunction((this.textReponse * 0.1))
          break;
        case 2:
          this.bilanCO2 = this.textReponse * 0.8 + this.bilanCO2
          this.saveEmissionFunction((this.textReponse * 0.8))
          break;
        case 3:
          console.log(Object.values(this.questions[this.index].reponses[this.multipleReponse]))
          this.bilanCO2 = Object.values(this.questions[this.index].reponses[this.multipleReponse]) * 0.7 + this.bilanCO2
          this.saveEmissionFunction((Object.values(this.questions[this.index].reponses[this.multipleReponse]) * 0.7))
          break;
        case 4:
          questions[index].reponses
          break;
        default:
          break;
      }
      console.log(this.saveEmission)
    },
    saveEmissionFunction(valueAdd){
      switch (this.questions[this.index].categorie) {
        case 'transport':
          this.saveEmission[0].amount = this.saveEmission[0].amount + valueAdd
          break;
        case 'nourriture':
          this.saveEmission[1].amount = this.saveEmission[1].amount + valueAdd
          break;
        case 'energie':
          this.saveEmission[2].amount = this.saveEmission[2].amount + valueAdd
          break;
      
        default:
          break;
      }
    },
    getAnswer(reponse){
      this.multipleReponse = reponse
      console.log(this.multipleReponse)
    },
    finir(){
      this.calculBilanCO2()
      this.indexpage = 'bilanpage'
    },
    getCategoryClass(categorie) {
      switch(categorie) {
        case 'transport':
          return 'transport-category';
        case 'nourriture':
          return 'nourriture-category';
        case 'energie':
          return 'energie-category';
        default:
          return '';
      }
    }
  }
};
</script>

<style scoped>
.feature-card {
  border-radius: 20px;
  padding: 20px;
  margin: 20px 0;
  height: 250px;
  display: flex;
  justify-content: center;
  align-items: center;
}

.feature-card-reponse {
  /* background-color: #C1E4C3; */
  border-radius: 20px;
  padding: 20px;
  margin: 20px 0;
  display: flex;
  justify-content: center;
  align-items: center;
}

.transport-category {
  background-color: blue; /* Couleur pour la catégorie transport */
}

.nourriture-category {
  background-color: red; /* Couleur pour la catégorie nourriture */
}

.energie-category {
  background-color: yellow; /* Couleur pour la catégorie énergie */
}

.text {
  font-size: xx-large;
}

.btn {
  background-color: #C1E4C3 !important;
  border-radius: 20px;
  margin: 20px 0;
}

.btn-response {
  border-radius: 20px;
  margin: 20px 0;
}

.text-btn {
  font-size: medium;
  width: 20vw;
  height: 60px;
}

@media (max-width: 768px) {
  .text {
    font-size: large;
  }

  .text-btn {
    font-size: small;
    width: 30vw;
    height: 60px;
  }
}

@media (max-width: 375px) {
  .text {
    font-size: large;
  }

  .text-btn {
    font-size: small;
    width: 40vw;
    height: 60px;
  }
}
</style>
