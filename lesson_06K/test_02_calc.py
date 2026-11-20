
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_slow_calculator() -> None:
    driver = webdriver.Chrome()

    try:
        driver.get(
            "https://bonigarcia.dev/"
            "selenium-webdriver-java/slow-calculator.html"
        )

        wait = WebDriverWait(driver, 10)

        delay_field = wait.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "#delay")
            )
        )
        delay_field.clear()
        delay_field.send_keys("45")

        for button_text in ["7", "+", "8", "="]:
            button = wait.until(
                EC.element_to_be_clickable(
                    (
                        By.XPATH,
                        f"//span[normalize-space()='{button_text}']"
                    )
                )
            )
            button.click()

        result = WebDriverWait(driver, 60).until(
            EC.text_to_be_present_in_element(
                (By.CLASS_NAME, "screen"),
                "15"
            )
        )

        assert result

        screen = driver.find_element(By.CLASS_NAME, "screen")
        assert screen.text == "15"

    finally:
        driver.quit()
