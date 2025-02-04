#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd                     # 데이터 분석 및 전처리용 모듈
import numpy as np                      # 배열(array)을 지원하는 파이썬 패키지

import streamlit as st
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt         # 데이터 시각화 즉, 그래프 관련 모듈 
import utils                            # 데이터확인용 


# In[2]:


# !pip install streamlit


# In[3]:


data = pd.read_csv('../DATA/titanic.csv')
ttDF = pd.DataFrame(data)
utils.setHangulFont()


# In[4]:


st.title(
    '데이터분석 및 시각화 - 타이타닉 호 승객 목록'
)
st.write(
    '''
    1. 데이터셋 : titanic.csv 
    2. 데이터 분석 방법 : 확증적 분석 
    2-1 가설 : 아메리칸 드림을 꿈꾸며 탄 독신 남성이 정말로 많았는가?
    2-1-1 그렇다면 그들의 사망율은 얼마나 높은가?
    2-2 가설 : 독신 남성을 제외한 나머지 인원의 수는 얼마나 되는가?
    2-2-1 그들의 생존율은 어떠하였는가?
    
    3. 목표 데이터: who, adult_male, alone
    4. feature/attribute: 나머지
    '''
)
ttDF.head(5)
st.divider()


# In[5]:


st.header(
   '[1] 모듈 로딩 및 데이터 준비'
)
st.code(
'''python
import pandas as pd                     # 데이터 분석 및 전처리용 모듈
import numpy as np                      # 배열(array)을 지원하는 파이썬 패키지

import streamlit as st
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt         # 데이터 시각화 즉, 그래프 관련 모듈 
import utils                            # 데이터확인용 


''')
st.divider()


# In[6]:


st.header(
   '[2] 데이터 준비'
)
st.code(
'''python
D_FILE = '../DATA/titanic.csv'
data1 = pd.read_csv(D_FILE)
ttDF = pd.DataFrame(data1)

''')
st.divider()


# In[7]:


st.header(
   '[3] 데이터 확인 및 전처리'
)
col1, col2 = st.columns(2)
with col1:
    st.code(
        '''
    ttDF.head(3)                   # 데이터확인용 
    ''')
    ttDF.head(3) 

    st.code(
        '''
    ttDF.info()                  # 데이터확인용 
    ''')
    ttDF.info()

    st.code(
        '''
    utils.printUniqueValue(ttDF)                  # 데이터확인용 
    ''')
    st.write(
    {utils.printUniqueValue(ttDF)}
    )
with col2:
    fig, ax = plt.subplots(figsize=(4, 8))
    utils.returnUniqueValue(ttDF)
    
st.divider()


# In[8]:


st.write('''
ttDF.isna().sum()
deck 는 688/891 이 nan이므로 데이터의 가치가 없음.''')
st.code(
'''
ttDF = ttDF.drop(columns='deck').copy()
tdDF = ttDF[ttDF['survived']==0]
utils.printUniqueValue(tdDF)''')


# age를 살펴보니 25%가량의 nan 데이터 확인
# 범위가 다양하게 퍼져있고, 특징이 보이지 않아 삭제하기 보단 따로 분류하여
# 미상 그룹을 만들기로 함.

# In[9]:


# 21세 기준이므로
# 21세 미만, 21~30, 31~40, 41~50, 51~60, 그이상 으로 하여 6가지분류로 그룹화
bins = [0, 21, 30, 40, 50, 60, float('inf')]
labels = ['21under', '20대', '30대', '40대', '50대', '60over']
ttDF['age_group'] = pd.cut(ttDF['age'], bins=bins, labels=labels, right=False)

# 위에서는 범위로 지정하였기 때문에 nan 값만을 따로 지정할수 없음
# 따로 범주를 추가하고, 데이터에도 별개로 처리
ordered_labels = ['missing', '21under', '20대', '30대', '40대', '50대', '60over']
ttDF['age_group'] = pd.Categorical(ttDF['age_group'], categories=ordered_labels, ordered=True)


ttDF['age_group'] = ttDF['age_group'].fillna('missing')
ttDF['age_group'].isna().sum()

ttDFama = ttDF[(ttDF['adult_male'] == True) & (ttDF['alone'] == True)]
ttDFama['class'].value_counts()
ttDFama['age'].isna().sum()
ttDFama['age'].min()
ttDFama['age'].max()
# 16세 데이터가 포함됨을 확인 
# 조사해보니 21세가 기준임을 확인.
# 21세 미만이며 성인남성으로 분류된 경우가 63건.
# age 분류의 정리가 필요.
ttDF[(ttDF['age'] < 21) & (ttDF['adult_male']==True)].count()  # 63
# ttDF[(ttDF['age'] < 21)].count()      # 180

