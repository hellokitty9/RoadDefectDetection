<template>
  <div id="app">
    <!-- <router-view></router-view> -->
     <MapTest1></MapTest1>
  </div>
</template>

<script>
// import Main from "views/main/Main.vue";
// import login from "components/Login.vue";
// import { setThis } from "api/index";
import MapTest1 from './views/main/test/MapTest1.vue'

export default {
  name: "App",
  components: {
    //Main,
    //login,
    MapTest1
  },
  mounted() {
    const user = localStorage.getItem("user");
    this.$store.commit("login", user);
  },
  created() {
    setThis(this);
  },
};
</script>

<style>
@import "assets/css/base.css";
</style>
