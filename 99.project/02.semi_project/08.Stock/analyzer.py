import pandas as pd
import pymysql
from datetime import datetime
from datetime import timedelta
import re

class MarketDB:
    def __init__(self):
        self.conn = pymysql.connect(host='localhost', user='root', password='apple123!!', db='investar', charset='utf8')
        self.codes = {}
        self.get_comp_info()
    
    
    def __del__(self):
        self.conn.close()
        
    def get_comp_info(self):
        """company_info 테이블에서 codes 불러와서 self.codes에 저장"""
        sql = """SELECT * FROM company_info"""
        krx = pd.read_sql(sql, self.conn)
        for idx in range(len(krx)):
            self.codes[krx['code'].values[idx]] = krx['company'].values[idx]
    
    # 종목의 일별 시세 DB에서 가져오기
    def get_daily_price(self, code, start_date=None, end_date=None):
            
        if start_date is None:
            one_year_ago = datetime.today() - timedelta(days=365)
            start_date = one_year_ago.strftime('%Y-%m-%d')
            print("start_date is initialized to '{}'".format(start_date))
        else:
            start_lst = re.split('\D+',start_date)
            start_year = int(start_lst[0])
            start_month = int(start_lst[1])
            start_day = int(start_lst[2])
        
        # start_date
        # 이상한 날짜 제거 처리    
        if start_year < 1900 or start_year > 2200:
            print(f"ValueError : start_year({start_year:d}) is wrong.")
            return
        if start_month < 1 or start_month > 12:
            print(f"ValueError : start_month({start_month}) is wrong.")
            return
        if start_day < 1 or start_day > 31:
            print(f"ValueError : start_day({start_day:d}) is wrong.")
            return
        
        
        # end_date
        # 딱히 이상한 날짜 없을 때:
        start_date = f"{start_year:04d}-{start_month:02d}-{start_day:02d}"
        
    
        if end_date is None:
            end_date = datetime.today().strftime('%Y-%m-%d')
            print("end_date is initialized to '{}'".format(end_date))
        else:
            end_lst = re.split('\D+',end_date)
            end_year = int(end_lst[0])
            end_month = int(end_lst[1])
            end_day = int(end_lst[2])
        
        # 이상한 날짜 제거 처리    
        if end_year < 1900 or end_year > 2200:
            print(f"ValueError : end_year({end_year:d}) is wrong.")
            return
        if end_month < 1 or end_month > 12:
            print(f"ValueError : end_month({end_month}) is wrong.")
            return
        if end_day < 1 or end_day > 31:
            print(f"ValueError : end_day({end_day:d}) is wrong.")
            return
        
        # 딱히 이상한 날짜 없을 때:
        end_date = f"{end_year : 04d}-{end_month:02d}-{end_day:02d}"
        
        codes_keys = list(self.codes.keys())
        codes_values = list(self.codes.values())
        
        if code in codes_keys:
            pass
        elif code in codes_values:
            idx = codes_values.index(code)
            code = codes_keys[idx]
            
        else:
            print(f"ValueError: Code({code}) doesn't exist.")
        
        
        sql = f"""
        select *  from daily_price
        where code = '{code}' and (date >='{start_date}' AND date <= '{end_date}');
        """
        df = pd.read_sql(sql, self.conn)
        df.index = df['date']
        
        return df




        
#     1. KRX 종목의 일별 시세를 
#     investar DB에서 가지고 와서 
#     데이터 프레임 형태로 변환하기
  
mk = MarketDB()
raw_df = mk.get_daily_price('000020', '2020-01-01','2023-12-10')
print(raw_df)  