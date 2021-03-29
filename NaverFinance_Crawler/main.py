import requests
import pandas as pd
from bs4 import BeautifulSoup
from NaverFinance import *

df_stock_list = pd.read_html('http://kind.krx.co.kr/corpgeneral/corpList.do?method=download', header=0)[0]

#df_stock_list = df_stock_list[['회사명', '종목코드']]                                        #전체종목
#df_stock_list = df_stock_list[:10]                                                        #10가지 종목 테스트
df_stock_list = pd.DataFrame(data={'회사명': '삼성전자', '종목코드': 5930},  index=[0])        #단일종목테스트

df_analysis = pd.DataFrame(columns=['name', 'code', 'growth_year_sale', 'growth_quarter_sale', 'growth_year_income', 'growth_quarter_income', 'growth_year_per', 'growth_quarter_per'])

for name, code in zip(df_stock_list['회사명'], df_stock_list['종목코드']):
    str_code = str(code)
    while (len(str_code) < 6):
        str_code = '0' + str_code

    url = "https://finance.naver.com/item/main.nhn?code=" + str_code
    print(name, str_code, url)

    html = requests.get(url).text
    bs = BeautifulSoup(html, 'html.parser')

    #크롤링한 데이터 Dataframe에 저장
    df_year_salse = pd.DataFrame(data={'data': GetNf_YearSales(bs)})
    df_quarter_salse = pd.DataFrame(data={'data': GetNf_QuarterSales(bs)})
    df_year_incomes = pd.DataFrame(data={'data': GetNf_YearIncomes(bs)})
    df_quarter_incomes = pd.DataFrame(data={'data': GetNf_QuarterIncomes(bs)})
    df_year_pers = pd.DataFrame(data={'data': GetNf_YearPers(bs)})
    df_quarter_pers = pd.DataFrame(data={'data': GetNf_QuarterPers(bs)})

    #각 목록별 상승률 계산
    df_year_sale_pct = df_year_salse['data'].diff() / df_year_salse['data'].abs().shift() * 100
    df_quarter_sale_pct = df_quarter_salse['data'].diff() / df_quarter_salse['data'].abs().shift() * 100
    df_year_income_pct = df_year_incomes['data'].diff() / df_year_incomes['data'].abs().shift() * 100
    df_quarter_income_pct = df_quarter_incomes['data'].diff() / df_quarter_incomes['data'].abs().shift() * 100
    df_year_per_pct = df_year_pers['data'].diff() / df_year_pers['data'].abs().shift() * 100
    df_quarter_per_pct = df_quarter_pers['data'].diff() / df_quarter_pers['data'].abs().shift() * 100

    #상승률 평균 계산
    growth_year_sale = df_year_sale_pct.mean()
    growth_quarter_sale = df_quarter_sale_pct.mean()
    growth_year_income = df_year_income_pct.mean()
    growth_quarter_income = df_quarter_income_pct.mean()
    growth_year_per = df_year_per_pct.mean()
    growth_quarter_per = df_quarter_per_pct.mean()

    print(growth_year_sale,
          growth_quarter_sale,
          growth_year_income,
          growth_quarter_income,
          growth_year_per,
          growth_quarter_per)
    print('')

    df_analysis = df_analysis.append(
        {"name": name,
         "code": str_code,
         "growth_year_sale": growth_year_sale,
         "growth_quarter_sale": growth_quarter_sale,
         "growth_year_income": growth_year_income,
         "growth_quarter_income": growth_quarter_income,
         "growth_year_per": growth_year_per,
         "growth_quarter_per": growth_quarter_per},
        ignore_index=True)