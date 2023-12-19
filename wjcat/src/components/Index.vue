<!--
程序名：网站首页
功能：对网站进行介绍
-->
<template>
  <div class="main">
    <el-carousel height="500px">
      <el-carousel-item v-for="(item, index) in topImg" :key="index">
        <!--<div style="background-color: black;width: 100%;height: 100%;">-->
        <img :src="item.url" style="width: 100%;height: 100%;" />
        <div class="cover">
          {{ item.title }}<br />
          <span style="font-size: 35px">{{ item.subTitle }}</span>
        </div>
      </el-carousel-item>
    </el-carousel>
    <!--<el-divider></el-divider>-->

    <!-- <img src="/static/images/demo1.png" class="demoImg" /><br /> -->
    <!-- <img src="/static/images/demo2.png" class="demoImg" /><br />
    <img src="/static/images/demo3.png" class="demoImg" /><br /><br /> -->



  </div>
</template>
<script>
import CodeDiv from "@/components/CodeDiv";
export default {
  components: {
    CodeDiv
  },
  data() {
    return {
      topImg: [
        {
          title: "心理测评系统",
          url: "/static/images/4.jpg"
        }
      ]
    };
  }
};
</script>
<style scoped>
.main {
  position: relative;
  width: 100%;
  height: 100%;
}
.bottom {
  height: 150px !important;
  background-color: #2e3e4e;
  color: #9b9ea0;
  position: relative;
  padding: 20px;
}
.demoImg {
  width: 100%;
  height: 100%;
}
.cover {
  position: absolute;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.6);
  z-index: 100;
  left: 0;
  top: 0;
  color: white;
  font-size: 50px;
  line-height: 60px;
  padding-top: 180px;
}
.lj {
}
.b {
  font-weight: 700;
}
</style>
