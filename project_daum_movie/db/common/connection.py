# DB: MariaDB
#   **root
#   - root: RDB계열에 모두 존재하는 계정
#   - 최상위 계정(신급 권한을 가진 계정)

# 예) 문서확인(제 보안등급으로 확인이 불가!!)
# DB에는 개인정보 뿐만 아니라 중요한 데이터가 저장
# 아무나 접근하게 하지 않음
# 계정별로 권한을 주고 접근할 수 있는 DB 및 테이블과
# 기능을 제한함!

# DB관리자 -> 사원별로 계정(+권한)
# 개발1팀 조직
# 팀장 tl_01(tbl_member:WXR, tbl_board:WXR)
# ㄴ 대리 tl_02(tbl_member:WX)
# ㄴ 사원1 tl_03(tbl_board:WR)
# ㄴ 사원2 tl_04(tbl_member:R, tbl_board:R)

# python - pymysql -------------------MariaDB

# ** COMMIT
#   -원본문서 -> "HI" 추가 -> 저장 -> 원본문서(업데이트)
#   - 원본문서 -> "HI" 추가 -> 저장X -> 원본문서(기존과 동일)

# TABLE -> INSERT, UPDATE, DELETE -> COMMIT(안하면) -> 변경X

#우리 DB 구조
# MariaDB(DBMS)
# ㄴ daum(Database)
#       ㄴ tbl_review(Table)

import pymysql

def connection():
    try:
        conn = pymysql.connect(
            host="127.0.0.1",
            port=3306,
            user="root",
            password="12341234",
            db="daum",
            charset="utf8",
            autocommit=True,
            cursorclass=pymysql.cursors.DictCursor
        )
    except pymysql.Error as e:
        print(f"MARIADB 연결 실패 {e}")

