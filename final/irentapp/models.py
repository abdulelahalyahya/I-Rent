from django.db import models

class irent(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)






class items(models.Model):
    title = models.CharField(max_length=1024)
    content = models.TextField()
    date = models.DateTimeField()
    included = models.BooleanField()


class ask(models.Model):
    items = models.ForeignKey(items, on_delete = models.CASCADE)
    name = models.CharField(max_length=256)
    content = models.TextField()
    added_at = models.DateTimeField(auto_now=True)


