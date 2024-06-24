<template>
    <div class="modal fade" id="loginModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title" id="exampleModalLabel">Login/Register</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <div class="accordion" id="loginRegisterDisplay">
                        <div class="accordion-item">
                            <h2 class="accordion-header">
                                <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#loginCollapse"
                                    aria-expanded="true" aria-controls="loginCollapse">
                                    Login
                                </button>
                            </h2>
                            <div id="loginCollapse" class="accordion-collapse collapse show" data-bs-parent="#loginRegisterDisplay">
                                <div class="accordion-body">
                                    <form @submit.prevent="onSubmittingLogin">
                                        <div class="form-floating mb-3">
                                            <input type="email" class="form-control" id="emailLoginInput" v-model="loginEmail"
                                                placeholder="name@example.com">
                                            <label for="emailLoginInput">Email address</label>
                                        </div>
                                        <div class="form-floating mb-3">
                                            <input type="password" class="form-control" id="passwordLoginInput" v-model="loginPassword"
                                                placeholder="Password">
                                            <label for="passwordLoginInput">Password</label>
                                        </div>
                                        <p class="errorMessage ps-2 mb-1" v-if="loginError">{{ loginError }}</p>
                                        <div class="text-end">
                                            <button id="loginButton" type="submit" class="btn btn-primary">Login</button>
                                        </div>
                                    </form>
                                </div>
                            </div>
                        </div>
                        <div class="accordion-item">
                            <h2 class="accordion-header">
                                <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse"
                                    data-bs-target="#registerCollapse" aria-expanded="false" aria-controls="registerCollapse">
                                    Register
                                </button>
                            </h2>
                            <div id="registerCollapse" class="accordion-collapse collapse" data-bs-parent="#loginRegisterDisplay">
                                <div class="accordion-body">
                                    <form @submit.prevent="onSubmittingRegister">
                                        <div class="form-floating mb-3">
                                            <input type="text" class="form-control" id="PrenomLoginInput" v-model="registerPrenom"
                                                placeholder="Prenom">
                                            <label for="PrenomLoginInput">Prénom</label>
                                        </div>
                                        <div class="form-floating mb-3">
                                            <input type="text" class="form-control" id="NomLoginInput" v-model="registerNom"
                                                placeholder="Nom">
                                            <label for="NomLoginInput">Nom</label>
                                        </div>
                                        <div class="form-floating mb-3">
                                            <input type="text" class="form-control" id="NumEtudiantLoginInput" v-model="registerNumEtudiant"
                                                placeholder="NumEtudiant">
                                            <label for="NumEtudiantLoginInput">Numéro Etudiant</label>
                                        </div>
                                        <div class="form-floating mb-3">
                                            <select class="form-control" id="niveauRegisterSelect" v-model="registerPromo">
                                                <option value="" disabled selected>Select your level</option>
                                                <option value="L1">L1</option>
                                                <option value="L2">L2</option>
                                                <option value="L3">L3</option>
                                                <option value="M1">M1</option>
                                                <option value="M2">M2</option>
                                            </select>
                                            <label for="niveauRegisterSelect">Niveau</label>
                                        </div>
                                        <div class="form-floating mb-3">
                                            <input type="email" class="form-control" id="emailRegisterInput" v-model="registerEmail"
                                                placeholder="name@example.com">
                                            <label for="emailRegisterInput">Adresse email</label>
                                        </div>
                                        <div class="form-floating mb-3">
                                            <input type="password" class="form-control" id="passwordRegisterInput" v-model="registerPassword"
                                                placeholder="Password">
                                            <label for="passwordRegisterInput">Mot de passe</label>
                                        </div>
                                        <p class="errorMessage ps-2 mb-1" v-if="registerError">{{ registerError }}</p>
                                        <div class="text-end">
                                            <button id="registerButton" type="submit" class="btn btn-primary">Register</button>
                                        </div>
                                    </form>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <p class="errorMessage ps-2 mb-1" v-if="generalError">{{ generalError }}</p>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import AuthService from "../services/auth.service.js";
export default {
    name: 'login_registerPage',
    data() {
        return {
            loginEmail: '',
            loginPassword: '',
            registerPrenom: '',
            registerNom: '',
            registerNumEtudiant : '',
            registerEmail: '',
            registerPassword: '',
            registerPromo: '',
            loginError: '',
            registerError: '',
            generalError: ''
        };
    },
    methods: {
        onSubmittingLogin() {
            AuthService.login({ email: this.loginEmail, password: this.loginPassword })
                .catch(error => {
                    this.loginError = error.message || 'An error occurred during login.';
                });
        },
        onSubmittingRegister() {
            AuthService.register({promoUser: this.registerPromo, prenomUser: this.registerPrenom, nomUser: this.registerNom, numUser: this.registerNumEtudiant ,emailUser: this.registerEmail, passwordUser: this.registerPassword })
                .catch(error => {
                    this.registerError = error.message || 'An error occurred during registration.';
                });
        }
    }
}
</script>

<style scoped>
/* Optional custom styles */
</style>
