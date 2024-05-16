from django.db import models

# Create your models here.
class Testimonial(models.Model):
    name = models.CharField(max_length=50)
    testimonial = models.TextField()
    picture = models.ImageField(upload_to="testimonials/")
    rating = models.IntegerField()

    def __str__(self):
        return self.testimonial