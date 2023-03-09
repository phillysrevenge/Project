from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.


class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=10000)
    content = models.TextField(null=True, blank=True)
    date_created = models.DateTimeField(default=timezone.now)
    likes = models.ManyToManyField(User, related_name='likes')

    def __str__(self):
        return f'{self.user.username} - Question'

    def get_absolute_url(self):
        # kwargs helps us return to the specific index of the question
        return reverse('stackbase:question-detail', kwargs={'pk': self.pk})

    def likes_count(self):
        return self.likes.count()


class Answer(models.Model):
    question = models.ForeignKey(
        Question, related_name="answer", on_delete=models.CASCADE)
    name = models.CharField(max_length=500)
    content = models.TextField(null=True, blank=True)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return '%s - %s' % (self.question.title, self.question.user)

    def get_absolute_url(self):
        # kwargs helps us return to the specific index of the question
        return reverse('stackbase:question-detail', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
