import uuid
from django.db import models


class Question(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    question_text = models.TextField(max_length=200)

    class Meta:
        app_label = 'quickstart'

    def __str__(self):
        return str(self.question_text)
