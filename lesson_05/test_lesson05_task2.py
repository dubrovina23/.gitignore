
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_form_submission() -> None:
    driver = webdriver.Chrome()

    try:
        driver.get("https://httpbin.qa-territory.online/forms/post")

        name_field = driver.find_element(By.NAME, "custname")
        name_field.send_keys("Екатерина")

        submit_button = driver.find_element(
            By.XPATH, "//button[normalize-space()='Submit']"
        )
        submit_button.click()

        WebDriverWait(driver, 10).until(
            EC.title_contains("Форма отправлена")
        )

        assert driver.current_url.endswith("/forms/post")

        assert "Екатерина" in driver.find_element(
            By.TAG_NAME, "body"
        ).text

    finally:
        driver.quit()
