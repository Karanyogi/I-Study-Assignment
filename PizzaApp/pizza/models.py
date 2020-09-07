from django.db import models
from django.conf import settings
from django.urls import reverse

# pip install misaka
import misaka



class Pizza(models.Model):
    name = models.TextField(max_length=25, unique=True)
    price = models.TextField(max_length=10)
    discription = models.TextField(max_length=25)
    discription_html = models.TextField(editable=False)


    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.discription_html = misaka.html(self.discription)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse(
            "pizzas:single",
            kwargs={
                "name": self.name,
                "pk": self.pk
            }
        )

    class Meta:
        ordering = ["-name"]
        unique_together = ["name", "discription"]
