from celery import Celery
from django.contrib.auth import get_user_model
from django.core.mail import send_mail

from quote.models import EmailHistory

app = Celery('celery_tasks', broker='pyamqp://guest@localhost//', backend='rpc://', )


@app.task
def sed_email_celery(template, operator, organization_email):
    """
    send a email with quot object
    """
    try:
        # fail_silently >> if argument is none then use the DEFAULT config
        send_mail('Quote', template, operator, organization_email, fail_silently=False)
        EmailHistory.objects.create(creator=get_user_model().objects.get(user=operator), email=organization_email)
        return None
    except:
        EmailHistory.objects.create(creator=get_user_model().objects.get(user=operator), email=organization_email)
        return None
