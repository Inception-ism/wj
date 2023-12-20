<!--
程序名：分析页面
功能：填写完问卷跳转的页面
-->
<template>
  <div class="thankYou">
    <el-card shadow="never" style="font-size: 18px;line-height: 40px;padding: 10px;">
      <i class="el-icon-circle-check" style="color: green;font-size: 50px"></i>
      <p>
        结果分析
      </p>
      <div class="container mx-auto mt-10">
        <div class="bg-white shadow-md rounded my-6">
            <table class="text-left w-full border-collapse">
                <!-- Table Header -->
                <thead class="bg-blue-600 text-white">
                    <tr>
                        <th class="py-4 px-6 bg-grey-lightest font-bold uppercase text-sm text-grey-dark border-b border-grey-light">因子</th>
                        <th class="py-4 px-6 bg-grey-lightest font-bold uppercase text-sm text-grey-dark border-b border-grey-light">得分</th>
                        <th class="py-4 px-6 bg-grey-lightest font-bold uppercase text-sm text-grey-dark border-b border-grey-light">结果</th>
                    </tr>
                </thead>
                <tbody>
                    <!-- Dynamically repeated items based on data -->
                    <tr class="hover:bg-gray-100" v-for="(value, name, index) in analysis" :key="index">
                        <td class="py-4 px-6 border-b border-grey-light">{{translateName(name)}}</td>
                        <td class="py-4 px-6 border-b border-grey-light">{{value}}</td>
                        <td class="py-4 px-6 border-b border-grey-light">{{tsl(name, 3, value)[1]}}</td>
                    </tr>
                    <!-- ... other rows ... -->
                </tbody>
            </table>
        </div>
        <p class="text-right mt-4 text-gray-600">Updated at: 2023-12-20 13:28:11</p>
    </div>
      <el-link type="info" href="/index">返回主页</el-link>
    </el-card>
  </div>
</template>
<style scoped>
  .thankYou{
    padding: 40px;
  }
</style>
<style>
  .el-divider--horizontal{
    margin: 10px;
  }
</style>
<script>
import {answerOpera} from './api';
export default {
  name:'analysis',
  data(){
    return{
      wjId:this.$route.query.wjId,
      submitId:this.$route.query.submitId,
      answers:[],
      analysis:{
        "totalScore": 85,
        "totalAvgScore": 4.2,
        "positiveItem": 5,
        "Somatization": 3,
        "ObsessiveCompulsive": 4,
        "interpersonalSensibility": 5,
        "depression": 2,
        "anxiety": 3,
        "angerHostility": 4,
        "phobicAnxiety": 5,
        "paranoidIdeation": 3,
        "Psychoticism": 4
      }
    }
  },
  methods:{
    queryAnswer(){
      answerOpera({
          opera_type:'get_answer_with_option',
          wjId:this.$route.query.wjId,
          submitId:this.$route.query.submitId
        })
          .then(data=>{
            console.log(data,"nm");
            if(data.code==0){
              //提交成功
              this.submitLoading=false;
              this.submitText='提交';
              this.answers=data.detail;              
            }
            else{
              this.submitLoading=false;
              this.submitText='提交';
              this.$notify.error({
                title: '错误',
                message: data.msg,
              });
            }
          })
    },
    getAnalysis() {
      answerOpera({
          opera_type:'getSclAnswer',
          wjId:this.$route.query.wjId,
          submitId:this.$route.query.submitId
        })
          .then(data=>{
            console.log(data,"nms");
            if(data.code==0){
              this.analysis=data.detail;              
            }
            else{
              this.submitLoading=false;
              this.submitText='提交';
              this.$notify.error({
                title: '错误',
                message: data.msg,
              });
            }
          })
    },
    tsl(name, base, value) {
      let translatedName = this.translateName(name);
      let status = value < base ? "健康" : `处于${translatedName}状态`;
      return [`${translatedName}（${value < base ? "低于" : "高于"}基准值）`, status];
    },
    translateName(name) {
      switch (name) {
        case "ObsessiveCompulsive":
          return "强迫症倾向";
        case "Psychoticism":
          return "精神质";
        case "Somatization":
          return "躯体化";
        case "angerHostility":
          return "愤怒敌对";
        case "anxiety":
          return "焦虑";
        case "depression":
          return "抑郁";
        case "interpersonalSensibility":
          return "人际敏感";
        case "paranoidIdeation":
          return "偏执思维";
        case "phobicAnxiety":
          return "恐怖焦虑";
        case "positiveItem":
          return "积极项目";
        case "totalAvgScore":
          return "总平均分";
        case "totalScore":
          return "总分";
        default:
          return "错误";
      }
    },
  },
  watch:{
    "$route":{
      handler(){
        // this.queryAnswer();
        // this.getAnalysis()
      },
      immediate:true
    }
  },
}
</script>
