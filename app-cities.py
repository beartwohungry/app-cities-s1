


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn')

st.title('World Cities')

df = pd.read_csv('worldcities.csv')

# add slider

pop_slider = st.slider('Choose Populaiton', 0.0, 40.0, 3.6)

# add a multi selector
capital_filter = st.sidebar.multiselect(
     'Capital Selector',
     ['primary', 'admin', 'nan', 'minor'], # options
     ['primary']) # defaults

# input box
form = st.sidebar.form("country_form")
country_filter = form.text_input('Country Name (enter ALL to reset)', 'ALL')
form.form_submit_button("Apply")


# filter by popultion
df = df[df.population >= pop_slider]


# filter by capital
df = df[df.capital.isin(capital_filter)]

# filter by country name
if country_filter!='ALL':
    df = df[df.country == country_filter]


st.map(df)

st.write(df)

fig, ax = plt.subplots()
pop_sum = df.groupby('country')['population'].sum()
pop_sum.plot.bar(ax=ax)
st.pyplot(ax)