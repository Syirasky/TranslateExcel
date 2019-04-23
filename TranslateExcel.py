import xlrd
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
from googletrans import Translator

translator = Translator()
print("Excel File Translate for Apps Language Translate")

loc = ("Example_Labels.xlsx")

df = pd.read_excel(loc)
print("Count in data record")
print(df.count())

EnWordStr = df['EN'][0].encode('utf-8')
TranslatedEnStr = translator.translate(EnWordStr , dest='ms')
print(EnWordStr," -> ", TranslatedEnStr.text.encode('utf-8'))
