from django.db import models

class Mobil(models.Model):
    MobilID = models.CharField(max_length=5, primary_key=True)  # Menggunakan CharField untuk ID dengan format khusus
    Merek = models.CharField(max_length=50)
    Model = models.CharField(max_length=50)
    Tahun = models.IntegerField()
    Status = models.CharField(max_length=15, choices=(('Tersedia', 'Tersedia'), ('Sedang Disewa', 'Sedang Disewa')))

    def save(self, *args, **kwargs):
        if not self.MobilID:
            last_mobil = Mobil.objects.order_by('-MobilID').first()
            if last_mobil:
                last_id = int(last_mobil.MobilID[1:])  # Ambil angka dari ID terakhir
                new_id = 'C' + str(last_id + 1).zfill(3)  # Format ulang ID baru dengan format 'C000'
            else:
                new_id = 'C000'  # Jika belum ada ID mobil lain, gunakan 'C000'
            self.MobilID = new_id
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.Merek} {self.Model} ({self.Tahun})"
