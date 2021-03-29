# 년도별 매출액
def GetNf_YearSales(bs):
    year_salse = []
    for i in range(4):
        selector = 'div.section.cop_analysis > div.sub_section > table > tbody > tr:nth-child(1) > td:nth-child(' + str(
            i + 2) + ')'
        try:
            year_sale = bs.select(selector)[0]
        except:
            break
        year_sale = year_sale.text.strip().replace(',', '').replace('-', '')
        if year_sale != '':
            year_salse.append(int(year_sale))

    return year_salse


# 분기별 매출액
def GetNf_QuarterSales(bs):
    quarter_salse = []
    for i in range(6):
        selector = 'div.section.cop_analysis > div.sub_section > table > tbody > tr:nth-child(1) > td:nth-child(' + str(
            i + 6) + ')'
        try:
            quarter_sale = bs.select(selector)[0]
        except:
            break
        quarter_sale = quarter_sale.text.strip().replace(',', '').replace('-', '')
        if quarter_sale != '':
            quarter_salse.append(int(quarter_sale))

    return quarter_salse


# 년도별 순이익
def GetNf_YearIncomes(bs):
    year_incomes = []
    for i in range(4):
        selector = 'div.section.cop_analysis > div.sub_section > table > tbody > tr:nth-child(3) > td:nth-child(' + str(
            i + 2) + ')'
        try:
            year_income = bs.select(selector)[0]
        except:
            break
        year_income = year_income.text.strip().replace(',', '')
        if len(year_income) == 1 and year_income == '-':
            year_income = year_income.replace('-', '')
        if year_income != '':
            year_incomes.append(int(year_income))

    return year_incomes


# 분기별 순이익
def GetNf_QuarterIncomes(bs):
    quarter_incomes = []
    for i in range(6):
        selector = 'div.section.cop_analysis > div.sub_section > table > tbody > tr:nth-child(3) > td:nth-child(' + str(
            i + 6) + ')'
        try:
            quarter_income = bs.select(selector)[0]
        except:
            break
        quarter_income = quarter_income.text.strip().replace(',', '')
        if len(quarter_income) == 1 and quarter_income == '-':
            quarter_income = quarter_income.replace('-', '')
        if quarter_income != '':
            quarter_incomes.append(int(quarter_income))

    return quarter_incomes


# 년도별 PER
def GetNf_YearPers(bs):
    year_pers = []
    for i in range(4):
        selector = 'div.section.cop_analysis > div.sub_section > table > tbody > tr:nth-child(11) > td:nth-child(' + str(
            i + 2) + ')'
        try:
            year_per = bs.select(selector)[0]
        except:
            break
        year_per = year_per.text.strip().replace(',', '')
        if len(year_per) == 1 and year_per == '-':
            year_per = year_per.replace('-', '')
        if year_per != '':
            year_pers.append(float(year_per))

    return year_pers


# 분기별 PER
def GetNf_QuarterPers(bs):
    quarter_pers = []
    for i in range(6):
        selector = 'div.section.cop_analysis > div.sub_section > table > tbody > tr:nth-child(11) > td:nth-child(' + str(
            i + 6) + ')'
        try:
            quarter_per = bs.select(selector)[0]
        except:
            break
        quarter_per = quarter_per.text.strip().replace(',', '')
        if len(quarter_per) == 1 and quarter_per == '-':
            quarter_per = quarter_per.replace('-', '')
        if quarter_per != '':
            quarter_pers.append(float(quarter_per))

    return quarter_pers