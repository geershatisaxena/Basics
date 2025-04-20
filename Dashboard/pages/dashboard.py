import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

st.title("This is the Dashboard Page")

df = sns.load_dataset("diamonds")
st.dataframe(df)

fig1 = px.scatter(df, x='carat', y='price', color='cut', title='Carat vs Price',template='plotly_dark')
st.plotly_chart(fig1)

fig2 = px.histogram(df, x='carat', color='cut', title='Carat Distribution by Cut', template='plotly_dark')
st.plotly_chart(fig2)

fig = px.histogram(df, x='price', nbins=30, title='Distribution of Price',template='plotly_dark',color_discrete_sequence=['crimson'])
st.plotly_chart(fig)

fig3 = px.box(df, x='cut', y='price', title='Price by Cut',template='plotly_dark',color_discrete_sequence=['mediumvioletred'])
st.plotly_chart(fig3)

fig4 = px.violin(df, x='color', y='price', box=True, title='Price by Color',template='plotly_dark',color_discrete_sequence=['indigo'])
st.plotly_chart(fig4)

fig5 = px.bar(df.groupby('cut')['price'].mean().reset_index(), x='cut', y='price', title='Mean Price by Cut',template='plotly_dark',color_discrete_sequence=['lime'])
st.plotly_chart(fig5)

df_grouped = df.groupby('carat')['price'].mean().reset_index()
fig6 = px.line(df_grouped, x='carat', y='price', title='Mean Price by Carat',template='plotly_dark',color_discrete_sequence=['crimson'])
st.plotly_chart(fig6)

fig7 = px.pie(df, names='cut', title='Distribution of Cut',template='plotly_dark',color_discrete_sequence=px.colors.sequential.Rainbow)
st.plotly_chart(fig7)

pivot = df.pivot_table(values='price', index='cut', columns='color', aggfunc='mean')
fig8 = px.imshow(pivot, text_auto=True, color_continuous_scale='viridis', title='Mean Price by Cut and Color',template='plotly_dark')
st.plotly_chart(fig8)

fig9 = px.scatter(df, x='carat', y='price', trendline='ols', title='Carat vs Price with Regression Line',template='plotly_dark',color_discrete_sequence=['crimson'])
st.plotly_chart(fig9)

fig10 = px.strip(df, x='color', y='price', title='Price by Color (Stripplot)',template='plotly_dark',color_discrete_sequence=['red'])
st.plotly_chart(fig10)

fig11 = px.strip(df, x='color', y='price', title='Price by Color (Stripplot)',template='plotly_dark',color_discrete_sequence=['red'])
st.plotly_chart(fig11)

fig12= px.box(df, x='cut', y='depth', title='Price by Cut (Boxenplot)',template='plotly_dark',color_discrete_sequence=['lime'])
st.plotly_chart(fig12)