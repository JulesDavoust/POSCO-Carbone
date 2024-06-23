<template>
    <div id="bilanpage">
        <div class="container">
            <div class="row justify-content-center my-4">
                <div class="col-12 col-md-8 text-center">
                    <h4 class="label">Mon empreinte :</h4>
                    <div class="progress">
                        <div class="progress-bar bg-success" role="progressbar" :style="{ width: bilan_prop + '%' }" :aria-valuenow="bilan_prop" aria-valuemin="0" aria-valuemax="100">{{ bilan_prop }}</div>
                    </div>
                    <h4 class="label-moy label">Empreinte moyenne :</h4>
                    <div class="progress">
                        <div class="progress-bar bg-success" role="progressbar" :style="{ width: bilanMoy_prop + '%' }" :aria-valuenow="bilanMoy_prop" aria-valuemin="0" aria-valuemax="100">{{ bilanMoy_prop }}</div>
                    </div>
                </div>
            </div>

            <div class="row justify-content-center my-4">
                <div class="col-12 col-md-8 text-center">
                    <h4 class="label">Mes principales sources d’émissions :</h4>
                    <div v-for="(source, index) in sortedEmission" :key="index" class="my-2">
                        <button class="btn btn-block text-left source-btn" :class="source.color" @click="toggleDetails(index)">
                            {{ index + 1 }} : {{ source.name }} - {{ source.amount }} tonnes
                        </button>
                        <div v-if="activeSource === index" class="details">
                            <div class="card mt-2" v-for="(advice, idx) in getAdvicesForSource(source.name)" :key="idx">
                                <div class="card-body">
                                    <h5 class="card-title">{{ advice.saving }} kg</h5>
                                    <p class="card-text">{{ advice.description }}</p>
                                    <p class="card-text"><small class="text-muted">{{ advice.percentage }}% de votre empreinte</small></p>
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
.label {
  background-color: #C1E4C3;
  padding: 10px 20px;
  border-radius: 20px;
  display: inline-block;
  margin-bottom: 10px;
}

.source-btn {
  border: none;
  border-radius: 10px;
  padding: 10px;
  width: 100%;
  font-size: 1rem;
  color: white;
  cursor: pointer;
}

.details .card {
  background-color: #E0F7FA;
  border: none;
  border-radius: 10px;
  margin-top: 10px;
}

.details .card-title {
  font-size: 1.5rem;
  margin-bottom: 10px;
}

.details .card-text {
  font-size: 1rem;
}

.label-moy {
  margin-top: 2%;
}

.bg-blue {
  background-color: blue;
}

.bg-red {
  background-color: red;
}

.bg-yellow {
  background-color: yellow;
}
</style>

  