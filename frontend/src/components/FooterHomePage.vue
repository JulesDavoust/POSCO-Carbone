<template>
    <div class="foot">
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
                <button class="btn connect-button mt-3">Contactez-nous</button>
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
    name: 'QuoteSection',
  };
  </script>
  
  <style scoped>

@media(max-width: 767px){
    .foot{
        margin-top: 180vh;
    }
}

@media(min-width: 767px){
    .foot{
        margin-top: 90vh;
    }
}

  .quote-section {
    padding: 50px 0;
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
  }
  
  .language-options .btn-language {
    background-color: #003366;
    color: white;
    border: none;
    margin: 0 5px;
  }
  </style>
  