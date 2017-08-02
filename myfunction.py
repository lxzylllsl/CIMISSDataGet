#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 09:58:06 2017

@author: bbr
"""

def cimissread(stationid,element,timeRange,hourorDay=0):
"""
inputvar: one stationid, one meterological element, timeRange and 1 for 'hour'
0 for 'day', 0('day') is default.

output: array of cimiss data
'day' : year month day 'value'
'hour': year month day time 'value'

"""    
    if hourorDay==0:
        dataSetName='SURF_CHN_MUL_DAY'
    else:
        dataSetName='SURF_CHN_MUL_HOR'
        
    baseUrl = 'http://10.226.89.17:8008/cimiss-web/api?userId=user_ssny&pwd=23333559\
&interfaceId=getSurfEleByTimeRangeAndStaID\
&dataCode=%s\
&elements=%s\
&timeRange=%s\
&staIds=%s\
&dataFormat=' % (dataSetName,element,timeRange,stationId)