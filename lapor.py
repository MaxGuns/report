from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Fungsi untuk melaporkan akun di TikTok dengan beberapa akun
def laporkan_akun_multi(accounts_to_report, reason):
    for account in accounts_to_report:
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
        username_input.send_keys(account['username'])

        password_input = driver.find_element(By.CSS_SELECTOR, "input[name='password']")
        password_input.send_keys(account['password'])

        # Klik tombol "Log in"
        login_submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        login_submit_button.click()

        # Tunggu beberapa detik untuk masuk ke akun
        time.sleep(10)

        # Buka profil akun yang ingin dilaporkan
        driver.get("https://www.tiktok.com/@" + account['target_username'])

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

        # Tutup browser
        driver.quit()

# Daftar akun yang akan digunakan untuk login dan melaporkan
accounts = [
    {
        "username": "Username1",
        "password": "Password1",
        "target_username": "AkunTarget1"
    },
    {
        "username": "Username2",
        "password": "Password2",
        "target_username": "AkunTarget2"
    },
    # Tambahkan akun lainnya di sini sesuai kebutuhan
]

# Alasan pelaporan
reason = "Inappropriate Content"

# Panggil fungsi untuk melaporkan akun dengan beberapa akun yang telah disiapkan
laporkan_akun_multi(accounts, reason)
