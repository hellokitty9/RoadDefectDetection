<template>
  <div id="map"></div>
</template>

<script>
export default {
  name: 'MapTest1',

  components: {},

  data() {
    return {};
  },

  mounted() {

    // 生成坐标点
    var WGSPoints = [];
    const baseX = 118.60054983;
    const baseY = 31.67399917;
    const increment = 0.00100000; // 每次增加的量
    const pointCount = 10; // 需要生成的点数量

    for (let i = 0; i < pointCount; i++) {
      WGSPoints.push(new BMapGL.Point(baseX + increment * i, baseY - increment * i));
    }

    // 创建地图实例
    var map = new BMapGL.Map("map");
    var originPoint = new BMapGL.Point(118.61821200, 31.66542117); // 创建点坐标
    map.centerAndZoom(originPoint, 15);  // 初始化地图，设置中心点坐标和地图级别
    map.enableScrollWheelZoom(true);      //开启鼠标滚轮缩放
    map.addControl(new BMapGL.NavigationControl()); // 添加地图控件
    map.addControl(new BMapGL.ScaleControl());

    const MAX_DISTANCE = 100; // 两点之间的最大距离

    //坐标转换完后的回调函数
    var translateCallback = function (data){
      if(data.status === 0) {
        // Add markers to map
        let totalDistance = MAX_DISTANCE;
        let lastPoint = data.points[0];

        for (let i = 0; i < data.points.length; i++) {
          let currentPoint = data.points[i];
          let distance = map.getDistance(lastPoint, currentPoint);
          totalDistance += distance;
          
          if (totalDistance >= MAX_DISTANCE) {
            map.addOverlay(new BMapGL.Marker(currentPoint));
            map.addOverlay(new BMapGL.Polyline([lastPoint, currentPoint], {
              strokeColor: i % 2 === 0 ? "red" : "blue",
              strokeWeight: 3,
              strokeOpacity: 0.5
            }));
            totalDistance = 0;
            lastPoint = currentPoint;
          }
        }
      }
    }
    setTimeout(function(){
        var convertor = new BMapGL.Convertor();
        var COORDINATES_WGS84 = 1; // WGS84 坐标
        var COORDINATES_BD09 = 5; // BD09 坐标
        convertor.translate(WGSPoints, COORDINATES_WGS84, COORDINATES_BD09, translateCallback)
    }, 1000);
    
    },
  methods: {
  }
}

</script>

<style scoped>
#map {
  width: 100%;
  height: 700px;
}
</style>