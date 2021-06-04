<template>
  <div class="charts">
    <h4>All reviews analysis</h4>
    <h5 class="pt-3">
      <h5 class="fake-routers" @click="changeCharts(0)">All</h5>
      <h5 class="liner">|</h5>
      <h5 class="fake-routers" @click="changeCharts(1)">Positive</h5>
      <h5 class="liner">|</h5>
      <h5 class="fake-routers" @click="changeCharts(2)">Negative</h5>
      <!--      <h5 class="nav-link test-button" @click="changeCharts">All</h5>-->
    </h5>
    <b-container class="pt-2">
      <b-row class="justify-content-center">
        <b-col>
          <h4 class="subtitle">Most commonly used nouns</h4>
        </b-col>
        <b-col>
          <h4 class="subtitle">Most commonly used phrases</h4>
        </b-col>
      </b-row>
      <b-row class="justify-content-md-center chart">
        <b-col md="4" class="chart">
          <vue-chart :chartData="nouns" :options="options"></vue-chart>
        </b-col>
        <b-col md="4" offset-md="2" class="chart">
          <vue-chart :chartData="phrases" :options="options"></vue-chart>
        </b-col>
      </b-row>
      <b-row class="justify-content-start">
        <b-col>
          <h4 class="subtitle left pt-5 pb-5">Emotions:</h4>
        </b-col>
      </b-row>
      <b-row class="pieplace">
        <b-col md="8"  >
          <pie-chart class="custompie" :chartData="pie" :options="poptions"></pie-chart>
        </b-col>
      </b-row>
    </b-container>

  </div>
</template>

<script>
import info from "@/charts_info/dummy-chart-data";
import info2 from "@/charts_info/dummy-chart-data2";
import info3 from "@/charts_info/dummy-pie-data";
import emotion_colors from "@/charts_info/emotion_colors";
// import Chart from "chart.js";
import axios from 'axios'

export default {
  name: "ChartContainer",
  data() {
    return {
      nouns: JSON.parse(JSON.stringify(info['data'])),
      phrases: JSON.parse(JSON.stringify(info2['data'])),
      pie: JSON.parse(JSON.stringify(info3['data'])),
      poptions: info3['options'],
      options: info['options'],
      id: 0
    }
  },
  mounted: async function () {
    let nounsData = await this.getNounsData()
    let phrasesData = await this.getNounsData()
    let emotionsData = await this.getEmotionsData()
    // console.log(nounsData)
    // console.log(this.nouns['datasets'][0]['data'])
    this.setNounsData(nounsData)
    this.setPhrasesData(phrasesData)
    this.setEmotionsData(emotionsData)
    // this.buildChart(this.chartData)
    // const ctx = document.getElementById('dummy-chart');
    // this.chart = new Chart(ctx, this.chartData);
  },
  watch: {
    // eslint-disable-next-line no-unused-vars
    async id(oldVal, newVal) {
      console.log("changed")
      let nounsData = await this.getNounsData()
      let phrasesData = await this.getPhrasesData()
      let emotionsData = await this.getEmotionsData()
      this.setNounsData(nounsData)
      this.setPhrasesData(phrasesData)
      this.setEmotionsData(emotionsData)
    }
  },
  methods: {
    getNounsData: async function () {
      const {data} = await axios.get(
          "http://localhost:8080/nouns/" + this.id
      )
      return data;
    },
    getPhrasesData: async function () {
      const {data} = await axios.get(
          "http://localhost:8080/phrases/" + this.id
      )
      return data;
    },
    getEmotionsData: async function(){
      const {data} = await axios.get(
          "http://localhost:8080/emotions/" + this.id
      )
      data["colors"] = emotion_colors.get_emotion_colors(data['labels'])
      console.log('changed ems')
      console.log(data)
      return data
    },
    setEmotionsData(emotionsData){
      let tmp = JSON.parse(JSON.stringify(info3['data']))
      tmp['datasets'][0]['data'] = emotionsData['data']
      tmp['labels'] = emotionsData['labels']
      tmp['datasets'][0]['backgroundColor'] = emotionsData['colors']
      console.log('SET EM')
      console.log(tmp)
      this.pie = JSON.parse(JSON.stringify(tmp))
    },
    setNounsData(nounsData){
      let tmp = JSON.parse(JSON.stringify(info['data']))
      tmp['datasets'][0]['data'] = nounsData['data']
      tmp['labels'] = nounsData['labels']
      console.log('SETNOUNS')
      console.log(tmp)
      this.nouns = JSON.parse(JSON.stringify(tmp))
    },
    setPhrasesData(phrasesData){
      let tmp = JSON.parse(JSON.stringify(info2['data']))
      tmp['datasets'][0]['data'] = phrasesData['data']
      tmp['labels'] = phrasesData['labels']
      this.phrases = JSON.parse(JSON.stringify(tmp))
    },
    changeCharts(id) {
      this.id = id
        console.log(id)
    }
  }
}
</script>

<style scoped lang="scss">
.charts {
  text-align: center;
}

.chart {
  /*padding-left:40px;*/
  /*padding-right:40px;*/
}
.pieplace{
  height: 200px;
}
.custompie{
  height:80%
}
.left {
  text-align: left;
  width: 100%;
}


.test-button {
  padding-top: 1em;
  color: #000000;
  transition: 2s background-color;

  &:after {
    content: '';
    bottom: 0;
    width: 0;
    height: 1px;
    background-color: rgba(255, 255, 255, 0.5);
    /*left: 50%;*/
    -webkit-transform: translateX(-50%);
    transform: translateX(-50%);
    position: absolute;
    z-index: 5;
    -webkit-transition-duration: 500ms;
    transition-duration: 500ms;


  }

  .test-button:hover::after, .nav-link:focus::after {
    width: 70px;
    background-color: #000000;
  }
}

.fake-routers {
  color: #000000;
  text-transform: uppercase;
  text-decoration: none;
  letter-spacing: 0.15em;

  display: inline-block;
  padding: 10px 20px;
  position: relative;
  &:after{
    background: none repeat scroll 0 0 transparent;
    bottom: 0;
    content: "";
    display: block;
    height: 2px;
    left: 50%;
    position: absolute;
    background: #000000;
    transition: width 0.3s ease 0s, left 0.3s ease 0s;
    width: 0;
  }
  &:hover{
    cursor: pointer;
  }
  &:hover:after{
    width: 100%;
    left: 0;
  }
}

.liner{
  display: inline-block;
}

</style>