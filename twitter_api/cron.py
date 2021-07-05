# from django_cron import CronJobBase, Schedule


# Schduled job
# class SyncSpreadSheet(CronJobBase):
#     RUN_EVERY_MINS = 120 # every 2 hours

#     schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
#     code = 'twitter_project.my_cron_job'    # a unique code

#     def do(self):
#         print("Hello World")    # do your thing here


def my_scheduled_job():
  print("Hello World")