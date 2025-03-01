<template>
  <div id="map"></div>
</template>

<script>
export default {
  name: 'Map',

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
        let totalDistance = 0;
        let lastPoint = data.points[0];

        for (let i = 0; i < data.points.length; i++) {
          let currentPoint = data.points[i];
          let distance = map.getDistance(lastPoint, currentPoint);
          totalDistance += distance;
          
          if (totalDistance >= MAX_DISTANCE) {
            // Message box
            var opts = {
              width : 200,     // 信息窗口宽度
              height: 100,     // 信息窗口高度
              title : "路线信息" , // 信息窗口标题
              message:"路线信息"
            }
            var infoWindow = new BMapGL.InfoWindow("地址：北京市东城区王府井大街88号乐天银泰百货八层", opts);  // 创建信息窗口对象
            let midPoint = new BMapGL.Point(
              (lastPoint.lng + currentPoint.lng) / 2,
              (lastPoint.lat + currentPoint.lat) / 2,
            );

            // 在折线的端点添加标记点
            let pointMarker = new BMapGL.Marker(lastPoint);

            // Add point and line to map
            map.addOverlay(pointMarker); // Add point to map
            let polyLine = new BMapGL.Polyline([lastPoint, currentPoint], { // Add line to map
              strokeColor: i % 2 === 0 ? "red" : "blue",
              strokeWeight: 3,
              strokeOpacity: 0.5,
            });

            // 为折线添加鼠标经过事件
            polyLine.addEventListener("mouseover", function(e){
              map.openInfoWindow(infoWindow, midPoint); // 在折线的中点显示信息窗口
            });

            map.addOverlay(polyLine);
            
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