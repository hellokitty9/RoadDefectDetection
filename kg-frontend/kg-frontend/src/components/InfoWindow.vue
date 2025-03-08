<template>
  <div id="infoWindow" class="infoWindow">
    <div class="info-image">
      <img
      id="imgDemo"
      src="../assets/img/image_14-59-27-649.jpg"
    />
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
      <div class="div_btn">
        <button class="btn" @click="edit">
          <span>编辑</span>
        </button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'InfoWindow',
  component: {},

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
  .infoWindow {
    display: flex;
    justify-content: center;
    width: 320px;
    height: 100%;
    /* padding: 10px; */
  }

  .info-image img {
    display: block;
    width: 300px;
    margin: 0 auto;
    float: middle;
  }

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
    padding-left: 2px;
  }

  .div_btn {
    display: flex;
    justify-content: right;
    width: auto;
    padding: 0 15px 0 0;
  }

  .btn {
    display: flex;
    justify-content: center;
    width: auto;
    padding: 0 5px;
    margin-top: 10px;
    border: 1px solid #878787;
  }
</style>