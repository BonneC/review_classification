<template>
  <div class="hello">
    <b-container>
      <b-row class="justify-content-md-center">
        <b-col>
          <h4>Single Review Analysis</h4>
        </b-col>
      </b-row>
      <b-row class="pt-5">
        <b-col>
          <h5 class="left subtitle">Insert review</h5>
        </b-col>
      </b-row>
      <b-row >
        <b-col>
          <input class="left" v-model="message" placeholder="Review...">
        </b-col>
      </b-row>
      <b-row class="pt-2">
        <b-col>
          <button type="button" class="btn btn-primary button" @click="analyzeReview">Analyse</button>
          <!--           <button class="btn-light button">Review</button>-->
        </b-col>
      </b-row>
      <b-row>
        <b-col>
          <div class="border-div">
            <hr/>
          </div>
        </b-col>
      </b-row>
      <span v-if="show_analysis">
        <h5 class="left subtitle">Analysis:</h5>
        <b-row class="pt-4">
        <b-col>
          <span class="sentiment-pos">
            <font-awesome-icon icon="smile"/>
          </span>
          <h5>{{ positive }}%</h5>
        </b-col>
          <b-col>
            <div class="sentiment-neg">
            <font-awesome-icon icon="angry"/>
          </div>
            <h5>{{ negative }}%</h5>
          </b-col>
      </b-row>
        <h5 v-if="positive>negative" class="align-content-start subtitle pt-5">Review is {{ positive}} % positive.</h5>
        <h5 v-else class="align-content-start subtitle pt-5">Review is {{ negative }}% negative.</h5>
        <h5 class="left subtitle pt-5">Emotions:</h5>
        <h5 class="left subtitle pt-5">(might be innacurate)</h5>
        <b-row class="pieplace">
          <b-col md="12"  >
          <pie-chart class="custompie" :chartData="data" :options="options"></pie-chart>
        </b-col>
        </b-row>
      </span>

    </b-container>

    <!--    <p>Message is: {{ message }}</p>-->

    <!--    <vue-chart></vue-chart>-->
  </div>
</template>

<script>
// import Chart from 'chart.js'
// import VueChart from "@/components/VueChart";

import info3 from "@/charts_info/dummy-pie-data";
import axios from "axios";
import emotion_colors from "@/charts_info/emotion_colors";

export default {
  name: "MainComp",
  components: {
    // VueChart
  },
  data() {
    return {
      dummy_graph: [],
      message: '',
      show_analysis: false,
      data:JSON.parse(JSON.stringify(info3['data'])),
      options: info3['options'],
      positive: 0,
      negative: 0
    }
  },
  methods: {
    analyzeReview: async function () {
      console.log('MSG')
      console.log()
      if(this.message.length > 0){
        const {data} = await axios.get(
            "http://localhost:8080/analysis/",
            {params: {
              review: this.message
              }}
        )
        let tmp = JSON.parse(JSON.stringify(info3['data']))
        tmp['datasets'][0]['data'] = data['data']
        tmp['labels'] = data['labels']
        tmp['datasets'][0]['backgroundColor'] = emotion_colors.get_emotion_colors(data['labels'])

        this.data = JSON.parse(JSON.stringify(tmp))
        this.positive = data['positive']
        this.negative = data['negative']
        this.show_analysis = true
        // return data;
      }

    },
  }
}
</script>

<style scoped lang="scss">
.hello {

}

.left {
  text-align: left;
  width: 100%;
}
.pieplace{
  height: 200px;
}
.custompie{
  height:100%
}

.button {
  text-transform: uppercase;
  letter-spacing: 0.15em;
  font-weight: bold;
  width: 100%;
  border-radius: 0%;
  background-color: rgb(217,30,30);
  border-color: rgb(217,30,30);

  &:hover {
    background-color: rgb(179, 5, 5);
    border-color: rgb(179, 5, 5);
  }

  &:active {
    border-style: outset;
    box-shadow: none !important;
    outline: none !important;
  }

  &:focus {
    outline: none !important;
    box-shadow: none !important;
    background-color: rgb(217,30,30);
    border-color: rgb(217,30,30);
  }

}

.sentiment-pos {
  font-size: 50px;
  color: #7add3b;
}

.sentiment-neg {
  font-size: 50px;
  color: #e94a4a;
}

.border-div {

}
</style>