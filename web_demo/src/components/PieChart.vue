<script>
import {  Pie, mixins } from 'vue-chartjs'
// import info from "@/charts_info/dummy-chart-data";
const {reactiveProp} = mixins

export default {
  extends: Pie,
  props: ['options'],
  mixins: [reactiveProp],
  name: "PieChart",
  data(){
    return{
      // chartData: info['data'],
      // options: info['options']
    }
  },
  mounted () {
    // this.setVars()
    this.renderChart(this.chartData, this.options)
  },
  methods:{
    // setVars()
  }
}
</script>


<style scoped>

</style>