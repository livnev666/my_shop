from celery import shared_task
from django.core.mail import send_mail

from .models import Order


@shared_task
def order_created(order_id):
    """
    Задача: отправить уведомление по электронной почте при
    успешном создании заказа.
    """
    order = Order.objects.get(id=order_id)
    subject = 'Order nr. {}'.format(order.id)
    message = 'Уважаемый {},\n\nВы успешно разместили заказ.\
                  Ваш идентификатор заказа {}.'.format(order.first_name, order.id)
    mail_sent = send_mail(subject, message, 'livnev@gmail.com', [order.email])
    return mail_sent
