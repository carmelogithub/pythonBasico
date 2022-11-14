print('Práctica')
#muestra un gráfico
#de uso de m3 y de número de clientes

import pandas as pd
import matplotlib.pyplot as plt

def mostrar_grafico():
    datos=pd.read_csv('C:\\Users\\Tecnicos\\Desktop\\Carmelo\\Programacion\\agua.csv')
    #print(datos)
    #Ús,any_,m3_registrats,núm_clients,ObjectId,CODI_ENS,NOM_ENS
    df=datos[['Ús','m3_registrats','núm_clients']] #dataFrame
    #print(df)
    # histograma
    df.m3_registrats.plot.hist()
    plt.show()
    # grafico de barras
    m3_por_uso = df.groupby("Ús")["m3_registrats"].mean()
    m3_por_uso.head(10).plot.barh()
    plt.show()



mostrar_grafico()