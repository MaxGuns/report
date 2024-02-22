from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Fungsi untuk melaporkan akun di TikTok
def laporkan_akun(username, password, target_username, reason):
    # Path ke driver Selenium (misalnya, Chrome WebDriver)
    driver = webdriver.Chrome(executable_path='/path/to/chromedriver')

    # Buka halaman TikTok
    driver.get("https://www.tiktok.com/")

    # Tunggu beberapa detik untuk halaman TikTok dimuat sepenuhnya
    time.sleep(5)

    # Temukan tombol "Login" dan klik
    login_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Log in')]")
    login_button.click()

    # Tunggu beberapa detik untuk halaman login dimuat sepenuhnya
    time.sleep(5)

    # Temukan dan isi formulir login
    username_input = driver.find_element(By.CSS_SELECTOR, "input[name='username']")
    username_input.send_keys(username)

    password_input = driver.find_element(By.CSS_SELECTOR, "input[name='password']")
    password_input.send_keys(password)

    # Klik tombol "Log in"
    login_submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    login_submit_button.click()

    # Tunggu beberapa detik untuk masuk ke akun
    time.sleep(10)

    # Buka profil akun yang ingin dilaporkan
    driver.get("https://www.tiktok.com/@" + target_username)

    # Tunggu beberapa detik untuk halaman profil dimuat sepenuhnya
    time.sleep(5)

    # Temukan tombol tiga titik (opsi) di profil akun dan klik
    options_button = driver.find_element(By.CSS_SELECTOR, "button[class*='more']")
    options_button.click()

    # Tunggu beberapa detik untuk menu opsi muncul
    time.sleep(2)

    # Temukan dan klik opsi "Laporkan"
    report_button = driver.find_element(By.XPATH, "//span[contains(text(), 'Report')]")
    report_button.click()

    # Tunggu beberapa detik untuk menu pelaporan muncul
    time.sleep(2)

    # Pilih alasan pelaporan
    reason_option = driver.find_element(By.XPATH, f"//div[contains(text(), '{reason}')]")
    reason_option.click()

    # Tunggu beberapa detik untuk konfirmasi alasan pelaporan
    time.sleep(2)

    # Klik tombol "Submit"
    submit_button = driver.find_element(By.XPATH, "//span[contains(text(), 'Submit')]")
    submit_button.click()

    # Tunggu beberapa detik untuk proses pelaporan selesai
    time.sleep(5)

    # Cek apakah laporan berhasil atau tidak
    success_message = "Your report has been submitted"
    if success_message in driver.page_source:
        print(f"Akun {username} berhasil melaporkan akun {target_username}!")
    else:
        print(f"Akun {username} gagal melaporkan akun {target_username}.")

    # Tutup browser
    driver.quit()

# Fungsi untuk meminta input dari pengguna untuk 50 akun
def get_input():
    print("### Laporan Akun TikTok ###")
    accounts = []
    for i in range(50):
        print(f"### Akun ke-{i+1} ###")
        username = input("Masukkan username TikTok Anda: ")
        password = input("Masukkan password TikTok Anda: ")
        target_username = input("Masukkan username target yang ingin dilaporkan: ")
        print("Pilihan alasan pelaporan:")
        print("1. Inappropriate Content")
        print("2. Bullying or Harassment")
        print("3. Impersonation")
        print("4. Hate Speech or Symbols")
        print("5. Scam or Fraud")
        reason_choice = input("Pilih nomor alasan pelaporan: ")
        reasons = {
            "1": "Inappropriate Content",
            "2": "Bullying or Harassment",
            "3": "Impersonation",
            "4": "Hate Speech or Symbols",
            "5": "Scam or Fraud"
        }
        reason = reasons.get(reason_choice, "Inappropriate Content")
        accounts.append({
            "username": username,
            "password": password,
            "target_username": target_username,
            "reason": reason
        })

    return accounts

# Fungsi untuk menampilkan jumlah akun yang sudah terkumpul
def tampilkan_jumlah_akun(accounts):
    jumlah_akun = len(accounts)
    print(f"Total {jumlah_akun} akun telah terkumpul.")

# Fungsi utama
def main():
    accounts = get_input()
    tampilkan_jumlah_akun(accounts)

    for account in accounts:
        laporkan_akun(account["username"], account["password"], account["target_username"], account["reason"])

# Panggil fungsi main()
if __name__ == "__main__":
    main()
