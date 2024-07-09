<template>
  <div id="bilanpage">
    <div class="container">
      <div class="row justify-content-center my-4">
        <div class="col-12 col-md-5 text-center mb-4">
          <h4 class="label">Mon empreinte :</h4>
          <div class="progress mx-auto">
            <div class="progress-bar bg-success" role="progressbar" :style="{ width: bilan_prop + '%' }" :aria-valuenow="bilan_prop" aria-valuemin="0" aria-valuemax="100">{{ bilan_prop }} kgCO2e</div>
          </div>
          <h4 class="label-moy label">Empreinte moyenne : {{ bilanMoy_prop }} kgCO2e</h4>
          <div class="progress mx-auto">
            <div class="progress-bar bg-success" role="progressbar" :style="{ width: bilanMoy_prop + '%' }" :aria-valuenow="bilanMoy_prop" aria-valuemin="0" aria-valuemax="100">{{ bilanMoy_prop }} kgCO2e</div>
          </div>
        </div>
        <div class="col-12 col-md-7 text-center">
          <h4 class="label">Mes principales sources d’émissions :</h4>
          <div v-for="(source, index) in sortedEmission" :key="index" class="my-2">
            <button class="btn btn-block text-left source-btn" :style="{ backgroundColor: source.color }" @click="toggleDetails(index)">
              {{ index + 1 }} : {{ source.name }} - {{ source.amount }} kgCO2e
            </button>
            <div v-if="activeSource === index" class="details">
              <div class="card mt-2" v-for="(advice, idx) in getAdvicesForSource(source.name)" :key="idx">
                <div class="card-body">
                  <p class="card-text">{{ advice.description }}</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import AuthService from '../../services/auth.service.js'

export default {
  name: 'CarbonFootprint',
  data() {
    return {
      conseils: [],
      activeSource: null,
      objectif: 2.5,
      API_URL: "http://localhost:5000/"
    };
  },
  props: {
    bilanMoy_prop: Number,
    bilan_prop: Number,
    emission: Array
  },
  computed: {
    sortedEmission() {
      return this.emission.sort((a, b) => b.amount - a.amount);
    }
  },
  async created() {
    console.log(this.emission);
    console.log(this.bilan_prop);
    await this.fetchConseils();
  },
  methods: {
    toggleDetails(index) {
      this.activeSource = this.activeSource === index ? null : index;
    },
    getAdvicesForSource(name) {
      console.log("Searching for advice with name:", name);
      const conseil = this.conseils.find(c => c.name.toLowerCase().trim() === name.toLowerCase().trim());
      console.log("Found conseil:", conseil);
      return conseil ? conseil.advices : [];
    },
    async fetchBilanCarbone(userId) {
      const headers = AuthService.authHeader();

      try {
        const response = await fetch(`${this.API_URL}bilan_carbone_par_utilisateur`, {
          method: 'GET',
          headers: headers
        });

        if (!response.ok) {
          throw new Error(`An error has occured: ${response.status}`);
        }

        this.bilanCarbone = await response.json();
        console.log(this.bilanCarbone);
      } catch (error) {
        console.error('There was an error!', error);
      }
    },
    async fetchConseils() {
      const categories = ['Transport', 'Nourriture', 'Energie'];
      const headers = AuthService.authHeader();

      try {
        const allConseils = await Promise.all(
          categories.map(categorie =>
            fetch(`${this.API_URL}conseils_par_categorie/${categorie}`, {
              method: 'GET',
              headers: headers
            }).then(response => {
              if (!response.ok) {
                throw new Error(`An error has occurred: ${response.status}`);
              }
              return response.json();
            })
          )
        );

        this.conseils = categories.map((categorie, index) => ({
          name: categorie,
          advices: this.getRandomItems(allConseils[index], 3).map(conseil => ({
            description: conseil.Texte
          }))
        }));
        console.log(this.conseils);
      } catch (error) {
        console.error('There was an error!', error);
      }
    },
    getRandomItems(arr, count) {
      const shuffled = arr.sort(() => 0.5 - Math.random());
      return shuffled.slice(0, count);
    },
  }
};
</script>

<style scoped>
.progbar {
  margin-right: 10%;
}

.label {
  background-color: rgb(174, 211, 169);
  padding: 10px 15px;
  border-radius: 10px;
  display: inline-block;
  margin-bottom: 15px;
  font-size: 1rem;
  font-weight: normal;
}

.source-btn {
  border: none;
  border-radius: 10px;
  padding: 10px;
  width: 100%;
  font-size: 1rem;
  color: white;
  cursor: pointer;
  background-color: #6c757d; /* Default color if none provided */
  margin-top: 10px;
}

.details .card {
  background-color: #E0F7FA;
  border: none;
  border-radius: 10px;
  margin-top: 10px;
}

.details .card-title {
  font-size: 1.2rem;
  margin-bottom: 5px;
}

.details .card-text {
  font-size: 0.9rem;
}

.label-moy {
  margin-top: 15px;
}

.progress {
  height: 20px;
  width: 100%;
  max-width: 500px;
  margin-bottom: 15px;
}

.progress-bar {
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.9rem;
  font-weight: normal;
  color: white;
}

.bg-blue {
  background-color: blue !important;
}

.bg-red {
  background-color: red !important;
}

.bg-yellow {
  background-color: yellow !important;
}
@media (min-width: 769px) {
  .container {
    max-width: 1200px;
    border-radius: 20px;
    padding: 5vh;
    background-color: #C1E4C3;
  }
}

@media (max-width: 769px) {
  .container {
    max-width: 100%;
    padding: 0 15px;
  }
}
</style>
