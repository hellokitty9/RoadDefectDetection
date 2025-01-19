<template>
  <div id="map"></div>
</template>

<script>
export default {
  name: 'Map',
  mounted() {
    // 创建地图实例
    var map = new BMapGL.Map("map");
    // 创建点坐标
    var point = new BMapGL.Point(118.62611650, 31.66587267);
    // 初始化地图，设置中心点坐标和地图级别
    map.centerAndZoom(point, 15);
    //开启鼠标滚轮缩放
    map.enableScrollWheelZoom(true);
    // 添加地图控件
    map.addControl(new BMapGL.NavigationControl());
    map.addControl(new BMapGL.ScaleControl());
    map.addControl(new BMapGL.OverviewMapControl());
  }
}
</script>

<style scoped>
#map {
  width: 100%;
  height: 650px;
}
</style>