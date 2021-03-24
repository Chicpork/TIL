# %%
import pandas as pd

dat = pd.read_csv('gold.csv', encoding = 'utf-8')
print(dat)
#df = pd.read_excel('C:\\develop\\TIL\\apt\\wti.csv')



# %%
# for ix in range(len(dat["날짜"]-1, -1, -1)):
#     print(dat["날짜"][ix])
a = list(reversed(dat["날짜"]))
b = list(reversed(dat["종가"]))

dict = {'날짜':a, '종가':b}

df = pd.DataFrame(dict)

df.to_csv('test.csv', encoding="utf8")
    

# %%
