# 2주차 원격 개발 환경 구축 실습

## 1. 프로젝트 설명
Raspberry Pi 원격 접속, 가상환경 세팅 및 GitHub 버전 관리 실습

## 2. 하드웨어 및 네트워크 조건
* 기기: Raspberry Pi
* 네트워크: 노트북 2.4GHz 모바일 핫스팟 사용 예정
* 하드웨어 핀 연결: 2주차는 단순 시스템 정보 확인이므로 GPIO 연결 없음

## 3. 실행 방법 (재현 절차)
1. 원격 접속: `ssh rpi-class` (설정된 별칭 사용)
2. 가상환경 활성화: 프로젝트 폴더로 이동 후 `source .venv/bin/activate` 실행
3. 패키지 설치: `pip install -r requirements.txt` 실행하여 환경 복원
4. 코드 실행: `python3 remote_check.py`