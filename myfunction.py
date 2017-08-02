#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 09:58:06 2017

@author: bbr
"""
import urllib2
import sys
from xml.etree import ElementTree

def cimissread(stationid,element,timeRange,hourorDay=0):
"""
inputvar: one stationid, one meterological element, timeRange and 1 for 'hour'
0 for 'day', 0('day') is default.

output: array of cimiss data
'day' : year month day 'value'
'hour': year month day time 'value'
"""

# initial the element
    if hourorDay==0:
        dataSetName='SURF_CHN_MUL_DAY'
        var1=['Station_Id_d','Year','Mon','Day']
    else:
        dataSetName='SURF_CHN_MUL_HOR'
        var1=['Station_Id_d','Year','Mon','Day','Time']
    var=var1+element
    elements=','.join(var)
        
    baseUrl = 'http://10.226.89.17:8008/cimiss-web/api?userId=user_ssny&pwd=23333559\
&interfaceId=getSurfEleByTimeRangeAndStaID\
&dataCode=%s\
&elements=%s\
&timeRange=%s\
&staIds=%s\
&dataFormat=' % (dataSetName,elements,timeRange,stationId)

    dateFormat='xml'
	req = urllib2.Request(baseUrl + dataFormat)
	response = urllib2.urlopen(req)
	data = response.read()
	# print data
	root = ElementTree.fromstring(data)
	lst_node = root.getiterator("DS")

	for node in lst_node[0]:
		Station_Id_d.append(node.get('Station_Id_d'))
		Year.append(node.get('Year'))
		Mon.append(node.get('Mon'))
		Day.append(node.get('Day'))
		meElment.append(node.get(var_query[0]))

if __name__=="__main__":
    cimissread('54517','TEM_Avg','[20160101000000,20161231000000]')


