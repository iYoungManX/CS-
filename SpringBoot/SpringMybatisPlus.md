## Mybatis-plus 学习笔记

作者:  iYoungMan
时间:  2022-12-24 

#### 官网
https://baomidou.com/

### Maven 依赖
SpringBoot starter
记得springboot 不能用3.0, 整合会出错
```xml
<dependency>
    <groupId>com.baomidou</groupId>
    <artifactId>mybatis-plus-boot-starter</artifactId>
    <version>3.5.2</version>
</dependency>
```


### 配置文件yml
```yml
server:
  port: 80
spring:
  datasource:
    driver-class-name: com.mysql.cj.jdbc.Driver
    url: jdbc:mysql://localhost:3306/db_mp?serverTimezone=UTC
    username: root
    password: root

#mybatis-plus配置
mybatis-plus:
  #配置Mapper映射文件
  mapper-locations: classpath:/mybatis/mappers/*.xml
  # 配置Mybatis数据返回类型别名（默认别名为类名）
  type-aliases-package: com.iyoungman.mybatisplus.POJO
  configuration:
    # 自动驼峰命名
    map-underscore-to-camel-case: false

#配置控制台打印日志Debug
logging:
  level:
    com.jd.mapper: debug
```

#### Dao 层
```java
@Data
@TableName("USER") // tablename 表名
public class User {
    // value 主键字段名,IdType.AUTO 数据库自增
    @TableId(value="id",type = IdType.AUTO)
    private Long id;
    @TableField("NAME")
    private String name;
    private Integer age;
    private String email;
}
```





用自bybatis 方法增删改查
```java
User user = new User();
user.setEmail("yah@126.com");
user.setAge(19);
user.setName("zhaoyang");
userDao.insert(user);

QueryWrapper<User> queryWrapper = new QueryWrapper<>();
queryWrapper.eq("name","mayun");
userDao.delete(queryWrapper);

userDao.updateById(user);

userDao.selectById(1);
queryWrapper = new QueryWrapper<>();
queryWrapper.eq("name","zhaoyang");
userDao.selectList(queryWrapper);

```


#### Reverse Engineer 快速生成Controller, Service, Dao

```java
 private  String projectPath = System.getProperty("user.dir");
    // 数据源配置
    private static final DataSourceConfig.Builder DATA_SOURCE_CONFIG = new DataSourceConfig.Builder("jdbc:mysql://localhost:3306/mybatis?serverTimezone=GMT%2B8", "root", "123456")
            .typeConvert(new MySqlTypeConvert());

    public void CodeGenerate(String[] args) {
        FastAutoGenerator.create("jdbc:mysql://localhost:3306/reggie?serverTimezone=UTC", "root", "root")
                .globalConfig(builder -> {
                        builder.author("iyoungman") // 设置作者
                                // .enableSwagger() // 开启 swagger 模式
                                .disableOpenDir() // 执行完毕不打开文件夹
                                .fileOverride() // 覆盖已生成文件
                                .outputDir(projectPath + "/src/main/java"); // 指定输出目录// 指定输出目录
                })
                //包配置
                .packageConfig(builder -> {
                    builder.parent("com.iyoungman.mybatisplus") // 设置父包名
                            .controller("Controller") //生成controller层
                            .entity("POJO") //生成实体层
                            .service("Service") //生成服务层
                            .mapper("Dao")
                            .xml("MapperXML")
                            .pathInfo(Collections.singletonMap(OutputFile.xml, projectPath + "/src/main/resources/MapperXml")); //生成mapper层

                    // .moduleName("mybatisplus");
                })
                //策略配置
                .strategyConfig(builder -> {
                    builder.addInclude("address_book","dish","order_detail") // 设置需要生成的表名
                            .addTablePrefix("tbl_")// 设置过滤表前缀
                            .serviceBuilder() //开启service策略配置
                            .formatServiceFileName("%sService") //取消Service前的I
                            .controllerBuilder() //开启controller策略配置
                            .enableRestStyle() //配置restful风格
                            .enableHyphenStyle() //url中驼峰转连字符
                            .entityBuilder() //开启实体类配置
                            .enableLombok() //开启lombok
                            .enableChainModel(); //开启lombok链式操作

                })
                //模板配置
                .templateEngine(new FreemarkerTemplateEngine()) // 使用Freemarker引擎模板，默认的是Velocity引擎模板
                //执行
                .execute();
    }

```