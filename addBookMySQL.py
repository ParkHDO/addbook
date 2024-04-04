import sys
import pymysql
from PyQt5.QtWidgets import QApplication

class mysqlDB():
    def __init__(self) -> None:
        pymysql.version_info = (1, 4, 2, "final", 0)
        pymysql.install_as_MySQLdb()
        super().__init__()
        self.connection = pymysql.connect(
            host='localhost',
            user='pa',
            passwd='1234',
            db='pa',
            charset='utf8',
            port=3306,
            cursorclass=pymysql.cursors.DictCursor
        )

    def insert(self, new_name, new_phone, new_filename):
        with self.connection.cursor() as cursor:
            sql = "INSERT INTO addbook (name, phone, filename) VALUES (%s, %s, %s)"
            result = cursor.execute(sql, (new_name, new_phone, new_filename))
            self.connection.commit()
            return result
    
    def update(self, name_key, new_phone, new_filename):
        with self.connection.cursor() as cursor:
            sql = "UPDATE addbook SET phone = %s, filename = %s WHERE name = %s"
            result = cursor.execute(sql, (new_phone, name_key, new_filename))
            self.connection.commit()
            return result
    
    def delete(self, name_key):
        with self.connection.cursor() as cursor:
            sql = "DELETE FROM addbook WHERE name = %s"
            result = cursor.execute(sql, name_key)
            self.connection.commit()
            return result

    def getAllData(self):
        print("여기는 전부 읽기")
        with self.connection.cursor() as cursor:
            sql = "SELECT * FROM addbook"
            
        
    def search(self, any_key):
        with self.connection.cursor() as cursor:
            sql = "SELECT * FROM addbook WHERE 'name' LIKE %s OR phone LIKE %s OR filename LIKE %s"
            key = '%' + any_key + '%'
            cursor.execute(sql, (key, key, key))
            result = cursor.fetchone()
    
    def pause(self):
        input("다음 테스트를 진행하려면 Enter를 누르세요...")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    db = mysqlDB()
    
    # 추가 테스트
    result = db.insert("홍길동fromPython", "010-1222-1212", "C:\hdh2024\myPrj02\res\dd.jpg")
    print("Insert test: ", result)   

    # 수정 테스트
    result = db.update("홍길동fromPython","010-1222-1214", "C:\hdh2024\myPrj02\res\dd.jpg")
    print("Update Test : ", result)

    # 찾기 테스트
    result = db.search("홍")
    print("Search Test : ", result)

    # 삭제 테스트
    result = db.delete("홍길동fromPython")
    print("Delete Test : ", result)

    app.exec_()
