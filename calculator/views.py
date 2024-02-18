from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, reverse
DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }

from django import forms

class DishForm(forms.Form):
    dish = forms.CharField(label='dish', max_length=100)


def home_view(request):
    template_name = 'calculator/home.html'
    dishes = [
        'Omlet',
        'pasta',
        'buter'
    ]
    context = {
        'dishes': dishes
    }
    return render(request, template_name, context)

def index(request):
    template_name = 'calculator/index.html'
    context = {}
    form = DishForm(request.GET)
    if form.is_valid():
        params = form.data.dict()
        dish = str(params['dish']).upper()
        coutn_ingrs = int(params["count_ingrs"])
        # count_ingridients = request.GET['count_ingrs']
        recipe = {}
        for dish_dict, ingridients_dict in DATA.items():
            if dish_dict.upper() == dish:
                for key, value in ingridients_dict.items():
                    if coutn_ingrs != 0:
                        ingridient = key
                        result_amount = value * coutn_ingrs
                        recipe.setdefault(ingridient,result_amount)
                    else:
                        ingridient = key
                        result_amount = value
                        recipe.setdefault(ingridient,result_amount)
        # context = {
        #     'recipe': recipe
        # }
        context.setdefault('recipe',recipe)

    return render(request, template_name, context)