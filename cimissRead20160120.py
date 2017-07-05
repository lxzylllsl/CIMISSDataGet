# coding:utf8
'''
Created on 2015/12/30
@author:BBR
Introduction: 读取cimiss中的数据，并写成高鹰软件输出的格式
version: 0.1
'''

import os
import datetime
import urllib2
import json
import sys
import csv
from xml.etree import ElementTree
reload(sys)
sys.setdefaultencoding('utf8')

# def readini(filename):
#     M=open(filename,"r")
#     stationIds=[]
#     for line in M:
#     	stationIds.append(line.strip())
#     return stationIds


# stationId_all=readini(r'.\ini\StationID.txt')


timeRange='[20160101000000,20161231000000]'   #查询的时间段，根据需要修改
var_query=['WIN_D_Avg_2mi_C']     #'TEM_Avg','TEM_Max','TEM_Min','PRE_Time_2020']  #查询的变量，根据需要修改PRE_1h，Snow_Depth
dataCode='SURF_CHN_MUL_DAY'  #要查询的数据集，根据需要修改,更改此处的话，后面可能需要进行修改SURF_CHN_MUL_DAY、SURF_CHN_MUL_HOR

var1=['Station_Id_d','Year','Mon','Day']
var=var1+var_query
elements=','.join(var)
stationId_all=['59082','59116','59271','59280','59287','59288','59289','59293','59298',
               '59306','59312','59316','59462','59478','59480','59485','59488','59493','59501',
               '59658','59663','59664']
stationNums=len(stationId_all)  #len(stationId_all)
#headName=['年','月','日','蓟县','宝坻','武清','宁河','静海','西青','北辰','市区','东丽','津南','大港','汉沽','塘沽']
headName=['year','month','day']+stationId_all

Station_Id_d=[[] for i in range(stationNums)]
Year=[[] for i in range(stationNums)]
Mon=[[] for i in range(stationNums)]
Day=[[] for i in range(stationNums)]
TEM_Avg=[[] for i in range(stationNums)]

for s in range(0,stationNums):
	print s
	stationId=stationId_all[s]
	print stationId
	baseUrl = 'http://10.226.89.17:8008/cimiss-web/api?userId=user_ssny&pwd=23333559\
&interfaceId=getSurfEleByTimeRangeAndStaID\
&dataCode=%s\
&elements=%s\
&timeRange=%s\
&staIds=%s\
&dataFormat=' % (dataCode,elements,timeRange,stationId)

	dataFormat='xml'

	req = urllib2.Request(baseUrl + dataFormat)
	response = urllib2.urlopen(req)
	data = response.read()
	# print data
	root = ElementTree.fromstring(data)
	lst_node = root.getiterator("DS")

	for node in lst_node[0]:
		Station_Id_d[s].append(node.get('Station_Id_d'))
		Year[s].append(node.get('Year'))
		Mon[s].append(node.get('Mon'))
		Day[s].append(node.get('Day'))
		TEM_Avg[s].append(node.get(var_query[0]))

	# print TEM_Avg
	# write data to file
filename = var_query[0]+timeRange+'.csv'
print filename
f=file(filename,"w")
f.write('%s,' % (headName))
f.write('\n')
for d in range(0,len(Day[0])):
	f.write('%s,%s,%s,' %(Year[0][d],Mon[0][d],Day[0][d]))
	for z in range(0,stationNums):
		f.write('%s,' % (TEM_Avg[z][d]))
	f.write('\n')
f.close()
