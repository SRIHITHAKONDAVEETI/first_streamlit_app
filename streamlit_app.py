import streamlit
streamlit.title('My parents new healthy diner')
streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text(' 🥗Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔Hard-boiled Free_Range Egg')
streamlit.text('🥑🍞Avacado toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')




import pandas

fruit_listed = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

streamlit.dataframe(fruit_listed)
