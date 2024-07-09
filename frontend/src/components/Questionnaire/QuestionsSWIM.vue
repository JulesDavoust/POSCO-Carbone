<template>
  <div>
    <div class="container" v-if="indexpage === 'secondpage'">

      <!-- Formulaire -->
      <div class="conteneur text-center">
        <div class="card-wrapper">
          <div class="progress-container mb-3">
            <div class="progress" style="height: 30px;">
              <div class="progress-bar bg-transport" role="progressbar" :style="{ width: transportCO2 + '%' }"
                aria-valuenow="transportCO2" aria-valuemin="0" aria-valuemax="100">{{ transportCO2 }}</div>
              <div class="progress-bar bg-nourriture" role="progressbar" :style="{ width: nourritureCO2 + '%' }"
                aria-valuenow="nourritureCO2" aria-valuemin="0" aria-valuemax="100">{{ nourritureCO2 }}</div>
              <div class="progress-bar bg-energie" role="progressbar" :style="{ width: energieCO2 + '%' }"
                aria-valuenow="energieCO2" aria-valuemin="0" aria-valuemax="100">{{ energieCO2 }}</div>
            </div>
          </div>

          <transition :name="randomTransition" mode="out-in">
            <div v-if="currentQuestion < filteredQuestions.length" :key="currentQuestion"
              :class="['card', getCategoryClass(filteredQuestions[currentQuestion].categorie)]" class="mt-4">
              <div class="card-body">
                <h5 class="card-title">{{ filteredQuestions[currentQuestion].question }}</h5>

                <div v-if="filteredQuestions[currentQuestion].type === 'Texte'" class="mt-4">
                  <input type="number" class="form-control" placeholder="Votre réponse" v-model="textReponse" min="0">
                </div>

                <div v-if="filteredQuestions[currentQuestion].type === 'Multiple'"
                  class="d-flex flex-wrap justify-content-center mt-4">
                  <button v-for="(answer, index) in filteredQuestions[currentQuestion].answers" :key="index"
                    @click="selectAnswer(answer.value)"
                    :class="['btn m-2', getButtonClass(filteredQuestions[currentQuestion].categorie)]">
                    {{ answer.text }}
                  </button>
                </div>

                <button class="btn btn-primary mt-3" @click="nextQuestion()">{{ currentQuestion < filteredQuestions.length - 1 ? 'Question suivante' : 'Terminer le questionnaire' }}</button>
              </div>
            </div>
          </transition>
        </div>
      </div>
    </div>
    <BilanEEPage v-else :bilan-moy_prop="moyBilanCO2" :bilan_prop="bilanCO2" :emission="saveEmission" />
  </div>
</template>




