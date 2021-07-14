from selenium.webdriver.common.by import By
from src.testproject.classes import DriverStepSettings, StepSettings
from src.testproject.decorator import report_assertion_errors
from src.testproject.enums import SleepTimingType
from src.testproject.sdk.drivers import webdriver
import pytest


"""
This pytest test was automatically generated by TestProject
    Project: My first Project
    Package: TestProject.Generated.Tests.MyFirstProject
    Test: CP-004-2
    Generated by: Ruben Rodriguez (rdrm.05@gmail.com)
    Generated on 07/14/2021, 22:26:54
"""


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(token="jAoYsZdMEgRqqPtB0JkVcHYdA_A0iOGbXoFE-wqhxVk",
                              project_name="My first Project",
                              job_name="CP-004-2")
    step_settings = StepSettings(timeout=15000,
                                 sleep_time=500,
                                 sleep_timing_type=SleepTimingType.Before)
    with DriverStepSettings(driver, step_settings):
        yield driver
    driver.quit()


@report_assertion_errors
def test_main(driver):
    """Se intentará acceder a la plataforma con un usuario y/o correo no registrado."""
    # Test Parameters
    # Auto generated application URL parameter
    ApplicationURL = "https://www.google.com/"

    # 1. Navigate to '{ApplicationURL}'
    # Navigates the specified URL (Auto-generated)
    driver.get(f'{ApplicationURL}')

    # 2. Navigate to 'http://ecommercetest.local/wp-login.php'
    driver.get("http://ecommercetest.local/wp-login.php")

    # 3. Click 'log'
    log = driver.find_element(By.CSS_SELECTOR,
                              "#user_login")
    log.click()

    # 4. Type 'Test' in 'log'
    log = driver.find_element(By.CSS_SELECTOR,
                              "#user_login")
    log.send_keys("Test")

    # 5. Click 'pwd'
    pwd = driver.find_element(By.CSS_SELECTOR,
                              "#user_pass")
    pwd.click()

    # 6. Type '12345678' in 'pwd'
    pwd = driver.find_element(By.CSS_SELECTOR,
                              "#user_pass")
    pwd.send_keys("12345678")

    # 7. Click 'wp-submit'
    wp_submit = driver.find_element(By.CSS_SELECTOR,
                                    "#wp-submit")
    wp_submit.click()

    # 8. Click 'Unknown username. Check again or try ...'
    unknown_username_check_again_or_try_ = driver.find_element(By.CSS_SELECTOR,
                                                               "#login_error")
    unknown_username_check_again_or_try_.click()
