#!/usr/bin/env python
# coding: utf-8

# - 데이터셋:
#     * 총 운항 기록 24/07/01~ 24/12/31
#     * 총 이상운항 기록 24/07/01 ~ 24/12/31
# - 가설 : 기상/기술 조건에 의한 항공지연이 발생하면, 추가적인 접속/연결 지연 발생률이 증가할 것이다.
# - 가설 : 기술적 문제로 인한 지연은 다른 항공편에 미치는 영향이 크며, 연쇄 지연의 발생 확률이 기상 조건에 의한 지연보다 높다.
# 검증 목표 : 총 운항기록중 시간대별로 여객기와 화물수송기를 분류, 최초지연과 그 이후 이어지는 지연사건이 몇건이나 되는지 확인하여, 지연사고 최초발생과 그 이후 생기는 연결/접속 지연사고의 관계성을 밝힘
# 
# 

# In[109]:


## [1] 모듈 로딩
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

import utils


# In[110]:


## 데이터 로딩및 확인
dataDF07 = pd.read_excel('./DATA/normal/항공기출도착현황240701.xlsx')
dataDF08 = pd.read_excel('./DATA/normal/항공기출도착현황240801.xlsx')
dataDF09 = pd.read_excel('./DATA/normal/항공기출도착현황240901.xlsx')
dataDF10 = pd.read_excel('./DATA/normal/항공기출도착현황241001.xlsx')
dataDF11 = pd.read_excel('./DATA/normal/항공기출도착현황241101.xlsx')
dataDF12 = pd.read_excel('./DATA/normal/항공기출도착현황241201.xlsx')

# 계획시간 별로 소트하여 지연 현황을 찾고, 해당 지연 원인을 abnormal 폴더에서 해당날짜와 같은 날짜에서 찾아오기


# In[111]:


dataDF07.tail(20)


# In[112]:


dataDF07.info()


# In[113]:


# 데이터 분류방법 / 조건문  / groupby
dataDF07 = dataDF07.sort_values(['날짜', '계획시간'])
dataDF07.head()
# dataDF07.loc[(dataDF07['현황']=='지연')]
dataDF07.loc[:,'현황']
(dataDF07['현황'] == '지연').idxmax()


# In[114]:


dataDF07['현황'] == '지연'


# In[57]:





# In[115]:


""" def findlate(df, end_idx):
    # if end_idx == len(df.index):
    
    first_idx = (df.loc[end_idx:,'현황'] == '지연').idxmax()
    first_not_idx = (df.loc[first_idx:,'현황'] != '지연').idxmax()
    print('first_idx = ', first_idx)
    print('first_not_idx = ', first_not_idx)
    
    lateCount = 0 
    
    for n in np.arange(first_idx, first_not_idx):
        lateDate = df.loc[n,'날짜']
        lateName = df.loc[n,'편명']
        lateDay = pd.read_csv(f"./DATA/abnormal/filtered_data_{lateDate}.csv")
        lateReason = lateDay.loc[(lateDay['항공편명'] == lateName), '비정상원인']
        # print(lateReason, lateReason.dtype)
        if lateReason.str.contains('연결').any():         
            lateCount += 1
   
    if lateDate:    
        if (lateCount, lateDate) in lateDF.index and lateDate in lateDF.columns:
            lateDF.loc[lateCount, lateDate] += 1
        else:
            lateDF.loc[lateCount, lateDate] = 1
    
    # print('end_idx = ', first_not_idx)
    if first_not_idx >= len(dataDF07.index):
        print( lateDF )
        quit
    
    return findlate(df, first_not_idx)
         """


# In[116]:


