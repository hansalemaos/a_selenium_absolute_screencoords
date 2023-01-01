# Calculates the absolute screen coordinates of any Selenium element so that you can click on them with every basic automation tool

```python
# Tested with:
# https://github.com/ultrafunkamsterdam/undetected-chromedriver
# Python 3.9.13
# Windows 10

$pip install a-selenium-absolute-screencoords

You need only those 2 functions:
abscoord = get_absolute_screen_coords_of_element(
    driver,x,y,)
coords_clicker.left_click_xy_natural(*abscoord) # Has more options, check it out: https://github.com/hansalemaos/mousekey


# Here is an example:

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from a_selenium2df import get_df
from selenium.webdriver.common.by import By
from a_selenium_kill import add_kill_selenium
from time import sleep
from auto_download_undetected_chromedriver import download_undetected_chromedriver
import undetected_chromedriver as uc
from a_selenium_absolute_screencoords import (
    get_absolute_screen_coords_of_element,
    coords_clicker,
)


@add_kill_selenium  # https://github.com/hansalemaos/a_selenium_kill
def get_driver():
    folderchromedriver = "f:\\seleniumdriver2"
    path = download_undetected_chromedriver(
        folder_path_for_exe=folderchromedriver, undetected=True
    )  # https://github.com/hansalemaos/auto_download_undetected_chromedriver
    driver = uc.Chrome(driver_executable_path=path)
    return driver


if __name__ == "__main__":
    folderchromedriver = "f:\\seleniumdriver3"
    path = download_undetected_chromedriver(
        folder_path_for_exe=folderchromedriver, undetected=True
    )
    driver = get_driver()
    driver.get(
        r"https://github.com/signup?ref_cta=Sign+up&ref_loc=header+logged+out&ref_page=%2F%3Cuser-name%3E%2F%3Crepo-name%3E&source=header-repo"
    )
    sleep(2)
    df = get_df(
        driver,
        By,
        WebDriverWait,
        expected_conditions,
        queryselector="a",
        with_methods=False,
    )  # https://github.com/hansalemaos/a_selenium2df
    abscoord = get_absolute_screen_coords_of_element(
        driver,
        df.aa_offsetLeft.iloc[2] + df.aa_offsetWidth.iloc[2] // 2,
        df.aa_offsetTop.iloc[2],
    )
    coords_clicker.left_click_xy_natural(*abscoord)
	
```




