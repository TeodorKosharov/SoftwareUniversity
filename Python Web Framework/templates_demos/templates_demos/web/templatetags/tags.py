from django.template import Library

register = Library()


@register.simple_tag(name='student_info')
def show_student_info(student):
    return f'My name is {student.name} and I am {student.age}-years old.'


@register.inclusion_tag('tags/nav.html', name='app_nav')
def generate_nav(*args):
    context = {
        'url_names': args
    }

    return context

