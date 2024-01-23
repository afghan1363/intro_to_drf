from celery import shared_task
from django.core.mail import send_mail

from vehicle.models import Car, Moto


@shared_task
def check_milage(pk, model):
    if model == 'Car':
        instance = Car.objects.filter(pk=pk).first()
    else:
        instance = Moto.objects.filter(pk=pk).first()
    if instance:
        prev_milage = -1
        for m in instance.milage.all():
            if prev_milage == -1:
                prev_milage = m.milage

            else:
                if prev_milage < m.milage:
                    print('Неверный пробег')
                    break


def check_filter():
    filter_price = {'price__lte': 5000}
    if Car.objects.filter(**filter_price).exists():
        # send_mail(
        #     subject='У нас есть авто',
        #     message='Мы нашли для Вас машину',
        #     from_email='mail@mail.com',
        #     recipient_list=[user.email]
        # )
        print('ФИЛЬТРРРР')
