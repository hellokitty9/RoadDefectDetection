<template>
    <div class="image-container">
        <img id="imgDemo" :src="getImageUrl" alt="示例图片">
    </div>
</template>

<script>
export default {
    name: 'ImageViewer',
    data() {
        return {
            currentIndex: 0,
            images: [
                'assets/img/image_14-59-27-649.jpg',
                'assets/img/image_14-59-29-821.jpg',
                'assets/img/image_14-59-32-485.jpg',
            ]
        }
    },
    computed: {
        getImageUrl() {
            return require(`@/${this.images[this.currentIndex]}`);
        },
        currentImage() {
        return this.images[this.currentIndex];
        },
    },
    methods: {
        prevImage() {
            if (this.currentIndex > 0) {
                this.currentIndex--
            } else {
                this.currentIndex = this.images.length - 1
            }
        },
        nextImage() {
            if (this.currentIndex < this.images.length - 1) {
                this.currentIndex++
            } else {
                this.currentIndex = 0
            }
        }
    }
}
</script>

<style scoped>
.image-container {
    display: block;
    /* width: 300px; */
    margin: 0 auto;
    float: middle;
}

.image-container img {
    display: block;
    width: 300px;
    margin: 0 auto;
    float: middle;
}
</style>