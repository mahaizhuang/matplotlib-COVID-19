import matplotlib.pyplot as plt
import matplotlib.image as mping
import xlrd 
import pprint
import numpy as np
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['font.family']='sans-serif'
#
book = xlrd.open_workbook(r'C:\\Users\csjmj\Desktop\武汉肺炎趋势预测.xlsx')
sheet = book.sheet_by_name('Sheet1')
#
a1 = '河南省郑州市新型肺炎感染确诊人数时间变化'
a2 = '河南省新型肺炎感染确诊人数时间变化'
a3 = '河南省新型肺炎接受医学观察人数时间变化'
#
list1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34]
list2 = []
list3 = []
list4 = [] 
list6 = []
list7 = []
list8 = []
list9 = []
list5 = ['2020/1/23','2020/1/24','2020/1/25','2020/1/26','2020/1/27','2020/1/28','2020/1/29','2020/1/30','2020/1/31',
'2020/2/1','2020/2/2','2020/2/3','2020/2/4','2020/2/5','2020/2/6','2020/2/7','2020/2/8','2020/2/9','2020/2/10',
'2020/2/11','2020/2/12','2020/2/13','2020/2/14','2020/2/15','2020/2/16','2020/2/17','2020/2/18','2020/2/19',
'2020/2/20','2020/2/21','2020/2/22','2020/2/23','2020/2/24','2020/2/25']
r1 = 2
r2 = 2 
r3 = 2
r6 = 2
r7 = 2 
r8 = 2 
r9 = 2
r4 = len(list1)-1
r5 = len(list1)+1
print(r4)
for i in range(8):
    if i == 1:
        while r1 <=r5:
            row1 = sheet.cell(i,r1).value
            list2.append(row1)
            r1 = r1 + 1 
    elif i == 2:
        while r2 <=r5:
            row1 = sheet.cell(i,r2).value
            list3.append(row1)
            r2 = r2 + 1
    elif i == 3:
        while r3 <=r5:
            row1 = sheet.cell(i,r3).value
            list4.append(row1)
            r3 = r3 + 1 
    elif i == 4: 
        while r6 <=r5:
            row1 = sheet.cell(i,r6).value
            list6.append(row1)
            r6 = r6 + 1 
    elif i == 5: 
        while r7 <=r5:
            row1 = sheet.cell(i,r7).value
            list7.append(row1)
            r7 = r7 + 1 
    elif i == 6: 
        while r8 <=r5:
            row1 = sheet.cell(i,r8).value
            list8.append(row1)
            r8 = r8 + 1 
    elif i == 7: 
        while r9 <=r5:
            row1 = sheet.cell(i,r9).value
            list9.append(row1)
            r9 = r9 + 1 
              
print(list1,list2,list3,list4,list5,list6,list7,list8,list9)
#
ax1 = plt.figure(num=1,facecolor='khaki',frameon=True)
x = list1
y = list2
ax1.add_axes([0.06,0.1,0.89,0.85])
ax1 = plt.plot(x,y,marker='o',color='yellow',label=a1,linestyle='--',mfc='red',mec='red',ms=4)
ax1 = plt.legend(fontsize=8)
ax1 = plt.title(a1,color='k',fontsize=12,loc='center')
ax1 = plt.xlim(0,r5)
ax1 = plt.ylim(0,200)
ax1 = plt.xlabel('日期',fontdict=None,labelpad=None,color='plum',fontsize=12)
ax1 = plt.ylabel('相关人数',fontdict=None,labelpad=None,color='plum',fontsize=12)
ax1 = plt.axhspan(0,200,facecolor='seashell')
#
i1 = 0
while i1 <=r4:
    ax1 = plt.text(list1[i1],list2[i1],list2[i1],fontsize=10,color='k',horizontalalignment='center',verticalalignment='bottom',rotation=45)
    i1 = i1 + 1
#
x_ticks=np.linspace(1,r5,r5)
y_ticks=np.linspace(0,200,21)
ax1 = plt.xticks(x_ticks,list5,rotation=60)
ax1 = plt.yticks(y_ticks)
ax1 = plt.show()
#


ax2 = plt.figure(num=2,facecolor='khaki',frameon=True)
x = list1
y = list3
ax2.add_axes([0.06,0.1,0.89,0.85])
ax2 = plt.plot(x,y,marker='o',color='yellow',label=a2,linestyle='--',mfc='red',mec='red',ms=4,)
ax2 = plt.legend(fontsize=8)
ax2 = plt.title(a2,color='k',fontsize=12,loc='center')
ax2 = plt.xlim(0,r5)
ax2 = plt.ylim(0,1500)
ax2 = plt.xlabel('日期',fontdict=None,labelpad=None,color='k',fontsize=12)
ax2 = plt.ylabel('相关人数',fontdict=None,labelpad=None,color='plum',fontsize=12)
ax2 = plt.axhspan(0,1500,facecolor='lavender')
#
i1 = 0
while i1 <=r4:
    ax2 = plt.text(list1[i1],list3[i1],list3[i1],fontsize=10,color='k',horizontalalignment='center',verticalalignment='bottom',rotation=45)
    i1 = i1 + 1
#
x_ticks=np.linspace(1,r5,r5)
y_ticks=np.linspace(0,1500,21)
ax2 = plt.xticks(x_ticks,list5,rotation=60)
ax2 = plt.yticks(y_ticks)
ax2 = plt.show()
#


ax3 = plt.figure(num=3,facecolor='beige',frameon=True)
x = list1
y = list9
ax3.add_axes([0.06,0.1,0.89,0.85])
ax3 = plt.plot(x,y,marker='o',color='yellow',label=a3,linestyle='--',mfc='red',mec='red',ms=4)
ax3 = plt.legend(fontsize=8)
ax3 = plt.title(a3,color='k',fontsize=12,loc='center')
ax3 = plt.xlim(0,r5)
ax3 = plt.ylim(0,20000)
ax3 = plt.xlabel('日期',fontdict=None,labelpad=None,color='plum',fontsize=12)
ax3 = plt.ylabel('相关人数',fontdict=None,labelpad=None,color='plum',fontsize=12)
ax3 = plt.axhspan(0,20000,facecolor='peachpuff')
#
i1 = 0
while i1 <=r4:
    ax3 = plt.text(list1[i1],list9[i1],list9[i1],fontsize=10,color='k',horizontalalignment='center',verticalalignment='bottom',rotation=45)
    i1 = i1 + 1
#
x_ticks=np.linspace(1,r5,r5)
y_ticks=np.linspace(0,20000,21)
ax3 = plt.xticks(x_ticks,list5,rotation=60)
ax3 = plt.yticks(y_ticks)
ax3 = plt.show()
#
