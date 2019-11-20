from django.db import models
from django.urls import reverse
import uuid
import os


def get_image_path(instance, filename):
    return os.path.join('photos', str(instance.id), filename)


class ElectronicType(models.Model):
    name = models.CharField(max_length=200, help_text="Enter an electronic type")

    def __str__(self):
        return self.name


class Electronic(models.Model):

    electronicName = models.CharField(max_length=200)
    producer = models.ForeignKey('Producer', on_delete=models.SET_NULL, null=True)
    description = models.TextField(max_length=1000, help_text="Enter a brief description of the electronic")
    electronicType = models.ForeignKey('ElectronicType', on_delete=models.SET_NULL, null=True)
    picture = models.ImageField(upload_to=get_image_path, blank=True, null=True)

    def __str__(self):
        return self.electronicName

    def get_absolute_url(self):
        return reverse('electronic-detail', args=[str(self.id)])


class ElectronicInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text="Unique ID for this particular book across whole market")
    electronic = models.ForeignKey('Electronic', on_delete=models.SET_NULL, null=True)

    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('s', 'Sold'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )
    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='m', help_text='Book availability')

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return '%s (%s)' % (self.id, self.electronic.electronicName)


class Producer(models.Model):

    company_name = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        return '%s' % self.company_name

