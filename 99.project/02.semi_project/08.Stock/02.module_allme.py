import pandas as pd
import pymysql
from datetime import datetime
from datetime import timedelta
import re

class MarketDB:
    def __init__(self):
        self.conn = pymysql.connect(host='localhost', user='root', password='apple123!!', db='investar', charset='utf8')
        self.conn.commit()
        pass
    
    
    def __del__(self):
        self.conn.close()
        pass
    
    # 종목의 일별 시세 DB에서 가져오기
    def get_daily_price(self, code, start_date=None, end_date=None):
            today = datetime.today().strftime('%Y-%m-%d')
            if end_date is None:
                if start_date is not None:
                    end_date = (datetime.strptime(start_date, '%Y-%m-%d') - timedelta(days=365)).strftime('%Y-%m-%d')
                else:
                    start_date = today
                    end_date = (datetime.today() - timedelta(days=365)).strftime('%Y-%m-%d')    
                
            sql = f"""
            select *  from daily_price
            where code = '{code}' and (date >='{start_date}' AND date <= '{end_date}');
            """
            
            df = pd.read_sql(sql, self.conn)
            return df




        
#     1. KRX 종목의 일별 시세를 
#     investar DB에서 가지고 와서 
#     데이터 프레임 형태로 변환하기
  
mk = MarketDB()
raw_df = mk.get_daily_price('000020', '2020-01-01','2023-12-10')
print(raw_df)  