from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from django.template.loader import render_to_string
from notifikasi.models import Pengguna

class Command(BaseCommand):
    help = 'Mengirim email notifikasi ke pengguna tertentu.'

    def add_arguments(self, parser):
        parser.add_argument('user_id', type=int, help='ID dari pengguna yang akan dikirimi email')
        parser.add_argument('pesan', type=str, help='Isi pesan yang akan dikirimkan')

    def handle(self, *args, **kwargs):
        user_id = kwargs['user_id']
        pesan_custom = kwargs['pesan']

        try:
            pengguna = Pengguna.objects.get(pk=user_id)
        except Pengguna.DoesNotExist:
            self.stderr.write(self.style.ERROR(f'Pengguna dengan ID {user_id} tidak ditemukan.'))
            return

        # Render template teks menjadi sebuah string
        context = {'pengguna': pengguna, 'pesan': pesan_custom}
        isi_email = render_to_string('notifikasi/email_pemberitahuan.txt', context)

        # Kirim email (yang akan dicetak ke konsol)
        send_mail(
            subject='Pemberitahuan Penting Untuk Anda',
            message=isi_email,
            from_email='noreply@proyekdjango.com', 
            recipient_list=[pengguna.email],
            fail_silently=False,
        )

        self.stdout.write(self.style.SUCCESS(f'Email untuk "{pengguna.nama}" telah berhasil "dikirim" ke konsol.'))