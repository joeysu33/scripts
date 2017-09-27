#!/usr/bin/python
#coding=utf8

'''
给学生管理系统生成各种测试数据，用来学习数据库
系统原理的课程
'''

import pymysql.cursors
from faker import Faker
from random import Random

PORT = 3306
STUDENT_COUNT = 300
MAX_COURSE_FOR_STUDENT = 4

faker = Faker('zh_CN')
rand = Random()

#连接到数据库
conn = pymysql.connect(host='127.0.0.1',
        port=PORT,
        user='wh',
        password='root',
        db='stutmp',
        charset = 'utf8',
        cursorclass=pymysql.cursors.DictCursor)


try:
    students = []
    sid = 1002
    for i in range(STUDENT_COUNT):
        with conn.cursor() as cursor:
            #执行sql语句
            sql = 'insert into `student` values \
                    (%s,%s,%s,%s,%s,%s)'

            sno = str(sid)
            name=faker.name()
            sex = 'M' if faker.boolean() else 'F'
            birthday = faker.date()
            height = faker.random_int(1300, 2000) / 10.0
            age = faker.random_int(18,25)

            students.append(sid)
            #cursor.execute(sql, (sno, name, sex, birthday, height, age))

            sid += 1
    conn.commit()

    coursenames = ['语文','数学','英语', '政治','历史', '体育', '韩语', '日语', '地理', '天文', '化学', '物理']
    
    cid = 2001
    courses = []
    for i in coursenames:
        with conn.cursor() as cursor:
            sql = 'insert into `course` values (%s,%s,%s,%s,%s)'
            cno = str(cid)
            name = i
            hour = faker.random_int(30, 80)
            credit = faker.random_int(4, 10)
            semester = '春' if faker.boolean() else '夏'

            courses.append(cid)
            #cursor.execute(sql, (cno, name, hour, credit, semester))
            cid += 1
    conn.commit()

    for i in students:
        sno = i
        index = set()
        courseNum = faker.random_int(1,4)
        while courseNum != len(index):
            index.add(faker.random_int(0,len(courses) - 1))

        for idx in index:
            with conn.cursor() as cursor:
                cno = str(courses[idx])
                sql = 'insert into selectcourse values (%s,%s,%s)'
                grade = faker.random_int(40, 100)
                cursor.execute(sql, (sno, cno,grade))
    conn.commit()

finally:
    conn.close();


