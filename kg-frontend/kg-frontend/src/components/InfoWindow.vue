<template>
  <div id="infoWindow" class="infoWindow">
    <div class="info-image">
      <el-button-group class="button_left">
        <el-button type="text" icon="el-icon-arrow-left" @click="handlePrevImage"></el-button>
        <!-- 路段图片展示 -->
        <ImageViewer ref="imageComponent"></ImageViewer>
        <el-button type="text" icon="el-icon-arrow-right" @click="handleNextImage"></el-button>
      </el-button-group>
      <!-- 路段数据展示 -->
      <RoadData></RoadData>
      <el-button type="primary" icon="el-icon-edit" class="edit_btn" @click="edit">编辑</el-button>
    </div>
  </div>
</template>

<script>
import ImageViewer from './ImageViewer.vue';
import RoadData from './RoadData.vue';
export default {
  name: 'InfoWindow',
  // 传入 Map 的路由对象
  props: ['router'],
  components: {
    ImageViewer,
    RoadData,
  },
  data() {},
  methods: {
    handlePrevImage() {
      this.$refs.imageComponent.prevImage();
    },
    handleNextImage() {
      this.$refs.imageComponent.nextImage();
    },
    edit() {
      // 使用路由导航到编辑页面
      this.$props.router.push({
        name: 'Edit',
        params: {
          id: '1', // 传入路段 id
        },
      }).then(() => {
        console.log('路由跳转成功');
      }).catch(err => {
        console.error('路由跳转失败', err);
      });
    },
  },
  mounted() { },
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

  .edit_btn {
    display: flex;
    justify-content: center;
    margin: 5px 0 0 240px;
    padding: 8px 13px 8px 10px;
    border-radius: 15px;
  }
</style>