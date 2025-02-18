<script setup lang="ts">
import { ref, onMounted } from 'vue';
import api from '@/api';

interface Place {
    id: number;
    numero: number;
    disponible: boolean;
}

const places = ref<Place[]>([]);

const fetchPlaces = async () => {
    try {
        const response = await api.get('/places/');
        places.value = response.data;
    } catch (error) {
        console.error('Erreur lors de la récupération des places:', error);
    }
};

onMounted(fetchPlaces);
</script>

<template>
    <div>
        <h1 class="text-xl font-bold mb-4">Places de parking disponibles</h1>
        <ul v-if="places.length">
            <li v-for="place in places" :key="place.id" class="p-2 mb-2 border rounded"
                :class="place.disponible ? 'bg-green-200' : 'bg-red-200'">
                Place n°{{ place.numero }} - {{ place.disponible ? 'Disponible' : 'Occupée' }}
            </li>
        </ul>
        <p v-else>Aucune place disponible.</p>
    </div>
</template>

<style scoped>
/* Ajoute du style si nécessaire */
</style>
