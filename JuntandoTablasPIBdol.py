import numpy as np
import pandas as pd
import pickle
import matplotlib.pyplot as plt

#Estabelcemos el data frame para la fecha
print("\nPrograma de Co2 para juntar las tablas :D\n")



anio70=pd.read_csv('anio1970.csv')
anio71=pd.read_csv('anio1971.csv')
anio72=pd.read_csv('anio1972.csv')
anio73=pd.read_csv('anio1973.csv')
anio74=pd.read_csv('anio1974.csv')
anio75=pd.read_csv('anio1975.csv')
anio76=pd.read_csv('anio1976.csv')
anio77=pd.read_csv('anio1977.csv')
anio78=pd.read_csv('anio1978.csv')
anio79=pd.read_csv('anio1979.csv')
anio80=pd.read_csv('anio1980.csv')
anio81=pd.read_csv('anio1981.csv')
anio82=pd.read_csv('anio1982.csv')
anio83=pd.read_csv('anio1983.csv')
anio84=pd.read_csv('anio1984.csv')
anio85=pd.read_csv('anio1985.csv')
anio86=pd.read_csv('anio1986.csv')
anio87=pd.read_csv('anio1987.csv')
anio88=pd.read_csv('anio1988.csv')
anio89=pd.read_csv('anio1989.csv')
anio90=pd.read_csv('anio1990.csv')
anio91=pd.read_csv('anio1991.csv')
anio92=pd.read_csv('anio1992.csv')
anio93=pd.read_csv('anio1993.csv')
anio94=pd.read_csv('anio1994.csv')
anio95=pd.read_csv('anio1995.csv')
anio96=pd.read_csv('anio1996.csv')
anio97=pd.read_csv('anio1997.csv')
anio98=pd.read_csv('anio1998.csv')
anio99=pd.read_csv('anio1999.csv')
anio00=pd.read_csv('anio2000.csv')
anio01=pd.read_csv('anio2001.csv')
anio02=pd.read_csv('anio2002.csv')
anio03=pd.read_csv('anio2003.csv')
anio04=pd.read_csv('anio2004.csv')
anio05=pd.read_csv('anio2005.csv')
anio06=pd.read_csv('anio2006.csv')
anio07=pd.read_csv('anio2007.csv')
anio08=pd.read_csv('anio2008.csv')
anio09=pd.read_csv('anio2009.csv')
anio10=pd.read_csv('anio2010.csv')
anio11=pd.read_csv('anio2011.csv')
anio12=pd.read_csv('anio2012.csv')

DFanio70=pd.DataFrame(anio70)
DFanio71=pd.DataFrame(anio71)
DFanio72=pd.DataFrame(anio72)
DFanio73=pd.DataFrame(anio73)
DFanio74=pd.DataFrame(anio74)
DFanio75=pd.DataFrame(anio75)
DFanio76=pd.DataFrame(anio76)
DFanio77=pd.DataFrame(anio77)
DFanio78=pd.DataFrame(anio78)
DFanio79=pd.DataFrame(anio79)
DFanio80=pd.DataFrame(anio80)
DFanio81=pd.DataFrame(anio81)
DFanio82=pd.DataFrame(anio82)
DFanio83=pd.DataFrame(anio83)
DFanio84=pd.DataFrame(anio84)
DFanio85=pd.DataFrame(anio85)
DFanio86=pd.DataFrame(anio86)
DFanio87=pd.DataFrame(anio87)
DFanio88=pd.DataFrame(anio88)
DFanio89=pd.DataFrame(anio89)
DFanio90=pd.DataFrame(anio90)
DFanio91=pd.DataFrame(anio91)
DFanio92=pd.DataFrame(anio92)
DFanio93=pd.DataFrame(anio93)
DFanio94=pd.DataFrame(anio94)
DFanio95=pd.DataFrame(anio95)
DFanio96=pd.DataFrame(anio96)
DFanio97=pd.DataFrame(anio97)
DFanio98=pd.DataFrame(anio98)
DFanio99=pd.DataFrame(anio99)
DFanio00=pd.DataFrame(anio00)
DFanio01=pd.DataFrame(anio01)
DFanio02=pd.DataFrame(anio02)
DFanio03=pd.DataFrame(anio03)
DFanio04=pd.DataFrame(anio04)
DFanio05=pd.DataFrame(anio05)
DFanio06=pd.DataFrame(anio06)
DFanio07=pd.DataFrame(anio07)
DFanio08=pd.DataFrame(anio08)
DFanio09=pd.DataFrame(anio09)
DFanio10=pd.DataFrame(anio10)
DFanio11=pd.DataFrame(anio11)
DFanio12=pd.DataFrame(anio12)

##--------------------------MERGE--------------------------
##UNIR COLUMNAS

#JuntosAB= pd.merge(DataFrameA,DataFrameB,on='ABC')
#dfJuntosAB=pd.DataFrame(JuntosAB)
#print(dfJuntosAB)

#JuntosABC= pd.merge(dfJuntosAB,DataFrameC,on='ABC')
#dfJuntosABC=pd.DataFrame(JuntosABC)
#print(dfJuntosABC)

#JuntosABCD= pd.merge(dfJuntosABC,DataFrameD,on='ABC')
#dfJuntosABCD=pd.DataFrame(JuntosABCD)
#print(dfJuntosABCD)

#JuntosABCDE= pd.merge(dfJuntosABCD,DataFrameE,on='ABC')
#dfJuntosABCDE=pd.DataFrame(JuntosABCDE)
#print(dfJuntosABCDE)

