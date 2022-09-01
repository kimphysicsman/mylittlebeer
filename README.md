# 🍻 MyLittleBeer

맥주 추천 웹서비스  

<br />

# 📃 프로젝트 정보

### 1. 제작기간

> 2022.06.02 ~ 06.13

### 2. 참여 인원

> |                    Name                    |  Position   |
> | :----------------------------------------: | :---------: |
> | [김동우](https://github.com/kimphysicsman) | Back, Front |
> |   [김진수](https://github.com/creamone)    | Back, Front |
> |     [이윤지](https://github.com/yunji3)    | Back, Front |
> |    [최민기](https://github.com/mankic)     | Back, Front |

### 3. 역할 분담

> - 김동우 : 사용자가 선호하는 맥주 특징을 고르면 그것과 비슷한 유형의 맥주를 추천 (저장가능)
> - 김진수 : 로그인 / 회원가입 / 회원수정 / 회원탈퇴
> - 이윤지 : 저장된 추천 받은 검색 기록 리스팅 / 삭제 페이지
> - 최민기 : 맥주 정보를 볼 수 있는 리스팅 페이지 (조건을 걸어서 종류별로 리스팅할 수 있게)

<br />

# 📚 기술 스택

### 1. Back-end

> Python3  
> Django  

### 2. Front-end
  
> Javascript  
> Html  
> Css  

<br />

# 📊 ERD

<details>
<summary>ERD</summary>
<div markdown="1" style="padding-left: 15px;">
<img src="https://user-images.githubusercontent.com/52207954/186103086-b7e62343-69bb-46bb-af76-a888db74c8ef.png" width="800px"/>
</div>
</details>

<br />


# 🔑  구현내용

### 1. 데이터 전처리
> 데이터셋의 문자열타입의 리스트를 리스트 타입으로 파싱  
> [코드보러가기](https://github.com/kimphysicsman/mylittlebeer/blob/master/recommend/functions.py#L6)  
> <img width="500" src="https://user-images.githubusercontent.com/68724828/187816783-bbe21a31-9c1f-4cba-8691-cc2a84f680fb.png" /><br />

<br />

### 2. 자카드 유사도 구현
> 맥주의 특징에 대한 유사도를 측정하기위한 자카드 유사도 알고리즘  
> [코드보러가기](https://github.com/kimphysicsman/mylittlebeer/blob/master/recommend/functions.py#L19)

<br />

### 3. 자카드 유사도를 이용한 맥주 추천 기능 구현
> 사용자가 입력한 맥주의 특징들을 받아 DB의 맥주 데이터들과 유사도를 측정하고 가장 유사도가 높은 맥주를 return하는 함수  
> [코드보러가기](https://github.com/kimphysicsman/mylittlebeer/blob/master/recommend/functions.py#L28)



<br />

# 📕 기타 자료

### 1. 기획문서

> [MyLittleBeer - Notion](https://www.notion.so/kimphysicsman/MLB-MyLittleBeer-3c4edfa70eb24593ab1cc9b05f8e6e61)

### 2. 데이터셋 77종류의 맥주 정보

> [Beer_dataset - Github](https://github.com/ghgit1798/Crawling-Preprocessing/blob/main/CBF_Beer/%EB%A7%A5%EC%A3%BC_cbf_data.csv)


### 3. 추천 알고리즘

> [recommend_algorithm](https://colab.research.google.com/drive/1eaEzktpnYVwAdhBeXs2LBt0xSENqSdtl#scrollTo=xdFp-9f7VGnn)

### 4. 발표영상

<table>
  <tbody>
      <td>
        <p align="center"> 22.08.05 발표 </p>
        <a href="https://www.youtube.com/watch?v=FcY93t-2oMI" title="MyLittleBeer 최종발표">
          <img align="center" src="https://user-images.githubusercontent.com/52207954/186103974-c47141f0-3084-4bbc-92c3-ec8f05fca9a6.png" width="300" >
        </a>
      </td>
  </tbody>
</table>
