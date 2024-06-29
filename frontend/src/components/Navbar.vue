<template>
    <div>
        <nav class="navbar navbar-expand-lg">
            <div class="container-fluid">
                <a class="navbar-brand" href="#">
                    <img src="../assets/logo.png" alt="Bootstrap" width="108" height="73">
                </a>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarText" aria-controls="navbarText" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse" id="navbarText">
                    <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                        <li class="nav-item">
                            <div class="EE" @click="switchPage(2)"><a class="nav-link">Espace EFREI</a></div>
                        </li>
                        <li class="nav-item">
                            <div class="NC" @click="switchPage(3)"><a class="nav-link">Nos Conseils</a></div>
                        </li>
                        <li class="nav-item">
                            <div class="FAQ" @click="switchPage(4)"><a class="nav-link">FAQ</a></div>
                        </li>
                    </ul>
                    <ul class="navbar-nav ms-auto mb-2 mb-lg-0 align-items-center">
                        <li class="nav-item dropdown" @click="toggleDropdown">
                            <a class="nav-link d-flex align-items-center dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                                <font-awesome-icon icon="fa-solid fa-user" size="lg" class="me-2"/> Mon profil
                            </a>
                            <ul class="dropdown-menu" :class="{ show: drop }" aria-labelledby="navbarDropdown">
                                <li><a class="dropdown-item" href="#">Paramètres</a></li>
                                <li><a class="dropdown-item" href="#">Déconnexion</a></li>
                            </ul>
                        </li>
                    </ul>
                </div>
            </div>
        </nav>
        <login_registerPage v-if="modal"></login_registerPage>
    </div>
</template>

<script>
import AuthService from "../services/auth.service.js";
import login_registerPage from "./login_registerPage.vue";
import bootstrap from "bootstrap/dist/js/bootstrap.bundle";

export default {
components:{
    login_registerPage
},
data(){
    return{
        modal: true,
        dev: true,
        drop: false
    }
},
methods:{
    switchPage(page){
        console.log(this.modal)
        // 
        if (true) {
            switch (page) {
                case 0:
                    console.log("EspaceEfrei")
                    this.$router.push({'name':'EspaceEfrei'})
                    break;
                case 1:
                    console.log("Conseils")
                    this.$router.push({'name':'Conseils'})
                    break;
                case 2:
                    console.log("FAQ")
                    this.$router.push({'name':'FAQ'})
                    break;
                default:
                    break;
            }
        }
        else{
            console.log('modal')
            this.$nextTick(() => {
                var modal = new bootstrap.Modal(document.getElementById('loginModal'));
                modal.show();
            });
        }
        
    },


    toggleDropdown(){
        if(AuthService.isLogged()){
            this.drop = !this.drop;
        }else{
            this.$nextTick(() => {
                var modal = new bootstrap.Modal(document.getElementById('loginModal'));
                modal.show();
            });
        }
        
    }

}
}
</script>

<style scoped>
.navbar{
    background-color: #C1E4C3;
}

.container-fluid{
    margin-left: 5%;
    margin-right: 5%;
}

.profil-all{
    width: 120px;
    /* border: solid 2px; */
}

.profil{
    margin-right: 4%;
}
</style>