##---------------------------APPEND--------------------
##UNIR RENGLONES

Juntos701=DFanio70.append(DFanio71)
dfJuntos701=pd.DataFrame(Juntos701)

Juntos712=dfJuntos701.append(DFanio72)
dfJuntos712=pd.DataFrame(Juntos712)

Juntos723=dfJuntos712.append(DFanio73)
dfJuntos723=pd.DataFrame(Juntos723)

Juntos734=dfJuntos723.append(DFanio74)
dfJuntos734=pd.DataFrame(Juntos734)

Juntos745=dfJuntos734.append(DFanio75)
dfJuntos745=pd.DataFrame(Juntos745)

Juntos756=dfJuntos745.append(DFanio76)
dfJuntos756=pd.DataFrame(Juntos756)

Juntos767=dfJuntos756.append(DFanio77)
dfJuntos767=pd.DataFrame(Juntos767)

Juntos778=dfJuntos767.append(DFanio78)
dfJuntos778=pd.DataFrame(Juntos778)

Juntos789=dfJuntos778.append(DFanio79)
dfJuntos789=pd.DataFrame(Juntos789)

Juntos890=dfJuntos789.append(DFanio80)
dfJuntos890=pd.DataFrame(Juntos890)

Juntos801=dfJuntos890.append(DFanio81)
dfJuntos801=pd.DataFrame(Juntos801)

Juntos812=dfJuntos801.append(DFanio82)
dfJuntos812=pd.DataFrame(Juntos812)

Juntos823=dfJuntos812.append(DFanio83)
dfJuntos823=pd.DataFrame(Juntos823)

Juntos834=dfJuntos823.append(DFanio84)
dfJuntos834=pd.DataFrame(Juntos834)

Juntos845=dfJuntos834.append(DFanio85)
dfJuntos845=pd.DataFrame(Juntos845)

Juntos856=dfJuntos845.append(DFanio86)
dfJuntos856=pd.DataFrame(Juntos856)

Juntos867=dfJuntos856.append(DFanio87)
dfJuntos867=pd.DataFrame(Juntos867)

Juntos878=dfJuntos867.append(DFanio88)
dfJuntos878=pd.DataFrame(Juntos878)

Juntos889=dfJuntos878.append(DFanio89)
dfJuntos889=pd.DataFrame(Juntos889)

Juntos990=dfJuntos889.append(DFanio90)
dfJuntos990=pd.DataFrame(Juntos990)

Juntos901=dfJuntos990.append(DFanio91)
dfJuntos901=pd.DataFrame(Juntos901)

Juntos912=dfJuntos901.append(DFanio92)
dfJuntos912=pd.DataFrame(Juntos912)

Juntos923=dfJuntos912.append(DFanio93)
dfJuntos923=pd.DataFrame(Juntos923)

Juntos934=dfJuntos923.append(DFanio94)
dfJuntos934=pd.DataFrame(Juntos934)

Juntos945=dfJuntos934.append(DFanio95)
dfJuntos945=pd.DataFrame(Juntos945)

Juntos956=dfJuntos945.append(DFanio96)
dfJuntos956=pd.DataFrame(Juntos956)

Juntos967=dfJuntos956.append(DFanio97)
dfJuntos967=pd.DataFrame(Juntos967)

Juntos978=dfJuntos967.append(DFanio98)
dfJuntos978=pd.DataFrame(Juntos978)

Juntos989=dfJuntos978.append(DFanio99)
dfJuntos989=pd.DataFrame(Juntos989)

Juntos090=dfJuntos989.append(DFanio00)
dfJuntos090=pd.DataFrame(Juntos090)

Juntos001=dfJuntos090.append(DFanio01)
dfJuntos001=pd.DataFrame(Juntos001)

Juntos012=dfJuntos001.append(DFanio02)
dfJuntos012=pd.DataFrame(Juntos012)

Juntos023=dfJuntos012.append(DFanio03)
dfJuntos023=pd.DataFrame(Juntos023)

Juntos034=dfJuntos023.append(DFanio04)
dfJuntos034=pd.DataFrame(Juntos034)

Juntos045=dfJuntos034.append(DFanio05)
dfJuntos045=pd.DataFrame(Juntos045)

Juntos056=dfJuntos045.append(DFanio06)
dfJuntos056=pd.DataFrame(Juntos056)

Juntos067=dfJuntos056.append(DFanio07)
dfJuntos067=pd.DataFrame(Juntos067)

Juntos078=dfJuntos067.append(DFanio08)
dfJuntos078=pd.DataFrame(Juntos078)

Juntos089=dfJuntos078.append(DFanio09)
dfJuntos089=pd.DataFrame(Juntos089)

Juntos090=dfJuntos089.append(DFanio10)
dfJuntos090=pd.DataFrame(Juntos090)

Juntos001=dfJuntos090.append(DFanio11)
dfJuntos001=pd.DataFrame(Juntos001)

Juntos012=dfJuntos001.append(DFanio12)
dfJuntos012=pd.DataFrame(Juntos012)


##-------------------------PICKLE------------------------

archivo = open("TABLASJuntasPIBdol.txt","wb")
pickle.dump(dfJuntos012,archivo)
archivo.close()

archivo = open("TABLASJuntasPIBdol.txt","rb")
texto2=pickle.load(archivo)
archivo.close()
print('Se va a desplegar a continuación el picke')
print(texto2)

##-------------------------EXPORTAR CSV-------------------------

dfJuntos012.to_csv (r'C:\Users\danny\OneDrive\Ciencia de Datos\ApibUMN\export_dataframe.csv', index = False, header=True)

