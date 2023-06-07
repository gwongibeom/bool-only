# bool-only

bool-only is place only for complaints in seoul digitech high school

## 실행 방법

### 필요 라이브러리 설치

```
pip install -r requirements.txt
```

### 실행

```
flask run
```

## 파일 구조

```

root:.
│  .gitignore 깃 이그노어
│  config.py 환경 설정파일
│  pybo.db db파일
│  README.md 리드미
│
├─.idea ide 관련파일(무관)
│  │  bool-only.iml
│  │  dataSources.local.xml
│  │  dataSources.xml
│  │  discord.xml
│  │  misc.xml
│  │  modules.xml
│  │  python-terminal.xml
│  │  vcs.xml
│  │  workspace.xml
│  │
│  ├─dataSources
│  │      3eeffa12-82c8-4a20-8d93-2fd98c7b06dc.xml
│  │
│  └─inspectionProfiles
│          profiles_settings.xml
│
├─bool 프로젝트 코어 디렉토리
│  │  filter.py 날짜 변환 필터 파일
│  │  forms.py 폼 파일
│  │  models.py db 모델 파일
│  │  __init__.py 메인 파일
│  │
│  ├─static 스테틱 파일(css,js,images)
│  │      create.css
│  │      detail.css
│  │      favicon.svg
│  │      font.css
│  │      index.css
│  │      nav.css
│  │      recommandAndNotRecommand.js
│  │      trend.js
│  │
│  ├─templates 템플릿(html)
│  │  │  base.html 기본 골조 
│  │  │  form_errors.html 폼 에러 
│  │  │  navbar.html 네브바 
│  │  │
│  │  ├─auth
│  │  │      login.html 로그인 페이지
│  │  │      signup.html 회원 가입 페이지
│  │  │
│  │  ├─bool
│  │  │      bool_detail.html 글 보기 페이지
│  │  │      bool_form.html 글 작성 페이지
│  │  │      bool_list.html 글 목록 페이지
│  │  │
│  │  └─profile
│  │          profile.html 프로필 페이지
│  │
│  ├─views
│  │  │  auth_views.py 계정 라우팅
│  │  │  bool_views.py 글 라우팅
│  │  │  comment_views.py 댓글 라우팅
│  │  │  main_views.py 메인 라우팅
│  │  │  profile_views.py 프로필 라우팅
│  │  │
│  │  └─__pycache__
│  │          auth_views.cpython-39.pyc
│  │          bool_views.cpython-39.pyc
│  │          comment_views.cpython-39.pyc
│  │          main_views.cpython-39.pyc
│  │          profile_views.cpython-39.pyc
│  │
│  └─__pycache__
│          filter.cpython-39.pyc
│          forms.cpython-39.pyc
│          models.cpython-39.pyc
│          __init__.cpython-39.pyc
│
├─migrations db 관련 파일
│  │  alembic.ini
│  │  env.py 가상 전역 변수 파일
│  │  README
│  │  script.py.mako
│  │
│  ├─versions
│  │  │  088a426aaba1_.py
│  │  │  139caa0fd3af_.py
│  │  │  1f9bb05708b8_.py
│  │  │  2a0dc91dc978_.py
│  │  │  2c9954fcf6f6_.py
│  │  │  3383ad93e55f_.py
│  │  │  4b8c248c7bac_.py
│  │  │  5b7b729ae9e0_.py
│  │  │  644d42e16dd6_.py
│  │  │  7ec5ff820773_.py
│  │  │  905b69a61dc8_.py
│  │  │  ab32a7d554e1_.py
│  │  │  c385a08a45b5_.py
│  │  │  e94b44a5ae78_.py
│  │  │  eed1484071f0_.py
│  │  │  f14aa9f574cc_.py
│  │  │
│  │  └─__pycache__
│  │          088a426aaba1_.cpython-39.pyc
│  │          139caa0fd3af_.cpython-39.pyc
│  │          1f9bb05708b8_.cpython-39.pyc
│  │          2a0dc91dc978_.cpython-39.pyc
│  │          2c9954fcf6f6_.cpython-39.pyc
│  │          3383ad93e55f_.cpython-39.pyc
│  │          4b8c248c7bac_.cpython-39.pyc
│  │          5b7b729ae9e0_.cpython-39.pyc
│  │          644d42e16dd6_.cpython-39.pyc
│  │          7ec5ff820773_.cpython-39.pyc
│  │          905b69a61dc8_.cpython-39.pyc
│  │          ab32a7d554e1_.cpython-39.pyc
│  │          c385a08a45b5_.cpython-39.pyc
│  │          e94b44a5ae78_.cpython-39.pyc
│  │          eed1484071f0_.cpython-39.pyc
│  │          f14aa9f574cc_.cpython-39.pyc
│  │
│  └─__pycache__
│          env.cpython-39.pyc
│
└─__pycache__
        config.cpython-39.pyc



```