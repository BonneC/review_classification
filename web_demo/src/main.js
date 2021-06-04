import BootstrapVue from "bootstrap-vue";
import Vue from 'vue'
import App from './App.vue'
import MainComp from "@/components/MainComp";
import DummyChart from "@/components/DummyChart";
import VueChart from "@/components/VueChart";
import ChartContainer from "@/components/ChartContainer";
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import './assets/css/style.scss'
// import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { library } from '@fortawesome/fontawesome-svg-core'
import { faSmile, faAngry } from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import PieChart from "@/components/PieChart";

library.add(faSmile)
library.add(faAngry)

Vue.use(BootstrapVue)
Vue.config.productionTip = false

Vue.component('font-awesome-icon', FontAwesomeIcon)
Vue.component('main-menu', MainComp)
Vue.component('chart-container', ChartContainer)
Vue.component('dummy-graph', DummyChart)
Vue.component('vue-chart', VueChart)
Vue.component('pie-chart', PieChart)

new Vue({
  render: h => h(App),
}).$mount('#app')
