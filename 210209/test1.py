# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 17:36:05 2021

@author: Dohun

1. 콘솔에 sql 구문을 입력하면 mariadb의 테이블들을 이용하여 결과를 출력할 수 있도록 프로그램 작성하기

   [결과]

sql 구문을 입력하세요 : select * from student

[결과]

sql 입력하세요=========

select * from dept

조회 레코드수: 5 ,조회 컬럼수:3

(10, '대표이사', '서울')

(20, '기획부', '서울')

(30, '기술부', '서울')

(40, '영업부', '서울')

(50, '운용팀', '울산')
"""
import pymysql

conn = pymysql.connect(host="localhost", port=3307, user="scott", passwd="1234", db="classdb", charset="utf8")
cur = conn.cursor()
sql = input("SQL 구문을 입력하세요: ")
cur.execute(sql)
result = cur.fetchall()

print("조회 레코드 수 : %d, 조회 컬럼 수: %d" % (len(result), len(result[0])))

for r in result:
    print(r)
    print()
    
conn.close()
cur.close()