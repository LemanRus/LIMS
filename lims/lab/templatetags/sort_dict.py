from django import template

register = template.Library()


@register.filter
def sort_dict(given_dict):
    print()
    return sorted(given_dict.items(), key=lambda item: list(item[1])[0].history_date, reverse=True)
