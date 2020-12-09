from django.db import models

TOPIC_CHOICES = (
    ('Investing', 'Investing'),
    ('Small Business Banking', 'Small Business Banking'),
    ('Consumer Banking', 'Consumer Banking'),
    ('Wealth Management', 'Wealth Management'),
)

STAR_CHOICES = (
    ('1 Star', '1 Star'),
    ('2 Stars', '2 Stars'),
    ('3 Stars', '3 Stars'),
    ('4 Stars', '4 Stars'),
    ('5 Stars', '5 Stars')
)

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    topic = models.CharField(max_length=25, blank=True, choices=TOPIC_CHOICES)
    feedback = models.CharField(max_length=500)

    def __str__(self):
        return self.name

class Review(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    stars = models.CharField(max_length=25, blank=True, choices=STAR_CHOICES)
    response = models.CharField(max_length=500)

    def __str__(self):
        return self.name