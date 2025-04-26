<template>
  <div id="app" class="container">
    <nav class="navbar navbar-expand border mb-2">
      <div class="container-fluid">
        <a class="navbar-brand" href="#">Vue3 App</a>
        <div class="collapse navbar-collapse">
          <ul class="navbar-nav me-auto mb-2 mb-lg-0">
            <li class="nav-item">
              <router-link to="/" class="nav-link">Main</router-link>
            </li>
            <li class="nav-item">
              <router-link to="/about" class="nav-link">About</router-link>
            </li>
          </ul>

        </div>
      </div>
    </nav>
    <router-view></router-view>
  </div>
</template>

<script lang="ts" setup>

</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
