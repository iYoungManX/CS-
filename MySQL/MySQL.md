## 数据库


#### MySQL 命令行操作

1. 登录
mysql -u root -p password;

#### 数据定义语言 （DDL）

1. 查询
SHOW DATABASES;
&emsp;

2. 创建
CREATE DATABASE 数据库名称；
CREATE DATABASE IF NOT EXISTS 数据库名称；
&emsp;

3. 删除
DROP DATABASE 数据库名称；
DROP DATABASE IF EXIST 数据库名称；
&emsp;

4. 使用数据库
SELECT DATABSE()；
USE 数据库名称；
&emsp;

5. 创建表
CREATE TABLE 表名{
    字段名： 类型,
    字段名： 类型,
    字段名： 类型
}
&emsp;

6. 删除表
DROP TABLE 表名
DROP TABLE IF EXISTS 表名
&emsp;
7. 修改
修改表名
ALTER TABLE 表名 RENAME TO 新的表名
添加一列
ALTER TABLE 表名 ADD 列名 数据类型
修改数据类型
ALTER TABLE 表名 MODIFY 列名 新数据类型
修改列名和数据类型
ALTER TABLE 表名 CHANGE 列名 新列名 新数据类型
删除一列
ALTER TABLE 表名 DROP 列名
&emsp;

8. 查看表结构
DESC 表名

#### 数据操纵语言 DML
1. 给指定列添加数据
INSERT INTO 表名（列名1,列名2） VALUES(值1,值2)
&emsp;
2. 给全部列添加数据
INSERT INTO 表名 VALUES(值1,值2)
&emsp;
3. 批量添加数据
INSERT INTO 表名（列名1,列名2） VALUES(值1,值2)，(值1,值2)，(值1,值2)
INSERT INTO 表名 VALUES(值1,值2)，(值1,值2)
&emsp;
4. 修改表数据
UPDATE 表名 SET 列名1=值1, 列名2= 值2，..[WHERE 条件]
（如果没有加条件，将会吧表中所有数据修改）
&emsp;
5. 删除数据
DELETE FROM 表名 [WHERE 条件]

#### 数据查询语言 DQL
1. 单表查询： 
SELECT
&emsp; &emsp; 字段列表
FROM
&emsp; &emsp; 表名列表
WHERE
&emsp; &emsp; 条件列表
GROUP BY
&emsp; &emsp; 分组字段
HAVING
&emsp; &emsp; 分组后条件
ORDER BY
&emsp; &emsp; 排序字段
LIMIT
&emsp; &emsp; 分页限定


#### 数据表约束 

1. 分类
非空约束 NOT NULL
唯一约束 UNIQUE
主键约束 PRIMARY KEY
检查约束 CHECK
默认约束 DEFAULT
外键约束 FOREIGN KEY



