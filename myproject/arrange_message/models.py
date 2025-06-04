from django.db import models

class MessageData(models.Model):
    # ID (primary_key, auto_increment) は、特に指定しない限り
    # Django によって自動的に 'id' という名前で作成されます。
    message = models.CharField(max_length=500)
    arrange_message = models.CharField(max_length=500)