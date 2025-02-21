<template>
  <div>
    <header id="app">
      <h1 class="text-3xl font-bold text-center my-6">Gestion de Parking</h1>
    </header>
    <section>
      <router-view/>
    </section>
  </div>


</template>

<script setup>

</script>

<style scoped>
#app {
  font-family: 'Arial', sans-serif;


  justify-content: center;
  align-items: center;
}

header {
  padding: 20px;
  text-align: center;
}

h1 {
  margin: 0;
}


</style>
