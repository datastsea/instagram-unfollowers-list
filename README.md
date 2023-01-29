# Instagram Follow Check
- 인스타그램 팔로우 여부 확인
- 프로그램을 실행하려는 컴퓨터에 크롬 브라우저가 설치되어 있어야 함 (프로그램 실행 중에 크롬 브라우저 동작)
- Webdriver Manager로 설치된 드라이버는 `~/.wdm` 위치에 설치됨
- 팔로우 리스트를 가져오는 동안 타임슬립 존재

## Update Date
2023-01-29 (미완)

## Language & Library
- Python 3.9.16
- Selenium 4.8.0 (`pip install selenium`)
- Webdriver Manager 3.8.5 (`pip install webdriver_manager`)
- BeautifulSoup 4.11.1 (`pip install bs4`)
```bash
$ python --version     
Python 3.9.16

$ pip list
Package           Version
----------------- --------
selenium          4.8.0
webdriver-manager 3.8.5
beautifulsoup4    4.11.1
...
```

## Reference
- 크롬 드라이버: https://chromedriver.chromium.org/downloads