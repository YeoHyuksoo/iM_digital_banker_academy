-- 1. 최고 마일리지를 보유한 고객의 정보를 보이시오.

select * from 고객 where 마일리지 = (select max(마일리지) from 고객);

-- 2. 주문번호 ‘H0250’을 주문한 고객에 대해 고객회사명과 담당자명을 보이시오.

select 고객회사명, 담당자명 from 고객 where 고객번호 in 
	(select 고객번호 from 주문 where 주문번호 = 'H0250');
    
select 고객회사명, 담당자명
	from 고객 inner join 주문 on 고객.고객번호 = 주문.고객번호
    where 주문번호 = 'H0250';

-- 3. ‘부산광역시’고객의 최소 마일리지보다 더 큰 마일리지를 가진 고객 정보를 보이시오.

select * from 고객 where 마일리지 > 
	(select min(마일리지) from 고객 where 도시 = '부산광역시');
    
select * from 고객 where 마일리지 > any(select 마일리지 from 고객);

-- 4. ‘부산광역시’ 고객이 주문한 주문건수를 보이시오.

select count(*) as 주문건수 from 주문 where 고객번호 in
	(select 고객번호 from 고객 where 도시 = '부산광역시');

-- 5. ‘부산광역시’ 전체 고객의 마일리지보다 마일리지가 큰 고객의 정보를 보이시오.

select * from 고객 where 마일리지 > 
	(select max(마일리지) from 고객 where 도시 = '부산광역시');

-- 6. 각 지역의 어느 평균 마일리지보다도 마일리지가 큰 고객의 정보를 보이시오.

select * from 고객 where 마일리지 > 
	all(select avg(마일리지) from 고객
		where 지역 is not null
        group by 지역);


-- 7. 한 번이라도 주문한 적이 있는 고객의 정보를 보이시오.

select * from 고객 where 고객번호 in (select distinct 고객번호 from 주문);

-- 8. 고객 전체의 평균마일리지보다 평균마일리지가 큰 도시에 대해 도시명과 도시의 평균마일리지를 보이시오. 

select 도시, avg(마일리지) as '평균마일리지' from 고객 
    group by 도시
    having avg(마일리지) > (select avg(마일리지) from 고객);

-- 9. 담당자명, 고객회사명, 마일리지, 도시, 해당 도시의 평균마일리지를 보이시오. 
-- 그리고 고객이 위치하는 도시의 평균마일리지와 각 고객의 마일리지 간의 차이도 함께 보이시오.

select 고객번호, 담당자명, 고객회사명, 마일리지, 고객.도시, 도시평균마일리지,
	abs(마일리지 - 도시평균마일리지) as '고객이 위치한 도시의 평균마일리지와 고객 마일리지 간 차이'
	from 고객, (select 도시, avg(마일리지) as 도시평균마일리지 from 고객 group by 도시) as 고객_cp
	where 고객.도시 = 고객_cp.도시;

-- 인라인 뷰 -> from절에도 쿼리
-- 인라인 뷰에는 반드시 별칭을 설정해야함

-- 10. 고객번호, 담당자명과 고객의 최종 주문일을 보이시오.

select 고객.고객번호, 담당자명, 최종주문일
	from 고객, (select 고객번호, max(주문일) as 최종주문일 from 주문 group by 고객번호) as 주문
    where 고객.고객번호 = 주문.고객번호;

select 고객번호, 담당자명, (select max(주문일) from 주문 where 주문.고객번호 = 고객.고객번호) as 최종주문일
	from 고객;
    
-- 스칼라 서브쿼리 (Scalar SubQuery)
-- 서브쿼리가 하나의 값을 생성하는 형태.

-- 11. 제품 테이블에 있는 제품 중 단가가 가장 높은 제품명은 무엇인가?

select 제품명 from 제품 where 단가 = (select max(단가) from 제품);

-- 12. 제품 테이블에 있는 제품 중 단가가 가장 높은 제품의 주문수량합은 얼마인가?

select sum(주문수량) as 주문수량합
	from 주문세부, (select 제품번호, 단가 from 제품 where 단가 = (select max(단가) from 제품)) as 제품
	where 주문세부.제품번호 = 제품.제품번호;

-- 13. ‘아이스크림’ 제품의 주문수량합은 얼마인가?

select sum(주문수량) as 주문수량합 
	from 주문세부, (select 제품번호 from 제품 where 제품명 like '%아이스크림%') as 제품
    where 주문세부.제품번호 = 제품.제품번호;

-- 14. ‘서울특별시’ 고객들에 대해 주문년도별 주문건수를 보이시오.

select YEAR(주문일) as 주문년도, count(*) as 주문건수 
	from 주문, (select 고객번호 from 고객 where 도시 = '서울특별시') as 고객
    where 주문.고객번호 = 고객.고객번호
    group by 주문년도;
    

