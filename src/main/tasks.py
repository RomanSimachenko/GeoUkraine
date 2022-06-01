from celery import shared_task
from src.main.load.load_db import main


@shared_task
def update_universities():
    main()