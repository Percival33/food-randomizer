import streamlit as st
import requests

API_LINK = 'http://www.themealdb.com/api/json/v1/1/random.php'

st.set_page_config(page_title="Food randomizer", page_icon="🥦")

st.title('🧀 Food randomizer 🥑')

st.header("Just click a button to see what I've chosen specially for you!")


def get_dish(): 
    meals = requests.get(API_LINK).json()
    try:
        dish = dict()
        random_dish = meals['meals'][0]
        dish['name'] = random_dish['strMeal']
        dish['type'] = random_dish['strArea']
        dish['category'] = random_dish['strCategory']
        dish['picture'] = random_dish['strMealThumb']
        dish['url'] = random_dish['strSource']
    except KeyError:
        st.write("Sorry, I can't think of anythong right now 😰. Please try again later.")
    except:
        st.write("Oh common, just give me a break!")
    return dish

if st.button('Ready to roll 🎲?'):
    dish = get_dish()   
    st.subheader(f"Your food for today is {dish['name']} 🍴")
    st.image(dish['picture'])
    st.markdown(f"It is {dish['category']} coming from {dish['type']} cusine.")
    st.markdown(f"If you want to know details use this [link]({dish['url']})")

st.caption("Powered by [themealdb](https://www.themealdb.com/api.php) and created by [Percival33💙](https://github.com/Percival33)")