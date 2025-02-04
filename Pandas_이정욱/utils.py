def print_attribute(df,df_name):
    print(f"------[{df_name}]-------")
    print(f'{df_name}.dtypes\n', df.dtypes)
    print(f'{df_name}.index', df.index)
    print(f'{df_name}.columns', df.columns)
    print(f'{df_name}.ndim', df.ndim)
    print(f'{df_name}.shape', df.shape)
    print(f'{df_name}.values\n', df.values)
    

def summary(df, df_name):
    print(f"------[{df_name}]-------")
    df.info()       #요약정보
    df.head(2)      #실제데이터
    df.tail(2)
    df.describe()   #통계치
    
