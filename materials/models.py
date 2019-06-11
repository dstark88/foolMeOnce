from django.db import models


# class Article(models.Model):
#     article_text = models.CharField(max_length=2000)
#     pub_date = models.DateTimeField('date published')
#     def __str__(self):
#         return self.article_text
# def was_published_recently(self):
#     now = timezone.now()
#     return now - datetime.timedelta(days=1) <= self.pub_date <= now
