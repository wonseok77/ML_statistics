import pandas
# django 가상환경에서 cx_Oracle 설치해야 합니다.
# 설치 : 가상환경 프롬프트 > pip install cx_oracle
import cx_Oracle

# 오라클 연결 및 접속하기
def getConnection() :
    # 오라클 연결하기
    dsn = cx_Oracle.makedsn("localhost", 1521, "xe")
    
    # 오라클 접속하기
    conn = cx_Oracle.connect("busan_06", "dbdb", dsn)
    return conn

# 커서 받기
def getCursor(conn) :
    cursor = conn.cursor()
    return cursor

# 접속 정보 및 커서 반납하기
def dbClose(cursor, conn) :
    # 커서 반납 먼저
    cursor.close()
    # 마지막에 접속정보 반납
    conn.close()
    
###### <실제 사용하는 함수> #####



# 한건 행에 대한 딕셔너리 만드는 함수
def getDictType_FetchOne(col_name, row_one):
    dict_row = {}
    
    for i in range(0, len(row_one), 1) : 
        dict_row[col_name[i].lower()] = row_one[i]
    
    return dict_row    



# 주문내역 상세조회-1건조회
def getLogin(id, pw):
    conn = getConnection()
    cursor = getCursor(conn)
    
    sql = """ Select mem_id, mem_pass, mem_name 
                From member 
                Where mem_id = :mem_id
                And   mem_pass = :mem_pass """
    cursor.execute(sql, 
                    mem_id=id, 
                    mem_pass=pw)
    
    # 한건조회
    row = cursor.fetchone()
    
    # row 값이 없는 경우 : 조회 결과가 없는 경우
    # 아이디 또는 패스워드가 틀린 경우 조회 결과 없음..
    # 조회결과 없으면 오류 발생
    if row == None :
        dbClose(cursor, conn)
        return {"rs" : "no"}
    
    # 컬럼명 조회하기
    colname = cursor.description
    col = []
    for i in colname :
        col.append(i[0])

    # 딕셔너리로 데이터 구성하기..
    dict_row = getDictType_FetchOne(col, row)
    dict_row["rs"] = "yes"
    
    dbClose(cursor, conn)
    
    return dict_row
