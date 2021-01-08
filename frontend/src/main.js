import Vue from 'vue'
import VueRouter from 'vue-router'
import VueResource from 'vue-resource'
import Buefy from 'buefy'
import 'buefy/dist/buefy.css'

import App from './App.vue'

Vue.use(VueRouter)
Vue.use(VueResource)
Vue.use(Buefy)

Vue.config.productionTip = false
Vue.http.options.root = process.env.VUE_APP_API_ROOT

new Vue({
  render: h => h(App),
}).$mount('#app')