ttDFama['age_group'].isna().sum()

st.code('''
# 21세 기준이므로
# 21세 미만, 21~30, 31~40, 41~50, 51~60, 그이상 으로 하여 6가지분류로 그룹화
bins = [0, 21, 30, 40, 50, 60, float('inf')]
labels = ['21under', '20대', '30대', '40대', '50대', '60over']
ttDF['age_group'] = pd.cut(ttDF['age'], bins=bins, labels=labels, right=False)

# 위에서는 범위로 지정하였기 때문에 nan 값만을 따로 지정할수 없음
# 따로 범주를 추가하고, 데이터에도 별개로 처리
ordered_labels = ['missing', '21under', '20대', '30대', '40대', '50대', '60over']
ttDF['age_group'] = pd.Categorical(ttDF['age_group'], categories=ordered_labels, ordered=True)


ttDF['age_group'] = ttDF['age_group'].fillna('missing')
ttDF['age_group'].isna().sum()
    
ttDFama = ttDF[(ttDF['adult_male'] == True) & (ttDF['alone'] == True)]
ttDFama['class'].value_counts()
ttDFama['age'].isna().sum()
ttDFama['age'].min()
ttDFama['age'].max()
# 16세 데이터가 포함됨을 확인 
# 조사해보니 21세가 기준임을 확인.
# 21세 미만이며 성인남성으로 분류된 경우가 63건.
# age 분류의 정리가 필요.
ttDF[(ttDF['age'] < 21) & (ttDF['adult_male']==True)].count()  # 63
# ttDF[(ttDF['age'] < 21)].count()      # 180

ttDFama['age_group'].isna().sum()        
                
'''    
)
st.divider()


# In[10]:


# ttDF['age_group'].value_counts().values


# In[ ]:


col1, col2 = st.columns(2)
with col1:
        
        st.write('각 나이대별로 age 그룹 분리. ')        
        st.write(ttDF['age_group'].value_counts())

with col2:
        plt.figure(figsize=(10,6))
        # ttDF['age_group'].value_counts()
        plt.pie(ttDF['age_group'].value_counts().values, labels = ttDF['age_group'].value_counts().index,
                autopct='%1.1f%%', startangle=90)
        plt.title('age_group - all', fontdict={'size':'large'})
        st.pyplot(plt)

st.divider()


# In[12]:


ttDF.loc[(ttDF['age_group'] == '21under') & (ttDF['sex'] == 'female'), 'adult_male'] = False
ama = (ttDF[(ttDF['alone']==True)&(ttDF['age']>21)&(ttDF['sex']=='male')]['class'].value_counts())

col1, col2 = st.columns(2)

with col1:
    st.write('''전체 891명 중, 
             단독으로 탑승한 성인남성은 242명''')
    st.write(ama)
    
with col2:
    #성인 남성, 단독 총 410
    # 탑승항별
    plt.figure(figsize=(12,6))
    agg_count=ttDFama['alive'].value_counts()
    # xData = agg_count.index
    yData2 = agg_count.values
    print(yData2.shape)

    plt.pie(yData2, labels=agg_count.index, autopct='%1.1f%%', startangle=90)

    plt.title( 'adult_male & alone - alive ', fontdict={'size':'large'})

    st.pyplot(plt)


st.divider()


# In[13]:


# [3-1] 시각화
#성인 남성, 단독 총 410
#연령대별 분포.
plt.figure(figsize=(12,6))
ttDFama['age_group'] = pd.Categorical(ttDFama['age_group'], categories=labels, ordered=True)
agg_count=ttDFama['age_group'].value_counts()
agg_count = agg_count.reindex(labels, fill_value=0)
xData = agg_count.index
yData1 = ''
yData2 = agg_count.values
print(xData.shape, yData2.shape)
# print(ttDFama['age_group'].dtype)

for i in range(len(xData)):
    plt.text(xData[i], yData2[i] + 1, str(yData2[i]), ha='center', va='bottom')

plt.title( 'adult_male & alone - age_group')
plt.bar(xData,yData2)
st.pyplot(plt)

st.divider()


# In[14]:


