from django import template


register = template.Library()


NEWS_ARTICLES = {
   'news': 'N',
   'art': 'A',
}

CENSOR_WORDS = [
    'хайп',
    'жесть',
    'редиска',


]

@register.filter()
def post(value, code='art'):
   """
   value: значение, к которому нужно применить фильтр
   code: код валюты
   """
   postfix = NEWS_ARTICLES[code]

   return f'{value} {postfix}'

@register.filter()
def censor(value):
    """
    text: текст к которому нужно применить фильтр
    """
    for word in CENSOR_WORDS:
        value = value.replace(word[2:], '*' * len(word[2:]))
    return value