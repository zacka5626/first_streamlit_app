import streamlit
streamlit.title('My Parents New Healthy Diner')
streamlit.header('Breakfast Favourites')
streamlit.text('🥣 Omega 3 & blueberry oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Ranfe Eggs')
streamlit.text('🥑🍞 Avacado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list= my_fruit_list.set_index('Fruit')

#lets put a pickup list here so they can pickup the fruits they want to include
fruits_selected= streamlit.multiselect("Pick Some Fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show= my_fruit_list.loc[fruits_selected]

#display table on the page
streamlit.dataframe(fruits_to_show)


#New section to display fruitvice api response
streamlit.header('Fruityvice Fruit Advice!')

import requests
fruitvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruitvice_response.json())

#take json version of the response and normalize it
fruitvice_normalized = pandas.json_normalize(fruitvice_response.json())

#json output it as screen as table
streamlit.dataframe(fruitvice_normalized)
