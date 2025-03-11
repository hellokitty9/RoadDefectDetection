<template>
  <div>
    <div id="map"></div>
  </div>
</template>

<script>
import innerInfoWindow from '@/components/InfoWindow.vue';
import Vue from 'vue';
export default {
  name: 'Map',

  components: {},

  data() {
    return {
      map: null,
      infoWindow: '路线信息',
    };
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
    this.map = new BMapGL.Map("map");
    var originPoint = new BMapGL.Point(118.61754983, 31.67399917); // 创建点坐标
    this.map.centerAndZoom(originPoint, 16);  // 初始化地图，设置中心点坐标和地图级别
    this.map.enableScrollWheelZoom(true);     //开启鼠标滚轮缩放
    this.map.addControl(new BMapGL.NavigationControl()); // 添加地图控件
    this.map.addControl(new BMapGL.ScaleControl());

    // 创建信息窗口实例
    this.infoWindow = this.createInfoWindow();

    const MAX_DISTANCE = 100; // 两点之间的最大距离

    //坐标转换完后的回调函数
    const translateCallback = (data) => {
      if(data.status === 0) {
        let totalDistance = 0;
        let lastPoint = data.points[0];

        for (let i = 0; i < data.points.length; i++) {
          let currentPoint = data.points[i];
          let distance = this.map.getDistance(lastPoint, currentPoint);
          totalDistance += distance;
          
          if (totalDistance >= MAX_DISTANCE) {
            // 计算中点
            let midPoint = new BMapGL.Point(
              (lastPoint.lng + currentPoint.lng) / 2,
              (lastPoint.lat + currentPoint.lat) / 2
            );

            // 添加标记点
            let pointMarker = new BMapGL.Marker(lastPoint);
            this.map.addOverlay(pointMarker);

            // 创建并添加折线
            let polyLine = new BMapGL.Polyline([lastPoint, currentPoint], {
              strokeColor: i % 2 === 0 ? "red" : "blue",
              strokeWeight: 3,
              strokeOpacity: 0.5,
            });

            // 为折线添加鼠标经过事件
            polyLine.addEventListener("mouseover", (e) => {
              this.map.openInfoWindow(this.infoWindow, midPoint);
            });

            this.map.addOverlay(polyLine);
            
            totalDistance = 0;
            lastPoint = currentPoint;
          }
        }
      }
    }

    setTimeout(() => {
      var convertor = new BMapGL.Convertor();
      var COORDINATES_WGS84 = 1; // WGS84 坐标
      var COORDINATES_BD09 = 5; // BD09 坐标
      convertor.translate(WGSPoints, COORDINATES_WGS84, COORDINATES_BD09, translateCallback);
    }, 1000);
  },

  methods: {
    createInfoWindow() {
      // 创建一个包装器div
      const wrapper = document.createElement('div');
      
      // 创建新的Vue实例来挂载InfoWindow组件
      const infoWindowComponent = new Vue({
        render: h => h(innerInfoWindow)
      }).$mount();
      
      // 将组件的DOM添加到包装器中
      wrapper.appendChild(infoWindowComponent.$el);

      const opts = {
        width: 340,
        height: 380,
        title: "路线信息",
        enableMessage: true,
        enableAutoPan: true,
        message: "",
        enableDragging: true,
      }

      // 使用包装器的innerHTML作为内容创建信息窗口
      const infoWindow = new BMapGL.InfoWindow(wrapper, opts);
      
      // 保存Vue实例的引用以便后续使用
      infoWindow.vueInstance = infoWindowComponent;
      
      return infoWindow;
    }
}
}
</script>

<style>
#map {
  width: 100%;
  height: 650px;
}
/* 修改信息窗口标题样式 */
.BMap_bubble_title {
  padding: 5px 0 0 10px;
  font-size: large;
  font-weight: bold;
  color: #333;
  text-align: left;
  /* border-bottom: 1px solid #eee; */
}

.BMap_bubble_content {
  left: 3px;
}

</style>