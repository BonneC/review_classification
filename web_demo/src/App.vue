<template>
  <div id="app" class="container-fluid">
<!--    <h4>Review Classification Analysis</h4>-->
    <b-container fluid class="pt-3">
      <b-row>
        <b-col cols="4" class="main">
          <main-comp></main-comp>
        </b-col>
        <b-col cols="8">
          <chart-container></chart-container>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
import MainComp from './components/MainComp.vue'


export default {
  name: 'App',
  components: {
    MainComp
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  /*width:100%;*/
  margin-top: 30px;
}
.main{
  border-right: 2px solid #cdcdcd;
}
</style>
