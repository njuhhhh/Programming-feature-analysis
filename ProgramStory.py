# encoding=utf-8
import json
import time
import datetime

import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.tsa.stattools as ts

f = open('test_data.json', encoding='utf-8')
res = f.read()
data = json.loads(res)

def mysum(date,a,b):
	result=0
	for i in range(a,b):
		result+=date[i]
	return result

#ADF 检验
def ADF(datelist):
	b = np.array(datelist)
	adftest = ts.adfuller(b, autolag='AIC')
	print (adftest)

# 统计提交次数
def addList(maxlist, submission, l, i):
    sum_submission = sum(submission)
    if submission[i] != 0:
        if len(l) != 0:
            maxlist.append(submission[i] / sum_submission * np.mean(l))
        else:
            maxlist.append(0)
    else:
        maxlist.append(0)
    return maxlist


#寻找最小值
def Find_min(a):
    m = a[0]
    for i in range(1, len(a)):
        if a[i] < m:
            m = a[i]
    return m

#寻找最大值
def Find_max(a):
    m = a[0]
    for i in range(1, len(a)):
        if a[i] > m:
            m = a[i]
    return m

def GetTopStudent(list1):
    for i in data:
        if searchweaknessNum(i)>=90:
            list1.append(data[i]["user_id"])
    print(list1)


def searchweaknessNum(user_id):
    value_of_string = powervalue(data[user_id]["cases"], "字符串")
    value_of_lineartable = powervalue(data[user_id]["cases"], "线性表")
    value_of_array = powervalue(data[user_id]["cases"], "数组")
    value_of_searchalgorithm = powervalue(data[user_id]["cases"], "查找算法")
    value_of_sigitaloperation = powervalue(data[user_id]["cases"], "数字操作")
    value_of_treestructure = powervalue(data[user_id]["cases"], "树结构")
    value_of_graphstructure = powervalue(data[user_id]["cases"], "图结构")
    value_of_sortingalgorithm = powervalue(data[user_id]["cases"], "排序算法")
    a=[value_of_string, value_of_lineartable, value_of_array, value_of_searchalgorithm, value_of_sigitaloperation,
         value_of_treestructure, value_of_graphstructure, value_of_sortingalgorithm]
    weaknessNum=Find_min(a)
    temp=a.index(weaknessNum)
    lables = ["字符串", "线性表", "数组", "查找算法", "数字操作", "树结构", "图结构", "排序算法"]
    weakness=lables[temp]
    return weaknessNum

def searchweakness(user_id):
    value_of_string = powervalue(data[user_id]["cases"], "字符串")
    value_of_lineartable = powervalue(data[user_id]["cases"], "线性表")
    value_of_array = powervalue(data[user_id]["cases"], "数组")
    value_of_searchalgorithm = powervalue(data[user_id]["cases"], "查找算法")
    value_of_sigitaloperation = powervalue(data[user_id]["cases"], "数字操作")
    value_of_treestructure = powervalue(data[user_id]["cases"], "树结构")
    value_of_graphstructure = powervalue(data[user_id]["cases"], "图结构")
    value_of_sortingalgorithm = powervalue(data[user_id]["cases"], "排序算法")
    a=[value_of_string, value_of_lineartable, value_of_array, value_of_searchalgorithm, value_of_sigitaloperation,
         value_of_treestructure, value_of_graphstructure, value_of_sortingalgorithm]
    weaknessNum=Find_min(a)
    temp=a.index(weaknessNum)
    lables = ["字符串", "线性表", "数组", "查找算法", "数字操作", "树结构", "图结构", "排序算法"]
    weakness=lables[temp]
    return weakness

def searchstrongNum(uesr_id):
    value_of_string = powervalue(data[user_id]["cases"], "字符串")
    value_of_lineartable = powervalue(data[user_id]["cases"], "线性表")
    value_of_array = powervalue(data[user_id]["cases"], "数组")
    value_of_searchalgorithm = powervalue(data[user_id]["cases"], "查找算法")
    value_of_sigitaloperation = powervalue(data[user_id]["cases"], "数字操作")
    value_of_treestructure = powervalue(data[user_id]["cases"], "树结构")
    value_of_graphstructure = powervalue(data[user_id]["cases"], "图结构")
    value_of_sortingalgorithm = powervalue(data[user_id]["cases"], "排序算法")
    a = [value_of_string, value_of_lineartable, value_of_array, value_of_searchalgorithm, value_of_sigitaloperation,
         value_of_treestructure, value_of_graphstructure, value_of_sortingalgorithm]
    strongNum = Find_max(a)
    temp2 = a.index(strongNum)
    lables = ["字符串", "线性表", "数组", "查找算法", "数字操作", "树结构", "图结构", "排序算法"]
    strong = lables[temp2]
    return strongNum

