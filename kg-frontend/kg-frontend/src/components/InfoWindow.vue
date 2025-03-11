<template>
  <div id="infoWindow" class="infoWindow">
    <div class="info-image">
      <el-button-group class="button_left">
        <el-button type="text" icon="el-icon-arrow-left" @click="handlePrevImage"></el-button>
        <ImageViewer ref="imageComponent"></ImageViewer>
        <!-- <img
            id="imgDemo"
            :src="images[currentIndex]"
          /> -->
        <el-button type="text" icon="el-icon-arrow-right" @click="handleNextImage"></el-button>
      </el-button-group>
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
      <el-button type="primary" icon="el-icon-edit" class="edit_btn" @click="edit">编辑</el-button>
    </div>
  </div>
</template>

<script>
import ImageViewer from './Image.vue';
export default {
  name: 'InfoWindow',
  components: {
    ImageViewer,
  },
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
  methods: {
    handlePrevImage() {
      this.$refs.imageComponent.prevImage();
    },
    handleNextImage() {
      this.$refs.imageComponent.nextImage();
    },
    edit() {
      console.log('edit');
    },
  },
}
</script>

<style scoped>
.button_left .el-button {
  z-index: 1;
  position: relative;
}
  .infoWindow {
    display: flex;
    justify-content: center;
    width: 320px;
    height: 100%;
    /* padding: 10px; */
  }

  .button_left {
    display: flex;
    justify-content: center;
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
    padding-left: 10px;
  }

  .edit_btn {
    display: flex;
    justify-content: center;
    margin: 5px 0 0 240px;
    padding: 8px 13px 8px 10px;
    border-radius: 15px;
  }
</style>