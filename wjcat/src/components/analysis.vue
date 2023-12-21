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
                    <tr class="hover:bg-gray-100" v-for="(value, name, index) in analysis" :key="index">
                        <td class="py-4 px-6 border-b border-grey-light">{{translateName(name)}}</td>
                        <td class="py-4 px-6 border-b border-grey-light">{{value.toFixed(1)}}</td>
                        <td class="py-4 px-6 border-b border-grey-light">{{tsl(name, 3, value)[1]}}</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>

      <div class="container mx-auto px-6 py-12">
      <!-- Article -->
      <article class="max-w-8xl mx-auto p-8 bg-white rounded-lg shadow-md">
        <!-- Title -->
        <h3 class="text-lg font-semibold mt-4 mb-2">[心理健康状况]</h3>
        <!-- Subtitle -->
        <h2 class="text-xl text-gray-600">得分: {{  this.analysis.totalScore }}</h2>
        <!-- Content -->
        <h3 class="text-lg mt-4 mb-2 text-left">[说明]</h3>
        <p class="mt-4 text-gray-700">
          {{ illustrate(1) }}
        </p>
        <!-- Additional paragraphs -->
        <h3 class="text-lg mt-4 mb-2 text-left">[指导建议]</h3>
        <p class="mt-4 text-gray-700">
            {{ additionalContent(1) }}
        </p>
      </article>

        <article class="max-w-8xl mx-auto p-8 bg-white rounded-lg shadow-md">
        <!-- Title -->
        <h3 class="text-lg font-semibold mt-4 mb-2">[躯体化]</h3>
        <!-- Subtitle -->
        <h2 class="text-xl text-gray-600">得分: {{ this.analysis.Somatization.toFixed(2) }}</h2>
        <!-- Content -->
        <h3 class="text-lg mt-4 mb-2 text-left">[说明]</h3>
        <p class="mt-4 text-gray-700">
          {{ illustrate(2) }}
        </p>
        <!-- Additional paragraphs -->
        <h3 class="text-lg mt-4 mb-2 text-left">[指导建议]</h3>
        <p class="mt-4 text-gray-700">
            {{ additionalContent(2) }}
        </p>
      </article>

        <article class="max-w-8xl mx-auto p-8 bg-white rounded-lg shadow-md">
        <!-- Title -->
        <h3 class="text-lg font-semibold mt-4 mb-2">[强迫症状]</h3>
        <!-- Subtitle -->
        <h2 class="text-xl text-gray-600">得分: {{ this.analysis.ObsessiveCompulsive.toFixed(2) }}</h2>
        <!-- Content -->
        <h3 class="text-lg mt-4 mb-2 text-left">[说明]</h3>
        <p class="mt-4 text-gray-700">
          {{ illustrate(3) }}
        </p>
        <!-- Additional paragraphs -->
        <h3 class="text-lg mt-4 mb-2 text-left">[指导建议]</h3>
        <p class="mt-4 text-gray-700">
            {{ additionalContent(3) }}
        </p>
      </article>

      <article class="max-w-8xl mx-auto p-8 bg-white rounded-lg shadow-md">
        <!-- Title -->
        <h3 class="text-lg font-semibold mt-4 mb-2">[人际关系敏感]</h3>
        <!-- Subtitle -->
        <h2 class="text-xl text-gray-600">得分: {{ this.analysis.interpersonalSensibility.toFixed(2) }}</h2>
        <!-- Content -->
        <h3 class="text-lg mt-4 mb-2 text-left">[说明]</h3>
        <p class="mt-4 text-gray-700">
          {{ illustrate(4) }}
        </p>
        <!-- Additional paragraphs -->
        <h3 class="text-lg mt-4 mb-2 text-left">[指导建议]</h3>
        <p class="mt-4 text-gray-700">
            {{ additionalContent(4) }}
        </p>
      </article>  

      <article class="max-w-8xl mx-auto p-8 bg-white rounded-lg shadow-md">
        <!-- Title -->
        <h3 class="text-lg font-semibold mt-4 mb-2">[抑郁]</h3>
        <!-- Subtitle -->
        <h2 class="text-xl text-gray-600">得分: {{ this.analysis.depression.toFixed(2) }}</h2>
        <!-- Content -->
        <h3 class="text-lg mt-4 mb-2 text-left">[说明]</h3>
        <p class="mt-4 text-gray-700">
          {{ illustrate(5) }}
        </p>
        <!-- Additional paragraphs -->
        <h3 class="text-lg mt-4 mb-2 text-left">[指导建议]</h3>
        <p class="mt-4 text-gray-700">
            {{ additionalContent(5) }}
        </p>
      </article>

      <article class="max-w-8xl mx-auto p-8 bg-white rounded-lg shadow-md">
        <!-- Title -->
        <h3 class="text-lg font-semibold mt-4 mb-2">[焦虑]</h3>
        <!-- Subtitle -->
        <h2 class="text-xl text-gray-600">得分: {{ this.analysis.anxiety.toFixed(2) }}</h2>
        <!-- Content -->
        <h3 class="text-lg mt-4 mb-2 text-left">[说明]</h3>
        <p class="mt-4 text-gray-700">
          {{ illustrate(6) }}
        </p>
        <!-- Additional paragraphs -->
        <h3 class="text-lg mt-4 mb-2 text-left">[指导建议]</h3>
        <p class="mt-4 text-gray-700">
            {{ additionalContent(6) }}
        </p>
      </article>

      <article class="max-w-8xl mx-auto p-8 bg-white rounded-lg shadow-md">
        <!-- Title -->
        <h3 class="text-lg font-semibold mt-4 mb-2">[敌对]</h3>
        <!-- Subtitle -->
        <h2 class="text-xl text-gray-600">得分: {{ this.analysis.angerHostility.toFixed(2) }}</h2>
        <!-- Content -->
        <h3 class="text-lg mt-4 mb-2 text-left">[说明]</h3>
        <p class="mt-4 text-gray-700">
          {{ illustrate(7) }}
        </p>
        <!-- Additional paragraphs -->
        <h3 class="text-lg mt-4 mb-2 text-left">[指导建议]</h3>
        <p class="mt-4 text-gray-700">
            {{ additionalContent(7) }}
        </p>
      </article>

      <article class="max-w-8xl mx-auto p-8 bg-white rounded-lg shadow-md">
        <!-- Title -->
        <h3 class="text-lg font-semibold mt-4 mb-2">[恐怖]</h3>
        <!-- Subtitle -->
        <h2 class="text-xl text-gray-600">得分: {{ this.analysis.phobicAnxiety.toFixed(2) }}</h2>
        <!-- Content -->
        <h3 class="text-lg mt-4 mb-2 text-left">[说明]</h3>
        <p class="mt-4 text-gray-700">
          {{ illustrate(8) }}
        </p>
        <!-- Additional paragraphs -->
        <h3 class="text-lg mt-4 mb-2 text-left">[指导建议]</h3>
        <p class="mt-4 text-gray-700">
            {{ additionalContent(8) }}
        </p>
      </article>

      <article class="max-w-8xl mx-auto p-8 bg-white rounded-lg shadow-md">
        <!-- Title -->
        <h3 class="text-lg font-semibold mt-4 mb-2">[偏执]</h3>
        <!-- Subtitle -->
        <h2 class="text-xl text-gray-600">得分: {{ this.analysis.paranoidIdeation.toFixed(2) }}</h2>
        <!-- Content -->
        <h3 class="text-lg mt-4 mb-2 text-left">[说明]</h3>
        <p class="mt-4 text-gray-700">
          {{ illustrate(9) }}
        </p>
        <!-- Additional paragraphs -->
        <h3 class="text-lg mt-4 mb-2 text-left">[指导建议]</h3>
        <p class="mt-4 text-gray-700">
            {{ additionalContent(9) }}
        </p>
      </article>

      <article class="max-w-8xl mx-auto p-8 bg-white rounded-lg shadow-md">
        <!-- Title -->
        <h3 class="text-lg font-semibold mt-4 mb-2">[精神病性]</h3>
        <!-- Subtitle -->
        <h2 class="text-xl text-gray-600">得分: {{ this.analysis.Psychoticism.toFixed(2) }}</h2>
        <!-- Content -->
        <h3 class="text-lg mt-4 mb-2 text-left">[说明]</h3>
        <p class="mt-4 text-gray-700">
          {{ illustrate(10) }}
        </p>
        <!-- Additional paragraphs -->
        <h3 class="text-lg mt-4 mb-2 text-left">[指导建议]</h3>
        <p class="mt-4 text-gray-700">
            {{ additionalContent(10) }}
        </p>
      </article> 

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
      },
      reference:{
        Somatization: { X: 1.37, SD: 0.48 },
        ObsessiveCompulsive: { X: 1.62, SD: 0.58 },
        interpersonalSensibility: { X: 1.65, SD: 0.61 },
        depression: { X: 1.5, SD: 0.59 },
        anxiety: { X: 1.43, SD: 0.57 },
        angerHostility: { X: 1.46, SD: 0.55 },
        phobicAnxiety: { X: 1.23, SD: 0.41 },
        paranoidIdeation: { X: 1.43, SD: 0.57 },
        Psychoticism: { X: 1.29, SD: 0.42 }
      }
    }
  },
  mounted(){
    const script = document.createElement('script');
    script.src = '/static/js/echarts.min.js';
    script.onload = () => this.initECharts();
    document.head.appendChild(script);
  },
  computed:{
    keyFigure(){
      return this.analysis.totalScore || '未定义'
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
          opera_type:'get_sclanswer',
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
    illustrate(idx){
      switch(idx) {
        case 1:
          if(this.analysis.totalScore < 160 && this.analysis.positiveItem<=43 && this.analysis.Somatization <= 2 && this.analysis.ObsessiveCompulsive <= 2 && this.analysis.interpersonalSensibility <= 2 && this.analysis.depression <= 2 && this.analysis.anxiety <= 2 && this.analysis.angerHostility <= 2 && this.analysis.phobicAnxiety <= 2 && this.analysis.Psychoticism <= 2)
            return "被测者的心理健康状况良好。被测试者很少因心理原因出现身体不适感。能积极面对社会和生活中的各种问题，心理状态好，信任他人，对人友善。一般没有过于焦虑、悲伤等情况。总之，被测试者拥有比较健康的心态和情绪，能够较好地处理生活中的挫折和压力。能很好的适应工作、社会生活，并从中获得满足和快乐，个人价值感和幸福感较高。"
          else if(this.analysis.totalScore > 220) 
            return "被测者的心理健康状况不佳, 急需加以调适。被测试者可能在某一个或几个方面自感有很明显的症状。比如，可能出现因心理原因而引起的头晕、头痛、心慌、胸闷、胃部不适，或经常陷入痛苦体验和悲伤、抑郁的心境，或出现恐惧和回避社交的行为等。且因为痛苦而多次寻医但得不到确切结果，这种状况在中年女性中尤为常见。被测试者可以仔细查看自己的分测量表结果，结合自己日常生活的感受确认自己需要调整的主要问题。总之，被测试者可能遇到一些比较严重的困难，且受其困扰，常处于极端消极的心境当中，这种不良心境反过来严重影响了个体的工作效率、人际关系和生活质量，而这种影响也引起了被测试者本人或家人的注意。"
          else
          return "被测试者的心理健康处于亚健康状态。被测试者可能有一个或几个方面自感有较明显的症状。比如，可能出现因心理原因而引起的头晕、头痛、心慌、胸闷、胃部不适，发病前常出现痛苦体验和压抑的情绪。被测试者需仔细查看自己的分量表结果，结合自己日常生活的感受确认自己需要调整的主要问题。总之，被测试者在生活和工作上可能遇到了一些不易解决的问题，且受其困扰，常处于不良情绪状态之中，这种不良情绪反过来又会影响个体的工作效率、人际关系和生活质量，使个体处于一种恶性循环当中。但这种症状可能并不是很明显或者只是时而出现，并没有影响到个体正常的生活和工作，也正因为如此，目前个体症状并没有引起被测试者本人或家人足够的重视。"
        case 2:
          if(this.analysis.Somatization <= 2 || this.analysis.Somatization <= reference.Somatization.SD + reference.Somatization.X)
            return "被测者主观感觉身体健康。被试很少感到身体不适，比如心血管、胃肠道、呼吸和其他系统的主诉不适，也无头晕、头痛、心慌、胸闷、胃部不适等症状。"
          else
            return "被测者主观感觉身体不适。被测试者会经常感到身体某些部位不适，比如心血管、胃肠道、呼吸和其他系统的不适或头晕、头痛、心慌、胸闷、胃部不适等。症状严重的被测试者可能因此会反复去医院检查，但都没有任何结果，而被测试者认为这些症状是躯体性的（器质性病变所引起）要求进一步检查。"
        case 3:
          if(this.analysis.ObsessiveCompulsive <= 2 || this.analysis.ObsessiveCompulsive <= reference.ObsessiveCompulsive.SD + reference.ObsessiveCompulsive.X)
            return "被测者主观感觉身体健康。被试很少感到身体不适，比如心血管、胃肠道、呼吸和其他系统的主诉不适，也无头晕、头痛、心慌、胸闷、胃部不适等症状。"
          else
            return "被测者在生活中经常感到自身存在强迫性的想法或行为，即明知不必要却无法克制地要去想或要去做某事。比如无法停止反复想没有意义的事情；经常没有必要地反复做某些事情，例如检查门窗，开关，煤气，钱物，文件，表格，信件等；经常反复洗手而且洗手的时间很长，超过正常所需要；经常对病菌和各种疾病敏感，并毫无必要的担心等。这些强迫想法和行为让被测试者感到非常痛苦和焦虑，他们总是力图摆脱但往往越是企图抵制，反到感到紧张和痛苦。"
        case 4:
          if(this.analysis.interpersonalSensibility <= 2|| this.analysis.interpersonalSensibility <= this.reference.ObsessiveCompulsive.SD + this.reference.ObsessiveCompulsive.X)
            return "被测者在生活中不存在或很少存在强迫性的想法或行为。即没有出现反复而持久的观念、思想、印象或冲动念头。也没明知没有必要但还是要去做的反复动作，比如强迫洗涤、强迫检查、强迫计数等。"
          else 
            return "被测者存在人际关系敏感的问题。被测试者在与人交往时缺乏自信，敏感多虑，和人相处谨小慎微。容易和他人保持一定距离，虽然自己也希望拥有“知心朋友”，但又难与人建立亲密关系。与人相处很不自然，小心翼翼，害怕带给人麻烦，害怕别人嫌弃自己。有时会表现得特别有礼貌，实则给人距离和拘谨。很在意他人对自己的评价，很关注自己的言行是否得当。有的表现为特别害怕与异性交往。"
        case 5:
          if(this.analysis.depression <= 2 || this.analysis.depression <= this.reference.depression.SD + this.reference.depression.X)
            return "被测者不存在抑郁症状。被测试者精力旺盛，对生活充满信心和希望、兴趣广泛，自尊感高。即使偶尔遇到一些困难和挫折，也能很好应对和调节，并能从他人那里获得支持和帮助。"
          else
            return "被测者存在抑郁症状。被测试者懒散，随遇而安，对以往的爱好，甚至嗜好，以及日常生活都失去了兴趣，经常无精打采。思维反应迟钝，遇事难以决断，有的会出现失眠、早醒现象。对异性失去兴趣，食欲不振，体重下降。感觉自己没有生存的价值和意义，处于严重抑郁状态下的人无法自理生活，甚至有自杀行为。"
        case 6:
          if(this.analysis.anxiety <= 2 || this.analysis.anxiety <= this.reference.anxiety.SD + this.reference.anxiety.X)
            return "被测者不存在焦虑症状。被测试者很少有焦虑、烦躁、恐惧、紧张和不安情绪，也很少出现躯体症状，如心悸,心慌,胸闷,气短等。做事从容不破。能以平和的心态面对生活和工作中的压力。"
          else 
            return "被测者存在焦虑症状。被测试者时常会有焦虑、烦躁、恐惧、紧张和不安情绪，经常为一些尚未发生的事情担心而坐立不安，小动作增多,注意力无法集中,自己也不知道为什么如此惶恐不安。对未来生活缺乏信心和乐趣.有时情绪激动,失去平衡,经常无故地发怒,与家人争吵,对什么事情都看不惯,不满意。除这些不良情绪外，往往会伴有一些躯体症状，如心悸,心慌,胸闷,气短等。"
        case 7:
          if(this.analysis.angerHostility <= 2 || this.analysis.angerHostility <= this.reference.angerHostility.SD + this.reference.angerHostility.X)
            return "被测者不存在敌对症状。被测试者善于与人相处，信任他人。当与人发生矛盾时，很少有过激情绪和行为，比如争吵、摔东西等，一般能理智处理人际矛盾，有效调节化解自己的不良情绪。总之，被测试者能客观的评价事物和他人的言行，较友善的处理人际关系。"
          else
            return "被测者存在敌对症状。对一些给自己打击的人或和自己意见相左的人产生敌对情绪，认为有些人总是居心叵测或者有意针对自己，防范心理相对比较重。可能因一些很小的事情就与人发生口角，甚至摔物或争斗。情绪易激动，且不容易控制。存在一定人际关系问题。"
        case 8:
          if(this.analysis.phobicAnxiety <= 2 || this.analysis.phobicAnxiety <= this.reference.phobicAnxiety.SD + this.reference.phobicAnxiety.X)
            return "被测者不存在恐怖症状。被测试者很少有异常恐怖和害怕，对空旷场所、人群聚集处及公共场所等日常生活场所不会感到莫名的害怕，社交活动正常。"
          else 
            return "被测者存在恐怖症状。被测试者会有异常恐怖和害怕现象，害怕开放的空间或害怕离家（或独自在家），也包括害怕置身于人群拥挤场合以及难以逃回安全处所（多为家）的其他地方如商店、剧院、车厢等。尽管当时并无真正危险，但患者仍然极力回避所害怕的物体或处境。害怕并回避与某人或某类型人交往的情景。"
        case 9:
          if(this.analysis.paranoidIdeation <= 2 || this.analysis.paranoidIdeation <= this.reference.paranoidIdeation.SD + this.reference.paranoidIdeation.X)
            return "被测者不存在偏执症状。对周围事情的解释符合实际情况，很少有偏执想法和行为，如无根据的怀疑被人利用或伤害，过分自负，把错误和失败都归咎于他人，妄想某种关系的存在等等。能正确认识客观条件和局限，能接纳他人意见。"
          else 
            return "被测者存在偏执症状。被测试者对周围事情的解释经常不符合实际情况，脱离实际地好争辩与敌对，固执地追求个人不够合理的“权利”或利益，且很难用说理或事实来改变被测试者的想法。会有一些偏执想法和行为，如无根据的怀疑被人利用或伤害，过分自信，把错误和失败都归咎于他人，妄想某种关系的存在等等。"
        case 10:
          if(this.analysis.paranoidIdeation <= 2 || this.analysis.paranoidIdeation <= this.reference.paranoidIdeation.SD + this.reference.paranoidIdeation.X)
            return "被测者不存在精神病性症状。被测试者的精神正常，很少或从来没有出现幻觉，比如凭空听到有人在说话，看到或感觉到现实情况下不存在的东西。被测试者没有如下精神病性症状：如感到别人有特异功能，能看穿自己的想法，对他人有强烈的防范意识，与人疏离。认为自己有一些罪恶的想法，并很自责。" 
          else
            return "被测者存在精神病性症状。有时会出现幻觉，比如凭空听到有人在说话，看到或感觉到现实情况下不存在的东西。有如下精神病性症状：感到别人有特异功能，能看穿自己的想法，对他人有强烈的防范意识，与人疏离。认为自己有一些罪恶的想法，并很自责。"
        }
    },
    additionalContent(idx){
      switch(idx) {
        case 1:
          if(this.analysis.totalScore < 160 && this.analysis.positiveItem<=43 && this.analysis.Somatization <= 2 && this.analysis.ObsessiveCompulsive <= 2 && this.analysis.interpersonalSensibility <= 2 && this.analysis.depression <= 2 && this.analysis.anxiety <= 2 && this.analysis.angerHostility <= 2 && this.analysis.phobicAnxiety <= 2 && this.analysis.Psychoticism <= 2)
            return "被测者的心理健康状况良好。希望被试继续保持这种积极的心态和良好的行为方式。健康对我们每个人的生活和工作都起着重要的作用，好的身体来源于健康的心态，能解除心理疲劳。好的心态有助于我们克服困难，即使受到挫折与坎坷，依然能够保持乐观的情绪，保持旺盛的斗志。你也可以从以下方面进一步提高你的生活质量，如多与人为善，建立完善的人际网络作为自己心理支持的后盾，掌握一些保持身心健康的常识和技巧，保持乐观、自信的心态面对生活等。"
          else if(this.analysis.totalScore > 220)
            return "被测者的心理健康状况不佳, 急需调适。被测试者可能在几个分测验上的得分超出正常范围（存在或明显存在某些症状）。测试者应仔细查看每个分测验的结果，结合自身感受和他人的反馈，找到需要调适的主要方面。因为被测试者的心理健康状况已经受到破坏，精神压力比较大，不良症状比较多，单靠自身的调节可能很难较快地摆脱这种状态，建议被测试者到专业心理咨询或治疗机构进行咨询和就诊。而被测试者本人也应培养积极的心态，多多寻求各方面的帮助和支持，合理、适度地宣泄自己的情绪，这都有助于不良状态的改善。"
          else 
            return "测试者的心理健康处于亚健康状态。被测试者可能在某一个或几个分测验上存在超出正常范围。首先你要找出自己在哪个或哪些得分较高（存在某一症状），这样才能做到“对症下药”。其实，心理健康失调往往是不能很好的应对社会生活中的种种压力，采用了不恰当的方式如回避、夸大困难程度、压抑消极情绪、拒绝沟通、不寻求社会支持等等。不良的应对方式不仅不能解决问题，而且还会带来更多的负面情绪，这样个体就会陷入恶性循环的深渊。所以解决问题的关键是跳出这种怪圈，找到应对困难的正确方法。被测试者的情况还没有达到非常严重的程度，所以完全可以通过自身调节逐步恢复到健康水平。如有需要，也可以向他人或专业的心理工作者咨询。"
        case 2:
          if(this.analysis.Somatization <= 2 || this.analysis.Somatization <= this.reference.Somatization.SD + this.reference.Somatization.X)
            return "被测者主观感觉身体健康。这说明被测试者能较好的应对社会生活中的压力，能调整自己的心态，宣泄或转移不良情绪，有效防止心理因素躯体化，即表现出各种身体不适感。但没有身体上的不适感并非说，被测试者心理就一定很健康，也有可能这些心理压力未转化为躯体症状，所以建议被测试者保持积极、乐观的生活态度和自信、宽容的处世原则，此外，还应注意饮食均衡，作息有规律，适度体育锻炼等。"
          else
            return "被测试者主观感觉身体不适。被测试者应该首先到医院检查看是否有器质性病变，如果没有器质性病变，则应注意这些症状出现前是否承受了巨大心理压力，或者长期以来都有心理困扰，如果存在这些心理压力很可能是心理因素的躯体化表现。这时，减轻躯体不适的关键是消除这些不健康的心理因素。被测试者即不应该忽视身体的不适，也不必过分关注和夸大这些不适，而应“对症下药”。保持心情愉悦、正确认识和应对压力、适度的体育锻炼，对维持身心健康必不可少。"
        case 3:
          if(this.analysis.ObsessiveCompulsive <= 2 || this.analysis.ObsessiveCompulsive <= this.reference.ObsessiveCompulsive.SD + this.reference.ObsessiveCompulsive.X)
            return "被测者在生活中不存在或很少存在强迫性的想法或行为。被测试者要保持现在的状态，不要苛求自己，该怎么办就怎么办，做了以后就不要再去想它，也不要去评价它，议论它。用平和的心态面对自己，对于目标要努力争取但也不必强求，而应顺其自然。不对自己和他人过于苛求，接受自己和他人的缺点与不足。"
          else
            return "被测者在生活中经常感到自身存在强迫性的想法或行为。运用“听其自然”方法，不要苛求自己，该怎么办就怎么办，做了以后就不要再去想它，也不要去评价它，议论它。如果出现异常观念和行为要从认知上进行调节，要么完全接受它，顺其自然，要么通过夸张的想法，使其达到荒诞透顶的程度，以致自己也觉得很可笑，由此消除强迫想法或行为。当自己处于莫名其妙的紧张和焦虑状态时可以进行自我暗示，说服自己不要紧张。当出现强迫现象采用其它活动来转移或直接对抗强迫思维，如高声唱歌，背诵诗词等。 被测试者还可以寻求专业心理工作者的帮助。"
        case 4:
          if(this.analysis.interpersonalSensibility <= 2|| this.analysis.interpersonalSensibility <= this.reference.ObsessiveCompulsive.SD + this.reference.ObsessiveCompulsive.X)
            return "被测者不存在人际关系敏感的问题。被测试者应保持这样状态，在人际交往中保持乐观、开朗、自信的心态，同时加强与人交往的技巧。真诚待人，遇事多站在对方立场考虑 。良好的亲密关系，一方面给人归属感和价值感，另一方面，只有当一个人很好接纳自己才能更容易被他人接纳。"
          else 
            return "被测者存在人际关系敏感的问题。被测试者应加强在人际交往过程中的信心，不要过分注意自己的言行是否妥当，也不必太过在意他人对你的评价，应自然、自信的交往。多找些自己和他人的长处，同时正视自己的缺点，遇到让自己感到难堪的时刻，学会自我解嘲。建立自己的积极形象，想象自己希望成为的样子，越细致越好，这种积极的自我暗示有助于增加对自己的接纳和信心。同时，应适当了解对方的背景和需要，即提高人际“敏感度”。"
        case 5:
          if(this.analysis.depression <= 2 || this.analysis.depression <= this.reference.depression.SD + this.reference.depression.X)
            return "被测者不存在抑郁症状。希望被测试者在今后的日子里继续保持开朗乐观的心态，因为生活中难免不会遇到挫折和暂时的低谷，而真正的力量来自心的力量，所以健康的心理是战胜困难的法宝。暂时的情绪低落和消沉没有什么可怕，要认识到这些情绪产生的原因，理性分析问题，调节不良情绪，选择恰当应对方式。"
          else
            return "被测试者存在抑郁症状。如果被测试者抑郁情绪因某事而起，且持续时间不长，则需要采用合理的渠道宣泄自己的情绪，比如，找人倾诉、哭泣、书写等，心情平静后，理智的分析问题产生的原因以及可以采取的办法。如果被测试者抑郁情绪持续时间比较长，而且在一定程度上影响了自己的工作和生活的，首先，不要自责，抑郁表现是一种疾病，人们没有能力选择它。其次，简化生活，不要要求自己同时做很多事，或快速完成某项任务，这可能会让你觉得力不从心，而变得更加沮丧。再次，可以参加一些擅长的、能让自己有成就感的活动。"
        case 6:
          if(this.analysis.anxiety <= 2 || this.analysis.anxiety <= this.reference.anxiety.SD + this.reference.anxiety.X)
            return "被测者不存在焦虑症状。这说明被测试者生活压力不大或者能很好的应对压力，懂得避免或缓解焦虑情绪。人们在面临某种威胁或不可控的情境时会产生紧张、不安和焦虑。适度的焦虑有利于人们调动自身的资源（智力和体力）来应对问题，这是人类正常的应激机制，所以不必担心。但过度或长时间的焦虑对个体的身心健康有很大的危害，一方面，焦虑是许多心理症状和一些生理症状的直接原因。另一方面，过度的焦虑对人的行为、智力、人格等造成不良的影响。日常生活中，人们会面临格式各样的压力，容易出现焦虑情绪，因此需要学会控制和消除焦虑的方法，比如转移注意力、放松法、认清威胁来源的真正内容，对当前的情境进行具体分析。"
          else 
            return "被测者存在焦虑症状。适度的焦虑有利于人们调动自身的资源（智力和体力）来应对问题，这是人类正常的应激机制，所以不必担心。但过度或长时间的焦虑对个体的身心健康有很大的危害，一方面，焦虑是许多心理症状和一些生理症状的直接原因。另一方面，过度的焦虑对人的行为、智力、人格等造成不良的影响。由于被测试者目前已经存在焦虑症状，建议被测试者用以下方法应对焦虑：(1)可找朋友谈，参加一些文体活动，使自己的焦虑郁闷情绪得以宣泄而达到情绪的稳定。 （2）正确评价自己，既看到自己的优势，也要看到自己的不足；期望值不要定得太高，要正视现实，理想与现实之间的距离不要太大。不妨调整一下自己的目标，就能从困境中得到解脱。（3）以足够的睡眠消除疲劳，换取充沛的精力和清醒的头脑。"
        case 7:
          if(this.analysis.angerHostility <= 2 || this.analysis.angerHostility <= this.reference.angerHostility.SD + this.reference.angerHostility.X)
            return "被测者不存在敌对症状。友善、豁达的态度有助于赢得更多的友谊，也更容易得到他人更多的信任、理解和帮助。希望被测试者保持这种接纳、宽容的心对待他人，相信生活会更加和谐。"
          else
            return "被测者存在敌对症状。被测试者对他人的敌对情绪和行为一方面反应了自我控制力弱，另一方面表明存在认识或人格上的缺陷。比如可能不够豁达，即使很小的事情也耿耿于怀，无法站在他人的角度看到问题等。建议被测试者在与人交往时，如果出现敌对的思想，要用理智来克制自己的情感，使敌意、怒气渐渐消除、化解。遇事不能鲁莽，应设身处地地替别人想一想，这样才能理解他人的观点和行为举止。在生活中，人与人之际爱你难免有误解，而一个得体的幽默，往往能使双方摆脱困窘的境地。与人叫我那个应不抱成见，寻找机会取得他人的信任，奉行以诚相待的原则。"
        case 8:
          if(this.analysis.phobicAnxiety <= 2 || this.analysis.phobicAnxiety <= this.reference.phobicAnxiety.SD + this.reference.phobicAnxiety.X)
            return "被测者不存在恐怖症状。恐怖情绪对人类而言有适应功能，有助于人们回避、逃离危险刺激，保护自我。生活中每个人都会遇到令自己恐怖的场景或事物，比如怕蛇、怕黑、怕高。适度的恐惧不会影响个体的生活，也不必进行人为干预。"
          else 
            return "被测试者存在恐怖症状。如果被测试者自感恐惧心理不很严重，可先从认知上接受恐惧发生时的身心变化，不要去抗拒、抑制或掩饰它；同时，进行放松训练，如感到恐惧时，有意识地做深呼吸，放松全身。对于比较严重的症状，目前最为常用的是系统脱敏法，这种方法让患者循序渐进地暴露于引起焦虑、恐惧的刺激，使患者对恐怖刺激的敏感性逐渐降低。严重的恐怖症患者还应配合药物治疗，如抗焦虑药、抗抑郁药。自感症状严重者建议寻求心理咨询师的帮助。"
        case 9:
          if(this.analysis.paranoidIdeation <= 2 || this.analysis.paranoidIdeation <= this.reference.paranoidIdeation.SD + this.reference.paranoidIdeation.X)
            return "被测者不存在偏执症状。被试者对周围的人和事能够以客观、理智的态度来对待,不会苛求、走极端。希望被测试者保持这种状态，在与人交往时，真诚相见，以诚交心，主动帮助朋友，取得对方的信任和巩固的友谊。尊重差异，和谐相处。"
          else 
            return "被测者存在偏执症状。被测试者应克服多疑敏感、固执、不安全感和自我中心的人格缺陷。可以从以下几个方面进行校正：（1）与他人建立信任关系，在相互信任的基础上交流情感，以诚相待，告诉对方自己在人格上缺陷和想改变的愿望。（2）积极主动地进行交友活动，在交友中学会信任他人，消除不安全感。（3）自我反省，认识自己的偏执观念，并对这些观念加以改造，以除去其中极端偏激的成份。"
        case 10:
          if(this.analysis.paranoidIdeation <= 2 || this.analysis.paranoidIdeation <= this.reference.paranoidIdeation.SD + this.reference.paranoidIdeation.X)
            return "被测者不存在精神病性症状。被测试者有稳定的情绪和理性的思维。这是精神健康的表现，希望被测试者在今后生活中，继续保持这种心态和方法。"
          else
            return "被测试者存在精神病性症状。被测试者需要到正规医院的精神科接受进一步检查，以确定症状是否确实存在，以及对应的矫治或治疗方法，如有需要需在专业医生指导下采用心理和药物的协同方式来减轻和消除这些精神症状。"     
      }
    },
    initECharts(){
      this.createChart();
    },
    createChart(){
      const echarts = require('echarts');

      // 基于准备好的dom，初始化echarts实例
      let myChart = echarts.init(this.$refs.chart);

      // 指定图表的配置项和数据
      let option = {
        title: {
          text: '心理健康状况'
        },
        tooltip: {},
        legend: {
          data:['得分']
        },
        xAxis: {
          data: Object.keys(this.analysis)
        },
        yAxis: {},
        series: [{
          name: '得分',
          type: 'line',
          data: Object.values(this.analysis)
        }]
      };

    // 使用刚指定的配置项和数据显示图表。
      myChart.setOption(option);
    }
  },
  watch:{
    "$route":{
      handler(){
         this.getAnalysis()
      },
      immediate:true
    }
  },
}
</script>
