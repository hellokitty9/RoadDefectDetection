<template>
  <div>
    <div class="image-container">
      <div class="inner-image">
        <el-image src="https://cube.elemecdn.com/6/94/4d3ea53c084bad6931a56d5158a48jpeg.jpeg"></el-image>
      </div>
    </div>
    <div class="edit_data">
      <div class="top">
        <div class="input-item">
          <span class="label">起点：</span>
          <el-input v-model="formData.origin"></el-input>
        </div>
        <div class="input-item">
          <span class="label">距离：</span>
          <el-input v-model="formData.distance"></el-input>
        </div>
        <div class="input-item">
          <span class="label">收集日期：</span>
          <el-date-picker
            v-model="formData.collection_date"
            type="date"
            placeholder="选择日期">
          </el-date-picker>
        </div>
        <div class="input-item">
          <span class="label">开始时间：</span>
            <el-time-picker
              v-model="formData.start_time"
              :picker-options="{
                selectableRange: ''
              }"
              placeholder="任意时间点">
            </el-time-picker>
        </div>
      </div>
      <div class="bottom">
        <div class="input-item">
          <span class="label">终点：</span>
          <el-input v-model="formData.finish"></el-input>
        </div>
        <div class="input-item">
          <span class="label">速度：</span>
          <el-input v-model="formData.speed"></el-input>
        </div>
        <div class="input-item">
          <span class="label">RMS：</span>
          <el-input v-model="formData.rms"></el-input>
        </div>
        <div class="input-item">
          <span class="label">结束时间：</span>
          <el-time-picker
            v-model="formData.end_time"
            :picker-options="{
              selectableRange: ''
            }"
            placeholder="任意时间点">
          </el-time-picker>
        </div>
      </div>
      <div class="save">
        <el-button type="primary" @click="handleSave">保存</el-button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Edit",
  components: {

  },
  data() {
    return {
      formData: {
        images: [
          'assets/img/image_14-59-27-649.jpg',
          'assets/img/image_14-59-29-821.jpg',
          'assets/img/image_14-59-32-485.jpg',
        ],
        origin: "118.61, 31.68",
        finish: "118.61, 31.68",
        distance: "100",
        speed: "50",
        collection_date: new Date(),
        start_time: new Date(2016, 9, 10, 18, 40),
        end_time: new Date(2016, 9, 10, 18, 40),
        rms: "1.2",
      },
    };
  },
  computed: {

  },
  methods: {
    handleSave() {
      console.log('表单数据:', this.formData);
      // 这里可以添加保存逻辑
    }
  },
  mounted() {
    // 如果需要，可以在这里初始化日期时间数据
    const now = new Date();
    this.formData.collection_date = now;
    this.formData.start_time = now;
    this.formData.end_time = now;
  },
};
</script>

<style scoped>
 .image-container {
    width: 100%;
    height: 350px;
    border: 1px solid #ccc;
  }

  .inner-image {
    display: flex;
    height: 100px;
  }

  .edit_data {
    width: 100%;
    height: 200px;
    margin-top: 10px;
    border: 1px solid #ccc;
  }

  .edit_data .top,
  .edit_data .bottom {
    display: flex;
    align-items: center;
    margin: 20px 0 0 10px;
    gap: 5px;
  }

  .input-item {
  display: flex;
  align-items: center;
  flex: 1;
}

  /* 字体格宽度 */
  .label {
    width: 100px;
    text-align: center;
    padding-right: 10px;
  }

  .edit_data :deep(.el-input) {
    width: 150px;
  }

  .save {
    display: flex;
    justify-content: center;
    margin-top: 25px;
  }
</style>