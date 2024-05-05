from django_apscheduler.jobstores import DjangoJobStore, register_events
from apscheduler.schedulers.background import BackgroundScheduler
from django.core.management import call_command
import contextlib

def db_backup():

    with contextlib.suppress(Exception):
        call_command('dbbackup')
    # try:
    #     call_command('dbbackup')
    # except Exception as e:
    #     print(e)

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_jobstore(DjangoJobStore(), 'default')
    scheduler.add_job(db_backup,'interval',minutes=1,jobstore='default',id='weekly_backup',replace_existing=True)
    register_events(scheduler)
    scheduler.start()

    



