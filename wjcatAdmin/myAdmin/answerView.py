"""
程序名：回答问卷请求接口
功能：回答问卷后台处理函数
"""
from django.shortcuts import HttpResponse
import json
from myAdmin.models import *
from django.db import transaction
import datetime


############################################################
#功能：问卷回答者操作主入口
#最后更新：2019-05-24
############################################################
def opera(request):
    response={'code':0,'msg':'success'}
    if request.method=='POST':
        body=str(request.body,encoding='utf-8')
        print(body)
        try:
            info = json.loads(body)#解析json报文
        except:
            response['code'] = '-2'
            response['msg'] = '请求格式有误'
        opera_type=info.get('opera_type')#获取操作类型
        if opera_type:
            if opera_type=='get_info':#获取问卷信息
                response=getInfo(info,request)
            elif opera_type=='get_temp_info':#获取问卷信息
                response=getTempInfo(info,request)
            elif opera_type=='submit_wj':#提交问卷
                response=submitWj(info,request)
            elif opera_type=='get_answer':#查询提交答案:
                response=getAnswer(info,request)
            elif opera_type=='get_answer_with_option':#查询提交答案
                response=getAnswerWithOption(info,request)
            else:
                response['code'] = '-7'
                response['msg'] = '请求类型有误'
        else:
            response['code'] = '-3'
            response['msg'] = '确少必要参数'
    else:
        response['code']='-1'
        response['msg']='请求方式有误'

    return HttpResponse(json.dumps(response))



def getInfo(info,request):
    response = {'code': 0, 'msg': 'success'}
    wjId=info.get('wjId')
    username = request.session.get('username')
    if wjId:
        try:#判断问卷id是否存在
            res=Wj.objects.get(id=wjId)#查询id为wjId
            response['title']=res.title
            response['desc']=res.desc
        except:
            response['code'] = '-10'
            response['msg'] = '问卷不存在'
        else:
            if res.username==username or res.status==1:#只有问卷发布者或者此问卷为已发布才能查看
                obj = Question.objects.filter(wjId=wjId)
                detail = []
                for item in obj:
                    temp = {}
                    temp['title'] = item.title
                    temp['type'] = item.type
                    temp['id'] = item.id  # 问题id
                    temp['row'] = item.row
                    temp['must'] = item.must
                    # 获取选项
                    temp['options'] = []
                    if temp['type'] in ['radio', 'checkbox']:  # 如果是单选或者多选
                        optionItems = Options.objects.filter(questionId=item.id)
                        for optionItem in optionItems:
                            temp['options'].append({'title':optionItem.title,'id':optionItem.id})
                    temp['radioValue'] = -1  # 接收单选框的值
                    temp['checkboxValue'] = []  # 接收多选框的值
                    temp['textValue'] = ''  # 接收输入框的值
                    detail.append(temp)
                response['detail'] = detail
            else:
                response['code'] = '-10'
                response['msg'] = '问卷尚未发布'
    else:
        response['code'] = '-3'
        response['msg'] = '确少必要参数'
    return response




############################################################
#功能：获取模板问卷信息
#最后更新：2019-06-16
############################################################
def getTempInfo(info,request):
    response = {'code': 0, 'msg': 'success'}
    wjId=info.get('wjId')
    username = request.session.get('username')
    if wjId:
        try:#判断问卷id是否存在
            res=TempWj.objects.get(id=wjId)#查询id为wjId
            response['title']=res.title
            response['desc']='问卷描述'
        except:
            response['code'] = '-10'
            response['msg'] = '模板不存在'
        else:
            obj = TempQuestion.objects.filter(wjId=wjId)
            detail = []
            for item in obj:
                temp = {}
                temp['title'] = item.title
                temp['type'] = item.type
                temp['id'] = item.id  # 问题id
                temp['row'] = item.row
                temp['must'] = item.must
                # 获取选项
                temp['options'] = []
                if temp['type'] in ['radio', 'checkbox']:  # 如果是单选或者多选
                    optionItems = TempOptions.objects.filter(questionId=item.id)
                    for optionItem in optionItems:
                        temp['options'].append({'title':optionItem.title,'id':optionItem.id})
                temp['radioValue'] = -1  # 接收单选框的值
                temp['checkboxValue'] = []  # 接收多选框的值
                temp['textValue'] = ''  # 接收输入框的值
                detail.append(temp)
            response['detail'] = detail
    else:
        response['code'] = '-3'
        response['msg'] = '确少必要参数'
    return response



def getOptionScore(optionId):
    try:
        option = Options.objects.get(id=optionId)
        return option.score
    except Options.DoesNotExist:
        return None

