<template>
  <div class="home container-fluid">

    <div class="toolbar d-flex bg sticky-top hstack gap-3">

      <!-- Button to delete photos -->
      <button @click="deleteSelected" class="btn btn-secondary p-2 ms-auto" title="Delete selected">
        <i class="bi bi-trash"></i>
      </button>

      <div class="vr"></div>


      <!-- Send Message Button -->
      <button @click="sendMessage" class="btn btn-primary p-2" :disabled="loading">
        <i class="bi bi-image"></i>
        ClickMe</button>
    </div>

    <h1>Welcome to the Vue 3 Docker App</h1>
    <p>This is the home page of the application. <router-link to="/about">Learn more about us</router-link></p>


    <p v-if="isMounted">This text is shown after the component is mounted.</p>
    <p v-else>This text is shown before the component is mounted.</p>

    <div class="hstack gap-2">
      <div class="card">
        <div class="card-body">
          <h5 class="card-title">Bootstrap Card</h5>
          <p class="card-text">This is an example of a Bootstrap card component used in a Vue 3 application.</p>
          <button @click="navigateToCard" class="btn btn-primary">Learn More</button>
        </div>
      </div>
      <div class="card">
        <div class="card-body">
          <h5 class="card-title">Bootstrap Card</h5>
          <p class="card-text">This is an example of a Bootstrap card component used in a Vue 3 application.</p>
          <div class="card-footer">
            <button @click="navigateToCard" class="btn btn-primary">Learn More</button>
          </div>
        </div>
      </div>
    </div>

    <table class="table table-striped table-bordered table-hover mt-3">
      <thead>
        <tr>
          <th scope="col">#</th>
          <th scope="col">First</th>
          <th scope="col">Last</th>
          <th scope="col">Handle</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th scope="row">1</th>
          <td>Mark</td>
          <td>Otto</td>
          <td>@mdo</td>
        </tr>
        <tr>
          <th scope="row">2</th>
          <td>Jacob</td>
          <td>Thornton</td>
          <td>@fat</td>
        </tr>
        <tr>
          <th scope="row">3</th>
          <td>John</td>
          <td>Doe</td>
          <td>@social</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script lang="ts" setup>
import { ref, onMounted } from 'vue';
const isMounted = ref(false);
onMounted(() => {
  isMounted.value = true;
});

function sendMessage() {
  alert('Do Smart!');
  console.log('Do sku da Smart MAND!');
}

function navigateToCard() {
  window.open('https://getbootstrap.com/docs/5.3/components/card/');

}

</script>

<style scoped>
.home {}
</style>