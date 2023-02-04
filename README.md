# Instagram Follow Check
인스타그램의 팔로우 여부를 확인하는 프로그램이다. 프로그램을 실행하면 자신의 팔로워/팔로잉 리스트와 함께, 자신이 팔로우 하고 있는 사람들 중, 자신을 팔로우하고 있지 않은 사람들(언팔한 사람들)들의 목록을 보여준다. 프로그램을 실행하면 원격으로 크롬 브라우저가 띄워지고, 로그인부터 자동으로 이루어진다. 이 과정에서 약간의 타임 딜레이가 발생하는데 팔로워/팔로잉 목록이 많다면 더 많은 시간이 소요된다. (띄워진 크롬 브라우저는 프로그램이 완료될 때 자동적으로 종료되므로, 프로그램이 실행 중일때는 해당 브라우저를 건드리면 안된다)

## Update Date
2023-02-04

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

## Usage
1. `python follow.py <ID> <PASSWORD>` 실행
    - `ID`와 `PASSWORD`에는 분석하고 싶은 인스타 계정을 입력
    - 프로그램이 실행되면 `Webdriver Manager`가 자동으로 드라이버 설치
      - 설치된 드라이버 위치: `~/.wdm`
2. 크롬 브라우저가 자동으로 실행되고, 조금만 기다리면 콘솔창에 팔로워/팔로잉 리스트와 함께 언팔한 사람들의 리스트 제공 
    - 만약 팔로우 리스트를 제대로 불러오지 못했다면, `follow.py` 파일 내의 `TIME_WAIT`(초 단위) 값을 늘림
    - 만약 인터넷이 빠른 환경이면, `TIME_WAIT` 값을 줄임으로써 조금 더 빠르게 프로그램 실행 가능

## Reference
- 크롬 브라우저: https://www.google.com/intl/ko_kr/chrome/
- 크롬 드라이버: https://chromedriver.chromium.org/downloads
