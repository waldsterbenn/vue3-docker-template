<template>
  <div class="about container">
    <h1>About This Application</h1>
    <p>This is a simple Vue 3 application using Bootstrap for UI elements.</p>
    <p>It demonstrates routing with a few simple components.</p>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'About'
});
</script>

<style scoped>
.about {}
</style>