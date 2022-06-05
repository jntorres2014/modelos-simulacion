import pandas as pd
import matplotlib.pyplot as plt

class Estadisticas(object):
    def __init__(self):
        pass

    def crearExcel(self):
        pass



df = pd.read_excel("sample_data.xlsx")
print(type(df))
print(df["X"])
tab = pd.crosstab(index=df["X"],columns=df["Y"])
colores = ['red','green','blue','yellow']
plt.pie(x=df["X"],labels=tab.index,colors=colores) 
plt.xlabel("Perdidas de tiempo")
plt.savefig("notas.png")
plt.show()

# list1 = [10,20,30,40]
# list2 = [40,30,20,10]
# col1 = "X"
# col2 = "Y"

# data = pd.DataFrame({col1:list1,col2:list2})

# data.to_excel('sample_data.xlsx', sheet_name='sheet1', index=False)
