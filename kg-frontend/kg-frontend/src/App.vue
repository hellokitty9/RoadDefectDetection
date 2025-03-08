<template>
  <div id="app">
    <router-view></router-view>
     <Map></Map>
  </div>
</template>

<script>
import Main from "views/main/Main.vue";
import login from "components/Login.vue";
import { setThis } from "api/index";
import Map from "views/main/map/Map.vue";

export default {
  name: "App",
  components: {
    Main,
    login,
    Map,
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
