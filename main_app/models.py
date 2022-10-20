from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator

OWNS = (
    ('Y', 'Yes'),
    ('N', 'No'),
)

class Buyer(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('buyers_detail', kwargs={'pk':self.id})
        
# Create your models here.
class Vinyl(models.Model):
    name = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    year = models.IntegerField()
    buyers = models.ManyToManyField(Buyer)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'vinyl_id': self.id})

class Purchase(models.Model):
    date = models.DateField('Date')
    price = models.PositiveIntegerField(validators=[MinValueValidator(0)])
    own = models.CharField(
        max_length=1,
        choices = OWNS,
        default = OWNS[1][0]
    )
    
    # Create a vinyl_id FK
    vinyl = models.ForeignKey(Vinyl, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.get_own_display()} on {self.date}'

    class Meta:
        ordering = ['-date']