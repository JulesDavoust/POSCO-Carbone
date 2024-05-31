<template>
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
                    <a class="nav-link active" aria-current="page" href="#">Accueil</a>
                    </li>
                    <li class="nav-item">
                    <a class="nav-link" href="#">Espace Personnel</a>
                    </li>
                    <li class="nav-item">
                    <a class="nav-link" href="#">Espace EFREI</a>
                    </li>
                    <li class="nav-item">
                    <a class="nav-link" href="#">Nos Conseils</a>
                    </li>
                    <li class="nav-item">
                    <a class="nav-link" href="#">FAQ</a>
                    </li>
                </ul>
                <ul class="navbar-nav ms-auto mb-2 mb-lg-0 align-items-center">
                    <li class="nav-item">
                        <a class="nav-link d-flex align-items-center" href="#"><font-awesome-icon icon="fa-solid fa-user" size="lg" class="me-2"/> Mon profil</a>
                    </li>
                </ul>
            </div>
        </div>
    </nav>
</template>

<script>
export default {

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