def searchstrong(uesr_id):
    value_of_string = powervalue(data[user_id]["cases"], "字符串")
    value_of_lineartable = powervalue(data[user_id]["cases"], "线性表")
    value_of_array = powervalue(data[user_id]["cases"], "数组")
    value_of_searchalgorithm = powervalue(data[user_id]["cases"], "查找算法")
    value_of_sigitaloperation = powervalue(data[user_id]["cases"], "数字操作")
    value_of_treestructure = powervalue(data[user_id]["cases"], "树结构")
    value_of_graphstructure = powervalue(data[user_id]["cases"], "图结构")
    value_of_sortingalgorithm = powervalue(data[user_id]["cases"], "排序算法")
    a = [value_of_string, value_of_lineartable, value_of_array, value_of_searchalgorithm, value_of_sigitaloperation,
         value_of_treestructure, value_of_graphstructure, value_of_sortingalgorithm]
    strongNum = Find_max(a)
    temp2 = a.index(strongNum)
    lables = ["字符串", "线性表", "数组", "查找算法", "数字操作", "树结构", "图结构", "排序算法"]
    strong = lables[temp2]
    return strong

def habit(user_id,type):
    case = data[user_id]["cases"]
    list1, list2, list3, list4, list5, list6, list7, list8, list9, list10, list11, list12 = [], [], [], [], [], [], [], [], [], [], [], []
    datelist = [0 for i in range(44)]
    submission = [0 for i in range(12)]
    for problems in case:
        uploads = problems["upload_records"]
        for upload in uploads:
            timeStamp = upload["upload_time"]
            score = upload["score"]
            timeArray = time.localtime(timeStamp / 1000)
            myTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)

            # 算天数
            dateStr = time.strftime("%m-%d", timeArray)
            a, b = int(time.strftime("%m", timeArray)), int(time.strftime("%d", timeArray))
            d1 = datetime.date(2020, 2, 17)
            d2 = datetime.date(2020, a, b)
            num = (d2 - d1).days  # int
            if (score == 100):
                datelist[num] = datelist[num] + 1

            # 算平均分
            hourStr = time.strftime("%H", timeArray)
            hour = int(hourStr)
            if hour >= 0 and hour < 2:
                list1.append(score)
                if score != 0:
                    submission[0] = submission[0] + 1
            elif hour >= 2 and hour < 4:
                list2.append(score)
                if score != 0:
                    submission[1] = submission[1] + 1
            elif hour >= 4 and hour < 6:
                list3.append(score)
                if score != 0:
                    submission[2] = submission[2] + 1
            elif hour >= 6 and hour < 8:
                list4.append(score)
                if score != 0:
                    submission[3] = submission[3] + 1
            elif hour >= 8 and hour < 10:
                list5.append(score)
                if score != 0:
                    submission[4] = submission[4] + 1
            elif hour >= 10 and hour < 12:
                list6.append(score)
                if score != 0:
                    submission[5] = submission[5] + 1
            elif hour >= 12 and hour < 14:
                list7.append(score)
                if score != 0:
                    submission[6] = submission[6] + 1
            elif hour >= 14 and hour < 16:
                list8.append(score)
                if score != 0:
                    submission[7] = submission[7] + 1
            elif hour >= 16 and hour < 18:
                list9.append(score)
                if score != 0:
                    submission[8] = submission[8] + 1
            elif hour >= 18 and hour < 20:
                list10.append(score)
                if score != 0:
                    submission[9] = submission[9] + 1
            elif hour >= 20 and hour < 2:
                list11.append(score)
                if score != 0:
                    submission[10] = submission[10] + 1
            elif hour >= 22 and hour <= 24:
                list12.append(score)
                if score != 0:
                    submission[1] = submission[1] + 1

    maxlist = []
    maxlist = addList(maxlist, submission, list1, i=0)
    maxlist = addList(maxlist, submission, list2, i=1)
    maxlist = addList(maxlist, submission, list3, i=2)
    maxlist = addList(maxlist, submission, list4, i=3)
    maxlist = addList(maxlist, submission, list5, i=4)
    maxlist = addList(maxlist, submission, list6, i=5)
    maxlist = addList(maxlist, submission, list7, i=6)
    maxlist = addList(maxlist, submission, list8, i=7)
    maxlist = addList(maxlist, submission, list9, i=8)
    maxlist = addList(maxlist, submission, list10, i=9)
    maxlist = addList(maxlist, submission, list11, i=10)
    maxlist = addList(maxlist, submission, list12, i=11)

    result = maxlist.index(max(maxlist))
    st = result * 2

    # ADF(datelist);

    if type==1:
        sum_submission = sum(submission)
        print("该同学作业完成类型为:", end="")
        if mysum(datelist,0,20)/sum_submission >=0.6:
            print("提前完成")
        elif mysum(datelist,30,44)/sum_submission >=0.6:
            print("拖后完成")
        else:
            print("平稳完成")

        plt.figure(figsize=(12,5))#拉长画布

        #时间段绘图
        title1=["0:00~2:00","2:00~4:00","4:00~6:00","6:00~8:00","8:00~10:00","10:00~12:00","12:00~14:00","14:00~16:00","16:00~18:00","18:00~20:00","20:00~22:00","22:00~24:00"]
        plt.subplot(1,2,1)
        plt.plot(title1,maxlist,label='Efficiency')
        plt.legend(loc="upper right")
        plt.xlabel('Time')
        plt.ylabel('Score')
        plt.xticks(rotation=-15)#倾斜标签

        #完成类型绘图
        title2=[i+1 for i in range(44)]
        plt.subplot(1,2,2)
        plt.plot(title2,datelist,label='Efficiency')
        plt.legend(loc="upper right")
        plt.xlabel('Number')
        plt.ylabel('Score')

        plt.show()

    return st    

