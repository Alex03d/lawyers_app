from django.shortcuts import render

from .models import Contract


def index(request):
    contracts = (
        Contract.objects.all().
        select_related('name', 'client')
    )
    context = {
        'contracts': contracts,
    }
    return render(request, 'contracts/index.html', context)


def contracts_list(request):
    # Адрес шаблона сохраним в переменную, это не обязательно, но удобно
    template = 'contracts/contracts_list.html'
    # Строку, которую надо вывести на страницу, тоже сохраним в переменную
    title = 'Список соглашений'
    # Словарь с данными принято называть context
    context = {
        # В словарь можно передать переменную
        'title': title,
        # А можно сразу записать значение в словарь. Но обычно так не делают
        'text': 'Список адвокатских соглашений',
    }
    # Третьим параметром передаём словарь context
    return render(request, template, context)
