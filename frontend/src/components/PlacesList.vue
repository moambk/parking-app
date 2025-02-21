<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const places = ref([])

const fetchPlaces = async () => {
    try {
        const response = await axios.get('http://127.0.0.1:8000/places/')
        places.value = response.data
    } catch (error) {
        console.error('Erreur lors du chargement des places:', error)
    }
}

const handlePlaceClick = (place) => {
    if (!place.is_occupied) {
        const userConfirmed = window.confirm(`Voulez-vous acheter un ticket pour la place n°${place.id} ?`)
        if (userConfirmed) {
            // Logique pour l'achat du ticket, par exemple un appel à une API
            console.log(`Ticket acheté pour la place n°${place.id}`)
        }
    }
}

onMounted(fetchPlaces)
</script>

<template>
    <div>
        <h1 class="text-xl font-bold mb-4">Places de parking disponibles</h1>
        <ul v-if="places.length">
            <li v-for="place in places" :key="place.id" class="p-2 mb-2 border rounded"
                :class="place.is_occupied ? 'bg-red-200' : 'bg-green-200'" @click="handlePlaceClick(place)">
                Place n°{{ place.id }} - {{ place.is_occupied ? 'Occupée' : 'Disponible' }}
            </li>
        </ul>
        <p v-else>Aucune place disponible.</p>
    </div>
</template>

<style scoped>
/* Conteneur principal */
div {
    max-width: 600px;
    margin: 20px auto;
    text-align: center;
    font-family: 'Arial', sans-serif;
}

/* Titre */
h1 {
    color: #2c3e50;
    font-size: 1.8rem;
    margin-bottom: 15px;
}

/* Liste des places */
ul {
    list-style: none;
    padding: 0;
}

/* Élément de la liste */
li {
    padding: 15px;
    border-radius: 8px;
    font-size: 1.1rem;
    font-weight: bold;
    transition: transform 0.2s, background 0.3s, box-shadow 0.3s;
    box-shadow: 2px 4px 8px rgba(0, 0, 0, 0.1);
}

/* Effet au survol */
li:hover {
    transform: scale(1.05);
    box-shadow: 4px 6px 12px rgba(0, 0, 0, 0.15);
}

/* Styles pour les places disponibles */
.bg-green-200 {
    background: #d4edda;
    color: #155724;
    border-left: 5px solid #28a745;
}

/* Styles pour les places occupées */
.bg-red-200 {
    background: #f8d7da;
    color: #721c24;
    border-left: 5px solid #dc3545;
}

/* Message quand aucune place n'est disponible */
p {
    font-size: 1.2rem;
    color: #e74c3c;
    font-weight: bold;
}
</style>