def gethabit(user_id):
    case = data[user_id]["cases"]
    list1, list2, list3, list4, list5, list6, list7, list8, list9, list10, list11, list12 = [], [], [], [], [], [], [], [], [], [], [], []
    datelist = [0 for i in range(44)]
    submission = [0 for i in range(12)]
    for problems in case:
        uploads = problems["upload_records"]
        for upload in uploads:
            timeStamp = upload["upload_time"]
            score = upload["score"]
            timeArray = time.localtime(timeStamp / 1000)
            myTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)

            # 算天数
            dateStr = time.strftime("%m-%d", timeArray)
            a, b = int(time.strftime("%m", timeArray)), int(time.strftime("%d", timeArray))
            d1 = datetime.date(2020, 2, 17)
            d2 = datetime.date(2020, a, b)
            num = (d2 - d1).days  # int
            if (score == 100):
                datelist[num] = datelist[num] + 1

            # 算平均分
            hourStr = time.strftime("%H", timeArray)
            hour = int(hourStr)
            if hour >= 0 and hour < 2:
                list1.append(score)
                if score != 0:
                    submission[0] = submission[0] + 1
            elif hour >= 2 and hour < 4:
                list2.append(score)
                if score != 0:
                    submission[1] = submission[1] + 1
            elif hour >= 4 and hour < 6:
                list3.append(score)
                if score != 0:
                    submission[2] = submission[2] + 1
            elif hour >= 6 and hour < 8:
                list4.append(score)
                if score != 0:
                    submission[3] = submission[3] + 1
            elif hour >= 8 and hour < 10:
                list5.append(score)
                if score != 0:
                    submission[4] = submission[4] + 1
            elif hour >= 10 and hour < 12:
                list6.append(score)
                if score != 0:
                    submission[5] = submission[5] + 1
            elif hour >= 12 and hour < 14:
                list7.append(score)
                if score != 0:
                    submission[6] = submission[6] + 1
            elif hour >= 14 and hour < 16:
                list8.append(score)
                if score != 0:
                    submission[7] = submission[7] + 1
            elif hour >= 16 and hour < 18:
                list9.append(score)
                if score != 0:
                    submission[8] = submission[8] + 1
            elif hour >= 18 and hour < 20:
                list10.append(score)
                if score != 0:
                    submission[9] = submission[9] + 1
            elif hour >= 20 and hour < 2:
                list11.append(score)
                if score != 0:
                    submission[10] = submission[10] + 1
            elif hour >= 22 and hour <= 24:
                list12.append(score)
                if score != 0:
                    submission[1] = submission[1] + 1
    sum_submission = sum(submission)
    habit=''
    if sum_submission==0:
        habit='平稳完成'
        return habit
    elif mysum(datelist, 0, 20) / sum_submission >= 0.6:
        habit='提前完成'
    elif mysum(datelist, 30, 44) / sum_submission >= 0.6:
        habit='拖后完成'
    else:
        habit='平稳完成'
    return habit

