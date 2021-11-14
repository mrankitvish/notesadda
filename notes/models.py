from django.db import models

# Create your models here.
class Files(models.Model):
    filename = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='pdfs/')
    cover = models.ImageField(upload_to='covers/', null=True, blank=True)

    def __str__(self):
        return self.filename

    def delete(self, *args, **kwargs):
        self.pdf.delete()
        self.cover.delete()
        super().delete(*args, **kwargs)