import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#Cuadrícula
#plt.grid(True,linestyle='-', linewidth='0.5', color='red')
#plt.show()

#Agregamos los datos del CSV a graficar e imprimimos las primeras 5 lineas para ver que este correcto
Juntos = pd.read_csv('co2vsgdp.csv')
h=Juntos.head()
print(h)

es_Mexico = Juntos["countryname"] == "México"
es_Brasil = Juntos["countryname"] == "Brasil"
es_USA = Juntos["countryname"] == "EstadosUnidos"
es_China = Juntos["countryname"] == "China"
es_Aus = Juntos["countryname"] == "Australia"
es_India = Juntos["countryname"] == "India"
es_Spain = Juntos["countryname"] == "España"
es_Sud = Juntos["countryname"] == "Sudán"
es_Ban = Juntos["countryname"] == "Bangladesh"
es_Alemania = Juntos["countryname"] == "Alemania"


JuntosPaises = Juntos[es_Mexico | es_Brasil | es_Ban | es_China | es_Sud | es_Aus | es_Alemania | es_India | es_USA | es_Spain]
PaisMex = Juntos[es_Mexico]
America = Juntos[es_Mexico | es_Brasil | es_USA]
Europa = Juntos[es_Spain | es_Alemania]
Asia = Juntos[es_India | es_China | es_Ban]
Africa = Juntos[es_Sud]
Oceania = Juntos[es_Aus]

datosTotales = Juntos.describe()
print(datosTotales)


#En el eje X con datos numéricos
#sns.distplot(JuntosPaises['height_cm'],bins=20)

#co2
#graficando solo datos numéricos
#sns.jointplot(x='anio', y='co2', data=JuntosPaises,sizes=(40, 400), alpha=.5, palette="muted",hue='countryname', height=6)

#gdp
#sns.jointplot(x='anio', y='gdp', data=JuntosPaises,sizes=(40, 400), alpha=.5, palette="muted",hue='countryname', height=6)

#--------------------------------------------

#f, ax=plt.subplots(figsize=(6,15))
#countries= JuntosPaises.sort_values("countryname",ascending=False)

#Primer Subset
#sns.set_color_codes("bright")
#sns.barplot(x="co2",y="countryname",data=countries,label="co2",color="g")
#plt.show()

#Segundo subset
#sns.set_color_codes("muted")
#sns.barplot(x="gdp",y="countryname",data=countries,label="gdp",color="yellow")

#ax.legend(ncol=2, loc="lower right",frameon=True)
#ax.set(xlim=(0.24),ylabel="",xlabel="PP")
#sns.despine(top=False,right=False)

#--------------------------------

#todos los paises en una misma gráfica en todos los años
#co2
#g = sns.catplot(x="countryname",y="co2",hue="anio",data=JuntosPaises,height=6,kind="bar",palette="muted")
#g.despine(left=True)
#g.set_ylabels("co2")

#gdp
#g = sns.catplot(x="countryname",y="gdp",hue="anio",data=JuntosPaises,height=6,kind="bar",palette="muted")
#g.despine(left=True)
#g.set_ylabels("gdp")

#-----------------------------------

#tamaño circulo es el gdp y se muestra co2
#sns.relplot(x="anio", y="co2", size="gdp",
#            sizes=(40, 400), alpha=.5, palette="muted",hue='countryname',
#            height=6, data=JuntosPaises)

#gráfica co2 con gdp
#sns.relplot(x="co2", y="gdp",
#            sizes=(40, 400), alpha=.5, palette="muted",hue='countryname',
#            height=6, data=JuntosPaises)

#--------------------------------------

#variospaises hex
#sns.set_theme(style="ticks")
#sns.jointplot(x="co2", y="gdp",data=JuntosPaises,color="#4CB391",hue="countryname")

#mexico
#sns.set_theme(style="ticks")
#sns.jointplot(x="co2", y="gdp", kind="hex",data=PaisMex,color="#4CB391")

#-------------------------------------------

#Por continentes de co2
#sns.set_theme( style='darkgrid')
#f, ax=plt.subplots(figsize=(150,100))
#AAmerica = America.sort_values("co2",ascending=False)
#EEuropa  = Europa.sort_values("co2",ascending=False)
#AAsia  = Asia.sort_values("co2",ascending=False)
#AAfrica  = Africa.sort_values("co2",ascending=False)
#OOceania  = Oceania.sort_values("co2",ascending=False)
#PM  = PaisMex.sort_values("co2",ascending=False)

#sns.lineplot(x="anio",y="co2",data=EEuropa,label="CO2 Europa")
#Se crea el segundo subset a guardar en el subplot
#sns.lineplot(x="anio",y="co2",data=AAmerica,label="CO2 America")
#sns.lineplot(x="anio",y="co2",data=AAsia,label="CO2 Asia")
#sns.lineplot(x="anio",y="co2",data=AAfrica,label="CO2 Africa")
#sns.lineplot(x="anio",y="co2",data=OOceania,label="CO2 Oceania")

#------------------------------


plt.show()
  