<script>
import BilanEEPage from './BilanEEPage.vue';
import AuthService from '../../services/auth.service.js'
export default {
  components: {
    BilanEEPage
  },
  data() {
    return {
      API_URL: 'http://localhost:5000/',
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
      saveEmission: [{ name: 'Transport', amount: 0, color: '#aed6f1' }, { name: 'Nourriture', amount: 0, color: '#f5b7b1' }, { name: 'Energie', amount: 0, color: '#f9e79f' }],
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
      randomTransition: 'fade',
      questionsWithResponses: [],
      bilanData: {
        BilanTotal: 0,
        BilanCatégorie: 2,
        Date_BilanCarbone: new Date().toISOString(),
        ID_Formulaire: 2
      },
      conseils: {
        transport: [],
        nourriture: [],
        énergie: []
      }
    };
  },
  props: {
    token: String
  },
  computed: {
    filteredQuestions() {
      this.questionsWithResponses.filter(question => question.faite);
      console.log(this.questionsWithResponses)
      return this.questionsWithResponses
    }
  },
  methods: {
    nextQuestion() {
      if (this.filteredQuestions[this.currentQuestion].type === 'Texte') {
        if (this.textReponse) {
          console.log(this.textReponse)
          this.calculBilanCO2();
          this.textReponse = '';
        } else {
          alert("Veuillez entrer une réponse.");
          return;
        }
      } else if (this.filteredQuestions[this.currentQuestion].type === 'Multiple') {
        if (this.multipleReponse) {
          console.log("mult: ",this.multipleReponse)
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
    formatDateToSQL(date) {
      return date.toISOString().split('T')[0]; // Retourne la date au format YYYY-MM-DD
    },
    async handleBilanCarbone() {
      const headers = {
        ...AuthService.authHeader(),
        'Content-Type': 'application/json'
      };

      // Formater la date
      this.bilanData.Date_BilanCarbone = this.formatDateToSQL(new Date());
      this.bilanData.BilanTotal = this.bilanCO2
      try {
        const response = await fetch(`${this.API_URL}bilan_carbone_par_utilisateur`, {
          method: 'GET',
          headers: headers
        });

        if (!response.ok) {
          throw new Error(`An error has occurred: ${response.status}`);
        }

        const bilansCarbone = await response.json();

        if (bilansCarbone.length > 0) {
          // Si l'utilisateur a déjà un bilan, le mettre à jour
          const bilanId = bilansCarbone[0].ID_BilanCarbone; // Prendre le premier bilan trouvé
          const updateResponse = await fetch(`${this.API_URL}bilans/${bilanId}`, {
            method: 'PUT',
            headers: headers,
            body: JSON.stringify(this.bilanData)
          });

          if (!updateResponse.ok) {
            throw new Error(`An error has occurred: ${updateResponse.status}`);
          }

          this.message = 'BilanCarbone updated successfully';
          console.log(await updateResponse.json());
        } else {
          // Si l'utilisateur n'a pas de bilan, en créer un nouveau
          const createResponse = await fetch(`${this.API_URL}bilans`, {
            method: 'POST',
            headers: headers,
            body: JSON.stringify(this.bilanData)
          });

          if (!createResponse.ok) {
            throw new Error(`An error has occurred: ${createResponse.status}`);
          }

          this.message = 'BilanCarbone created successfully';
          console.log(await createResponse.json());
        }
      } catch (error) {
        this.message = 'There was an error!';
        console.error('There was an error!', error);
      }
    },
    async fetchRandomQuestionDetailsAndResponses(userId) {
      const headers = AuthService.authHeader();

      try {
        // Étape 1 : Récupérer toutes les questions associées au formulaire ID 2
        const response = await fetch(`${this.API_URL}avoir`, {
          method: 'GET',
          headers: headers
        });

        if (!response.ok) {
          throw new Error(`An error has occurred: ${response.status}`);
        }

        const questions = await response.json();
        console.log(questions);
        const filteredQuestions = questions.filter(q => q.ID_Formulaire === 2);
        console.log(filteredQuestions);

        // Étape 2 : Récupérer toutes les questions non répondues
        const nonReponduesResponse = await fetch(`${this.API_URL}question_non_repondue`, {
          method: 'GET',
          headers: headers
        });

        if (!nonReponduesResponse.ok) {
          throw new Error(`An error has occurred: ${nonReponduesResponse.status}`);
        }

        const nonRepondues = await nonReponduesResponse.json();
        console.log(nonRepondues);

        // Filtrer les questions non répondues associées au formulaire ID 2
        const filteredNonRepondues = nonRepondues.filter(q => filteredQuestions.some(fq => fq.ID_Question === q.ID_Question));
        console.log(filteredNonRepondues);

        // Étape 3 : Sélectionner 5 questions aléatoires parmi les questions non répondues filtrées
        const randomQuestions = this.getRandomItems(filteredNonRepondues, 5);
        const randomQuestionIds = randomQuestions.map(q => q.ID_Question);
        console.log(randomQuestionIds);

        // Étape 4 : Récupérer les réponses pour chaque question
        const questionResponsesPromises = randomQuestionIds.map(id =>
          fetch(`${this.API_URL}reponses_par_question/${id}`, {
            method: 'GET',
            headers: headers
          }).then(response => {
            if (!response.ok) {
              throw new Error(`An error has occurred: ${response.status}`);
            }
            return response.json();
          })
        );

        const questionResponses = await Promise.all(questionResponsesPromises);
        console.log(questionResponses)
        // Étape 5 : Récupérer l'émission CO2 pour chaque réponse
        const emissionsPromises = questionResponses.flat().map(response =>
          fetch(`${this.API_URL}emission_co2_par_reponse/${response.ID_Reponse}`, {
            method: 'GET',
            headers: headers
          }).then(response => {
            if (!response.ok) {
              throw new Error(`An error has occurred: ${response.status}`);
            }
            return response.json().then(emission => ({
              ...response,
              Coefficient_EmissionCO2: emission.Coefficient_EmissionCO2,
              ID_EmissionCO2: emission.ID_EmissionCO2
            }));
          })
        );

        const emissions = await Promise.all(emissionsPromises);
        console.log(emissions);

        // Étape 6 : Combiner les détails des questions avec leurs réponses et les émissions de CO2
        this.questionsWithResponses = randomQuestions.map(question => ({
          id: question.ID_Question,
          question: question.Texte,
          answers: questionResponses
            .flat()
            .filter(response => response.ID_Question === question.ID_Question)
            .map(response => {
              const emission = emissions.find(e => e.ID_EmissionCO2 === response.ID_EmissionCO2);
              console.log('emission found:', emission);
              return {
                text: response.Texte_reponse,
                value: emission ? emission.Coefficient_EmissionCO2 : null
              };
            }),
          type: question.Type,
          categorie: question.Catégorie
        }));
        console.log(this.questionsWithResponses);
      } catch (error) {
        console.error('There was an error!', error);
      }
    },
    getRandomItems(arr, count) {
      const shuffled = arr.sort(() => 0.5 - Math.random());
      return shuffled.slice(0, count);
    },
    

    selectAnswer(value) {
      this.multipleReponse = value;
    },
    calculBilanCO2() {
      let question = this.filteredQuestions[this.currentQuestion];
      console.log(question)
      let value = question.type === 'Texte' ? parseFloat(this.textReponse) : parseFloat(this.multipleReponse);
      console.log(value)
      this.bilanCO2 += (value);
      console.log(this.bilanCO2)
      switch (question.categorie) {
        case 'Transport':
          console.log(question.categorie)
          this.transportCO2 += value;
          this.saveEmission[0].amount = this.transportCO2
          console.log(this.saveEmission)
          break;
        case 'Nourriture':
          console.log(question.categorie)
          this.nourritureCO2 += value;
          this.saveEmission[1].amount = this.nourritureCO2
          console.log(this.saveEmission)
          break;
        case 'Energie':
          console.log(question.categorie)
          this.energieCO2 += value;
          this.saveEmission[2].amount = this.energieCO2
          console.log(this.saveEmission)
          break;
      }
    },
    getCategoryClass(categorie) {
      switch (categorie) {
        case 'Transport':
          return 'transport-category';
        case 'Nourriture':
          return 'nourriture-category';
        case 'Energie':
          return 'energie-category';
        default:
          return '';
      }
    },
    getButtonClass(categorie) {
      switch (categorie) {
        case 'Transport':
          return 'btn-transport';
        case 'Nourriture':
          return 'btn-nourriture';
        case 'Energie':
          return 'btn-energie';
        default:
          return '';
      }
    },
    // finishQuestionnaire() {
    //   this.indexpage = 'bilanpage';
    // },
    async finishQuestionnaire() {
      console.log(this.bilanCO2)
      await this.handleBilanCarbone()
      this.indexpage = 'bilanpage';
      try {
        const response = await fetch(`${this.API_URL}questionnaire/complete`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({ token: this.token })
        });

        const data = await response.json();
        if (data.message === 'Questionnaire completed') {
          this.token = data.new_token;
          localStorage.setItem('swim', this.token);
        } else {
          console.error('Error marking questionnaire as completed:', data.message);
        }
      } catch (error) {
        console.error('An error occurred while marking the questionnaire as completed:', error);
      }
    }
  },
  created() {
    this.fetchRandomQuestionDetailsAndResponses();
  },
};
</script>


<style scoped>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s;
}

.fade-enter,
.fade-leave-to {
  opacity: 0;
}

.slide-right-enter-active,
.slide-right-leave-active {
  transition: transform 0.5s;
}

.slide-right-enter,
.slide-right-leave-to {
  transform: translateX(100%);
}

.flip-up-enter-active,
.flip-up-leave-active {
  transition: transform 0.5s;
  transform-style: preserve-3d;
}

.flip-up-enter,
.flip-up-leave-to {
  transform: rotateX(90deg);
}

.rotate-right-enter-active,
.rotate-right-leave-active {
  transition: transform 0.5s;
}

.rotate-right-enter,
.rotate-right-leave-to {
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