@transaction.atomic
def submitWj(info,request):
    response = {'code': 0, 'msg': 'success'}
    wjId = info.get('wjId')
    useTime=info.get('useTime')
    detail=info.get('detail')
    if 'HTTP_X_FORWARDED_FOR' in request.META:
        ip = request.META.get('HTTP_X_FORWARDED_FOR')
    else:
        ip = request.META.get('REMOTE_ADDR')

    s1 = transaction.savepoint()#设置事务保存点 回滚使用
    if wjId:

        try:  # 判断问卷id是否存在
            res = Wj.objects.get(id=wjId)  # 查询id为wjId
            response['title'] = res.title
            response['desc'] = res.desc
            response['wjId'] = wjId
        except:
            response['code'] = '-10'
            response['msg'] = '问卷不存在'
            return response
        if res.status==0:#当问卷状态为1(已发布)时才可回答
            response['code'] = '-10'
            response['msg'] = '问卷尚未发布'
            return response

        #记录提交信息
        submitInfo=Submit.objects.create(
            wjId=wjId,
            submitTime=datetime.datetime.now(),
            submitIp=ip,
            useTime=useTime
        )
        response['submitId']=submitInfo.id
        qItems=Question.objects.filter(wjId=wjId,must=True)#查询所有必填题目
        musts=[]
        for qItem in qItems:
            musts.append(qItem.id)#记录所有必填题目的题目id
        totalScore = 0
        avgScore = 0.0
        positiveItem = 0
        Somatization = 0.0
        SomatizationList = [1,4,12,27,40,42,48,49,52,53,56,58]
        ObsessiveCompulsive=0.0
        ObsessiveCompulsiveList = [3,9,10,28,38,45,46,51,55,65]
        interpersonalSensibility=0.0
        interpersonalSensibilityList= [6,21,34,36,37,41,61,69,73]
        depression = 0.0
        depressionList = [5,14,15,20,22,26,29,30,31,32,54,71,79]
        anxiety = 0.0
        anxietyList=[2,17,23,33,39,57,72,78,80,86]
        angerHostility=0.0
        angerHostilityList=[11,24,63,67,74,81]
        phobicAnxiety=0.0
        phobicAnxietyList=[13,25,47,50,70,75,82]
        paranoidIdeation=0.0
        paranoidIdeationList=[8,18,43,68,76,83]
        Psychoticism=0.0
        PsychoticismList=[7,16,35,62,77,84,85,87,88,90]
        additionalItems=0.0
        #记录答案
        for item in detail:
            if item['type']=='radio':#单选题
                if item['id'] in musts and item['radioValue']==-1:#此必填选项未填 回滚
                    print('开始回滚')
                    transaction.savepoint_rollback(s1)
                    print('已回滚')
                    response['code'] = '-11'
                    response['msg'] = '有必答题目未回答'
                    break
                questionId = item['id']
                Answer.objects.create(
                    questionId=questionId,
                    submitId=submitInfo.id,
                    wjId=wjId,
                    type=item['type'],
                    answer=item['radioValue']
                )
                if wjId =="1":
                    value  = item['radioValue']
                    score = getOptionScore(value)
                    if questionId in SomatizationList:
                        Somatization += score
                    elif questionId in ObsessiveCompulsiveList:
                        ObsessiveCompulsive += score
                    elif questionId in interpersonalSensibilityList:
                        interpersonalSensibility += score
                    elif questionId in depressionList:
                        depression += score
                    elif questionId in anxietyList:
                        anxiety += score
                    elif questionId in angerHostilityList:
                        angerHostility += score
                    elif questionId in phobicAnxietyList:
                        phobicAnxiety += score
                    elif questionId in paranoidIdeationList:
                        paranoidIdeation += score
                    elif questionId in PsychoticismList:
                        Psychoticism += score
                    totalScore += score
                    if score > 2:
                        positiveItem += 1
            elif item['type']=='checkbox':#多选题
                if item['id'] in musts and len(item['checkboxValue'])==0:#此必填选项未填 回滚
                    print('开始回滚')
                    transaction.savepoint_rollback(s1)
                    print('已回滚')
                    response['code'] = '-11'
                    response['msg'] = '有必答题目未回答'
                    break
                for value in item['checkboxValue']:
                    Answer.objects.create(
                        questionId=item['id'],
                        submitId=submitInfo.id,
                        wjId=wjId,
                        type=item['type'],
                        answer=value
                    )
            elif item['type']=='text':#填空题
                if item['id'] in musts and item['textValue']=='':#此必填选项未填 回滚
                    print('开始回滚')
                    transaction.savepoint_rollback(s1)
                    print('已回滚')
                    response['code'] = '-11'
                    response['msg'] = '有必答题目未回答 '
                    break
                Answer.objects.create(
                    questionId=item['id'],
                    submitId=submitInfo.id,
                    wjId=wjId,
                    type=item['type'],
                    answerText=item['textValue']
                )
        avgScore = totalScore / 90
        Somatization /= 12    
        ObsessiveCompulsive /= 10
        interpersonalSensibility /= 9
        depression /= 13
        anxiety /= 10
        angerHostility /= 6
        phobicAnxiety /= 7
        paranoidIdeation /= 6
        Psychoticism /= 10
        SCLanalysis.objects.create(
            wjId=wjId,
            submitId = submitInfo.id,
            totalScore = totalScore,
            totalAvgScore = avgScore,
            positiveItem = positiveItem,
            Somatization=Somatization,
            ObsessiveCompulsive = ObsessiveCompulsive,
            interpersonalSensibility = interpersonalSensibility,
            depression = depression,
            anxiety = anxiety,
            angerHostility = angerHostility,
            phobicAnxiety = phobicAnxiety,
            paranoidIdeation = paranoidIdeation,
            Psychoticism = Psychoticism,
        )
    else:
        response['code'] = '-3'
        response['msg'] = '确少必要参数'

    return response

