from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from web_tools_demos.web.models import Employees

UserModel = get_user_model()


# Този сигнал се задейства когато се направи post_save върху модела Employees, тоест когато се създаде
# нов запис в модела тогава ще се извика този сигнал и ще се изпълни кодът там
@receiver(post_save, sender=Employees)
def hande_employee_created(*args, **kwargs):
    print(args)
    print(kwargs)


@receiver(post_save, sender=UserModel)
def create_employee_on_user_created(instance, created, *args, **kwargs):
    if not created:
        return

    Employees.objects.create(user_id=instance.pk)

