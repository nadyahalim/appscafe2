from os import system
 
def view_menu():
 	system("cls")
 	menu = """
 	***==== CAMILLE'S DESSERT CAFE APPS ====***
 	[A] - LIHAT DAFTAR MAKANAN
 	[B] - CARI MAKANAN 
 	[C] - PESAN MAKANAN
 	[D] - UPDATE MENU
 	[E] - HAPUS MENU
 	[F] - TENTANG APLIKASI
 	[Q] - KELUAR
 		"""
 	print(menu)

def verify_ans(char):
	char = char.upper()
	if char =="Y":
		return True
	else:
		return False

def print_header(msg):
	system("cls")
	print(msg)

def create_id_menu():
	today = datetime.now()
	year = today.year
	month = today.month
	hari = today.day
	counter = len(data_menu)+1
	id_menu = str("%4d%02d%02d-H%03d" % (year, month, hari, counter))
	print(id_menu)

def print_data_menu(id_menu = None, all_fields = False, harga = True):
	if id_menu != None and all_fields == False:
		print(f"""
			==MENU DITEMUKAN==
			ID \t:{id_menu}
			Nama \t:{data_menu[id_menu]["nama"]}
			Komposisi \t:{data_menu[id_menu]["komposisi"]}
			Harga \t:{data_menu[id_menu]["harga"]}
					""")
	elif id_menu != None and harga == False:
		print(f"""
			==MENU DITEMUKAN==
			ID \t:{id_menu}
			Nama \t:{data_menu[menu]["nama"]}
			Harga \t:{data_menu[menu]["harga"]}
				""")
	elif all_fields == True:
		for id_menu in data_menu:
			nama = data_menu[id_menu]["nama"]
			komposisi = data_menu[id_menu]["komposisi"]
			harga = data_menu[id_menu]["harga"]
			print(f"ID:{id_menu}\tNAMA:{nama}\tKOMPOSISI:{komposisi}\tHarga:{harga}")

def see_menu():
	print_header("-Lihat SEMUA MENU-")
	if len(data_menu) == 0:
		print("-*MENU MAKANAN*-")
	else:
		print_data_menu(all_fields=True)
		input("Klik ENTER untuk kembali ke MENU")

def search_by_menu(menu):
	for id_menu in data_menu:
		if data_menu[id_menu]["nama"] == menu:
			print_data_menu(id_menu=id_menu)
			return id_menu
	else:
		print("<MAKANAN YANG DIPESAN>")
		return False
def get_id_menu_from_name(contact):
	for id_menu in data_menu:
		if data_menu[id_menu]["nama"] == id_menu:
			return id_menu

def find_menu():
	print_header("<CARI MENU NAMA>\n")
	nama = input("Nama makanan yang ingin dicari : ")
	result = search_by_menu(nama)
	input("Klik ENTER untuk kembali ke MENU")

def order_menu():
	print_header("//PESAN MENU//\n")
	nama = ""
	while True:
		if nama == "Q":
			break
		nama = input("Ingin memesan apa : ")
		result = search_by_menu(nama) 
		if result:
			respon = input("Makanan anda akan segera dibuat")
	input("Klik ENTER untuk kembali ke MENU")

def delete_menu():
	print_header("=MENGHAPUS KONTAK=")
	nama = input("Masukkan Nama Menu yang ingin dihapus : ")
	result = search_by_menu(nama)
	if result:
		respon = input(f"Yakin ingin Menghapus {nama} (Y/N)")
		if verify_ans(respon):
			del data_menu[result]
			print("Menu telah dihapus.")

		else:
			print("Menu Batal dihapus.")
	input("Klik ENTER untuk kembali ke MENU")

def update_nama(menu):
	print(f"Nama Lama\t:{data_menu[menu]['nama']}")
	new_nama = input("Nama Baru\t: ")
	respon = input("Apakah Anda Yakin ingin mengganti nama tersebut (Y/N) : ")
	if verify_ans(respon):
		data_menu[menu]['nama'] = new_nama
		print("-Menu telah di-update-")
	else:
		print("-Menu batal di-update-")

def update_komposisi(menu):
	id_menu = get_id_menu_from_name(menu)
	print(f"Nama\t:{data_menu[menu]['nama']}")
	print(f"Komposisi Lama\t:{data_menu[menu]['komposisi']}")
	new_komposisi = input("Komposisi Baru\t: ")
	respon = input("Apakah Anda Yakin ingin mengganti komposisi tersebut (Y/N) : ")
	if verify_ans(respon):
		data_menu[menu]['komposisi'] = new_komposisi
		print("-Menu telah di-update-")
	else:
		print("-Menu batal di-update-")

def update_harga(menu):
	id_menu = get_id_menu_from_name(menu)
	print(f"Nama \t:{data_menu[menu]['nama']}")
	print(f"Harga Lama\t:{data_menu[menu]['harga']}")
	new_harga = input("Harga Baru\t: ")
	respon = input("Apakah Anda Yakin ingin mengganti harga tersebut (Y/N) : ")
	if verify_ans(respon):
		data_menu[menu]['harga'] = new_harga
		print("-Menu telah di-update-")
	else:
		print("-Menu batal di-update-")

def update_menu():
	print_header("//UPDATE MENU MAKANAN//\n")
	nama = input("Nama makanan yang ingin di-update : ")
	result = search_by_menu(nama)
	if result:
		print("Menu yang ingin diganti : ")
		print("[1].Nama , [2]. Komposisi , [3]. Harga")
		respon = input("Option : ")
		if respon == "1":
			update_nama(result)
		if respon == "2":
			update_komposisi(result)
		if respon == "3":
			update_harga(result)
		input("Klik ENTER untuk kembali ke MENU")

def about_apps():
	print_header("Cafe ini memiliki aplikasi khusus dan memudahkan orang untuk melihat menu, memesan makanan, dll. Aplikasi ini dibuat pada tahun 2020.Makanan yang ada di cafe ini manarik dan affordable banget.")
	input("Klik ENTER untuk kembali ke MENU")


def check_input(char):
	char = char.upper()
	if char == "Q":
		return True
	elif char == "A":
		see_menu()
	elif char =="B":
		find_menu()
	elif char == "C":
		order_menu()
	elif char =="D":
		update_menu()
	elif char =="E":
		delete_menu()
	elif char =="F":
		about_apps()

data_menu = {
	"20201021-H001" : {
	"nama" : "Puding Kopi",
	"komposisi" : "kopi, cinnamon, susu, telur, cornstarch, vanilla extract",
	"harga" : "10000"
	},
	"20201021-H002" : {
	"nama" : "Thai Tea",
	"komposisi" : "teh thai, susu, air, es batu",
	"harga" : "5000"
	}
}
stop = False

while not stop:
	view_menu()
	user_input = input("Pilihan: ")
	stop = check_input(user_input)










