<template>
  <div id="app">
    <h1>BeSquared</h1>
    <div id="nav">
     <router-link :to="{ name: 'home' }">Dashboard</router-link> |
     <router-link :to="{ name: 'add_entry' }">Add Entry</router-link>
    </div>
    <router-view/>
  </div>
</template>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
