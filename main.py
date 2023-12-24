from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Создание экземпляра драйвера Firefox
driver = webdriver.Firefox()

# Переход на страницу авторизации
driver.get("https://cabinet.tgmaps.ru/login")

# Ожидание загрузки страницы авторизации
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.ID, "exampleInputEmail1")))

# Ввод логина
email_input = driver.find_element(By.ID, "exampleInputEmail1")
email_input.send_keys("YOUR_LOGIN")

# Ввод пароля
password_input = driver.find_element(By.ID, "exampleInputPassword1")
password_input.send_keys("YOUR_PASSWORD")

# Нажатие кнопки "Войти"
login_button = driver.find_element(By.CLASS_NAME, "btn-primary")
login_button.click()

# Ожидание успешной авторизации
wait.until(EC.url_to_be("https://cabinet.tgmaps.ru/"))

# Переход на страницу с креативами
driver.get("https://cabinet.tgmaps.ru/creatives")

# Ожидание загрузки страницы с креативами
wait.until(EC.presence_of_element_located((By.CLASS_NAME, "ItemsAds_itemsRows__zp7zt")))

# Открываем файл для записи текста креативов
with open("creativesisusihfhgfhfhfg.docx", "w", encoding="utf-8") as file:
    # Проходим по каждой странице
    page_number = 1
    while True:
        # Находим все элементы с классом "ItemsAds_itemsRows__zp7zt"
        items = driver.find_elements(By.CLASS_NAME, "ItemsAds_itemsRows__zp7zt")

        # Проходим по каждому элементу
        for item in items:
            # Находим все элементы с классом "ItemAd_itemAd__MB8OV"
            creatives = item.find_elements(By.CLASS_NAME, "ItemAd_itemAd__MB8OV")
            # Проходим по каждому креативу
            for creative in creatives:
                try:
                    # Находим элемент с классом "ItemAd_contentAdText__qzXEM" и получаем текст
                    text = creative.find_element(By.CLASS_NAME, "ItemAd_contentAdText__qzXEM").text
                    # Записываем текст в файл
                    file.write(text + "\n")
                    # Добавляем отступ в две красные строки
                    file.write("\n\n")

                except:
                    # Если элемент не найден, переходим к следующему креативу
                    continue

        # Проверяем наличие ссылки на следующую страницу
        next_page_link = driver.find_element(By.XPATH, "//ul[@class='pagination justify-content-center']/li/a[@class='page-link' and text()='{}']".format(str(page_number + 1)))
        if "disabled" in next_page_link.get_attribute("class"):
            break

        # Прокручиваем страницу до ссылки на следующую страницу
        driver.execute_script("arguments[0].scrollIntoView();", next_page_link)

        # Переход на следующую страницу
        driver.execute_script("arguments[0].click();", next_page_link)

        # Ожидание загрузки следующей страницы с креативамир
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "ItemsAds_itemsRows__zp7zt")))

        # Увеличиваем номер страницы
        page_number += 1

# Закрываем браузер
driver.quit()
