<template>
  <div id="app">
    <b-navbar :fixed-top="true" :centered="true" type="is-dark">
      <template slot="brand">
        <b-navbar-item tag="router-link" :to="{ path: '/' }">GPIO SERVER</b-navbar-item>
      </template>
      <template slot="start">
        <b-navbar-item tag="router-link" :to="{ path: '/gpio' }">GPIO</b-navbar-item>
        <b-navbar-item tag="router-link" :to="{ path: '/i2c' }">I2C</b-navbar-item>
      </template>
    </b-navbar>

    <router-view></router-view>
  </div>
</template>

<script>
  import VueRouter from 'vue-router'

  import GPIOComponent from './components/GPIOComponent'
  import I2CComponent from './components/I2CComponent'

  const router = new VueRouter({
    mode: 'history',
    routes: [
      { path: '/', redirect: '/gpio' },
      { path: '/gpio', component: GPIOComponent },
      { path: '/i2c', component: I2CComponent },
    ],
  })

  export default {
    name: 'App',
    router,
  }
</script>
