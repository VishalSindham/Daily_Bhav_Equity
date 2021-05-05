
<template>
<!-- <div class="row">
  <input type="text" name="search"/>
</div> -->
<div id="app">
  <div class="row">
    <!-- <input class="form-control" type="text" v-model="searchQuery" placeholder="Search" /> -->
  </div>
<div class="row">
<div class="col-lg-6" >
<table class="table table-striped">
  <thead>
    <tr>
        <th>SC_CODE</th>
        <th>SC_NAME</th>
        <th>SC_GROUP</th>
        <th>SC_TYPE</th>
        <th>OPEN</th>
        <th>HIGH</th>
        <th>LOW</th>
        <th>CLOSE</th>
        <th>LAST</th>
        <th>PREVCLOSE</th>
        <th>NO_TRADES</th>
        <th>NO_OF_SHRS</th>
        <th>NET_TURNOV</th>
        <!-- <th>TDCLOINDI</th>
        <th>Edit</th>
        <th>delete</th> -->
    </tr>
  </thead>
  <tbody>
    <tr v-for='bhav in bhavs' v-bind:key="bhav.SC_CODE">
      <td>{{bhav.SC_CODE}}</td>
          <td>{{bhav.SC_NAME}}</td>
          <td>{{bhav.SC_GROUP}}</td>
          <td>{{bhav.SC_TYPE}}</td>
          <td>{{bhav.OPEN}}</td>
          <td>{{bhav.HIGH}}</td>
          <td>{{bhav.LOW}}</td>
          <td>{{bhav.CLOSE}}</td>
          <td>{{bhav.LAST}}</td>
          <td>{{bhav.PREVCLOSE}}</td>
          <td>{{bhav.NO_TRADES}}</td>
          <td>{{bhav.NO_OF_SHRS}}</td>
          <td>{{bhav.NET_TURNOV}}</td>
          <td>{{bhav.TDCLOINDI}}</td>
          <!-- <td>
            <button @click="getOne(bhav)" class="btn bn-sm btn-sucess" ><i class="fa fa-pencil"></i></button>
          </td>
          <td>
            <button @click="deleteOne(bhav.SC_CODE)" class="btn bn-sm btn-sucess" ><i class="fa fa-trash"></i></button>
          </td> -->
    </tr>

  </tbody>
</table>
</div>

</div>
</div>
</template>

<script>

import axios  from 'axios'
export default {
  name: 'Container',
  props: {
    msg: String
  },
  data(){
  return{
    bhavs:null,
    SC_CODE :'',
    SC_NAME :'',
    SC_GROUP:'',
    SC_TYPE:'',
    OPEN:'',
    HIGH:'',
    LOW:'',
    CLOSE:'',
    LAST:'',
    PREVCLOSE:'',
    NO_TRADES:'',
    NO_OF_SHRS:'',
    NET_TURNOV:'',
    TDCLOINDI:''
    
  }
  },
  mounted(){
    this.getAll();
  },
  methods:{
    getAll(){
      // alert("hello")
      axios.get(`http://localhost:8000/api/bhavs`)
      .then((res)=>{
        this.bhavs = res.data
        // alert("hello")
      })
    }
  }
}
</script>

<style scoped>

</style>