st.code('''
ttDFamay = ttDFama.loc[(ttDFama['alive']=='yes'),'age_group']
ttDFaman = ttDFama.loc[(ttDFama['alive']=='no'),'age_group']

plt.figure(figsize=(12,6))
ttDFamay = pd.Categorical(ttDFamay, categories=labels, ordered=True)
agg_count1 = ttDFamay.value_counts()
agg_count1 = agg_count1.reindex(labels, fill_value=0)

ttDFaman = pd.Categorical(ttDFaman, categories=labels, ordered=True)
agg_count2 = ttDFaman.value_counts()
agg_count2 = agg_count2.reindex(labels, fill_value=0)

xData1 = agg_count1.index
xData2 = agg_count2.index
yData1 = agg_count1.values
yData2 = agg_count2.values
print(xData1.shape,yData1.shape, yData2.shape)
# print(ttDFama['age_group'].dtype)
width=0.2
xData1_num = np.arange(len(xData1))
plt.bar(xData1_num-width,yData1, width=0.4, label='yes')
plt.bar(xData1_num+width,yData2, width=0.4, label='no')


for i in range(len(xData1)):
    plt.text(xData1_num[i]-width, yData1[i] + 0.5, str(yData1[i]), ha='center', va='bottom')
for i in range(len(xData1)):
    plt.text(xData1_num[i]+width, yData2[i] + 0.5, str(yData2[i]), ha='center', va='bottom')
plt.xticks(xData1_num, xData1)
plt.title( 'adult_male & alone - age_group')
plt.legend()
st.pyplot(plt)
''')
ttDFamay = ttDFama.loc[(ttDFama['alive']=='yes'),'age_group']
ttDFaman = ttDFama.loc[(ttDFama['alive']=='no'),'age_group']

plt.figure(figsize=(12,6))
ttDFamay = pd.Categorical(ttDFamay, categories=labels, ordered=True)
agg_count1 = ttDFamay.value_counts()
agg_count1 = agg_count1.reindex(labels, fill_value=0)

ttDFaman = pd.Categorical(ttDFaman, categories=labels, ordered=True)
agg_count2 = ttDFaman.value_counts()
agg_count2 = agg_count2.reindex(labels, fill_value=0)

xData1 = agg_count1.index
xData2 = agg_count2.index
yData1 = agg_count1.values
yData2 = agg_count2.values
print(xData1.shape,yData1.shape, yData2.shape)
# print(ttDFama['age_group'].dtype)
width=0.2
xData1_num = np.arange(len(xData1))
plt.bar(xData1_num-width,yData1, width=0.4, label='yes')
plt.bar(xData1_num+width,yData2, width=0.4, label='no')


for i in range(len(xData1)):
    plt.text(xData1_num[i]-width, yData1[i] + 0.5, str(yData1[i]), ha='center', va='bottom')
for i in range(len(xData1)):
    plt.text(xData1_num[i]+width, yData2[i] + 0.5, str(yData2[i]), ha='center', va='bottom')
plt.xticks(xData1_num, xData1)
plt.title( 'adult_male & alone - age_group')
plt.legend()
st.pyplot(plt)

st.divider()


# In[15]:


plt.figure(figsize=(12,6))
ttDFamay = pd.Categorical(ttDFamay, categories=labels, ordered=True)
agg_count1 = ttDFamay.value_counts()
agg_count1 = agg_count1.reindex(labels, fill_value=0)

ttDFaman = pd.Categorical(ttDFaman, categories=labels, ordered=True)
agg_count2 = ttDFaman.value_counts()
agg_count2 = agg_count2.reindex(labels, fill_value=0)

xData1 = agg_count1.index
xData2 = agg_count2.index
yData1 = agg_count1.values
yData2 = agg_count2.values
print(xData1.shape,yData1.shape, yData2.shape)
# print(ttDFama['age_group'].dtype)

plt.plot(xData1,yData2, 'o-', label='no')
plt.plot(xData1,yData1, 'o-', label='yes')

plt.bar(xData1,yData2, width=0.4, label='no')
plt.bar(xData1,yData1, width=0.4, label='yes')


for i in range(len(xData1)):
    plt.text(xData1[i], yData1[i] + 0.5, str(yData1[i]), ha='center', va='bottom')
for i in range(len(xData1)):
    plt.text(xData1[i], yData2[i] + 0.5, str(yData2[i]), ha='center', va='bottom')
plt.xticks(xData1)
plt.title( 'adult_male & alone - age_group')
plt.legend()
st.pyplot(plt)

st.divider()


# In[16]:


