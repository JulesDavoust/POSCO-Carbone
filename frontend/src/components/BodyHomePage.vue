<template>
  <div class="body">
    <div class="container text-center mt-5">
        <div class="row row-cols-1 row-cols-sm-2 row-cols-md-4">
            <div class="col-md-6"><h4 class="main-title"><b>Pourquoi utiliser POSCO ?</b></h4></div>
        </div>
        <div class="row mt-4">
            <div class="col-md-4 col-css1">
                <div class="feature-card  col-css">
                    <img src="../assets/empreinte-carbone.png" alt="Icon 1" class="feature-icon img-fluid larger-icon">
                    <h5 class="feature-title">Évaluation Précise de l’Empreinte Carbone</h5>
                    <p class="feature-text">Suivez votre bilan carbone en temps réel tout au long de votre parcours académique. Prenez le contrôle de votre impact environnemental en ajustant vos habitudes de vie et de voyage pour minimiser votre empreinte carbone.</p>
                </div>
            </div>
            <div class="col-md-4 col-css2">
                <div class="feature-card  col-css">
                    <img src="../assets/sensibilisation-ecologique.png" alt="Icon 2" class="feature-icon img-fluid larger-icon">
                    <h5 class="feature-title">Sensibilisation et Engagement Étudiant</h5>
                    <p class="feature-text">POSCO est une plateforme éducative qui sensibilise les futurs ingénieurs aux impacts environnementaux de leurs choix quotidiens et les encourage à devenir des acteurs du changement vers des pratiques durables.</p>
                </div>
            </div>
            <div class="col-md-4">
                <div class="feature-card col-css3 col-css">
                    <img src="../assets/innovation.png" alt="Icon 3" class="feature-icon img-fluid larger-icon">
                    <h5 class="feature-title">Innovation Ouverte et Partagée</h5>
                    <p class="feature-text">Fièrement développé en open source en collaboration avec l’équipe de l’INSA de Lyon, POSCO permet à tout établissement d’adopter et d’adapter cette technologie. Participez à la rendre encore plus efficace et adaptée aux besoins de tous.</p>
                </div>
            </div>
        </div>
    </div>
    <div class="transition-page">
      <div class="container-fluid">
        <div class="row align-items-center">
          <div class="col-md-6 text-section">
            <h2>Contribuer à une Transition Écologique</h2>
            <p>En utilisant POSCO, vous faites partie d'une communauté engagée pour la transition écologique. Les établissements d'enseignement supérieur s'unissent pour créer des campus bas carbone et développer des stratégies durables en collaboration avec leurs étudiants.</p>
          </div>
          <div class="col-md-6 logo-section">
            <img src="../assets/imageschools.png" alt="Logos des établissements" class="img-fluid imageschools">
          </div>
        </div>
      </div>
    </div>
    <div class="quote-section">
      <div class="container text-center">
          <div class="row justify-content-center">
          <div class="col-md-10">
              <div class="quote-box">
              <div class="row align-items-center">
                  <div class="col-md-2 d-none d-md-block">
                  <img src="../assets/annonce.png" alt="Megaphone Icon" class="img-fluid megaphone-icon">
                  </div>
                  <div class="col-md-10">
                  <p class="quote-text">
                      “Intégrez POSCO dans votre quotidien et devenez un acteur clé dans la lutte contre le changement climatique. Ensemble, façonnons un avenir durable pour nous et pour les générations futures.“
                  </p>
                  </div>
              </div>
              </div>
              <button class="btn connect-button mt-3">Connectez-nous</button>
          </div>
          </div>
      </div>
      <div class="footer mt-5">
          <div class="container">
          <div class="row justify-content-between align-items-center">
              <div class="col-md-4 text-center text-md-left">
              <p class="mb-1">Recevoir nos actualités :</p>
              <div class="social-icons">
                  <a href="#"><img src="../assets/Facebook_logo.png" alt="Facebook" class="social-icon"></a>
                  <a href="#"><img src="../assets/Instagram_icon.png" alt="Instagram" class="social-icon"></a>
                  <a href="#"><img src="../assets/x_logo.png" alt="Twitter" class="social-icon"></a>
                  <a href="#"><img src="../assets/LinkedIn_logo.png" alt="LinkedIn" class="social-icon"></a>
              </div>
              </div>
              <div class="col-md-4 text-center">
              <img src="../assets/logo.png" alt="Posco Logo" class="footer-logo">
              </div>
              <div class="col-md-4 text-center text-md-right">
              <p class="mb-1">Choix de la langue :</p>
              <div class="language-options">
                  <button class="btn btn-sm btn-language">FR</button>
                  <button class="btn btn-sm btn-language">EN</button>
                  <button class="btn btn-sm btn-language">ES</button>
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
    name: 'FeatureSection',
  };
  </script>
  
<style scoped>

.body{
  height: 145vh;
}
  .container {
    max-width: 1200px;
  }
  
  .main-title {
    background-color: #C1E4C3;
    padding: 10px 20px;
    border-radius: 20px;
    display: inline-block;
  }
  
  .feature-card {
    background-color: #C1E4C3;
    border-radius: 20px;
    padding: 20px;
    margin: 20px 0;
  }
  
  .feature-icon {
    width: 50px;
    height: 50px;
    margin-bottom: 10px;
  }
  
  .feature-title {
    font-size: 1.2rem;
    margin-top: 10px;
  }
  
  .feature-text {
    font-size: 0.9rem;
  }

@media(min-width: 768px) {
    .col-css1{
        margin-top: 2%;
    }

    .col-css2{
        margin-top: 5%;
    }

    .transition-page {
      height: 60vh;
      display: flex;
      align-items: center;
    }
}

@media(max-width: 767px) {
  .transition-page {
    height: 100vh;
    display: flex;
    align-items: center;
  }
}

.larger-icon {
  width: 30%;
  height: auto;
}

.text-section {
  padding: 20px;
}

.logo-section {
  background-color: #C1E4C3;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100%;
  padding: 20px;
}

.text-section h2 {
  font-weight: bold;
}

.text-section p {
  margin-top: 20px;
  line-height: 1.6;
}

.logo-section img {
  max-width: 80%;
  height: auto;
}



@media(max-width:767px){
  .quote-section {
    padding-top: 10vh;
  }
}
  
  .quote-box {
    background-color: #C1E4C3;
    border-radius: 10px;
    padding: 20px;
    position: relative;
  }
  
  .megaphone-icon {
    max-width: 100px;
  }
  
  .quote-text {
    font-size: 1.2rem;
    font-weight: bold;
  }
  
  .connect-button {
    background-color: #C1E4C3;
    border: none;
    border-radius: 20px;
    padding: 10px 20px;
    font-size: 1rem;
  }
  
  .footer {
    background-color: #6c757d;
    padding: 20px 0;
  }
  
  .footer p {
    color: white;
    margin-bottom: 5px;
  }
  
  .social-icons .social-icon {
    max-width: 30px;
    margin: 0 5px;
  }
  
  .footer-logo {
    max-width: 100px;
    margin: 10px;
    border-radius: 30px;
  }
  
  .language-options .btn-language {
    background-color: #003366;
    color: white;
    border: none;
    margin: 0 5px;
  }

</style>
  