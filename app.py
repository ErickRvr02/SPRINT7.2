import pandas as pd
import plotly.express as px
import streamlit as st
        
st.title('Primer Web con StreamLit')
st.write('Este es un proyecto del sprint7 de Tripleten')


car_data = pd.read_csv('vehicles_us.csv') # leer los datos
hist_button = st.button('Construir histograma') # crear un botón
        
if st.checkbox("Mostrar la base de datos completa"):
    st.write(car_data)

# Histograma: Distribución del odómetro con botón
if st.button("Mostrar histograma del total de coches por modelo"):
    st.write("Creación de un histograma para el conjunto de datos de anuncios de venta de coches.")
    fig = px.histogram(
        car_data, 
        x="model",
        title="Total de coches por modelo",
        labels={"model": "modelo del coche","count":"Total de coches"})
    st.plotly_chart(fig, use_container_width=True)

# Gráfico de dispersión: Precio vs. Año del modelo
st.subheader("Relación entre Precio y Año del Modelo")
fig = px.scatter(
        car_data, 
        x="model_year", 
        y="price", 
        title="Precio vs. Año del Modelo", 
        labels={"model_year": "Año del Modelo", "price": "Precio"}, opacity=0.5)
st.plotly_chart(fig, use_container_width=True)