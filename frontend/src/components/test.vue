<template>
  <div>
    <div class="container" v-if="indexpage === 'secondpage'">
      <!-- Page d'accueil -->
      <div v-if="!started" class="text-center mt-5">
        <h1>Bienvenue sur le calculateur de bilan carbone</h1>
        <button class="btn btn-primary mt-4" @click="startForm">Commencer le questionnaire</button>
      </div>

      <!-- Formulaire -->
      <div v-else class="conteneur text-center">
        <div class="card-wrapper">
          <div class="progress-container mb-3">
            <div class="progress" style="height: 30px;">
              <div class="progress-bar bg-transport" role="progressbar" :style="{ width: transportCO2 + '%' }" aria-valuenow="transportCO2" aria-valuemin="0" aria-valuemax="100">{{ transportCO2 }}</div>
              <div class="progress-bar bg-nourriture" role="progressbar" :style="{ width: nourritureCO2 + '%' }" aria-valuenow="nourritureCO2" aria-valuemin="0" aria-valuemax="100">{{ nourritureCO2 }}</div>
              <div class="progress-bar bg-energie" role="progressbar" :style="{ width: energieCO2 + '%' }" aria-valuenow="energieCO2" aria-valuemin="0" aria-valuemax="100">{{ energieCO2 }}</div>
            </div>
          </div>

          <transition :name="randomTransition" mode="out-in">
            <div v-if="currentQuestion < filteredQuestions.length" :key="currentQuestion" :class="['card', getCategoryClass(filteredQuestions[currentQuestion].categorie)]" class="mt-4">
              <div class="card-body">
                <h5 class="card-title">{{ filteredQuestions[currentQuestion].question }}</h5>
                
                <div v-if="filteredQuestions[currentQuestion].type === 'text'" class="mt-4">
                  <input type="number" class="form-control" placeholder="Votre réponse" v-model="textReponse" min="0">
                </div>

                <div v-if="filteredQuestions[currentQuestion].type === 'multiple'" class="d-flex flex-wrap justify-content-center mt-4">
                  <button v-for="(answer, index) in filteredQuestions[currentQuestion].answers" :key="index" @click="selectAnswer(answer.value)" :class="['btn m-2', getButtonClass(filteredQuestions[currentQuestion].categorie)]">
                    {{ answer.text }}
                  </button>
                </div>
                
                <button class="btn btn-primary mt-3" @click="nextQuestion">{{ currentQuestion < filteredQuestions.length - 1 ? 'Question suivante' : 'Terminer le questionnaire' }}</button>
              </div>
            </div>
          </transition>
        </div>
      </div>
    </div>
    <BilanEEPageVue v-else :bilan-moy_prop="moyBilanCO2" :bilan_prop="bilanCO2" :emission="saveEmission" />
  </div>
</template>




<script>
import BilanEEPageVue from './Questionnaire/BilanEEPage.vue';

