from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)


class SubCategory(models.Model):
    category = models.ForeignKey('main.Category', related_name='sub_categories', on_delete=models.CASCADE, null=True)

    name = models.CharField(max_length=100)


class Types(models.Model):
    sub_category = models.ForeignKey('main.SubCategory', related_name='Types', on_delete=models.CASCADE, null=True)

    name = models.CharField(max_length=100)
