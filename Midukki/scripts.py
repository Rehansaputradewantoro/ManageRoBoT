START_TXT = """
Halo 👋 {mention}

Saya <b>{bot}</b> ✨ manajemen Grup telegram tingkat lanjut

Saya di sini untuk membantu Anda mengelola grup Anda! Tekan /bantu untuk mengetahui lebih lanjut tentang cara menggunakan saya secara maksimal..!

Bergabunglah dengan <b><a href=http://t.me/Revanstoreya>saluran berita saya</a></b> untuk mendapatkan informasi tentang semua pembaruan terkini
"""

HELP_TXT = """
👋 <b>Halo {mention}!</b>

Saya Dapat Memandu Anda Melalui Semua Fitur Keren <b>{bot}</b> Dan Cara Menggunakannya dengan Benar. Gunakan Tombol Di Bawah Untuk Menavigasi Semua Modul

📚 <u><b>Banyak Perintah</b></u>:

- /start : Mulai saya! Anda mungkin sudah menggunakan ini!.
- /help : Mengirim pesan ini; Saya akan bercerita lebih banyak tentang model!
- /about : Mengirim pesan ini; Saya akan bercerita lebih banyak tentang diri saya!
- /donate : Memberimu info tentang cara mendukungku dan penciptaku!

<b>Semua perintah dapat digunakan dengan yang berikut ini: [ / ]</b>
"""

ABOUT_TXT = """
[{name}](t.me/{username}) Was created on September 4, 2022
Saat ini kami sedang mengembangkannya sebuah bot, using only the Pyrogram library.

➾ Developers : Revans503
➾ Language : Python3
➾ Framework : Pyrogram
➾ Database : Mongo db
"""

DONATE_TXT = """
Jika Anda menyukai proyek saya ini, Anda dapat berdonasi dengan mengklik tautan yang diberikan

Dev : [Revans](t.me/Revans503)
Paytm : [Click Here](https://t.me/Revans503)
  or UPI `@Revanstoreya`
"""

STATUS_TXT = """
**--{bot}'s STATUS--**

📡 __--Server Status--__
◉ Uptime: `{a}`
◉ CPU Usage: `{b}%`
◉ RAM Usage: `{c}%`
◉ Total Disk Space: `{d}`
◉ Used Space: `{e} ({f}%)`
◉ Free Space: `{g}`

🗃️ __--Database Status--__
◉ Tota Files: `{h}`
◉ Tota Users: `{i}`
◉ Tota Chats: `{j}`
◉ Used Storage: `{k}` 
◉ Free Storage: `{l}`
◉ Total Storage: `{m}` 
"""

AUTO_TXT = """
**--MODULE OF AUTOFILTER--**

● Saya Dapat Memberikan File Di Grup Anda, Caranya Sangat Mudah Cukup Tambahkan Saya Ke Grup Anda Dan Jadikan Saya Admin Di Grup Anda, Itu Saja.. Saya Akan Memberikan File Dari Grup Anda 
      
🔋 **--Usage & Commands--** :

◉ /autofilter : gunakan untuk menghidupkan & mematikan
◉ /set_temp : mengatur suhu hasil baru
◉ /del_temp : menghapus suhu hasil yang disetel
◉ /settings : digunakan untuk mengubah pengaturan autofilter

🔋 **--Supporting Vars--** :

 • `{mention}` : user profile link
 • `{query}` : request text
 • `{group_name}` : group name
"""

MANUAL_TXT = """
**--MODULE OF MANUALFILTER--**

● Filter Adalah Fitur Di Mana Pengguna Dapat Mengatur Balasan Otomatis Untuk Kata Kunci Tertentu Dan Bot Akan Merespon Setiap Kali Kata Kunci Ditemukan Pesannya

🔋 **--Note--** :

1. Bot ini harus memiliki hak istimewa admin.
2. hanya admin yang dapat menambahkan filter dalam chat.
3. tombol peringatan memiliki batas 64 karakter.

🔋 **--Commands and Usage--** :

◉ /add : tambahkan filter dalam obrolan
◉ /filters : mencantumkan semua filter obrolan
◉ /del : menghapus filter tertentu dalam obrolan
◉ /delall : menghapus seluruh filter dalam chat (khusus pemilik chat)
"""

CONNECTION_TXT = """
**--MODULE OF CONNECTIONS**--

● Digunakan untuk menghubungkan bot ke PM untuk mengelola filter
● membantu menghindari spamming dalam grup.

🔋 **--NOTE--** :

1. Hanya admin yang menambahkan koneksi.
2. Kirim <code>/connect</code> untuk menghubungkan saya ke PM Anda

🔋 **--Commands and Usage--** :

◉ /connect : menghubungkan obrolan tertentu ke PM Anda
◉ /disconnect : memutuskan sambungan dari obrolan
◉ /connections: daftar semua koneksi Anda
"""

INFO_TXT = """
**--MODULE OF INFO--**

● Ini adalah fitur tambahan dari bot ini

🔋 **--Commands and Usage--** :

◉ /id : dapatkan id pengguna tertentu.
◉ /info : mendapatkan informasi tentang pengguna.
◉ /json : dapatkan file json pengguna
"""

