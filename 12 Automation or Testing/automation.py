# import time

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.firefox.service import Service

# # Tentukan lokasi geckodriver
# geckodriver_path = "I:/Project Udemy/DataScience/The Complete Python Developer/12 Automation or Testing/geckodriver.exe"

# # Buat Service object dengan geckodriver path
# service = Service(geckodriver_path)

# # Inisialisasi Firefox driver dengan Service
# firefox_browser = webdriver.Firefox(service=service)

# # Maksimalkan jendela browser
# firefox_browser.maximize_window()

# # Buka URL target
# firefox_browser.get("https://www.coursera.org/articles/what-is-a-data-scientist")

# # Cek apakah judul halaman mengandung 'Data Scientist'
# print("Data Scientist" in firefox_browser.title)

# # Tunggu beberapa detik untuk memastikan halaman dimuat
# time.sleep(5)

# # Coba cari elemen pencarian menggunakan ID, CLASS, atau selektor lain jika NAME tidak berhasil
# try:
#     search_box = firefox_browser.find_element(By.NAME, "q")
# except:
#     search_box = firefox_browser.find_element(By.CSS_SELECTOR, 'input[name="q"]')

# # Masukkan teks pencarian
# search_box.send_keys("machine learning")
# search_box.send_keys(Keys.RETURN)

# # Tunggu beberapa detik untuk memastikan hasil pencarian muncul
# time.sleep(5)

# # Ambil dan cetak URL halaman hasil pencarian pertama
# results = firefox_browser.find_elements(By.CSS_SELECTOR, "a.result-title")
# if results:
#     first_result = results[0]
#     print(first_result.get_attribute("href"))

# # Tutup browser setelah pengujian selesai
# firefox_browser.quit()


# # kalo yang ini jalan codenya
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service

# Tentukan lokasi geckodriver
geckodriver_path = "I:/Project Udemy/DataScience/The Complete Python Developer/12 Automation or Testing/geckodriver.exe"

# Buat Service object dengan geckodriver path
service = Service(geckodriver_path)

# Inisialisasi Firefox driver dengan Service
firefox_browser = webdriver.Firefox(service=service)

# Maksimalkan jendela browser
firefox_browser.maximize_window()

# Buka halaman Google
firefox_browser.get("https://www.google.com")

# Tunggu beberapa detik untuk memastikan halaman dimuat
time.sleep(5)

# Cari elemen pencarian di Google
search_box = firefox_browser.find_element(By.NAME, "q")

# Masukkan teks pencarian
search_box.send_keys("data scientist")
search_box.send_keys(Keys.RETURN)

# Cek apakah judul halaman mengandung 'Data Scientist'
print("Data Scientist" in firefox_browser.title)

# Tunggu beberapa detik untuk memastikan hasil pencarian muncul
time.sleep(5)

# Ambil dan cetak URL halaman hasil pencarian pertama
results = firefox_browser.find_elements(By.CSS_SELECTOR, "a h3")
if results:
    first_result = results[0]
    first_result.click()

# Tunggu beberapa detik untuk melihat hasilnya
time.sleep(5)

# Tutup browser setelah pengujian selesai
firefox_browser.quit()
