<template>
  <div class="home container-fluid">

    <div class="toolbar d-flex bg sticky-top hstack gap-3">

      <!-- Button to delete photos -->
      <button @click="deleteSelected" class="btn btn-secondary p-2 ms-auto" title="Delete selected">
        <i class="bi bi-trash"></i>
      </button>

      <div class="vr"></div>

    </div>

    <h1>Welcome to the Vue 3 Docker App</h1>

    <div class="card">
      <div class="card-body">
        <h5 class="card-title">Data</h5>
        <p class="card-text">This is data from database.</p>
        <div class="card-footer">
          <div v-if="apiResult !== null" class="mt-2">
            <h5>API Result:</h5>
            <pre>{{ apiResult }}</pre>
          </div>
          <div v-if="apiTableData.length" class="mt-3">
            <h5>API Table:</h5>
            <table class="table table-striped table-bordered table-hover">
              <tbody>
                <tr v-for="(row, idx) in apiTableData" :key="idx">
                  <td>{{ typeof row === 'object' ? JSON.stringify(row) : row }}</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>

    <!-- Send Message Button -->
    <input type="text" placeholder="Enter your message" class="form-control w-25 m-2 p-2" v-model="userMessage" />

    <button @click="sendMessage" class="btn btn-primary p-2" :disabled="loading">
      <i class="bi bi-image"></i>
      Insert Message
    </button>

    <!-- Backend API Test Call -->
    <div class="mt-4">
      <button class="btn btn-success" @click="fetchApi">Get Message</button>

    </div>
  </div>
</template>

<script lang="ts" setup>
import { ref, onMounted } from 'vue';
const isMounted = ref(false);
const userMessage = ref();
onMounted(() => {
  isMounted.value = true;
});

const apiResult = ref<null | string>(null);
const apiTableData = ref<any[]>([]);
const loading = ref(false);

async function fetchApi() {
  try {
    const response = await fetch('http://localhost:5000/getdata');
    if (!response.ok) throw new Error('Network response was not ok');
    const data = await response.json();
    apiTableData.value = Array.isArray(data) ? data : [data];
    apiResult.value = JSON.stringify(data, null, 2);
  } catch (error) {
    apiResult.value = 'Error: ' + error;
    apiTableData.value = [];
  }
}

async function sendMessage() {
  alert('Do Smart!');
  console.log('Do sku da Smart MAND!');
  loading.value = true;
  try {
    const payload = { message: userMessage.value, timestamp: Date.now() };
    const response = await fetch('http://localhost:5000/newthing', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    });
    const result = await response.json();
    apiResult.value = JSON.stringify(result, null, 2);
  } catch (error) {
    apiResult.value = 'Error: ' + error;
  } finally {
    loading.value = false;
  }
}

function navigateToCard() {
  window.open('https://getbootstrap.com/docs/5.3/components/card/');
}

</script>

<style scoped>
.home {}
</style>