<template>
  <canvas id="dummy-chart" width="400" height="400"></canvas>
</template>

<script>
import Chart from 'chart.js'
// import dummyChartData from "@/charts_info/dummy-chart-data";

export default {
  name: "DummyChart",
  data(){
    return{
      chartData: [],
      chart: null
    }
  },
  mounted: async function() {
    this.chartData = await this.getListData()
    this.buildChart(this.chartData)
    // const ctx = document.getElementById('dummy-chart');
    // this.chart = new Chart(ctx, this.chartData);
  },
  methods:{
    buildChart(data){
      const ctx = document.getElementById("dummy-chart")
      // eslint-disable-next-line no-unused-vars
      let myChart = new Chart(ctx,data)
    },
    getListData: async function() {
      // const { data } = await axios.get(
      //     "https://my-json-server.typicode.com/isogunro/jsondb/chartData"
      // );
      //
      // return data;
    }
  }
}
</script>

<style scoped>

</style>