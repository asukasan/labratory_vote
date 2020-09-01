from django import template

register = template.Library()
@register.filter
def count(value1, list2):
    sum = 0
    for l in list2:
        if value1 > l.rank:
            sum += 1
    #自分の順位を表示するために+1をしとく        
    sum += 1        
    return sum        
