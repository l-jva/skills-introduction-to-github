import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px


st.set_option('deprecation.showPyplotGlobalUse', False)

st.title('EnergAI: The future of sustentaibility ⚡')

datafile = st.file_uploader('Cargar archivo CSV', type='csv', )
if datafile:
  df = pd.read_csv(datafile)

if 'df' in locals():
    st.title('Your data:')
    st.write(df)

if 'df' in locals():
    st.subheader('Visualizaciones')
    # Histograma
    plt.hist(df['energiaProducida'])
    st.pyplot()

    # Gráfico de dispersión
    fig = px.line(df, x="provincias", y="energiaProducida", title="Energy compliance")
    st.plotly_chart(fig)

    st.title('Energy analyzer')
    st.area_chart(df, x="provincias", y="energiaProducida", color="cantidadkw")