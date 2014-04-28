在前面已经介绍了IN运算符的简单使用，使用IN运算符可以用来匹配一个固定集合中的某一项。比如下面的SQL语句检索在2001、2003和2005年出版的所有图书：
```java  
SELECT * FROM T_Book WHERE FYearPublished IN(2001,2003,2005)
```
执行完毕我们就能在输出结果中看到下面的执行结果：
```java  
FId FName FYearPublished FCategoryId
1 About J2EE 2005 4
2 Learning Hibernate 2003 4
4 Jane Eyre 2001 1
15 DaoDeJing 2001 6
```
这里进行匹配的集合是已经确定的集合“2001,2003,2005”，如果要匹配的集合是动态的则无法用这种方式来进行匹配了。比如，需要检索所有图书出版年份内入会的读者信息，可以使用简单的SQL语句检索出所有的图书的出版年份：
```java  
select FYearPublished FROM T_Book
```
执行完毕我们就能在输出结果中看到下面的执行结果：
```java  
FYearPublished
2005
2003
1999
2001
2002
1982
1860
1700
2008
1930
1945
1970
1971
1771
2001
1995
```
这个查询结果是多行单列的，因此可以将其用来与IN 运算符进行匹配运算，SQL语句如下：
```java  
SELECT * FROM T_Reader WHERE FYearOfJoin IN(select FYearPublished FROM T_Book)
```
执行完毕我们就能在输出结果中看到下面的执行结果：
```java  
FId FName FYearOfBirth FCity FProvince FYearOfJoin
1 Tom 1979 TangShan Hebei 2003
2 Sam 1981 LangFang Hebei 2001
3 Jerry 1966 DongGuan GuangDong 1995
4 Lily 1972 JiaXing ZheJiang 2005
5 Marry 1985 BeiJing BeiJing 1999
6 Kelly 1977 ZhuZhou HuNan 1995
7 Tim 1982 YongZhou HuNan 2001
9 John 1979 QingDao ShanDong 2003
11 July 1983 ZhuMaDian HeNan 1999
12 Fige 1981 JinCheng ShanXi 2003
```