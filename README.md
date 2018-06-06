# Membuat Basic Twitter Phising dengan Flask

berikut adalah repository saya berlatih menggunakan salah satu framework dari Python yaitu Flask, dengan membuat sebuah halaman phising untuk twitter,

Sebelumnya apa itu Phising? Intinya dalah suatu metode untuk melakukan penipuan dengan mengelabui target dengan maksud untuk mencuri akun target. Istilah ini berasal dari kata “fishing” = “memancing” korban untuk terperangkap dijebakannya. Phising bisa dikatakan mencuri informasi penting dengan mengambil alih akun korban untuk maksud tertentu.

Bukan untuk berniat jahat ini hanya sekedar sharing saja syukur-syukur buat sobat dumay yang belum tau bahayanya phising bisa jadi lebih berhati-hati.

Langsung saja, tahapnya adalah:

- menyiapkan halaman login twitter terlebih dahulu dengan mengcopy and paste, lalu sedikit mengeditnya untuk method pada form, dan menambahkan meta tags supaya terlihat real.
- menyiapkan database MySQL.
- membuat halaman untuk melihat data username dan password yang masuk.
- setelah semua siap tinggal di-deploy.

Nah, lalu bagaimana supaya mendapatkan user twitter sendiri? ada berbagai macam metode, tapi yang paling basic menurut saya adalah:

- membuat akun twitter baru
- siapkan meta tags pada halaman phising dengan hal-hal yang berkaitan tentang isu terkini supaya seolah-olah seperti link berita asli.
- apa fungsi meta tags? fungsinya yaitu, seperti yang biasa kalian lihat di akun-akun portal berita, saat posting berita pasti ada card semacam preview dari isi berita tersebut.
- nah setelah semua siap, barulah gunakan akun twitter baru yang sudah dibuat, cari twit dengan ritweet terbanyak tentang isu yang sudah disiapkan pada tags.
- reply tweet tersebut dengan link phising yang sudah disiapkan, buat semenarik mungkin.

Nah sekian ajadeh basic phising menurut saya, lagian saya cuma numpang latihan pake Flask untuk membuat web app.

