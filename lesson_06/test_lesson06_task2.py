
import json
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


BASE_URL = "https://gitflic.ru"
SESSION_DIR = Path.home() / ".skypro_gitflic_sessions"


def login_with_cookies(driver, username: str) -> str:
    driver.get(BASE_URL)
    driver.delete_all_cookies()

    cookie_file = SESSION_DIR / f"{username}.json"

    with cookie_file.open(encoding="utf-8") as file:
        cookies = json.load(file)

    for cookie in cookies:
        driver.add_cookie(cookie)

    driver.refresh()

    driver.get(f"{BASE_URL}/project")

    WebDriverWait(driver, 15).until(
        lambda browser: f"@{username}" in browser.find_element(
            By.TAG_NAME, "body"
        ).text,
        message=f"Не удалось подтвердить вход под {username}",
    )

    driver.get(f"{BASE_URL}/user/{username}")

    WebDriverWait(driver, 15).until(
        EC.url_contains(f"/user/{username}")
    )

    return driver.current_url


def test_session_storage_auth() -> None:
    driver = webdriver.Chrome()

    try:
        url_user1 = login_with_cookies(driver, "kate_1")
        url_user2 = login_with_cookies(driver, "kate_2")

        assert url_user1.rstrip("/") == (
            "https://gitflic.ru/user/kate_1"
        )
        assert url_user2.rstrip("/") == (
            "https://gitflic.ru/user/kate_2"
        )
        assert url_user1 != url_user2

    finally:
        driver.quit()
