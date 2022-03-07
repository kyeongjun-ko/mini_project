use mini_project;
-- 데이터 지우기
TRUNCATE stores_db;

-- 테이블 확인하기
select * from stores_db;
select * from stores_db1;

-- 컬럼 순서바꾸기
ALTER TABLE stores_db MODIFY COLUMN lng varchar(128) AFTER lat;

-- 지역명이 겹치는 데이터가 몇개인지 추출하기
select area, count(*) from stores_db
group by area having count(*) > 1;

-- 지역별, 주소별 정렬하기
select * from stores_db
order by field(area,"경기","서울") desc , addr1 asc;
  
--  target1_code, target2_code 에 따라서 다르게 출력하기
CREATE TABLE stores_db1
SELECT *,(
	case target2_code
		when "" then "Nan"
		when "01" then "결식아동"
		when "02" then "독거노인"
		when "03" then "소방관"
		when "99" then target2_etc
        when "01,02" then concat("결식아동,", "독거노인")
        when "02,03" then concat("독거노인,", "소방관")
        when "01,03" then concat("결식아동,", "소방관")
        when "01,02,99" then concat("결식아동,","독거노인,",target2_etc)
		when "01,99" then concat("결식아동,",target2_etc)
		when "02,99" then concat("독거노인,",target2_etc)
	else target2_code
    end
    ) as "sup_obj" ,(
	case target1_code
		when "" then "Nan"
		when "01" then "아이 본인만"
		when "02" then "동반 1인"
		when "03" then "동반 2인"
		when "99" then target1_etc
	else target1_code
    end
	) as "sup_num" ,(
	case item_code
		when "" then ""
        when "01" then ""
        when "02" then ""
		when "99" then item_etc
	else item_code
    end
	) as "sup_item" from stores_db
order by field(area,"경기","서울") desc, addr1 asc,
         field(sup_obj,"소방관","독거노인","결식아동") desc,
		 field(sup_num, target1_etc,"동반 2인","동반 1인");
        

select *
INTO OUTFILE 'C:/stores_1.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
from stores_db1;

select * from stores_db1
