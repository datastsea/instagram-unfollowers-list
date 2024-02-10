import sys
import time

from bs4 import BeautifulSoup
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager

TIME_WAIT = 10

CHROME_DRIVER_PATH = './driver/121/chromedriver'
INSTAGRAM_URL = 'https://www.instagram.com'


def get_follow_list(driver: WebDriver, id: str, tag: str) -> list:
    """
    태그(followers, following)에 맞는 팔로우 리스트를 가져온다.
        Args:
            driver (WebDriver): 크롬 브라우저 드라이버
            id (str): 아이디 값
            tag (str): 태그 값 (followers, following)
        Returns:
            팔로우 list 반환
    """
    # Move to Follow Page
    driver.get(INSTAGRAM_URL + f'/{id}/{tag}/')
    time.sleep(TIME_WAIT)
    
    # Scroll Down to Get Follow List
    old_height, new_height = 0, 1
    dialog_element = "document.getElementsByClassName('_aano')[0]"
    while old_height != new_height:
        old_height = driver.execute_script(f'return {dialog_element}.scrollHeight')
        driver.execute_script(f'{dialog_element}.scrollTo(0, {dialog_element}.scrollHeight)')
        time.sleep(TIME_WAIT)
        new_height = driver.execute_script(f'return {dialog_element}.scrollHeight')
    
    # Parsing
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    follow_list = [follow.get_text() for follow in soup.find_all('a', ['notranslate'])]

    print(f'{tag}:', follow_list)
    print(f'total count: {len(follow_list)}\n')
    return follow_list


def main(driver: WebDriver, id: str, pw: str):
    ## Login
    driver.get(INSTAGRAM_URL)
    driver.find_element(by=By.NAME, value='username').send_keys(id)
    driver.find_element(by=By.NAME, value='password').send_keys(pw)
    driver.find_element(by=By.XPATH, value='//*[@id="loginForm"]/div[1]/div[3]/button').submit()

    try:
        driver.find_element(by=By.ID, value='slfErrorAlert')
        print('Invalid ID or password')
        return
    except:
        driver.find_element(by=By.XPATH, value='//main/div/div/div/div/div').click() # Click Later Button
    
    ## Get List
    followers_list = get_follow_list(driver, id, 'followers')
    following_list = get_follow_list(driver, id, 'following')

    ## Calculate Unfollowers
    unfollowers_list = list(set(following_list) - set(followers_list))
    print('unfollowers:', unfollowers_list)
    print(f'total count: {len(unfollowers_list)}')


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: python follow.py <ID> <PASSWORD>')
        exit(1)

    ## Connect Driver
    # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install())) # automatic
    driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH) # manual
    driver.implicitly_wait(TIME_WAIT)

    main(driver, sys.argv[1], sys.argv[2])

    ## Close Driver
    driver.close()