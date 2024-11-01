select * from information_schema.table_constraints
	where constraint_schema = "한빛무역";

-- 고객,주문 1:N관계

-- 


select num, buytbl.userID, prodName, birthYear from buytbl
	inner join usertbl on buytbl.userID = usertbl.userID -- 이너조인-> equal만 사용가능
    where buytbl.userID = 'JYP';
    
select * from usertbl;
select * from buytbl;
    
select * from buytbl join usertbl on buytbl.userID = usertbl.userID
	order by num;
    
    
select buytbl.userID, name, prodName, addr, concat(mobile1, mobile2) as 연락처
	from buytbl
		inner join usertbl
			on buytbl.userID = usertbl.userID
	order by num;
    
create table stdtbl (
	stdName varchar(10) not null primary key,
    addr char(4) not null
    );
    
create table clubtbl (
	clubName varchar(10) not null primary key,
    roomNo char(4) not null
    );

desc clubtbl;

create table stdclubtbl (
	num int auto_increment primary key,
    -- 정수형이면서 기본키or unique -> auto_increment
    stdName varchar(10) not null,
    clubName varchar(10) not null,
    foreign key (stdName) references stdtbl(stdName),
    foreign key (clubName) references clubtbl(clubName)
    );
    
insert into stdtbl values ('김범수', '경남'), ('성시경', '서울'),
					('조용필', '경기'), ('은지원', '경북'), ('바비킴', '서울');

insert into clubtbl values ('수영', '101호'), ('바둑', '102호'), ('축구', '103호'),
					('봉사', '104호');

insert into stdclubtbl values (null, '김범수', '바둑'), (null, '김범수', '축구'),
						(null, '조용필', '축구'), (null, '은지원', '축구'),
						(null, '은지원', '봉사'), (null, '바비킴', '봉사');

INSERT INTO stdclubtbl values (null, '은지원', '코딩');

select s.stdName, s.addr, sc.clubName, c.roomNo
	from stdtbl s
		inner join stdclubtbl sc
			on s.stdName = sc.stdName
		inner join clubtbl c
			on sc.clubName = c.clubName
	order by s.stdName;
    
select c.clubName, c.roomNo, s.stdName, s.addr
	from clubtbl c
		inner join stdclubtbl sc
			on c.clubName = sc.clubName
		inner join stdtbl s
			on sc.stdName = s.stdName
	order by c.clubName;
    
select u.userID, u.name, b.prodName, u.addr, concat(u.mobile1, u.mobile2) as '연락처'
	from usertbl u
		left outer join buytbl b
			on u.userID = b.userID
	order by u.userID;
    
    
select s.stdName, s.addr, c.clubName, c.roomNo
	from stdtbl s
		left outer join stdclubtbl sc
			on s.stdName = sc.stdName
		left outer join clubtbl c
			on sc.clubName = c.clubName
	order by s.stdName;


select s.stdName, s.addr, c.clubName, c.roomNo
	from stdtbl s
		left outer join stdclubtbl sc
			on s.stdName = sc.stdName
		right outer join clubtbl c
			on sc.clubName = c.clubName
	order by s.stdName;
    
    
    
select count(*) from buytbl cross join usertbl;
select count(*) from buytbl, usertbl;    

use employees;
select count(*) from employees;

use sqldb;

create table empTbl (
	emp char(3),
    manager char(3),
    empTel varchar(8)
    );

insert into empTbl values('나사장', NULL, '0000');
insert into empTbl values('김재무', '나사장', '2222');
insert into empTbl values('김부장', '김재무', '2222-1');
insert into empTbl values('이부장', '김재무', '2222-2');
insert into empTbl values('우대리', '이부장', '2222-2-1');
insert into empTbl values('지사원', '이부장', '2222-2-2');
insert into empTbl values('이영업', '나사장', '1111');
insert into empTbl values('한과장', '이영업', '1111-1');
insert into empTbl values('최정보', '나사장', '3333');
insert into empTbl values('윤차장', '최정보', '3333-1');
insert into empTbl values('이주임', '윤차장', '3333-1-1');

select * from emptbl;

