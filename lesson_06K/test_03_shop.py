
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_shop_checkout() -> None:
    driver = webdriver.Firefox()
    total_text = ""

    try:
        driver.get("https://www.saucedemo.com/")
        wait = WebDriverWait(driver, 15)

        # Авторизация
        username = wait.until(
            EC.visibility_of_element_located(
                (By.ID, "user-name")
            )
        )
        username.send_keys("standard_user")

        driver.find_element(
            By.ID, "password"
        ).send_keys("secret_sauce")

        wait.until(
            EC.element_to_be_clickable(
                (By.ID, "login-button")
            )
        ).click()

        # Добавление трёх товаров
        products = [
            "sauce-labs-backpack",
            "sauce-labs-bolt-t-shirt",
            "sauce-labs-onesie",
        ]

        for product in products:
            button = wait.until(
                EC.element_to_be_clickable(
                    (
                        By.CSS_SELECTOR,
                        f"[data-test='add-to-cart-{product}']"
                    )
                )
            )
            button.click()

        # Переход в корзину
        wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "[data-test='shopping-cart-link']")
            )
        ).click()

        # Оформление заказа
        wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "[data-test='checkout']")
            )
        ).click()

        # Заполнение данных покупателя
        customer = {
            "first-name": "Екатерина",
            "last-name": "Тестовая",
            "postal-code": "123456",
        }

        for field_name, value in customer.items():
            field = wait.until(
                EC.visibility_of_element_located(
                    (By.ID, field_name)
                )
            )
            field.send_keys(value)

        wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "[data-test='continue']")
            )
        ).click()

        # Получение итоговой стоимости
        total_element = wait.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "[data-test='total-label']")
            )
        )
        total_text = total_element.text

        print("Итоговая стоимость:", total_text)

    finally:
        driver.quit()

    # Проверка после закрытия браузера
    assert total_text == "Total: $58.29", (
        f"Ожидалось $58.29, получено: {total_text}"
    )