def findlate(df, start_idx):
    end_idx = len(df.index)
    lateDF = pd.DataFrame(index=range(30))
   
    while start_idx < end_idx:
        first_idx = (df.loc[start_idx:, '현황'] == '지연').idxmax()
        lateDate = df.loc[first_idx, '날짜']
        lateName = df.loc[first_idx, '편명']
        lateDay = pd.read_csv(f"./DATA/abnormal/filtered_data_{lateDate}.csv")
        lateReason = lateDay.loc[(lateDay['항공편명'] == lateName), '비정상원인']
        if not lateReason.str.contains('항공기 연결').any(): 
            first_not_idx = (df.loc[first_idx:, '현황'] != '지연').idxmax()
            
            # print('first_idx = ', first_idx)
            # print('first_not_idx = ', first_not_idx)

            lateCount = 0 

            for n in np.arange(first_idx, first_not_idx):
                lateDate = df.loc[n, '날짜']
                lateName = df.loc[n, '편명']
                lateDay = pd.read_csv(f"./DATA/abnormal/filtered_data_{lateDate}.csv")
                lateReason = lateDay.loc[(lateDay['항공편명'] == lateName), '비정상원인']
                
                if lateReason.str.contains('연결').any() | lateReason.str.contains('접속').any():         
                    lateCount += 1

            if lateDate in lateDF.columns:  # lateDate 변수가 정의되었는지 확인
                # print(lateCount, lateDate,'b')
                lateDF.loc[lateCount, lateDate] += 1
            else:
                # print(lateCount, lateDate, 'a')
                lateDF[lateDate] = [0] * len(lateDF)
                lateDF.loc[lateCount, lateDate] = 1
            
            if first_idx >= first_not_idx:
                txtname = str(lateDate)[4:6]
                globals()[f"lateDF{txtname}"] = lateDF.copy()
                print(f"lateDF{txtname} 생성")
                break  # 재귀 대신 종료

            start_idx = first_not_idx  # 다음 반복을 위해 업데이트
        else:
            start_idx = first_idx+1
    
    txtname = str(lateDate)[4:6]
    globals()[f"lateDF{txtname}"] = lateDF.copy()
    print(f"lateDF{txtname} 생성")


# In[117]:


findlate(dataDF07,0)
findlate(dataDF08,0)
findlate(dataDF09,0)
findlate(dataDF10,0)
findlate(dataDF11,0)
findlate(dataDF12,0)


# In[118]:


lateDF24sh = pd.DataFrame({'7월 합계':lateDF07.sum(axis=1),
                          '8월 합계':lateDF08.sum(axis=1),
                          '9월 합계':lateDF09.sum(axis=1),
                          '10월 합계':lateDF10.sum(axis=1),
                          '11월 합계':lateDF11.sum(axis=1),
                          '12월 합계':lateDF12.sum(axis=1)})
lateDF24sh.head(20)


# In[17]:





# In[119]:


def findlate_weather(df, start_idx):
    end_idx = len(df.index)
    lateDF = pd.DataFrame(index=range(30))
    
    # print(len(df.index))
    while start_idx < end_idx:
        # print(start_idx, end_idx)
        first_idx = (df.loc[start_idx:, '현황'] == '지연').idxmax()
        lateDate = df.loc[first_idx, '날짜']
        lateName = df.loc[first_idx, '편명']
        lateDay = pd.read_csv(f"./DATA/abnormal/filtered_data_{lateDate}.csv")
        lateReason = lateDay.loc[(lateDay['항공편명'] == lateName), '비정상원인']
        if lateReason.str.contains('기상').any(): 
            first_not_idx = (df.loc[first_idx:, '현황'] != '지연').idxmax()
            
            # print('first_idx = ', first_idx)
            # print('first_not_idx = ', first_not_idx)

            lateCount = 0 

            for n in np.arange(first_idx, first_not_idx):
                lateDate = df.loc[n, '날짜']
                lateName = df.loc[n, '편명']
                lateDay = pd.read_csv(f"./DATA/abnormal/filtered_data_{lateDate}.csv")
                lateReason = lateDay.loc[(lateDay['항공편명'] == lateName), '비정상원인']
                
                if lateReason.str.contains('연결').any() | lateReason.str.contains('접속').any():         
                    lateCount += 1

            if lateDate in lateDF.columns:  # lateDate 변수가 정의되었는지 확인
                # print(lateCount, lateDate,'b')
                lateDF.loc[lateCount, lateDate] += 1
            else:
                
                lateDF[lateDate] = [0] * len(lateDF)
                lateDF.loc[lateCount, lateDate] = 1
            
            if first_idx >= first_not_idx or first_not_idx == len(df.index):
                # print(lateCount, lateDate, 'a')
                txtname = str(lateDate)[4:6]
                globals()[f"lateDFwea{txtname}"] = lateDF.copy()
                print(f"lateDFwea{txtname} 생성")
                break  # 재귀 대신 종료

            start_idx = first_not_idx  # 다음 반복을 위해 업데이트
        else:
            start_idx = first_idx+1
            
            
    txtname = str(lateDate)[4:6]
    globals()[f"lateDFwea{txtname}"] = lateDF.copy()
    print(f"lateDFwea{txtname} 생성")