plt.figure(figsize=(12,6))
agg_count=ttDFama['embark_town'].value_counts()
xData = agg_count.index
yData2 = agg_count.values
print(xData.shape, yData2.shape)

# print(ttDFama['embark_town'].dtype)

for i in range(len(xData)):
    plt.text(xData[i], yData2[i], str(yData2[i]), ha='center', va='bottom')

plt.title('adult_male & alone - embark_town')
plt.bar(xData,yData2)
st.pyplot(plt)

st.divider()


# In[17]:


plt.figure(figsize=(12,6))
agg_count=ttDFama['pclass'].value_counts()
xData = agg_count.index
yData2 = agg_count.values
print(xData.shape, yData2.shape)

# print(ttDFama['pclass'].dtype)

for i in range(len(xData)):
    plt.text(xData[i], yData2[i], str(yData2[i]), ha='center', va='bottom')

plt.title('adult_male & alone -pclass')
plt.bar(xData,yData2)
st.pyplot(plt)

st.divider()


# In[18]:


plt.figure(figsize=(12,6))
agg_count1=ttDFama.loc[(ttDFama['alive']=='yes'),'pclass'].value_counts()
agg_count2=ttDFama.loc[(ttDFama['alive']=='no'),'pclass'].value_counts()

xData = agg_count1.index
yData1 = agg_count1.values
yData2 = agg_count2.values
print(xData.shape, yData2.shape)

width = 0.15
plt.bar(xData-width,yData1, width=0.3, label='yes')
plt.bar(xData+width,yData2, width=0.3, label='no')
# print(ttDFama['pclass'].dtype)

for i in range(len(xData)):
    plt.text(xData[i]-width, yData1[i], str(yData1[i]), ha='center', va='bottom')
    plt.text(xData[i]+width, yData2[i], str(yData2[i]), ha='center', va='bottom')
plt.legend()
plt.title('adult_male & alone - pclass')
plt.xticks(agg_count1.index)
st.pyplot(plt)

st.divider()


# In[19]:


ttDFnama = ttDF.loc[(ttDF['alone']==False) | (ttDF['adult_male']==False)]

plt.figure(figsize=(12,6))
agg_count=ttDFnama['alive'].value_counts()
# xData = agg_count.index
yData2 = agg_count.values
print(yData2.shape)

plt.pie(yData2, labels=agg_count.index, autopct='%1.1f%%', startangle=90)

plt.title( 'not (adult_male & alone) - alive ')

st.pyplot(plt)
st.divider()


# In[20]:


ttDFnamay = ttDFnama.loc[(ttDFnama['alive']=='yes'),'age_group']
ttDFnaman = ttDFnama.loc[(ttDFnama['alive']=='no'),'age_group']


plt.figure(figsize=(12,6))
ttDFnamay = pd.Categorical(ttDFnamay, categories=labels, ordered=True)
agg_count1 = ttDFnamay.value_counts()
agg_count1 = agg_count1.reindex(labels, fill_value=0)

ttDFnaman = pd.Categorical(ttDFnaman, categories=labels, ordered=True)
agg_count2 = ttDFnaman.value_counts()
agg_count2 = agg_count2.reindex(labels, fill_value=0)

xData1 = agg_count1.index
xData2 = agg_count2.index
yData1 = agg_count1.values
yData2 = agg_count2.values
print(xData1.shape,yData1.shape, yData2.shape)
# print(ttDFama['age_group'].dtype)
width=0.2
xData1_num = np.arange(len(xData1))
plt.bar(xData1_num-width,yData1, width=0.4, label='yes')
plt.bar(xData1_num+width,yData2, width=0.4, label='no')


for i in range(len(xData1)):
    plt.text(xData1_num[i]-width, yData1[i] + 0.5, str(yData1[i]), ha='center', va='bottom')
for i in range(len(xData1)):
    plt.text(xData1_num[i]+width, yData2[i] + 0.5, str(yData2[i]), ha='center', va='bottom')
plt.xticks(xData1_num, xData1)
plt.title( 'not (adult_male & alone) - age_group')
plt.legend()
st.pyplot(plt)

st.divider()


# In[21]:


plt.figure(figsize=(12,6))
agg_count1=ttDFnama.loc[(ttDFnama['alive']=='yes'),'pclass'].value_counts()
agg_count2=ttDFnama.loc[(ttDFnama['alive']=='no'),'pclass'].value_counts()

xData = agg_count1.index
yData1 = agg_count1.values
agg_count2 = agg_count2.reindex(agg_count1.index,fill_value=0)
yData2 = agg_count2.values

