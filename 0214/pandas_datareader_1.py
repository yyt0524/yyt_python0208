# -*- coding: UTF-8 -*-
import pandas_datareader as pdr
baidu_df = pdr.get_data_stooq('BIDU', start='2021-11-22', end='2022-2-13')
baidu_df.sort_index(inplace=True)
print(baidu_df)
baidu_df.rolling(5).mean()