select empt1.emp as 부하직원, empt2.emp as 직속상관, empt2.empTel as 직속상관연락처
from empTbl empt1
	inner join empTbl empt2
		on empt1.manager = empt2.emp;
-- where empt1.emp = '우대리';

select * from stdtbl
	union all
select * from clubtbl;

select name, concat(mobile1, mobile2) as 전화번호 from usertbl
	where name in (select name from usertbl where concat(mobile1, mobile2) is null);

-- 기본키를 이용한 데이터 검색과 그렇지 않은 검색 속도의 차이는 엄청 크다.
-- 하지만 기본키, 인덱스로 정렬하는 과정이 매 insert마다 필요하기 때문에 이것도 고려해야한다.

desc buytbl;	

create table prodtbl
	(	prodCode	char(3) not null,
		prodID		char(4) not null,
        prodDate	datetime not null,
        prodCur		char(10) null,
	constraint PK_prodtbl_prodCode_prodID
		primary key (prodCode, prodID)
	);
    
show index from prodtbl;

drop table if exists prodtbl;
create table prodtbl
	(	prodCode	char(3) not null,
		prodID		char(4) not null,
        prodDate	datetime not null,
        prodCur		char(10) null
	);
alter table prodtbl
	add constraint PK_prodtbl_prodCode_prodID
		primary key (prodCode, prodID);
        
use sqltest;

create table usertbl(
	userID char(8) not null primary key,
    name varchar(10) not null,
    birthYear int not null
    );

insert into usertbl values ('AAA', '이기자', 2000), ('BBB', '김기자', 2005),
						('CCC', '한기자', 2001);
select * from usertbl;

create table buytbl(
	num int auto_increment not null primary key,
    userID char(8) not null,
    prodName char(6) not null,
    constraint FK_usertbl_buytbl foreign key(userID)
		references usertbl(userID) on delete cascade
        );
        
insert into buytbl values (null, 'AAA', '휴대폰'), (null, 'BBB', '책상');

select * from buytbl;

delete from usertbl where userID = 'AAA';

select * from usertbl;
select * from buytbl;

alter table buytbl
	drop foreign key FK_usertbl_buytbl;

alter table buytbl
	add constraint FK_usertbl_buytbl foreign key (userID)
		references usertbl(userID);

delete from usertbl where userID = 'BBB';

drop table if exists buytbl;
drop table if exists usertbl;

create table usertbl (
	userID char(8) primary key,
    name varchar(10),
    birthYear int check (birthYear >= 1900 and birthYear <= 2023),
    mobile1 char(3) null,
    constraint CK_name check (name is not null)
    );
    
insert into usertbl values ('aaa', 'dlrlwk', '1999', '010');

insert into usertbl values ('bbb', null, '1999', '010');
insert into usertbl values ('bbb', 'rlarlwk', 1888, '010');
insert into usertbl values ('ccc', 'hyuksoo', 2022, '010');

alter table usertbl
	add constraint CK_mobile1 check 
    (mobile1 IN ('010', '011', '016', '017', '018', '019'));
    
insert into usertbl values ('bbb', 'rlarlwk', 1901, '100');

drop table if exists usertbl;

create table usertbl (
	userID	char(8) not null primary key,
    name	varchar(10) not null,
    birthYear int not null default -1,
    addr	char(2) not null default '서울',
    mobile1 char(3) null,
    mobile2 char(8) null,
    height 	smallint null default 170,
    mDate 	date null
    );
    
insert into usertbl(userID, name) values ('AAA', '이기자');
select * from usertbl;

desc usertbl;
alter table usertbl
	modify homepage varchar(30) default "https://www.hanbit.co.kr" null;
    
insert into usertbl (userID, name, mobile1) value ('yhs', 'asasdf', 010);    
select * from usertbl;

-- select * from information_schema.table_constraints
-- 	where constraint_schema = "employees";

alter table usertbl
	drop column mobile1;
    
select * from usertbl;

alter table usertbl
	drop column addr;
    
desc usertbl;

alter table usertbl
	change column name uName varchar(20) null;
    
desc usertbl;

