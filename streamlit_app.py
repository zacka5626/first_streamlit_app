import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError
streamlit.title('My Parents New Healthy Diner')
streamlit.header('Breakfast Favourites')
streamlit.text('🥣 Omega 3 & blueberry oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Ranfe Eggs')
streamlit.text('🥑🍞 Avacado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


#import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list= my_fruit_list.set_index('Fruit')

#lets put a pickup list here so they can pickup the fruits they want to include
fruits_selected= streamlit.multiselect("Pick Some Fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show= my_fruit_list.loc[fruits_selected]

#display table on the page
streamlit.dataframe(fruits_to_show)


#New section to display fruitvice api response
streamlit.header('Fruityvice Fruit Advice!')
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error('Please select a fruit to get a information.')
  else:
    fruitvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
    fruitvice_normalized = pandas.json_normalize(fruitvice_response.json())
    streamlit.dataframe(fruitvice_normalized)
    
except URLError as e:
  streamlit.error()

#Don't run anything past here while we troubleshoot
streamlit.stop()

#import snowflake.connector
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("The Fruit list contains:")
streamlit.dataframe(my_data_rows)

#Allow the end user to add fruit to the list
addmy_fruit = streamlit.text_input('What fruit would you like to add?','kiwi')
streamlit.write('Thanks for adding',addmy_fruit)

my_cur.execute("insert into fruit_load_list values('from streamlit')")
