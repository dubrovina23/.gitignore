
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_form_validation() -> None:
    driver = webdriver.Edge()

    try:
        driver.get(
            "https://bonigarcia.dev/"
            "selenium-webdriver-java/data-types.html"
        )

        wait = WebDriverWait(driver, 15)

        fields = {
            "first-name": "Иван",
            "last-name": "Петров",
            "address": "Ленина, 55-3",
            "e-mail": "test@skypro.com",
            "phone": "+7985899998787",
            "city": "Москва",
            "country": "Россия",
            "job-position": "QA",
            "company": "SkyPro",
        }

        for name, value in fields.items():
            field = wait.until(
                EC.visibility_of_element_located(
                    (By.NAME, name)
                )
            )
            field.send_keys(value)

        submit_button = wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "button[type='submit']")
            )
        )
        submit_button.click()

        zip_code = wait.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "#zip-code.alert-danger")
            )
        )

        assert "alert-danger" in zip_code.get_attribute("class")

        for name in fields:
            field = wait.until(
                EC.visibility_of_element_located(
                    (By.CSS_SELECTOR, f"#{name}.alert-success")
                )
            )

            assert "alert-success" in field.get_attribute("class")

    finally:
        driver.quit()
