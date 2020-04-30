from sys import getsizeof
from django.utils import timezone
from secrets import token_hex
from django.db import models
from django.shortcuts import reverse
from . import choices


def random_token():
    return token_hex(6)


class CodePaste(models.Model):
    token = models.CharField(max_length=40, default=random_token, primary_key=True)
    title = models.CharField(max_length=50, null=True, blank=True)
    author = models.CharField(max_length=50, null=True, blank=True)
    body = models.TextField()
    language = models.CharField(choices=choices.LANGUAGE_CHOICE, default=choices.LANGUAGE_DEFAULT, max_length=30)
    created = models.DateTimeField(auto_now_add=True)
    expired = models.CharField(choices=choices.EXPIRED_CHOICE, default=choices.EXPIRED_DEFAULT, max_length=3)
    expired_at = models.DateTimeField()
    objects = models.Manager

    def get_absolute_url(self):
        return reverse('detail', args=[self.pk])

    def get_raw_url(self):
        return reverse('raw', args=[self.pk])

    def get_size(self):
        return getsizeof(self.body)

    def save(self, *args, **kwargs):
        seconds = choices.EXPIRED.get(self.expired)['time']
        self.expired_at = timezone.now() + timezone.timedelta(seconds=seconds)
        super(CodePaste, self).save(*args, **kwargs)