export default {
  components: {
    BilanEEPageVue
  },
  data() {
    return {
      moyBilanCO2: 50,
      started: false,
      currentQuestion: 0,
      bilanCO2: 0,
      transportCO2: 0,
      nourritureCO2: 0,
      energieCO2: 0,
      userAnswers: [],
      textReponse: '',
      multipleReponse: '',
      indexpage: 'secondpage',
      saveEmission: [{name:'transport', amount:0, color:'#aed6f1'}, {name:'nourriture', amount:0, color:'#f5b7b1'}, {name:'energie', amount:0, color:'#f9e79f'}],
      questions: [
        {
          id: 0,
          question: "À quelle destination vous dirigez-vous?",
          answers: [
            { text: "Paris", value: 10 },
            { text: "New York", value: 30 },
            { text: "Tokyo", value: 50 }
          ],
          type: 'multiple',
          categorie: 'transport',
          faite: false
        },
        {
          id: 1,
          question: "Quel moyen de transport utilisez-vous?",
          answers: [
            { text: "Avion", value: 50 },
            { text: "Train", value: 20 },
            { text: "Voiture", value: 30 }
          ],
          type: 'multiple',
          categorie: 'transport',
          faite: true
        },
        {
          id: 2,
          question: "Comment vous déplacez-vous ?",
          answers: [
            { text: "Bus", value: 10 },
            { text: "Covoiturage", value: 20 },
            { text: "Métro", value: 10 },
            { text: "Voiture", value: 40 },
            { text: "Vélo", value: 5 }
          ],
          type: 'multiple',
          categorie: 'transport',
          faite: false
        },
        {
          id: 3,
          question: "Combien de fois par semaine mangez-vous de la viande?",
          type: 'text',
          categorie: 'nourriture',
          faite: true
        },
        {
          id: 4,
          question: "Quelle est l'énergie de votre logement pour vous chauffer?",
          answers: [
            { text: "Électricité", value: 10 },
            { text: "Gaz", value: 20 }
          ],
          type: 'multiple',
          categorie: 'energie',
          faite: true
        },
        {
          id: 5,
          question: "Sélectionnez le nombre de repas que vous mangez par semaine",
          answers: [
            { text: "Végétarien", value: 10 },
            { text: "Viande rouge", value: 50 },
            { text: "Viande maigre", value: 30 },
            { text: "Poisson", value: 20 }
          ],
          type: 'multiple',
          categorie: 'nourriture',
          faite: true
        }
      ],
      transitions: ['fade', 'slide-right', 'flip-up', 'rotate-right'],
      randomTransition: 'fade'
    };
  },
  computed: {
    filteredQuestions() {
      return this.questions.filter(question => question.faite);
    }
  },
  methods: {
    startForm() {
      this.started = true;
    },
    nextQuestion() {
      if (this.filteredQuestions[this.currentQuestion].type === 'text') {
        if (this.textReponse) {
          this.calculBilanCO2();
          this.textReponse = '';
        } else {
          alert("Veuillez entrer une réponse.");
          return;
        }
      } else if (this.filteredQuestions[this.currentQuestion].type === 'multiple') {
        if (this.multipleReponse) {
          this.calculBilanCO2();
          this.multipleReponse = '';
        } else {
          alert("Veuillez sélectionner une réponse.");
          return;
        }
      }

      if (this.currentQuestion < this.filteredQuestions.length - 1) {
        this.currentQuestion++;
        this.randomTransition = this.transitions[Math.floor(Math.random() * this.transitions.length)];
      } else {
        this.finishQuestionnaire();
      }
    },
    selectAnswer(value) {
      this.multipleReponse = value;
    },
    calculBilanCO2() {
      let question = this.filteredQuestions[this.currentQuestion];
      let value = question.type === 'text' ? this.textReponse : this.multipleReponse;
      this.bilanCO2 += (value / 10);

      switch (question.categorie) {
        case 'transport':
          this.transportCO2 += value / 10;
          this.saveEmission[0].amount = this.transportCO2
          break;
        case 'nourriture':
          this.nourritureCO2 += value / 10;
          this.saveEmission[1].amount = this.nourritureCO2
          break;
        case 'energie':
          this.energieCO2 += value / 10;
          this.saveEmission[2].amount = this.energieCO2
          break;
      }
    },
    getCategoryClass(categorie) {
      switch (categorie) {
        case 'transport':
          return 'transport-category';
        case 'nourriture':
          return 'nourriture-category';
        case 'energie':
          return 'energie-category';
        default:
          return '';
      }
    },
    getButtonClass(categorie) {
      switch (categorie) {
        case 'transport':
          return 'btn-transport';
        case 'nourriture':
          return 'btn-nourriture';
        case 'energie':
          return 'btn-energie';
        default:
          return '';
      }
    },
    finishQuestionnaire() {
      this.indexpage = 'bilanpage';
    }
  }
};
</script>


<style scoped>
.fade-enter-active, .fade-leave-active {
  transition: opacity 0.5s;
}
.fade-enter, .fade-leave-to {
  opacity: 0;
}

.slide-right-enter-active, .slide-right-leave-active {
  transition: transform 0.5s;
}
.slide-right-enter, .slide-right-leave-to {
  transform: translateX(100%);
}

.flip-up-enter-active, .flip-up-leave-active {
  transition: transform 0.5s;
  transform-style: preserve-3d;
}
.flip-up-enter, .flip-up-leave-to {
  transform: rotateX(90deg);
}

.rotate-right-enter-active, .rotate-right-leave-active {
  transition: transform 0.5s;
}
.rotate-right-enter, .rotate-right-leave-to {
  transform: rotateY(90deg);
}

.card-wrapper {
  width: 90vw;
  max-width: 600px;
  margin: auto;
}

.progress-container {
  width: 100%;
}

.transport-category {
  background-color: #D1ECF1;
  border-color: #BEE5EB;
}

.nourriture-category {
  background-color: #F8D7DA;
  border-color: #F5C6CB;
}

.energie-category {
  background-color: #FFF3CD;
  border-color: #FFEEBA;
}

.btn-transport {
  background-color: #85c1e9;
  color: #0b6f7f;
}

.btn-nourriture {
  background-color: #f1948a;
  color: #a01927;
}

.btn-energie {
  background-color: #F7DC6F;
  color: #a5b708;
}

.progress-bar {
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
}

.bg-transport {
  background-color: #aed6f1 !important;
}

.bg-nourriture {
  background-color: #f5b7b1 !important;
}

.bg-energie {
  background-color: #f9e79f !important;
}
</style>
