<template>
  <div id="bilanpage">
    <div class="container">
      <div class="row justify-content-center my-4">
        <div class="col-12 col-md-5 text-center mb-4">
          <h4 class="label">Mon empreinte :</h4>
          <div class="progress mx-auto">
            <div class="progress-bar bg-success" role="progressbar" :style="{ width: bilan_prop + '%' }" :aria-valuenow="bilan_prop" aria-valuemin="0" aria-valuemax="100">{{ bilan_prop }} kgCO2e</div>
          </div>
          <h4 class="label-moy label">Empreinte moyenne :</h4>
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
                  <h5 class="card-title">{{ advice.saving }} kgCO2e</h5>
                  <p class="card-text">{{ advice.description }} kgCO2e</p>
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
export default {
  name: 'CarbonFootprint',
  data() {
    return {
      conseils: [
        {
          name: 'transport',
          advices: [
            { saving: '-600', description: 'Prendre deux fois moins l\'avion', percentage: '10' },
            { saving: '-1200', description: 'Prendre le train', percentage: '20' }
          ]
        },
        {
          name: 'nourriture',
          advices: [
            { saving: '-200', description: 'Réduire votre consommation de viande', percentage: '5' }
          ]
        },
        {
          name: 'energie',
          advices: [
            { saving: '-100', description: 'Acheter des vêtements de seconde main', percentage: '3' }
          ]
        }
      ],
      activeSource: null,
      objectif: 2.5
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
  methods: {
    toggleDetails(index) {
      this.activeSource = this.activeSource === index ? null : index;
    },
    getAdvicesForSource(name) {
      const conseil = this.conseils.find(c => c.name === name);
      return conseil ? conseil.advices : [];
    }
  }
};
</script>

<style scoped>
.progbar{
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
