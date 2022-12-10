<!-- # server

인하대학교 5호관 건물 내부 길찾기 서비스 "인하대학교를 여행하는 히치하이커를 위한 안내서"의 서버 코드입니다.

서비스 주소 : <a href="http://inhamap.com">http://inhamap.com</a> -->


# 인하대학교를 여행하는 히치하이커를 위한 안내서

## Introduction
- 인하대학교 5호관 건물 내부 길찾기 서비스 **인하대학교를 여행하는 히치하이커를 위한 안내서**의 서버 코드입니다.

- 이 프로젝트는 2022-2 인하대학교 <a href="https://abeek.inha.ac.kr/01_prof/01_portfolio/PlanPrintInfo.aspx?CurrSeq=152095&ViewState=Y">창의적 정보통신 공학설계</a> 과목을 수강하면서 진행되었습니다.

- 서비스 주소
    - <a href="http://inhamap.com">inhamap.com</a>

## Description
<!-- 프로젝트에 대한 간단한 설명 기술
간결하고 명료하게 작성
프로젝트의 가치 전달 -->

### 프로젝트 주제 선정 이유
- 학교에 처음 방문한 외부인, 아직 학교에 익숙하지 않은 학생들은 학교 건물 내부에서 길을 잘 찾지 못 하는 경우가 많습니다.
- 시중의 지도 서비스를 이용해서 건물을 찾는 것까지는 가능하지만, 건물 내부에서 그러한 서비스를 이용해 길을 찾는 것은 거의 불가능합니다.
- 저희 팀은 이러한 문제를 해결하기 위해 학교 건물 내부, 특히 가장 구조가 복잡한 5호관 건물 내부 길찾기 서비스를 만들게 되었습니다.

### 서비스 흐름도
![image](https://user-images.githubusercontent.com/30434779/206861866-dde1b98e-b542-41b8-960b-9b3a553d235a.png)



<!-- TODO: 사진 추가해야함 -->
### 사용 방법
1. <a href="http://inhamap.com">inhamap.com</a>에 접속합니다.
2. 메인 화면에서 출발지와 도착지의 강의실 코드를 작성합니다. 강의실 코드 양식은 5[건물 방향][강의실 번호 세자리] 입니다. (예시: 5N102)
3. submit 버튼을 누릅니다.
4. 만약 빈칸이 있거나 존재하지 않는 강의실을 입력하셨다면 경고창이 뜨고 다시 메인 페이지로 돌아옵니다.
5. 제대로 출발지와 도착지 정보를 입력했다면 건물 약도와 함께 경로 텍스트가 표시됩니다.



## Environment
<!-- 실행환경에 대해 작성
OS, 컴파일러, CPU나 RAM -->
- Amazon Web Services(AWS) Lightsail
- Ubuntu 20.04
- Python 3.8.10
- Flask 2.2.2
- Nginx 1.18.0
- Gunicorn 20.1.0
- Jinja2 3.1.2

## Files
<!-- 각 파일들이 어떤 역할을 하는지 -->
- ```app.py```
    - 프로젝트의 메인 파일입니다. 페이지 라우팅을 담당하고 있습니다.
- ```bfs.py```
    - BFS(너비 우선 탐색) 알고리즘을 사용하여 경로를 탐색하는 함수가 있는 파일입니다.
- ```map.py```
    - 강의실 간의 관계를 딕셔너리 형태로 저장하고 있습니다. 이를 이용해 bfs.py에서 경로를 탐색합니다.
- ```text.py```
    - bfs.py를 이용해서 탐색한 결과를 안내 텍스트로 가공하는 함수가 있는 파일입니다.
    - 사용자가 입력한 출발지, 도착지 정보를 가공하는 함수가 있는 파일입니다.
- ```wsgi.py```
    - Gunicorn을 이용할 때 사용하는 파일입니다.
- ```templates/index.html```
    - 메인 페이지의 HTML 파일입니다.
- ```templates/service.html```
    - 지도와 경로 텍스트를 띄워주는 페이지의 HTML 파일입니다.
- ```templates/error.html```
    - 사용자가 존재하지 않는 강의실을 입력할 경우 에러 메세지를 띄우는 HTML 파일입니다.


<!-- ## Usage
작성한 코드들을 어떻게 실행해야 하는지 가이드라인 -->

## License
> MIT License
>
> Copyright (c) 2022 인하대학교를 여행하는 히치하이커를 위한 안내서
>
> Permission is hereby granted, free of charge, to any person obtaining a copy
> of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
>
> The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
>
>THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
