from django.db.models.signals import post_save
from django.dispatch import receiver

from movies.models import SearchTerm
from movies.tasks import notify_of_new_search_term

import django.dispatch


movie_filled = django.dispatch.Signal()


@receiver(post_save, sender=SearchTerm, dispatch_uid="search_term_saved")
def search_term_saved(sender, instance, created, **kwargs):
    if created:
        # New SearchTerm was created
        notify_of_new_search_term.delay(instance.term)


@receiver(movie_filled)
def movie_details_filled(sender, **kwargs):
    print("Movie is filled.")