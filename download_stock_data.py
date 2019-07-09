# -*- coding: utf-8 -*-
# file: download_stock_data.py
#
# Download datas of stock charts
# pandas_datareader を使って株価データをダウンロード
# 取得したデータを pandas plot を使用してグラフ表示する

from datetime import datetime
import matplotlib
import matplotlib.pyplot as plt
import numpy
import pandas as pd # To avoid error
pd.core.common.is_list_like = pd.api.types.is_list_like # To avoid error
import pandas_datareader.data as web

def init_plt():
    plt.style.use('ggplot')
    font = {'family' : 'sans'}
    matplotlib.rc('font', **font)

def download_stock(stocklist, start, end):
    return web.DataReader(stocklist, 'yahoo', start, end)

if __name__ == '__main__':
    init_plt()

    stocklist = ['^DJI', '^FTSE', '^GDAXI', '^GSPC', '^HSI', '^IXIC', '^N225']
    start = datetime(2009, 7, 4)
    end = datetime(2019, 7, 4)
    stock = download_stock(stocklist, start, end)
    stock = stock['Close']
    print (stock)
    print (len(stock))
    stock.plot()
    plt.show()
