# Create your models here.
from django.db import models
from cars.models import Mobil
from users.models import User

class Penyewaan(models.Model):
    PenyewaanID = models.CharField(max_length=5, primary_key=True)  # Menggunakan CharField untuk ID dengan format khusus
    MobilID = models.ForeignKey(Mobil, on_delete=models.CASCADE)
    UserID = models.ForeignKey(User, on_delete=models.CASCADE)
    TanggalSewa = models.DateField()
    Status = models.CharField(max_length=10, choices=(('Proses', 'Proses'), ('Konfirmasi', 'Konfirmasi')))

    def save(self, *args, **kwargs):
        if not self.PenyewaanID:
            last_penyewaan = Penyewaan.objects.order_by('-PenyewaanID').first()
            if last_penyewaan:
                last_id = int(last_penyewaan.PenyewaanID[1:])  # Ambil angka dari ID terakhir
                new_id = 'R' + str(last_id + 1).zfill(3)  # Format ulang ID baru dengan format 'R000'
            else:
                new_id = 'R000'  # Jika belum ada ID penyewaan lain, gunakan 'R000'
            self.PenyewaanID = new_id
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Penyewaan {self.PenyewaanID}"
