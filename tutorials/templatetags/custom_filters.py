from django import template

register = template.Library()

@register.filter
def minutes_to_hours(value):
    hours = value // 60
    minutes = value % 60
    if hours:
        return f"{hours}h {minutes}m"
    return f"{minutes}m"