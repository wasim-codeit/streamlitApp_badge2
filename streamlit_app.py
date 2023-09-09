import streamlit
import pandas

streamlit.header("Fruityvice Fruit Advice!")

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response.json())

streamlit.title('My hobby is to travel the world')
streamlit.title('My skill is to serve the world to be healthy')

streamlit.header('🍟 Breakfast Menu 🥪')
streamlit.text('🥩 Omega 3 & Blueberry oat meal')
streamlit.text('🥨 kale, spinach & rocket smoothie')
streamlit.text('🥚 hard-boiled free Range Egg')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
#streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

#Displays selected fruits
fruits_selected= streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

# Display the table on the page.
#streamlit.dataframe(my_fruit_list)
