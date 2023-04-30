import json
import pandas as pd
import requests


def get_data(url: str):
    response = requests.get(url)
    raw_data = response.content.decode("utf-8")
    json_data = json.loads(raw_data)
    return json_data


def get_meals_categories():
    data = get_data(
        'https://www.themealdb.com/api/json/v1/1/categories.php')
    categories = pd.DataFrame(data['categories'])
    return categories['strCategory'].values.tolist()


def get_meals_by_category(category: str):
    data = get_data(
        'https://www.themealdb.com/api/json/v1/1/filter.php?c={}'.format(category))
    meals = pd.DataFrame(data['meals'])
    mapped_meals = []
    for _, meal in meals.iterrows():
        mapped_meals.append({
            'mealId': meal['idMeal'],
            'name': meal['strMeal']
        })
    return mapped_meals


def get_meal_details(mealId: str):
    data = get_data(
        'https://www.themealdb.com/api/json/v1/1/lookup.php?i={}'.format(mealId))
    meal = pd.DataFrame(data['meals']).head(1)
    return {
        'mealId': meal['idMeal'].values[0],
        'name': meal['strMeal'].values[0],
        'instructions': meal['strInstructions'].values[0],
        'category': meal['strCategory'].values[0],
        'area': meal['strArea'].values[0],
        'imageUrl': meal['strMealThumb'].values[0]
    }
