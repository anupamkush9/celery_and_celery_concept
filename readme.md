### command for view the console of celery  worker
#### OR
### starting celery worker

$ celery -A <project_name> worker -l info


===========================================================

### command for viewing the console of celery beat inside the celery worker
#### OR
### command for starting celery beat
 celery -A <project_name>  beat -l info