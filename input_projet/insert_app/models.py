from django.db import models

# Create your models here.
class Test_ins(models.Model):
    """Model definition for test_ins."""

    # TODO: Define fields here
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    email = models.EmailField(max_length=254)
    image = models.ImageField(upload_to='profile/')

    class Meta:
        """Meta definition for test_ins."""

        verbose_name = 'test_ins'
        verbose_name_plural = 'test_inss'

    def __str__(self):
        """Unicode representation of test_ins."""
        pass
