from django.db import models
import os
import uuid

def upload_to(instance, filename):
    ext = filename.split('.')[-1]
    return f'informasi/{uuid.uuid4()}.{ext}'


class Informasi(models.Model):
    KATEGORI_CHOICES = [
        ('app', 'APP'),
        ('tagline', 'Brand Statement / Company Profile Intro'),
        ('alamat', 'Contact'),
        ('visi', 'Visi Misi'),
        ('brandcontent', 'Brand Content'),
        ('program', 'Programs'),
        ('faq', 'Frequently Asked Questions'),
        ('lead', 'Leadership'),
        ('pendaftaran', 'Enrollment'),
        ('medsos', 'Media Sosial'),
    ]

    kategori = models.CharField(max_length=100, choices=KATEGORI_CHOICES)
    judul = models.CharField(max_length=200)
    keterangan = models.TextField()

    gambar = models.ImageField(
        upload_to=upload_to,  # 🔥 pakai uuid biar aman
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.judul} ({self.kategori})"

    # 🔥 AUTO DELETE FILE LAMA SAAT UPDATE
    def save(self, *args, **kwargs):
        try:
            old = Informasi.objects.get(pk=self.pk)
            if old.gambar and old.gambar != self.gambar:
                if os.path.isfile(old.gambar.path):
                    os.remove(old.gambar.path)
        except Informasi.DoesNotExist:
            pass

        super().save(*args, **kwargs)

    # 🔥 AUTO DELETE FILE SAAT DATA DIHAPUS
    def delete(self, *args, **kwargs):
        if self.gambar:
            if os.path.isfile(self.gambar.path):
                os.remove(self.gambar.path)
        super().delete(*args, **kwargs)

class ContactMessage(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"