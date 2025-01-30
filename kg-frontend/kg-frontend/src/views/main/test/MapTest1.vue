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
    // 创建地图实例
    var map = new BMapGL.Map("map");
    // 创建点坐标
    var point = new BMapGL.Point(118.61821200, 31.66542117);
    // 初始化地图，设置中心点坐标和地图级别
    map.centerAndZoom(point, 15);
    //开启鼠标滚轮缩放
    map.enableScrollWheelZoom(true);
    // 添加地图控件
    map.addControl(new BMapGL.NavigationControl());
    map.addControl(new BMapGL.ScaleControl());

    // 添加更多坐标点
    var pathPoints = [
      // 添加更多坐标点
      new BMapGL.Point(118.60054983, 31.67399917),
      new BMapGL.Point(118.60643000, 31.66963150),
      new BMapGL.Point(118.61821200, 31.66542117),
      new BMapGL.Point(118.63232200, 31.66569183),
      new BMapGL.Point(118.65514950, 31.66284550),
    ];

    // 创建标点
    pathPoints.forEach((point, index) => {
      var marker = new BMapGL.Marker(point);
      map.addOverlay(marker);
    });

    var polyline = new BMapGL.Polyline(pathPoints, {
      strokeColor: "red",
      strokeWeight: 3,
      strokeOpacity: 0.4
    });
    map.addOverlay(polyline);
    //调用 splitPath 函数并获取分割后的路径段
    var segments = splitPath(pathPoints, 2500); // 分割段的长度，可以根据需要调整

    // 遍历 segments数组 将分割后的路径段添加到地图上
    segments.forEach((segment, index) => {
      var polyline = new BMapGL.Polyline(segment, {
        strokeColor: index % 2 === 0 ? "red" : "blue",
        strokeWeight: 3,
        strokeOpacity: 0.5
      });
      map.addOverlay(polyline);

      // 绑定鼠标事件
        this.bindPolylineEvents(map, polyline, index);

      // 在接点处添加点标记
        if (index > 0) {
          var connectionPoint = segment[0]; // 接点是当前段的第一个点
          var marker = new BMapGL.Marker(connectionPoint);
          map.addOverlay(marker);
        }
    });
      
      function splitPath(pathPoints, segmentLength) {
        var segments = []; // 汇总路径段
        var remainingLength = 0; // 当前子路径的剩余长度
        var currentSegment = [pathPoints[0]]; // 当前正在构建的子路径
        var totalLength = 0; // 总长度
  
        // 计算总长度
        for (var i = 1; i < pathPoints.length; i++) {
          totalLength += map.getDistance(pathPoints[i - 1], pathPoints[i]);
        }
        console.log(`Total length: ${totalLength} meters`);
  
        // 按分段长度计算分段点
        for (var i = 1; i < pathPoints.length; i++) {
          var prevPoint = pathPoints[i - 1];
          var currentPoint = pathPoints[i];
          var distance = map.getDistance(prevPoint, currentPoint);
          console.log(`Distance from ${i - 1} to ${i}: ${distance} meters`);
  
          // 如果当前累积长度加上当前线段长度小于分段长度，则继续累积
          if (remainingLength + distance < segmentLength) {
            currentSegment.push(currentPoint);
            remainingLength += distance;
          } else {
            // 计算分段点的位置
            var remainingSegmentLength = segmentLength - remainingLength;
            var ratio = remainingSegmentLength / distance;
            var midPoint = new BMapGL.Point(
              prevPoint.lng + (currentPoint.lng - prevPoint.lng) * ratio,
              prevPoint.lat + (currentPoint.lat - prevPoint.lat) * ratio
            );
  
            // 将分段点添加到当前子路径
            currentSegment.push(midPoint);
            segments.push(currentSegment);
  
            console.log(midPoint);
  
            // 在分割点上添加标记
            var marker = new BMapGL.Marker(midPoint);
            map.addOverlay(marker);
  
            // 开始新的子路径
            currentSegment = [midPoint];
            remainingLength = 0;
  
            // 重新检查当前点
            i--;
          }
        }
  
        // 添加最后一个子路径
        if (currentSegment.length > 1) {
          segments.push(currentSegment);
        }
        return segments;
      }
    },
    methods: {
      bindPolylineEvents(map, polyline, index) {
        var infoWindow = new BMapGL.InfoWindow("", {
          offset: new BMapGL.Size(10, -10), // 信息框偏移量
        });
  
        // 鼠标悬停事件
        polyline.addEventListener("mouseover", (e) => {
          // 设置信息框内容
          infoWindow.setContent(`分段 ${index + 1}`);
          // 显示信息框
          map.openInfoWindow(infoWindow, e.point);
        });
  
        // 鼠标移出事件
        polyline.addEventListener("mouseout", () => {
          // 隐藏信息框
          map.closeInfoWindow(infoWindow);
        });
      }
    }
  }



</script>

<style scoped>
#map {
  width: 100%;
  height: 700px;
}
</style>