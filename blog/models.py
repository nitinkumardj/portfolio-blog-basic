from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    image = models.ImageField(upload_to='blog/')
    body = models.TextField()

    def pub_date_only(self):
        return self.pub_date.strftime('%b %e, %Y')

    def summary(self):
        return self.body[:120]

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-pub_date',)
