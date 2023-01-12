from faker import Faker
import mysql.connector

fake = Faker()
title = fake.sentence()
body = fake.text()
author_id = fake.random_int(min=1, max=100)

cnx = mysql.connector.connect(
    host="localhost",
    user="user",
    password="password",
    database="mydatabase"
)

cursor = cnx.cursor()

sql = "INSERT INTO posts (title, body, author_id) VALUES (%s, %s, %s)"
cursor.execute(sql, (title, body, author_id))

cnx.commit()

cursor.close()
cnx.close()