print(xData.shape, yData2.shape)

width = 0.15
plt.bar(xData-width,yData1, width=0.3, label='yes')
plt.bar(xData+width,yData2, width=0.3, label='no')
# print(ttDFnama['pclass'].dtype)

for i in range(len(xData)):
    plt.text(xData[i]-width, yData1[i], str(yData1[i]), ha='center', va='bottom')
    plt.text(xData[i]+width, yData2[i], str(yData2[i]), ha='center', va='bottom')
plt.legend()
plt.title('not (adult_male & alone) - pclass')
plt.xticks(agg_count1.index)
st.pyplot(plt)

st.divider()


# In[22]:


# ttDFnama
# ttDFnama.info()
# %matplotlib inline


# In[23]:


st.title( ' 결론')
st.header('독신 남성의 수가 단일집단 치고는 많으며, 그 사망률 또한 높다.')
st.header('사망률과 유의미하게 관계있는 지표는 pclass 이다.')

st.header('독신남성을 제외한 집단의 경우 비교적 낮은 사망률을 보이며,')
st.header('독신 남성의 경우와 같이 pclass가 의미있는 지표를 보인다.')


# In[24]:


# 번외
st.code('''ttDF[ttDF['fare']==0]

ttDF.loc[(ttDF['age'].isna()) & (ttDF['sex']=='male'), ['pclass']]
ttDF.loc[(ttDF['age'].isna()) & (ttDF['sex']=='female'), ['pclass']]

ttDF.loc[(ttDF['age'].isna()) & (ttDF['sex']=='male'), ['pclass']]
ttDF.loc[(ttDF['age'].isna()) & (ttDF['sex']=='female'), ['pclass']].value_counts()

''')

st.divider()


# In[25]:


plt.figure(figsize=(12,6))
mis_count1= ttDF.loc[(ttDF['age'].isna()) & (ttDF['sex']=='male'), ['pclass']].value_counts()
mis_count2= ttDF.loc[(ttDF['age'].isna()) & (ttDF['sex']=='female'), ['pclass']].value_counts()
# print(mis_count1.index)

## 멀티 인덱스 구조를 가지고 있어, 리인덱스를 하기 힘들었음.
## 따라서 같은 배열을 가진 것을 
# mis_count1 = mis_count1.reindex(['1','2','3',])
# mis_count2 = mis_count2.reindex(['1','2','3',])
# mis_count2 = mis_count2.reindex([1,2,3,],fill_value=0)


xData = pd.Series([3,1,2])
yData1 = mis_count1.values
yData2 = mis_count2.values
# print(xData.shape, yData1.shape, yData2.shape)
# print(xData.dtype, yData1.dtype, yData2.dtype)

print(mis_count1)
print(mis_count2)

# xx = np.arange(1,4)
width = 0.2
plt.bar(xData-width,yData1, width=0.4, label='male')
plt.bar(xData+width,yData2, width=0.4, label='female')

for i in range(len(xData)):
    plt.text(xData[i]-width, yData1[i], str(yData1[i]), ha='center', va='bottom')
for i in range(len(xData)):
    plt.text(xData[i]+width, yData2[i], str(yData2[i]), ha='center', va='bottom')


plt.title('age missing - pclass',pad=20,  fontdict={'weight':'bold','size':'25'})
plt.legend()
plt.xticks([1,2,3])
st.pyplot(plt)

st.divider()


# In[26]:


st.header('번외')
st.write('fare 값의 최소치에 0이 존재. why?')

st.code('''
# ttDF.loc[(ttDF['pclass']==1) & (ttDF['fare']==0), 'age']
# age로는 이유를 파악할 수 없음.

ttDF.loc[(ttDF['pclass']==3) & (ttDF['fare']==0), 'sibsp']
# 'sibsp' 은 1,2,3 모두 0임.
ttDF.loc[(ttDF['pclass']==3) & (ttDF['fare']==0), 'embarked']
# 'alone' 은 1,2,3 모두 True임. why? 
# 'sex' 모두 male
# 'embarked' 는 모두 Southampton
# 자료의 오류인가? 
ttDF.loc[(ttDF['fare']==0),'alive']
# ttDF.loc[(ttDF['fare']==0)].count()
# 탑승비용이 0원인 자는, 15명이며 전원 사우스햄튼에서 탑승한 남성이며 동승자가 없다.
# 1명만 살아남았다.
        
       ''' )



