import pandas
excel = pandas.read_excel('ramenPhoSoba-interest.xlsx', names=["country", "pho", "ramen", "soba"])
data = excel.to_dict('records')
