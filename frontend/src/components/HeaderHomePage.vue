<template>
    <div class="video-container">
        <video autoplay muted loop class="w-100 h-100">
            <source src="../assets/video.mp4" type="video/mp4"/>
        </video>
        <div class="overlay-text">
            <h1>POSCO : Votre Partenaire pour un Avenir Durable</h1>
            <p>Un outil de mesure innovant conçu par les étudiants pour les étudiants.</p>
            <button type="button" class="btn">En savoir plus</button>
        </div>
    </div>
</template>

<script>
export default {
}
</script>

<style scoped>
.video-container{
    position: relative;
    width: 100%;
    height: 80vh;
    overflow: hidden;
}

video{
    height: 100%;
    width: 100%;
    object-fit: cover;
}

.overlay-text {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    color: white;
    text-align: center;
    width: 60vw;
}

.overlay-text h1 {
    margin: 0;
    font-size: 2rem;
}

.overlay-text p {
    margin: 0;
    font-size: 1rem;
}

.btn{
    background-color: #C1E4C3 !important; 
    margin-top: 3%;
    border-radius: 30px !important; 
}
</style>