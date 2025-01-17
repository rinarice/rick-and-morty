from characters.scraper import sync_characters_with_api

from celery import shared_task


@shared_task
def run_sync_with_api() -> None:
    return sync_characters_with_api()
