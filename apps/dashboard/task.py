from celery import shared_task
from techbox.celery import app
from django.core.mail import send_mail
from apps.dashboard.models import ToolsIssue
import datetime
from django.conf import settings

import pytz

ist = pytz.timezone("Asia/Calcutta")


@shared_task()
def mailtoassignemployee(subject, message, recipient_list):
    try:
        email_from = settings.EMAIL_HOST_USER
        send_mail(subject, message, email_from, recipient_list)
    except Exception as e:
        print(e)
    return "tool assign successfully"


@shared_task()
def status_change():
    print(ist)
    x = ist.localize(datetime.datetime.now())
    issue = ToolsIssue.objects.all()

    for data in issue:
        if data.submitDate < x:
            data.timeOut = True
            data.save()

    return None


@shared_task()
def mail_to_timeover_employee(subject, message, recipient_list):
    try:
        email_from = settings.EMAIL_HOST_USER
        send_mail(subject, message, email_from, recipient_list, fail_silently=False, )
    except Exception as e:
        print(e)
    return "mail send to time over success "


@shared_task()
def remind_to_employee():
    issue = ToolsIssue.objects.filter(timeOut=False)
    x = ist.localize(datetime.datetime.now())


    for emp in issue:
        subject = f'Hello reminder for {emp.techTool.name}'
        message = f'Hi your techtool- {emp.techTool.name} Usage time is complete ' \
                  f'within few days  Please Submit {emp.techTool.name} in office before you ' \
                  f' time is over if you already Submit then skip this mail Have A Good ! {x} day'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [emp.empName.email, ]
        send_mail(subject, message, email_from, recipient_list, fail_silently=False, )

    return "reminder mail successfully  "

@shared_task()
def send_mail_after_create_techtool(subject, message, recipient_list):
    email_from = settings.EMAIL_HOST_USER

    send_mail(subject, message, email_from, recipient_list)

    return "create item successfully "
