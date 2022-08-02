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

# 여러건에 대한 리스트 + 딕셔너리 만드는 함수
def getDictType_FetchAll(col_name, row):
    # [(1, 2, 3), (4, 5, 6)]
    # 첫번째 for문 : 리스트에서 튜플 가지고 오기
    # 두번째 for문 : 튜플에서 각각의 값을 가지고 오기
    list_row = []
    for tup in row :
        dict_row = {}
        
        for i in range(0, len(tup), 1) :
            dict_row[col_name[i].lower()] = tup[i]
            
        list_row.append(dict_row)
    
    return list_row

# 주문내역 전체 리스트 조회
def getCartList():
    conn = getConnection()
    cursor = getCursor(conn)
    
    sql = """ Select * From cart """
    cursor.execute(sql)
    
    row = cursor.fetchall()
    
    # 컬럼명 조회하기
    colname = cursor.description
    col = []
    for i in colname :
        col.append(i[0])

    # 딕셔너리로 데이터 구성하기..
    row_list = getDictType_FetchAll(col, row)
    
    dbClose(cursor, conn)
    
    return row_list


# 주문내역 상세조회-1건조회
def getCart(no, prod):
    conn = getConnection()
    cursor = getCursor(conn)
    
    sql = """ Select * From cart 
                Where cart_no = :cart_no
                And  cart_prod = :cart_prod """
    cursor.execute(sql, 
                    cart_no=no, 
                    cart_prod=prod)
    
    # 한건조회
    row = cursor.fetchone()
    
    # 컬럼명 조회하기
    colname = cursor.description
    col = []
    for i in colname :
        col.append(i[0])

    # 딕셔너리로 데이터 구성하기..
    dict_row = getDictType_FetchOne(col, row)
    
    dbClose(cursor, conn)
    
    return dict_row

# 주문내역 입력하기
def setCartInsert(id, prod, qty):
    conn = getConnection()
    cursor = getCursor(conn)
    
    # 주문번호 생성을 위한 sql문 작성
    sql = """ Select Decode(substr(max(cart_no), 1, 8), 
                to_char(sysdate, 'yyyymmdd'),
                max(cart_no)+1,
                to_char(sysdate, 'yyyymmdd') || '00001') as max_no
                From cart """
    cursor.execute(sql)    
    # 한건조회
    max_no = cursor.fetchone()
    no = max_no[0]
    
    # 주문내역 입력을 위한 sql문 작성
    sql = """ Insert Into cart(cart_member, cart_no, 
                                cart_prod, cart_qty)
                Values(:cart_member, :cart_no, 
                                :cart_prod, :cart_qty) """
    cursor.execute(sql,
                    cart_member=id,
                    cart_no=no,
                    cart_prod=prod,
                    cart_qty=qty)
    
    conn.commit()
    
    dbClose(cursor, conn)
    
    return "Y"

# 주문내역 입력하기
def setCartDelete(no, prod):
    conn = getConnection()
    cursor = getCursor(conn)
    
    # 주문내역 입력을 위한 sql문 작성
    sql = """ Delete From cart
                Where cart_no = :cart_no
                And cart_prod = :cart_prod """
                
    cursor.execute(sql,
                    cart_no=no,
                    cart_prod=prod)
    
    conn.commit()
    
    dbClose(cursor, conn)
    
    return "Y"

# 주문내역 수정하기
def setCartUpdate(no, prod, qty):
    conn = getConnection()
    cursor = getCursor(conn)
    
    # 주문내역 입력을 위한 sql문 작성
    sql = """ Update cart
                Set cart_qty  = :cart_qty
                Where cart_no = :cart_no
                And cart_prod = :cart_prod """
                
    cursor.execute(sql,
                    cart_qty=qty,
                    cart_no=no,
                    cart_prod=prod)
    
    conn.commit()
    
    dbClose(cursor, conn)
    
    return "Y"