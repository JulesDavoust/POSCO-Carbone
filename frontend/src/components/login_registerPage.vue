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
                                        <p class="errorMessage hide ps-2 mb-1"></p>
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
                                            <input type="email" class="form-control" id="emailRegisterInput" v-model="registerEmail"
                                                placeholder="name@example.com">
                                            <label for="emailRegisterInput">Email address</label>
                                        </div>
                                        <div class="form-floating mb-3">
                                            <input type="password" class="form-control" id="passwordRegisterInput" v-model="registerPassword"
                                                placeholder="Password">
                                            <label for="passwordRegisterInput">Password</label>
                                        </div>
                                        <p class="errorMessage hide ps-2 mb-1"></p>
                                        <div class="text-end">
                                            <button id="registerButton" type="submit" class="btn btn-primary">Register</button>
                                        </div>
                                    </form>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
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
            registerUsername: '',
            registerPP: '',
            registerEmail: '',
            registerPassword: '',
        };
    },
    methods: {
        onSubmittingLogin() {
            AuthService.login({ email: loginEmail.value, password: loginPassword.value });
        },
        onSubmittingRegister() {
            AuthService.register({emailUser: registerEmail.value, passwordUser: registerPassword.value})
        }
    }
}
</script>

<style scoped>
/* Optional custom styles */
</style>
