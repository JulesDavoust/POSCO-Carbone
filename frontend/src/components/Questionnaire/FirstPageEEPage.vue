<template>
    <div class="firstpage">
        <div v-if="currentpage === 'first'">
            <div class="row mt-4 justify-content-center align-items-center">
                <div class="col-8 col-md-6 col-css2">
                    <div class="feature-card  col-css">
                        Voici un exemple de paragraphe : Bienvenue dans l'espace EFREI. Cet espace est dédié à la sensibilisation 
                        de la consommation pour le climat. Explications ... blablabla, c'est pour cela que deux questionnaires ont été établis, 
                        un pour la SWIM et un pour le semestre à l'étranger.
                    </div>
                </div>
            </div>
            <button type="button" class="btn" @click="Start()">Je commence le questionnaire</button>
        </div>
        <SecondPageEEPage v-if="currentpage === 'second'" />
    </div>
</template>

<script>
import SecondPageEEPage from './SecondPageEEPage.vue'

export default {
    components:{
        SecondPageEEPage
    },
    data(){
        return{
            currentpage: 'first'
        }
    },
    methods:{
        Start(){
            console.log('modal')
            this.currentpage = 'second'
        }
    }
}
</script>

<style scoped>
.feature-card {
    background-color: #C1E4C3;
    border-radius: 20px;
    padding: 20px;
    margin: 20px 0;
    height:400px;
    display: flex;
    justify-content: center;
    align-items: center;
}

.btn{
    background-color: #C1E4C3 !important; 
    margin-top: 3%;
    border-radius: 30px !important; 
}
</style>