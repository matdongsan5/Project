import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

## 프로젝트 목적
## mpg 데이터에 대해 상세히 살피고
## 판다스 기능 및 각종 그래프 그리기 숙달

data = pd.read_csv('../DATA/auto_mpg.csv', encoding='euc-kr')
mpgDF = pd.DataFrame(data)
print(mpgDF)