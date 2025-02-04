import pandas as pd                     # 데이터 분석 및 전처리용 모듈
import numpy as np                      # 배열(array)을 지원하는 파이썬 패키지

import streamlit as st
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt         # 데이터 시각화 즉, 그래프 관련 모듈
from matplotlib import font_manager, rc 
import utils        

## -----------------------------------------------------
## 함수 기능 : DataFrame의 컬럼별 고유값 개수와 고유값 출력
## 함수 이름 : printUniqueValue
## 매개 변수 : df
## 반 환  값 : 없음
## -----------------------------------------------------
def printUniqueValue(df):
    for col in df.columns:
        print(f'\n[{col}컬럼의 고유값]=====')
        print('갯수 : ', df[col].nunique() )
        print( df[col].unique())
        print( df[col].value_counts())
        
        
def returnUniqueValue(df):
    for col in df.columns:
        st.write(f"\n[{col} 컬럼의 고유값]=====")
        st.write(f"갯수 : {df[col].nunique()}")
        # st.write(df[col].unique())
        st.write(df[col].value_counts())
        
        
WINDOWS_SYS_FONT = r'C:\Windows\Fonts\NanumGothic.ttf'
def setHangulFont(font_path=r'C:\Windows\Fonts\NanumGothic.ttf' ):
    # 설정할 한글 폰트 이름 추출
    font_name = font_manager.FontProperties(fname=font_path).get_name()
    # 폰트 설정하기
    rc('font', family=font_name)
    
    print(f"설정된 폰트: {font_name}")