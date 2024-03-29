from django.http import HttpResponse


# Този декоратор проверява дали потребителят е в подадените групи

def allow_groups(groups=None):
    if groups is None:
        groups = []

    def decorator(view_func):
        def wrapper(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return HttpResponse('Not authenticated!')

            if request.user.is_superuser:
                return view_func(request, *args, **kwargs)

            user_groups = request.user.groups.filter(name__in=groups)

            if not user_groups:
                return HttpResponse('Not in any of the allowed groups')

            return view_func(request, *args, **kwargs)

        return wrapper

    if callable(groups):
        func = groups
        groups = []
        return decorator(func)

    return decorator