SPELL_TXT = """
**--MODULE OF SPELLCHECK--**

● Segala Sesuatu Yang Terkait Dengan Modul Periksa Ejaan Ketika Tidak Ada Hasil Filter Otomatis Yang Ditemukan

🔋 **--Commands & Usage--** :

◉ /set_spell : Tetapkan Teks Periksa Ejaan Baru
◉ /del_spell : mulai ulang Pesan Periksa Ejaan

🔋 **--Supporting Vars--** :

 • `{mention}` : user profile link
 • `{query}` : request text 
 • `{title}` : get chat title

> Eg:- /setspell Periksa Ejaan Anda {query}
"""

CAP_TXT = """
**--MODULE OF CUSTOM CAPTION--**

● Gunakan Fitur Ini Untuk Menambahkan Keterangan Khusus Ke File

🔋 **--Commands & Usage--** :

◉ /set_cap : atur keterangan file baru
◉ /del_cap : memulai ulang keterangan file

🔋 **--Supporting Vars--** :

 • {mention} : user profile link
 • {file_name} : file name
 • {size} : file size 
 • {caption} : get original caption
"""

MUTE_TXT = """
**--MODULE OF MUTE--** 🤐

● beberapa orang perlu dibungkam secara publik: spammer, annkyances, atau hanya troll...! modul ini memungkinkan Anda melakukannya dengan mudah dengan menampilkan tindakan umum yang sama, sehingga semua orang akan melihatnya!!

🔋 **--Commands and Usage**-- :

◉ /mute : Bisukan pengguna
◉ /unmute : Mengaktifkan suara pengguna
◉ /tmute : Membisukan pengguna untuk sementara. Contoh nilai waktu: 4m = 4 menit, 3j = 3 jam, 6d = 6 hari
"""

BAN_TXT = """
**--MODULE OF BAN--** 🚫

● beberapa orang perlu diblokir secara publik: spammer, annkyances, atau hanya troll...! modul ini memungkinkan Anda melakukannya dengan mudah dengan menampilkan tindakan umum yang sama, sehingga semua orang akan melihatnya..!

🔋 **--Commands and Usage**-- :

◉ /ban : melarang pengguna
◉ /unban : membatalkan pemblokiran pengguna
◉ /tban : Memblokir sementara pengguna. Contoh nilai waktu: 30 detik = 30 detik, 4 menit = 4 menit, 3 jam = 3 jam
"""

PIN_TXT = """
**--MODULE OF PIN--** 📌

● semua perintah terkait pin dapat ditemukan di sini; terus perbarui obrolan Anda dengan berita terkini dengan pesan sederhana yang disematkan!!

🔋 **--Commands and Usage**-- :

◉ /pin : Sematkan pesan yang Anda balas pesan untuk mengirim pemberitahuan ke anggota grup
◉ /unpin : Melepas sematan pesan yang disematkan saat ini. jika digunakan sebagai balasan, lepaskan pin pesan yang dibalas
"""

ADMIN_PANEL = """
📤 **Admin Only**

- /channel : total channels
- /total : total files
- /delfile : del single files
- /delallfile : del all files
- /skip : skip index file
- /logs : bot logs
- /broadcast : broadcast message
"""

FILE_CAPTION_TXT = """{file_name}"""

SPELLCHECK_TXT = """Hai Tuan
Periksa Ejaan Anda
"""

IMDB_TEMPLATE_TXT = """
🙋‍♂️ Hai {mention} {query} Permintaan Anda sudah siap 👍
"""

SELAMAT DATANG_TXT = """
Hai {sebutkan}

Selamat datang di {obrolan} ❣️
"""

KIRIM_LOGS_A = """
#BOT_STARTED"""

PURGE_TXT = """
**--MODULE PURGE--** 🗑️

Hapus Banyak Pesan Dari Grup!

🔋 **--Perintah dan Penggunaan**-- :

● /purge : Menghapus Semua Pesan Dari Pesan yang Dibalas, Hingga Pesan Saat Ini
"""

TELEGRAPH_TXT = """
**--MODULE TE.LEGRA.PH--** 🗑️

• Lakukan sesuka Anda dengan modul telegra.ph!
• Perintah ini Tersedia dalam goups dan pms
• Perintah ini Dapat digunakan oleh semua orang

🔋 **--Perintah dan Penggunaan**-- :

● /telegraph - Kirimi saya balasan perintah ini dengan file gambar atau video Di Bawah (5MB)
"""

TTS_TXT = """
**--MODUL TTS--** 🗑️

Terjemahkan teks ke ucapan

🔋 **--Perintah dan Penggunaan**-- :

● /tts : mengubah teks menjadi ucapan
"""Hai Tuan
Periksa Ejaan Anda
"""



class Txt(object):
    START_TXT = START_TXT
    HELP_TXT = HELP_TXT
    ABOUT_TXT = ABOUT_TXT
    STATUS_TXT = STATUS_TXT
    AUTO_TXT = AUTO_TXT
    MANUAL_TXT = MANUAL_TXT
    INFO_TXT = INFO_TXT
    CONNECTION_TXT = CONNECTION_TXT
    CAP_TXT = CAP_TXT
    SPELL_TXT = SPELL_TXT
    MUTE_TXT = MUTE_TXT
    BAN_TXT = BAN_TXT
    PIN_TXT = PIN_TXT
    ADMIN_PANEL = ADMIN_PANEL
    PURGE_TXT = PURGE_TXT
    TELEGRAPH_TXT = TELEGRAPH_TXT
    TTS_TXT = TTS_TXT
