

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import PlacesList from './PlacesList.vue'

import axios from 'axios'

const places = ref([])
const route = useRoute()
const router = useRouter()
const ticket = ref(null) 

const fetchPlaces = async () => {
    try {
        const response = await axios.get('https://parking-app-v9k6.onrender.com/')
        places.value = response.data
    } catch (error) {
        console.error('Erreur lors du chargement des places:', error)
    }
}



onMounted(() => {
    const placeId = route.params.id
    if (placeId) {
        const currentDate = new Date()
        ticket.value = {
            placeId: placeId,
            date: currentDate.toLocaleDateString(),
            time: currentDate.toLocaleTimeString()
        }
    } else {
        console.error("Aucun ID de place trouvé dans les paramètres de la route.")
    }
})

const exitParking = () => {
    PlaceNotAsOccupied(route.params.id)
    router.push('/') 
}

const PlaceNotAsOccupied = async (placeId) => {
    try {
        await axios.patch(`https://parking-app-v9k6.onrender.com/${placeId }/`, {
            is_occupied: false
        })
        fetchPlaces()
    } catch (error) {
        console.error("Erreur lors de la mise à jour de la place:", error)
    }
}
onMounted(fetchPlaces)
</script>

<template>
    <meta http-equiv="refresh" content="30">
    <div class="container">
        <section class="ticket-section">
            <div class="ticket">
                <div v-if="ticket" class="ticket-content">
                    <h1 class="ticket-title">Ticket d'achat</h1>
                    <div class="ticket-info">
                        <p class="ticket-detail">Place n°{{ ticket.placeId }}</p>
                        <p class="ticket-detail">Date : {{ ticket.date }}</p>
                        <p class="ticket-detail">Heure : {{ ticket.time }}</p>
                    </div>
                    <button @click="exitParking" class="btn-exit">Sortir du parking</button>
                </div>
                <div v-else class="loading">
                    <p>Chargement du ticket...</p>
                </div>
            </div>
        </section>

        <section class="places-section">
            <div>
                <h1 class="text-xl font-bold mb-4">Places de parking disponibles</h1>
                <ul v-if="places.length">
                    <li v-for="place in places" :key="place.id" class="parking-place" :class="place.is_occupied ? 'occupied' : 'available'">
                        Place n°{{ place.id }} - {{ place.is_occupied ? 'Occupée' : 'Disponible' }} <span>{{ place.id == $route.params.id ? 'par Vous' : '' }}</span>
                    </li>
                </ul>
                <p v-else>Aucune place disponible.</p>
            </div>
        </section>
    </div>
    
</template> 

<style scoped>
.container {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    gap: 2rem;
    padding: 2rem;
    max-width: 1200px;
    margin: auto;
}

.ticket-section, .places-section {
    flex: 1;
}

.ticket {
    padding: 30px;
    background-color: #fff;
    border-radius: 10px;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
    text-align: center;
}

.ticket-title {
    font-size: 2rem;
    font-weight: bold;
    color: #333;
    margin-bottom: 20px;
}

.ticket-info {
    margin: 20px 0;
}

.ticket-detail {
    font-size: 1.2rem;
    color: #555;
    margin: 10px 0;
}

.btn-exit {
    background-color: #e74c3c;
    color: #fff;
    padding: 12px 25px;
    font-size: 1.1rem;
    font-weight: bold;
    border: none;
    border-radius: 8px;
    cursor: pointer;
    transition: background-color 0.3s;
    margin-top: 20px;
}

.btn-exit:hover {
    background-color: #c0392b;
}

.loading {
    font-size: 1.5rem;
    color: #3498db;
    font-weight: bold;
}

h1 {
    color: #065fb8;
    font-size: 1.8rem;
    margin-bottom: 15px;
}

ul {
    list-style: none;
    padding: 0;
}

.parking-place {
    padding: 15px;
    border-radius: 8px;
    font-size: 1.1rem;
    font-weight: bold;
    transition: transform 0.2s, background 0.3s, box-shadow 0.3s;
    box-shadow: 2px 4px 8px rgba(0, 0, 0, 0.1);
    margin-bottom: 10px;
    cursor: pointer;
}

.parking-place:hover {
    transform: scale(1.05);
    box-shadow: 4px 6px 12px rgba(0, 0, 0, 0.15);
}

.available {
    background: #d4edda;
    color: #155724;
    border-left: 5px solid #28a745;
}

.occupied {
    background: #f8d7da;
    color: #721c24;
    border-left: 5px solid #dc3545;
}

span {
    color: yellowgreen;
}
</style>
