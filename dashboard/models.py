from django.db import models

class Airport(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Flight(models.Model):
    flight_no = models.CharField(max_length=20)
    airport = models.ForeignKey(Airport, on_delete=models.CASCADE)
    passengers = models.IntegerField()
    delay = models.FloatField()
    status = models.CharField(max_length=20)

    def __str__(self):
        return self.flight_no


from django.db import models

class FlightData(models.Model):
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name

