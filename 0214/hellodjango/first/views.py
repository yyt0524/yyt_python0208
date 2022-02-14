from django.shortcuts import render

# Create your views here.

from random import sample

from django.http import HttpResponse


def show_index(request):
    # fruits = [
    #     'Apple', 'Orange', 'Pitaya', 'Durian', 'Waxberry', 'Blueberry',
    #     'Grape', 'Peach', 'Pear', 'Banana', 'Watermelon', 'Mango'
    # ]
    # selected_fruits = sample(fruits, 3)
    # content = '<h3>今天推荐的水果是：</h3>'
    # content += '<hr>'
    # content += '<ul>'
    # for fruit in selected_fruits:
    #     content += f'<li>{fruit}</li>'
    # content += '</ul>'
    # return HttpResponse(content)
    fruits = [
        'Apple', 'Orange', 'Pitaya', 'Durian', 'Waxberry', 'Blueberry',
        'Grape', 'Peach', 'Pear', 'Banana', 'Watermelon', 'Mango'
    ]
    selected_fruits = sample(fruits, 3)
    return render(request, 'index.html', {'fruits': selected_fruits})