def getAnswer(info,request):
    response = {'code': 0, 'msg': 'success'}
    wjId = info.get('wjId')
    submitId=info.get('submitId')
    if wjId and submitId:
        try:  # 判断问卷id是否存在
            res = Wj.objects.get(id=wjId)  # 查询id为wjId
            response['title'] = res.title
            response['desc'] = res.desc
            response['wjId'] = wjId
        except:
            response['code'] = '-10'
            response['msg'] = '问卷不存在'
            return response
        if res.status==0:#当问卷状态为1(已发布)时才可回答
            response['code'] = '-10'
            response['msg'] = '问卷尚未发布'
            return response

        #记录答案
        answerItems=Answer.objects.filter(wjId=wjId,submitId=submitId)
        detail=[]
        for item in answerItems:
            temp={}
            temp['questionId']=item.questionId
            temp['type']=item.type
            temp['answer']=item.answer
            temp['answerText']=item.answerText
            detail.append(temp)
        response['detail']=detail
    else:
        response['code'] = '-3'
        response['msg'] = '确少必要参数'

    return response


def getAnswerWithOption(info,request):
    response = {'code': 0, 'msg': 'success'}
    wjId = info.get('wjId')
    submitId=info.get('submitId')
    if wjId and submitId:
        try:  # 判断问卷id是否存在
            res = Wj.objects.get(id=wjId)  # 查询id为wjId
            response['title'] = res.title
            response['desc'] = res.desc
            response['wjId'] = wjId
        except:
            response['code'] = '-10'
            response['msg'] = '问卷不存在'
            return response
        if res.status==0:#当问卷状态为1(已发布)时才可回答
            response['code'] = '-10'
            response['msg'] = '问卷尚未发布'
            return response

        #记录答案
        answerItems=Answer.objects.filter(wjId=wjId,submitId=submitId)
        detail=[]
        for item in answerItems:
            temp={}
            temp['questionId']=item.questionId
            temp['type']=item.type
            temp['answer']=item.answer
            temp['answerText']=item.answerText
            if item.type in ['radio','checkbox']:
                temp['options']=[]
                optionItems=Options.objects.filter(questionId=item.questionId)
                for optionItem in optionItems:
                    temp['options'].append({'title':optionItem.title,'id':optionItem.id})
                    if item.answer==optionItem.id:
                        temp['answerTitle']=optionItem.title
            detail.append(temp)
        response['detail']=detail
    else:
        response['code'] = '-3'
        response['msg'] = '确少必要参数'

    return response

def getSclAnswer(info, request):
    response = {'code': 0, 'msg': 'success'}
    wjId = info.get('wjId')
    submitId=info.get('submitId')
    if wjId and submitId:
        try:  # 判断问卷id是否存在
            res = Wj.objects.get(id=wjId)  # 查询id为wjId
            response['title'] = res.title
            response['desc'] = res.desc
            response['wjId'] = wjId
        except:
            response['code'] = '-10'
            response['msg'] = '问卷不存在'
            return response
        if res.status==0:#当问卷状态为1(已发布)时才可回答
            response['code'] = '-10'
            response['msg'] = '问卷尚未发布'
            return response
        analysis = SCLanalysis.objects.filter(wjId=wjId, submitId=submitId)
        analysis_data = {
            "wjId": analysis.wjId,
            "submitId": analysis.submitId,
            "totalScore": analysis.totalScore,
            "totalAvgScore": analysis.totalAvgScore,
            "positiveItem": analysis.positiveItem,
            "Somatization": analysis.Somatization,
            "ObsessiveCompulsive": analysis.ObsessiveCompulsive,
            "interpersonalSensibility": analysis.interpersonalSensibility,
            "depression": analysis.depression,
            "anxiety": analysis.anxiety,
            "angerHostility": analysis.angerHostility,
            "phobicAnxiety": analysis.phobicAnxiety,
            "paranoidIdeation": analysis.paranoidIdeation,
            "Psychoticism": analysis.Psychoticism
        }
        response['detail'] = analysis_data
    else:
        response['code'] = '-3'
        response['msg'] = '确少必要参数'

    return response