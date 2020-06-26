from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=50)
    hod = models.CharField(max_length=50, default=1)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Requestor(models.Model):
    name = models.CharField(max_length=50)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Work(models.Model):
    name = models.CharField(max_length=50)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Location(models.Model):
    name = models.CharField(max_length=50)
    location_summary = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name', )


class Shelf(models.Model):
    label = models.CharField(max_length=20)
    shelf_summary = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.label

    class Meta:
        verbose_name_plural = 'Shelves'
        ordering = ['label']
