from django.db import models


class Blog(models.Model):

    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        # this will put names on admin page instead of BLogs object(1)
        return self.title

    def summary(self):
        return self.body[:100]
        # this will slice content of the body and we can print
        # that much content on page.

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e, %Y')
