import streamlit as st
import functions
import functions2


functions2.load_data()
# add a title
st.title(functions2.today_date())
st.title(functions2.app_name())
st.subheader(functions2.creator())
# add text

st.text("With this app, you can add shopping list app consist of :")
st.text("- item name")
st.text("- price (in dollar)") 
st.text("- quantity of the item")

import streamlit as st

# define a dictionary to store the shopping list
shopping_list = {}

# create a form to get user input
with st.form(key='shopping_form'):
    st.header('Shopping List App')

    # get user inputs
    item = st.text_input('Enter shopping item:')
    price = st.number_input('Enter price of the item:', min_value=0.0, step=0.01)
    quantity = st.number_input('Enter quantity of the items:', min_value=0)

    # submit button
    submit_button = st.form_submit_button(label='Add to shopping list')

# if the user has entered information and clicked the submit button, store it in the shopping list
if submit_button:
    if item and price and quantity:
        shopping_list[item] = {'price': price, 'quantity': quantity}
        st.success(f'{item} added to shopping list!')

# display the shopping list
if shopping_list:
    st.header('Shopping List')
    for item, info in shopping_list.items():
        st.write(f'{item}: {info["quantity"]} piece(s) at ${info["price"]} each')
