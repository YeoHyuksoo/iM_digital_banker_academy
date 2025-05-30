use sqldb;

create view v_usertbl
	as select userid, name, addr from usertbl;
    
show full tables in sqldb
	where TABLE_TYPE like 'VIEW';
    
select TABLE_NAME
	from information_schema.`TABLES`
    where TABLE_TYPE like 'VIEW' and TABLE_SCHEMA like 'sqldb';
  
create view v_userbytbl as
	select U.userid, U.name, B.prodName, U.addr, 
		concat(U.mobile1, U.mobile2) as '연락처'
		from usertbl U
			inner join buytbl B
				on U.userid = B.userid;
                
select * from v_userbytbl;

select userid, name, 연락처 from v_userbytbl;

alter view v_userbytbl
	as select U.userid as '사용자아이디', U.name as '이름',
		B.prodName as '제품 이름', U.addr,
        concat(U.mobile1, U.mobile2) as '연락처'
		from usertbl U
			inner join buytbl B
				on U.userid = B.userid;

select * from v_userbytbl;
select `사용자아이디`, `제품 이름` from v_userbytbl;

-- drop view v_userbytbl;
show create view v_userbytbl;

create or replace view v_usertbl
	as select userid, name, addr, birthYear from usertbl;

select * from v_usertbl;
update v_usertbl set addr = '부산' where userid = 'BBK';
select * from v_usertbl;    
select * from usertbl;

insert into v_usertbl(userid, name, addr, birthYear)
	values ('KBM', '김병만', '충북', 1987);

insert into v_usertbl(userid, name, birthYear, addr)
	values ('PJM', '박정민', 1987, '충북');
    

create view v_sum
	as select userID, sum(price*amount) as 'total'
	from buytbl group by userID;
    
select * from v_sum;

insert into v_sum values ('def', null);

create view v_height177
	as select * from usertbl where height >= 177;

select * from v_height177;
    
insert into v_height177 values
	('LSW', '이정우', 2000, '대구', '010', '12345678', 159, '2002-02-02');
    
alter view v_height177
	as select * from usertbl where height >= 177
		and height <= 202 with check option;
        

create table clustertbl (
	userID 	char(8),
    name	varchar(10)
    );
    
insert into clustertbl values('LSG', '이승기');
insert into clustertbl values('KBS', '김범수');
insert into clustertbl values('KKH', '김경호');
insert into clustertbl values('JYP', '조용필');
insert into clustertbl values('SSK', '성시경');
insert into clustertbl values('LJB', '임재범');
insert into clustertbl values('YJS', '윤종신');
insert into clustertbl values('EJW', '은지원');
insert into clustertbl values('JKW', '조관우');
insert into clustertbl values('BBK', '바비킴');


select * from clustertbl;
alter table clustertbl
	add constraint PK_clustertbl_userID
		primary key (userID);
        

select * from clustertbl where userID = 'KKH';

create database if not exists testdb;
use testdb;
drop table if exists secondarytbl;
create table secondarytbl(
	userID 	char(8),
    name	varchar(10)
    );
    
insert into secondarytbl values('LSG', '이승기');
insert into secondarytbl values('KBS', '김범수');
insert into secondarytbl values('KKH', '김경호');
insert into secondarytbl values('JYP', '조용필');
insert into secondarytbl values('SSK', '성시경');
insert into secondarytbl values('LJB', '임재범');
insert into secondarytbl values('YJS', '윤종신');
insert into secondarytbl values('EJW', '은지원');
insert into secondarytbl values('JKW', '조관우');
insert into secondarytbl values('BBK', '바비킴');
   
select * from secondarytbl;

alter table secondarytbl
	add constraint UK_secondarytbl_userID UNIQUE (userID);

use sqldb;
create index idx_usertbl_addr
	on usertbl(addr);
    
show index from usertbl;
select * from usertbl;

drop index idx_usertbl_addr on usertbl;

