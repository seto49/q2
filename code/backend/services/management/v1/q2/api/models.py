from django.db import models
import uuid

class Link(models.Model):
    id = models.UUIDField(
        primary_key = True,
        default = uuid.uuid4,
        editable = False)

    reference = models.URLField()
    active = models.BooleanField(default = False)
    created_at = models.DateTimeField(auto_now_add = True)
    last_modified_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.reference