# 计算某类题目的平均得分
def powervalue(cases, type):
    n = 0
    total_score = 0
    total_num=0
    if type=='字符串':
        total_num=17
    if type=='线性表':
        total_num=32
    if type=='数组':
        total_num=44
    if type=='查找算法':
        total_num=21
    if type=='数字操作':
        total_num=35
    if type=='树结构':
        total_num=28
    if type=='图结构':
        total_num=13
    if type=='排序算法':
        total_num=11
    for case in cases:
        if case["case_type"] == type:
            n = n + 1
            total_score = total_score + case["final_score"]
    # print(n)
    if n == 0:
        return 0
    else:
        average_score = total_score / n
        submitrate=n/total_num
        if submitrate>1:
            submitrate=1
        power_value=average_score*submitrate
        return power_value

#获取编程综合能力评分
def getaveragepower(user_id):
    value_of_string = powervalue(data[user_id]["cases"], "字符串")
    value_of_lineartable = powervalue(data[user_id]["cases"], "线性表")
    value_of_array = powervalue(data[user_id]["cases"], "数组")
    value_of_searchalgorithm = powervalue(data[user_id]["cases"], "查找算法")
    value_of_sigitaloperation = powervalue(data[user_id]["cases"], "数字操作")
    value_of_treestructure = powervalue(data[user_id]["cases"], "树结构")
    value_of_graphstructure = powervalue(data[user_id]["cases"], "图结构")
    value_of_sortingalgorithm = powervalue(data[user_id]["cases"], "排序算法")
    return (value_of_string+value_of_lineartable+value_of_array+value_of_searchalgorithm+value_of_sigitaloperation+
         value_of_treestructure+value_of_graphstructure+value_of_sortingalgorithm)/8

#计算、绘制能力图
def showpower(user_id):
    value_of_string = powervalue(data[user_id]["cases"], "字符串")
    value_of_lineartable = powervalue(data[user_id]["cases"], "线性表")
    value_of_array = powervalue(data[user_id]["cases"], "数组")
    value_of_searchalgorithm = powervalue(data[user_id]["cases"], "查找算法")
    value_of_sigitaloperation = powervalue(data[user_id]["cases"], "数字操作")
    value_of_treestructure = powervalue(data[user_id]["cases"], "树结构")
    value_of_graphstructure = powervalue(data[user_id]["cases"], "图结构")
    value_of_sortingalgorithm = powervalue(data[user_id]["cases"], "排序算法")
    matplotlib.rcParams['font.family'] = 'SimHei'
    matplotlib.rcParams['font.sans-serif'] = ['SimHei']
    lables = np.array(["字符串", "线性表", "数组", "查找算法", "数字操作", "树结构", "图结构", "排序算法"])
    nAttr = 8
    date = np.array(
        [value_of_string, value_of_lineartable, value_of_array, value_of_searchalgorithm, value_of_sigitaloperation,
         value_of_treestructure, value_of_graphstructure, value_of_sortingalgorithm])
    angles = np.linspace(0, 2 * np.pi, nAttr, endpoint=False)
    date = np.concatenate((date, [date[0]]))
    angles = np.concatenate((angles, [angles[0]]))
    fig = plt.figure(facecolor="white")
    plt.subplot(111, polar=True)
    plt.plot(angles, date, 'bo-', color='g', linewidth=2)
    plt.fill(angles, date, facecolor='g', alpha=0.25)
    plt.thetagrids(angles * 180 / np.pi, lables)
    plt.figtext(0.52, 0.95, 'python编程能力值雷达图', ha='center')
    plt.grid(True)
    plt.savefig('python_radar.JPG')
    plt.show()

