<!--
程序名：分析页面
功能：填写完问卷跳转的页面
-->
<template>
  <div class="thankYou">
    <el-card shadow="never" style="font-size: 18px;line-height: 40px;padding: 10px;">
      <i class="el-icon-circle-check" style="color: green;font-size: 50px"></i>
      <p v-for="(item, index) in answers" v-bind="index">
        {{ item.questionId }}: {{ item.answerTitle }}
      </p>
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
      answers:[]
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
    }
  },
  watch:{
    "$route":{
      handler(){
        this.queryAnswer();
      },
      immediate:true
    }
  },
}
</script>
