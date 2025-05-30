-- 1. 사원 테이블과 부서 테이블을 크로스 조인하여 ‘배재용’ 사원에 대한 정보 
-- (이름, 사원 테이블의 부서번호, 부서 테이블의 부서번호, 부서명)를 보이시오.

select 이름, 사원.부서번호, 부서.부서번호, 부서명 from 사원 cross join 부서 
    where 사원.이름 = '배재용';

/*non-ansi sql*/
select 이름, 사원.부서번호, 부서.부서번호, 부서명
from 부서, 사원
where 이름 = '배재용';

-- 2. ‘이소미’ 사원의 사원번호, 직위, 부서번호, 부서명을 보이시오.

select 사원.사원번호, 사원.직위, 부서.부서번호, 부서.부서명
	from 사원 inner join 부서
	on 사원.부서번호 = 부서.부서번호
    where 사원.이름 = '이소미';

-- 3. 고객 회사들이 주문한 주문건수를 주문건수가 많은 순서대로 보이시오. 
-- 이때 고객 회사의 정보로는 고객번호, 담당자명, 고객회사명을 보이시오.

select 고객.고객번호, 고객.담당자명, 고객.고객회사명, count(*) as 주문건수
	from 고객 inner join 주문 on 고객.고객번호 = 주문.고객번호
	group by 고객.고객번호, 고객.담당자명, 고객.고객회사명
	order by 주문건수 desc;

-- 4. 고객별(고객번호, 담당자명, 고객회사명)로 주문금액 합을 보이되, 주문금액 합이 많은 순서대로 보이시오.

select 고객.고객번호, 담당자명, 고객회사명,
	round(sum(단가 * (1 - 할인율) * 주문수량)) as 주문금액합
	from 고객
	inner join 주문 on 고객.고객번호 = 주문.고객번호
    inner join 주문세부 on 주문.주문번호 = 주문세부.주문번호
    group by 고객.고객번호, 담당자명, 고객회사명
    order by 주문금액합 desc;

-- 5. 고객 테이블과 마일리지등급 테이블을 크로스 조인하시오. 
-- 그 다음 고객 테이블에서 담당자가 ‘이은광’인 고객에 대하여 
-- 고객번호, 담당자명, 마일리지, (마일리지등급 테이블의 모든 컬럼)을 보이시오.

select 고객번호, 담당자명, 마일리지, 마일리지등급.*
	from 고객 cross join 마일리지등급
	where 담당자명 = '이은광';

-- 6. 고객 테이블에서 담당자가 ‘이은광’인 경우의 고객번호, 고객회사명, 담당자명, 마일리지와 마일리지등급을 보이시오.

select 고객번호, 고객회사명, 담당자명, 마일리지, 등급명 as 마일리지등급
	from 고객 cross join 마일리지등급
	where 담당자명 = '이은광' and (마일리지 between 하한마일리지 and 상한마일리지);

select 고객번호, 고객회사명, 담당자명, 마일리지, 등급명
	from 고객 inner join 마일리지등급 
		on 마일리지 >= 하한마일리지 and 마일리지 <= 상한마일리지
	where 담당자명 = '이은광';

-- 7. 부서명과 해당 부서의 소속 사원 정보를 보이시오. 
-- 이때 사원이 한 명도 존재하지 않는 부서명이 있다면 그 부서명도 함께 보이시오.

select 부서명, 사원.* from 부서 left outer join 사원
	on 부서.부서번호 = 사원.부서번호
    order by 부서명 desc;

-- 8. 사원이 한 명도 존재하지 않는 부서명을 보이시오.

select 부서명 from 부서 
	where 부서번호 not in 
		(select 부서번호 from 사원);
        
select 부서명 from 부서
	left outer join 사원
	on 부서.부서번호 = 사원.부서번호
    group by 부서.부서번호
    having count(사원번호) = 0;
    
select 부서명, 사원.*
	from 사원 right outer join 부서 on 사원.부서번호 = 부서.부서번호
    where 사원.부서번호 is null;

-- 9. 소속 부서가 없는 사원의 이름을 보이시오.

select 이름 from 사원 
	where 부서번호 not in 
		(select 부서번호 from 부서);
        
select 사원.이름 from 사원
	left outer join 부서
	on 사원.부서번호 = 부서.부서번호
    where 부서.부서번호 is null;
    

-- 10. 사원번호, 사원의 이름, 상사의 사원번호, 상사의 이름을 보이시오.

select emp.사원번호, emp.이름, sen.사원번호 as '상사의 사원번호', sen.이름 as '상사 이름'
	from 사원 as emp inner join 사원 as sen
		on emp.상사번호 = sen.사원번호;

-- 11. 사원이름, 직위, 상사이름을 상사이름 순으로 정렬하여 나타내시오. 
-- 이때 상사가 없는 사원의 이름도 함께 보이시오.

select emp.이름, emp.직위, sen.이름 as '상사 이름'
	from 사원 as emp left outer join 사원 as sen
		on emp.상사번호 = sen.사원번호
	order by sen.이름 is null, sen.이름;

-- 12. 마일리지 등급명별로 고객수를 보이시오

select count(*), 등급명 as 마일리지등급
	from 고객 cross join 마일리지등급
	where 마일리지 between 하한마일리지 and 상한마일리지
    group by 등급명;

-- 13. 주문번호 ‘H0249’를 주문한 고객의 모든 정보를 보이시오.

select 고객.* from 고객 inner join 주문
	on 고객.고객번호 = 주문.고객번호
	where 주문번호 = 'H0249';

-- 14. 2020년 4월 9일에 주문한 고객의 모든 정보를 보이시오.

select 고객.* from 고객 inner join 주문
	on 고객.고객번호 = 주문.고객번호
    where 주문일 = '2020-04-09';

-- 15. 도시별로 주문금액합을 보이되 주문금액합이 많은 상위 5개의 도시에 대한 결과만 보이시오.

select 도시, round(sum(단가 * (1 - 할인율) * 주문수량)) as 주문금액합
	from 고객 inner join 주문
	on 고객.고객번호 = 주문.고객번호
    inner join 주문세부
	on 주문.주문번호 = 주문세부.주문번호
    group by 도시
    order by 주문금액합 desc limit 5;

-- 쉽게냈습니다 mysql도 쉽게 출제했는데 주관식 5-6 있어요 2개의 테이블을 제시해놓고 간단하게 하는 문제 !
-- 조인문제 아주 심플합니다.

