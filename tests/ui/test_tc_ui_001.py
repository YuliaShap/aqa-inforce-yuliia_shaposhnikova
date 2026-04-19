from pages.home_page import HomePage


def test_check_availability(driver, base_url):
    home = HomePage(driver)

    home.open(base_url)
    home.wait_for_check_in()
    home.select_dates("2026-04-20", "2026-04-21")

    home.click_check_availability()

    assert "available" in driver.page_source.lower()