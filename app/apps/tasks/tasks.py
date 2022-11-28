import time
from celery import shared_task
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

@shared_task(queue='queue1')
def test_celery_task(n):
    logger.info(f'Running celery test task of size {n}')

    time.sleep(3)
    for i in range(n):
        logger.info(f'Step {i}')

    logger.info('Finished task!')
    
    return True