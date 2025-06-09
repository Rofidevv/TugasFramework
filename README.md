Menambahkan email penerima :
1. buka shell : python manage.py shell
2. di dalam shell jalankan :
from notifikasi.models import Pengguna
Pengguna.objects.create(nama="Andi Budiman", email="andi.b@example.com")
Pengguna.objects.create(nama="Citra Lestari", email="citra.l@example.com")
exit()

Run Aplikasi :
py manage.py kirimemail 1 "Selamat, akun Anda telah kami verifikasi. Selamat bergabung!"
