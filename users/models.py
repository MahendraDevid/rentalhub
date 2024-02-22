from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    userid = models.AutoField(primary_key=True)

    # Menambahkan related_name untuk menghindari konflik dengan relasi yang ada di model auth
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',  # Menggunakan nilai yang berbeda
        blank=True,
        verbose_name='groups',
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_set',  # Menggunakan nilai yang berbeda
        blank=True,
        verbose_name='user permissions',
        help_text='Specific permissions for this user.',
        error_messages={
            'unique': ("This user's permissions must be unique."),
        },
    )

    def __str__(self):
        return self.username
    userid = models.CharField(primary_key=True, max_length=4, unique=True)

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        # Cek apakah ID pengguna sudah ada
        if not self.userid:
            last_user = User.objects.order_by('-userid').first()
            if last_user:
                last_id = int(last_user.userid[1:])  # Ambil angka dari ID terakhir
                new_id = 'U' + str(last_id + 1).zfill(3)  # Format ulang ID baru dengan format 'U000'
            else:
                new_id = 'U000'  # Jika belum ada ID pengguna lain, gunakan 'U000'
            self.userid = new_id
        super().save(*args, **kwargs)
