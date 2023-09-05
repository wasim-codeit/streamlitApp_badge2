import streamlit
import pandas

streamlit.title('My hobby is to travel the world')

streamlit.header('🍟 Breakfast Menu 🥪')
streamlit.text('🥩 Omega 3 & Blueberry oat meal')
streamlit.text('🥨 kale, spinach & rocket smoothie')
streamlit.text('🥚 hard-boiled free Range Egg')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

# Display the table on the page.

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
