<template>
    <div class="massage">
        <div class="m_left">
          <ul>
            <li>起点：{{ origin }}</li>
            <li>终点：{{ finish }}</li>
            <li>距离：{{ speed }}km/h</li>
            <li>速度：{{ distance }}m</li>
          </ul>
        </div>
        <div class="m_right">
            <ul>
              <li>收集日期：{{ collection_date }}</li>
              <li>开始时间：{{ start_time }}</li>
              <li>结束时间：{{ end_time }}</li>
              <li>RMS：{{ rms }}</li>
            </ul>
        </div>
    </div>
</template>

<script>
export default {
  name: 'RoadData',
  data() {
    return {
      origin: "118.61, 31.68",
      finish: "118.61, 31.68",
      distance: "100",
      speed: "50",
      collection_date: "2024-06-26",
      start_time: "08:00",
      end_time: "09:00",
      rms: "1.2",
    };
  },
}
</script>

<style scoped>
 .massage {
    display: flex;
    justify-content: center;
  }
  
  .massage .m_left {
    display: flex;
    justify-content: left;
    bottom: 0;
    width: 100%;
  }
  .massage .m_right {
    display: flex;
    justify-content: left;
    bottom: 0;
    width: 100%;
  }

  .massage ul{
    padding-left: 10px;
  }
</style>