# In[120]:


findlate_weather(dataDF07,0)
findlate_weather(dataDF08,0)
findlate_weather(dataDF09,0)
findlate_weather(dataDF10,0)
findlate_weather(dataDF11,0)
findlate_weather(dataDF12,0)


# In[121]:


lateDF24shwea = pd.DataFrame({'7월 합계':lateDFwea07.sum(axis=1),
                          '8월 합계':lateDFwea08.sum(axis=1),
                          '9월 합계':lateDFwea09.sum(axis=1),
                          '10월 합계':lateDFwea10.sum(axis=1),
                          '11월 합계':lateDFwea11.sum(axis=1),
                          '12월 합계':lateDFwea12.sum(axis=1)})


# In[122]:


lateDF24shwea


# In[123]:


def findlate_ATFM(df, start_idx):
    end_idx = len(df.index)
    lateDF = pd.DataFrame(index=range(30))
    
    # print(len(df.index))
    while start_idx < end_idx:
        # print(start_idx, end_idx)
        first_idx = (df.loc[start_idx:, '현황'] == '지연').idxmax()
        lateDate = df.loc[first_idx, '날짜']
        lateName = df.loc[first_idx, '편명']
        lateDay = pd.read_csv(f"./DATA/abnormal/filtered_data_{lateDate}.csv")
        lateReason = lateDay.loc[(lateDay['항공편명'] == lateName), '비정상원인']
        if lateReason.str.contains('ATFM|운항통제|공항시설',).any(): 
            first_not_idx = (df.loc[first_idx:, '현황'] != '지연').idxmax()
            
            # print('first_idx = ', first_idx)
            # print('first_not_idx = ', first_not_idx)

            lateCount = 0 

            for n in np.arange(first_idx, first_not_idx):
                lateDate = df.loc[n, '날짜']
                lateName = df.loc[n, '편명']
                lateDay = pd.read_csv(f"./DATA/abnormal/filtered_data_{lateDate}.csv")
                lateReason = lateDay.loc[(lateDay['항공편명'] == lateName), '비정상원인']
                
                if lateReason.str.contains('연결').any() | lateReason.str.contains('접속').any():         
                    lateCount += 1

            if lateDate in lateDF.columns:  # lateDate 변수가 정의되었는지 확인
                # print(lateCount, lateDate,'b')
                lateDF.loc[lateCount, lateDate] += 1
            else:
                
                lateDF[lateDate] = [0] * len(lateDF)
                lateDF.loc[lateCount, lateDate] = 1
            
            if first_idx >= first_not_idx or first_not_idx == len(df.index):
                # print(lateCount, lateDate, 'a')
                txtname = str(lateDate)[4:6]
                globals()[f"lateDFatfm{txtname}"] = lateDF.copy()
                print(f"lateDFatfm{txtname} 생성")
                break  # 재귀 대신 종료

            start_idx = first_not_idx  # 다음 반복을 위해 업데이트
        else:
            start_idx = first_idx+1
            
            
    txtname = str(lateDate)[4:6]
    globals()[f"lateDFatfm{txtname}"] = lateDF.copy()
    print(f"lateDFatfm{txtname} 생성")


# In[124]:


findlate_ATFM(dataDF07,0)
findlate_ATFM(dataDF08,0)
findlate_ATFM(dataDF09,0)
findlate_ATFM(dataDF10,0)
findlate_ATFM(dataDF11,0)
findlate_ATFM(dataDF12,0)


# In[125]:


lateDF24shATFM = pd.DataFrame({'7월 합계':lateDFatfm07.sum(axis=1),
                          '8월 합계':lateDFatfm08.sum(axis=1),
                          '9월 합계':lateDFatfm09.sum(axis=1),
                          '10월 합계':lateDFatfm10.sum(axis=1),
                          '11월 합계':lateDFatfm11.sum(axis=1),
                          '12월 합계':lateDFatfm12.sum(axis=1)})


# In[126]:


lateDF24shATFM

