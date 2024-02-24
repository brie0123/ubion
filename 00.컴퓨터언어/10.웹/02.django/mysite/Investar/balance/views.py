from django.shortcuts import render
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request

# https://finance.naver.com/item/sise.nhn?code=005930
# Create your views here.

def get_data(symbol):
    url = f'https://finance.naver.com/item/sise.nhn?code={symbol}'
    
    with urlopen(url) as doc:
        soup = BeautifulSoup(doc,"lxml", from_encoding="euc-kr")
        cur_price = soup.find('strong',id='_nowVal')
        cur_rate = soup.find('strong',id='_rate')
        stock = soup.find('title')
        stock_name = stock.text.split(":")[0].strip()
    return cur_price.text, cur_rate.text.strip(), stock_name


def main_view(request):
    querydict = request.GET.copy()
    mylist = querydict.lists()
    
    rows = []
    total = 0
    
    for x in mylist:
        cur_price, cur_rate, stock_name = get_data(x[0]) #x[0] = 005930)
        price = cur_price.replace(",","")
        stock_count = format(int(x[1][0]),",")
        sum = int(price) * int(x[1][0])
        stock_sum = format(sum,",")
        
        # 종목명, 종목코드, 현재가, 주식수, 등락률, 평가금액
        rows.append([stock_name, x[0], cur_price, stock_count, cur_rate, stock_sum])
        
    total_amount = format(total,",")
    values = {'rows': rows, 'total':total_amount}
    return render(request,'balance.html',values)
        