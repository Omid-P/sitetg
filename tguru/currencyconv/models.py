from django.db import models
from django.utils import timezone

class Reviews(models.Model):
    #reviewedobject = models.ForeignKey('blog.Post', related_name='reviewss')
    author = models.CharField(max_length=30)
    title = models.CharField(max_length=200)
    rating = models.IntegerField(default=0)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def post(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
    #the __str__ method is called when you print an instance of the review class