import random

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

from webdriver_manager.chrome import ChromeDriverManager

# Podešavanje servisa
service = Service(ChromeDriverManager().install())

# Pokretanje pretraživača
driver = webdriver.Chrome(service=service)

# Otvori stranicu sa igrom
driver.get("https://igrawordy.netlify.app")


# Funkcija za rešavanje igre
def play_game():
    try:
        # Čekaj da se stranica učita (ukoliko je spor net, 2 sekunde bi bile dovloljno vljd idk)
        time.sleep(2)

        # Klikom na start dugme se pokreće igra
        start_button = driver.find_element(By.ID, "startBtn")
        start_button.click()

        # Čekanje prve reči
        time.sleep(1)

        # Ulazimo u petlju koja prati reči (ograničeno do 100 jer hipotetički može beskonačno dugo da radi)
        for x in range(100):
            try:
                # Pronađi trenutno prikazanu reč
                current_word = driver.find_element(By.ID, "wordDisplay").text

                # Pronađi input polje gde treba upisivati reč
                input_field = driver.find_element(By.ID, "inputField")

                # Unesi reč u input polje
                input_field.send_keys(current_word)

                # Pritisni Enter (ako je potrebno za potvrdu unosa)
                input_field.send_keys(Keys.RETURN)

                # Čekaj da se sledeća reč učita
                time.sleep(0.1)

            except Exception as e:
                print("Greška tokom rešavanja: ", e)
                break

    except Exception as e:
        print("Greška pri pokretanju igre: ", e)
    finally:

        time.sleep(2)

        player_name_field = driver.find_element(By.ID, "playerName")

        player_name_field.send_keys("Selenium" + str(random.randrange(1,999)))

        save_button = driver.find_element(By.ID, "saveNameBtn")

        save_button.click()

        # Čekaj da igra završi
        time.sleep(5)

        # Zatvori pretraživač
        driver.quit()


# Pokreni igru
play_game()
