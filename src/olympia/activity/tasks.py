import commonware.log
from olympia.amo.celery import task
from olympia.amo.decorators import write
from olympia.activity.utils import add_email_to_activity_log_wrapper


log = commonware.log.getLogger('z.amo.activity')


@task
@write
def process_email(message, **kwargs):
    """Parse emails and save activity log entry."""
    res = add_email_to_activity_log_wrapper(message)

    if not res:
        log.error('Failed to save email.')
