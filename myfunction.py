#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 09:58:06 2017
@author: bbr
"""
import urllib2
import json

"""
inputvar: one stationid, one meterological element, timeRange and 1 for 'hour'
0 for 'day', 0('day') is default.
output: array of cimiss data
'day' : year month day 'value'
'hour': year month day time 'value'
"""

def cimissread(queryvar,hourorDay=0):

    stationid=queryvar[0]
    element=queryvar[1]
    timeRange=queryvar[2]
    print hourorDay
    print 'deal station '+stationid
# initial the element
    if hourorDay==0:
        dataSetName='SURF_CHN_MUL_DAY'
        var1=['Station_Id_d','Year','Mon','Day']
    else:
        dataSetName='SURF_CHN_MUL_HOR'
        var1=['Station_Id_d','Year','Mon','Day','Hour']
   
    var=var1+[element]
    elements=','.join(var)
        
    baseUrl = 'http://10.226.89.17:8008/cimiss-web/api?userId=user_ssny&pwd=23333559\
&interfaceId=getSurfEleByTimeRangeAndStaID\
&dataCode=%s\
&elements=%s\
&timeRange=%s\
&staIds=%s\
&dataFormat=' % (dataSetName,elements,timeRange,stationid)

    dataFormat='json'
    html = urllib2.urlopen(baseUrl + dataFormat)
    hjson= json.loads(html.read())
    data=hjson['DS']
    
# save data
    stationname=[]
    Year=[]
    Mon=[]
    Day=[]
    Time=[]
    meElement=[]
    
    if hourorDay==0:
        for index,line in enumerate(data):
            stationname.append(line['Station_Id_d'])
            Year.append(line['Year'])
            Mon.append(line['Mon'])
            Day.append(line['Day'])
            meElement.append(line[element])
        return Year,Mon,Day,meElement
    else:
        for index,line in enumerate(data):
            stationname.append(line['Station_Id_d'])
            Year.append(line['Year'])
            Mon.append(line['Mon'])
            Day.append(line['Day'])
            Time.append(line['Hour'])
            meElement.append(line[element])
        return Year,Mon,Day,Time,meElement

    
if __name__=="__main__":

    queryvar=['54517','TEM','[20161230000000,20161231000000]']
    [Year,Mon,Day,Time,meElement]=cimissread(queryvar,1)
    print Time,meElement
