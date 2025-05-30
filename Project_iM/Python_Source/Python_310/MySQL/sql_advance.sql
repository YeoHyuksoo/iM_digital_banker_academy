use sqldb;

insert into usertbl values('LSG', '이승기', 1987, '서울', '011', '1111111', 182, '2009-10-20');
insert into buytbl values(null, 'KBS', 운동화, NULL, 30, 2);

create table usertbl2 (
		userID char(8),
		name varchar(10)
        );

insert into usertbl2 (userID, name)
	select userID, name
	from usertbl;

select * from usertbl2;

create table buytbl2 (select * from buytbl);

create table testTbl1 (id int, userName char(3), age int);

select * from buytbl2;
select * from buytbl;

insert into testTbl1 values (1, '홍길동', 25);
insert into testTbl1(id, userName) values (2, '설현');

insert into testTbl1(userName, age, id) values ('하니', 26, 3);

select * from testTbl1;

create table testTbl2(
	id int auto_increment primary key,
    userName char(3),
    age int
);

desc testTbl2;

insert into testTbl2 values (null, '지민', 25);
insert into testTbl2 values (null, '유나', 22);
select * from testTbl2;

select LAST_INSERT_ID();


set @myVar1 = 5;
set @myVar2 = 3;
set @myVar3 = 4.25;
set @myVar4 = "가수 이름 -->";
set @myVar5 = 3;

select @myVar1;
select @myVar2 + @myVar3;
select @myVar4, Name from usertbl where height > 180;

select AVG(amount) as '평균구매개수' from buytbl;
select cast(avg(amount) as signed integer) as '평균구매개수' from buytbl;
select convert(avg(amount), signed integer) as '평균구매개수' from buytbl;

select cast('2020*12*12' as date);
select cast('2020/12/12' as date);
select cast('2020-12-12' as date);

select num, concat(cast(price as char(10)), 'X',
	cast(amount as char(4)), '=') as '단가X수량', price*amount as '구매액'
	from buytbl;


select '100'+'200';
select concat('100', '200');
select concat(100, '200');
select 1 > '2mega'; -- 정수 2로 변환됨
select 3 > '2mega';
select 0 = 'mega2'; -- 문자는 0으로 변환됨

select case 10
		when 1 then '일'
        when 5 then '오'
        when 10 then '십'
        else 'etc'	
	end as 'case연습';
    
select ifnull(1, 100);
select ifnull(null, 100);

select ascii('A'), CHAR(97);

select bit_length('abc'), char_length('abc'), length('abc');
select bit_length('가나다'), char_length('가나다'), length('가나다');
-- 영문1자 1바이트, 한글1자 3바이트

SELECT CONCAT_WS('/', '2025', '01', '01');



-- SELECT ELT(1, "HYUKSOO", "YEO");
SELECT INSERT('ABCDEFGHI', 3, 4, '@@!1'); -- INSERT (기준문자열, 위치, 길이, 삽입할 문자열)
SELECT INSERT('ABCDEFGHI', 3, 2, '@@!1');

SELECT TRIM('   이것이  \t'), TRIM(BOTH 'ㅋ' FROM 'ㅋㅋㅋ재밌어요.ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ');
SELECT LPAD('이것이', 8, '##');

select substring('대한민국만세', 3, 2);
select substring('대한민국만세' from 1 for 3);
select substring_index('cafe.naver.com', '.', 2);
select substring_index('cafe.naver.com', '.', -2);

select ceiling(4.7), floor(3.7), round(4.7), round(-4.7);
select truncate(12345.12345, 2), truncate(12345.12345, -2); -- 소수점 기준으로 왼쪽, 오른쪽 2자리까지

select YEAR(curdate()), MONTH(curdate()), DAYOFMONTH(CURDATE());
select hour(curtime());
select minute(current_time());
select second(curtime());
select microsecond(current_time());

select date(now()), time(now());
select datediff('2018-02-20', '2019-10-20');
select adddate('2018-02-20', 607);
select subdate('2019-10-20', 607);


create table pivotTest (
		uName char(3),
		season char(2),
        amount int
        );
        
insert into pivotTest values 
	('김범수', '겨울', 10), ('윤종신', '여름', 15),('김범수', '가을', 25),('김범수', '봄', 3),
    ('김범수', '봄', 37),('윤종신', '겨울', 40),('김범수', '여름', 14),('김범수', '겨울', 22),
    ('윤종신', '여름', 64) ;
    
select * from pivotTest;

select uName,
	sum(IF(season = '봄', amount, 0)) as '봄',
	sum(IF(season = '여름', amount, 0)) as '여름',
    sum(IF(season = '가을', amount, 0)) as '가을',
    sum(IF(season = '겨울', amount, 0)) as '겨울',
    sum(amount) as '합계'
from pivotTest 
group by uName;


        