def StudentPortrait(user_id):
    showpower(user_id)
    weaknessNum=searchweaknessNum(user_id)
    strongNum=searchstrongNum(user_id)
    weakness=searchweakness(user_id)
    strong=searchstrong(user_id)
    list1=[]
    list3=[]
    list4=[]
    list5=[]
    list6=[]
    if weaknessNum ==100:
        print("该同学几乎完成了所有题目，可以去试试帮助别的同学~")
    elif strongNum<=20:
        print("该同学的题目完成度很低，所以需要一个大神")
        print("为该同学推荐的id为：")
        GetTopStudent(list1)

    print("该同学的弱项是:"+weakness)
    print("该同学在这块的综合得分是:"+str(round(weaknessNum,2)))
    print("该同学的强项是:" +strong)
    print("该同学在这块的综合得分是:" + str(round(strongNum, 2)))
    for i in data:
        if searchweaknessNum(i)!=100:
            list2=[]
            res=powervalue(data[i]["cases"],weakness)
            if res >= 90:
                list2.append(data[i]["user_id"])
                list4.append(data[i]["user_id"])
                #list4用于匹配编程习惯
                list2.append(round(res,2))
            if list2!=[]:
                list3.append(list2)
    print("在"+weakness+"中，得分较高的几位id为：")
    print(list3)
    for i in list4:
        cpWeakness=searchweakness(str(i))
        cpWeaknessNum=searchweaknessNum(str(i))
        if powervalue(data[str(i)]["cases"],cpWeakness) < powervalue(data[user_id]["cases"],cpWeakness):
            list5.append(i)
    print("其中，CP的弱项正好为该同学强项的id为：")
    print(list5)
    st=habit(user_id,1)
    end=st+2
    print("该同学的做题效率最高的时间段为：" + str(st) + ":00 ~ " + str(end) + ":00")
    for i in list5:
        if habit(str(i),0) == st:
            list6.append(i)
    if list6 != []:
        print("因此，与该同学编程能力互补，且编程习惯相同的最佳的几位CP为：")
        print(list6)
    else:
        print("因此，与该同学编程能力互补，且编程习惯相同的最佳的几位CP为：")
        print(list5)
class astudent:
    def __init__(self):
        self.id = ''     # id
        self.power = 0     # 能力值
        self.habit = ''     # 做题习惯
def Overall_sample_analyze():
    students=[]
    for student in data:
        newstudent=astudent()
        newstudent.id=data[student]["user_id"]
        newstudent.power=getaveragepower((str)(data[student]["user_id"]))
        newstudent.habit=gethabit((str)(data[student]["user_id"]))
        students.append(newstudent)
    x1=0;x2=0;x3=0;x4=0;x5=0
    for student in students:
        if 0<=student.power<20:
            x1=x1+1
        if 20 <= student.power < 40:
            x2 = x2 + 1
        if 40<=student.power<60:
            x3=x3+1
        if 60<=student.power<80:
            x4=x4+1
        if 80<=student.power<100:
            x5=x5+1
    # 这两行代码解决 plt 中文显示的问题
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    waters = ('0-20', '20-40', '40-60', '60-80', '80-100')
    buy_number = [x1, x2, x3,x4, x5]
    plt.bar(waters, buy_number)
    plt.title('整体得分分布')
    plt.savefig('整体得分分布.JPG')
    plt.show()
    y1=0;y2=0;y3=0;y4=0;y5=0;y6=0
    for student in students:
        if student.power>=80 and student.habit == '提前完成':
            y1=y1+1
        if student.power < 80 and student.habit == '提前完成':
            y2=y2+1
        if student.power >= 80 and student.habit == '平稳完成':
            y3 = y3 + 1
        if student.power < 80 and student.habit == '平稳完成':
            y4=y4+1
        if student.power >= 80 and student.habit == '拖后完成':
            y5=y5+1
        if student.power < 80 and student.habit == '拖后完成':
            y6=y6+1
    X = np.arange(3)
    Y = [y1, y3, y5]
    Y1 = [y2, y4, y6]
    bar_width = 0.35
    tick_label = ["提前完成", "平稳完成", "拖后完成"]
    plt.bar(X, Y, bar_width, align="center", color="c", label="评分高于等于80", alpha=0.5)
    plt.bar(X + bar_width, Y1, bar_width, color="b", align="center", label="评分低于80", alpha=0.5)
    plt.xlabel("做题习惯")
    plt.ylabel("人数")
    plt.xticks(X + bar_width / 2, tick_label)
    plt.legend()
    plt.show()

#类型1为学生画像，2为整体样本研究
type=input("请选择研究类型：")
if(type=='1'):
    user_id = input("请输入学生id:")
    StudentPortrait(user_id)
if(type=='2'):
    Overall_sample_analyze()