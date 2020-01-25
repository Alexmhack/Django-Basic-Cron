from django_cron import CronJobBase, Schedule


class AlertCronJob(CronJobBase):
    RUN_EVERY_MINS = 10

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = '3e95f623072941e3a3841a7a2f80909d'

    def do(self):
        print("ALERT JOB RAN")
