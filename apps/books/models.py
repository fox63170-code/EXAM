# from datetime import date
# from django.core.exceptions import ValidationError
# from django.db import models


# def validate_year(value):
#     current_year = date.today().year
#     if value > current_year:
#         raise ValidationError(f"хуета: {current_year}")


# class Book(models.Model):
#     title = models.CharField(max_length=255)
#     author = models.CharField(max_length=255)
#     year = models.IntegerField(validators=[validate_year])
#     is_read = models.BooleanField(default=False)

#     def __str__(self):
#         return self.title


from django.db import models
from django.core.exceptions import ValidationError
from datetime import date

def validate_year(value):
    current_year = date.today().year
    if value > current_year:
        raise ValidationError(f"хуета{current_year}")

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    year = models.IntegerField(validators=[validate_year])
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return self.title
        