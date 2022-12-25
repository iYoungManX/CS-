## SpringData JPA 学习笔记

作者:  iYoungMan
时间:  2022-12-24 

#### 官网

https://spring.io/projects/spring-data-jpa

pring Data JPA 是 Spring 基于 ORM 框架、JPA 规范的基础上封装的一套 JPA 应用框架，底层使用了 Hibernate 的 JPA 技术实现，可使开发者用极简的代码即可实现对数据的访问和操作。它提供了包括增删改查等在内的常用功能，且易于扩展！学习并使用 Spring Data JPA 可以极大提高开发效率。

ORM 全称是：Object Relational Mapping(对象关系映射)，其主要作用是在编程中，把面向对象的概念跟数据库中表的概念对应起来。举例来说就是，我定义一个对象，那就对应着一张表，这个对象的实例，就对应着表中的一条记录。



#### Maven 坐标依赖 

以SpringBoot 整合jpa 和MySql 为例
```xml
  <dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-data-jpa</artifactId>
  </dependency>
  <dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-web</artifactId>
  </dependency>
  <dependency>
    <groupId>com.mysql</groupId>
    <artifactId>mysql-connector-j</artifactId>
    <scope>runtime</scope>
  </dependency>
```


#### Application.yml 配置文件

```yml
spring:
  datasource:
    driver-class-name: com.mysql.cj.jdbc.Driver
    url: jdbc:mysql://localhost:3306/db_jpa
    username: root
    password: root
  jpa:
    show-sql: true
    # 可以理解项目启动时，根据实体类结构更新数据库表结构，且保留数据库中的数据。
    hibernate:
      ddl-auto: update  
```



#### POJO 实体类

```java
@Data
@Entity  // 表示这是一个数据对象类
@Table(name = "student") // 对应数据库中的goods表
public class Student {
    // 该字段对应数据库中的列为主键
    @Id
    // 主键自增长
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "id") // 对应student表中的id列
    private Integer id;
    private String name;
    private String email;
    // 一对一关联, 懒加载，用到再查Account
    @OneToOne(cascade = CascadeType.ALL, fetch = FetchType.LAZY)
    @JoinColumn(name="account_id")
    private Account account;

    @OneToMany(cascade = CascadeType.ALL)
    @JoinColumn(name="customer_id")
    private List<Message> messages;
}


@Entity
@Table(name = "account")
@Data
public class Account {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer id;
    private String username;
    private String password;
}


@Entity
@Table(name = "message")
@Data
public class Message {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer id;
    private String info;
}


```


#### DAO 接口 

可安装idea 插件 JPA Buddy
```java
public interface StudentDAO extends JpaRepository<Student,Integer> {
    // 基础查询已经由JpaRepository 接口提供

    // 自定义查询 1
    @Query("FROM Student WHERE name = ?1")
    List<Student> findStudentByName(String name);

    // 自定义查询 2
    @Query("FROM Student WHERE email = :email")
    List<Student> findStudentByEmail(@Param("email") String email);

    // 增删改 需要加上事务支持
    // 自定义更新
    @Query("UPDATE Student s SET s.name =:name WHERE s.id =:id")
    @Transactional
    @Modifying
    int updateStudent(@Param("id") int id, @Param("name") String name);

    // 自定义删除
    @Transactional
    @Modifying
    @Query("DELETE FROM Student  s WHERE  s.name=:name")
    int deleteStudentByName(String name);


    // 可以根据JPA 已经定义好的名字查询
     List<Student> findByEmailAndAndName(String email, String name);

}
```

也可以根据规定的名字自定义查询方法，详见
https://docs.spring.io/spring-data/jpa/docs/current/reference/html/#jpa.query-methods.query-creation  中的Table 3 和 Table 8


#### JPA 接口
jpa 的父接口 CrudRepository 的功能
```java
public interface CrudRepository<T, ID> extends Repository<T, ID> {

  <S extends T> S save(S entity);      (1)

  Optional<T> findById(ID primaryKey); (2)

  Iterable<T> findAll();               (3)

  long count();                        (4)

  void delete(T entity);               (5)

  boolean existsById(ID primaryKey);   (6)

  // … more functionality omitted.
}

```

(1) Saves the given entity.
(2) Returns the entity identified by the given ID.
(3) Returns all entities.
(4) Returns the number of entities.
(5) Deletes the given entity.
(6) Indicates whether an entity with the given ID exists.



#### Service
接口
```java
public interface StudentService {
    public Student findById(int id);
    public List<Student> findAll();
    public Student save(Student student);
    public Student edit(Student student);
    public boolean deleteById(int id);
}
```
实现类

```java
public class StudentServiceImpl implements StudentService {

    @Autowired
    private StudentDAO studentDAO;

    @Override
    public Student findById(int id){
        return studentDAO.findById(id).get();
    }

    @Override
    public List<Student> findAll(){
        return studentDAO.findAll();
    }


    @Override
    public Student save(Student student){
        return studentDAO.save(student);
    }

    @Override
    public Student edit(Student student){
        return studentDAO.save(student);
    }

    @Override
    public boolean deleteById(int id){
        boolean result = true;
        try{
            studentDAO.deleteById(id);
        }catch(Exception ex){
            result = false;
        }
        return result;
    }
}
```


#### 参考资料

B 站： https://www.bilibili.com/video/BV13Y411x7n9?p=16&spm_id_from=pageDriver&vd_source=3a932a9499613bd6c404fec463f907a8






