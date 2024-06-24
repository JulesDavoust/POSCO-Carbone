import router from "../router";
import bootstrap from "bootstrap/dist/js/bootstrap.bundle";

const API_URL = "http://localhost:5000/";


class AuthService {
  async login(user) {
    if (!this.isLogged()){
      await fetch(API_URL + 'user/signin', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(user)
      })
        .then(response => response.json())
        .then(data => {
          console.log(data)
          if (data[0].accessToken) {
            localStorage.setItem("user", JSON.stringify(data[0]));

            let modalElement = document.getElementById('loginModal');
            let modal = bootstrap.Modal.getInstance(modalElement);
            modal.hide();

            router.push({ name: 'Accueil' });
          } else {
            console.log(data[0]['message'])
            return Promise.reject(new Error(data[0]['message'] || 'Login failed'));
          }
      });
    }
  }

  async register(user, isLoggedDisplay) {
    if (!this.isLogged()){
      console.log(user)
      console.log(isLoggedDisplay)
      await fetch(API_URL + 'user/register', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(user)
      })
        .then(response => response.json())
        .then(data => {
          console.log(data[0]['message'])
          if (data[0]['message'] === "Registered") {
            this.login({promo: user.promoUser, nom: user.prenomUser, prenom: user.prenomUser, numEtudiant: user.numUser, email: user.emailUser, password: user.passwordUser })
              .then(data => {
                print(data)
                isLoggedDisplay = this.isLogged()
                print(isLoggedDisplay)
              });
          } else {
            console.log(data[0]['message'])
            return Promise.reject(new Error(data[0]['message'] || 'Registration failed'));
          }
      });

    }
  }

  logout () {
    localStorage.removeItem("user");
  }

  authHeader() {
    let user = JSON.parse(localStorage.getItem('user'));
    
    if (user && user.accessToken) {
      return { 'x-access-token': user.accessToken };
    } else {
      return {};
    }
  }

  isLogged() {
    return JSON.parse(localStorage.getItem("user")) ? true : false;
  }
}

export default new AuthService();