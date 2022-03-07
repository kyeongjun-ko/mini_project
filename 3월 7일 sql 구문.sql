use mini_project;

-- 데이터 지우기
-- TRUNCATE stores_db;

-- 테이블 확인하기
select * from stores_db;
select * from stores_db1;

-- 지역명이 겹치는 데이터가 몇개인지 추출하기
select area, count(*) from stores_db
group by area having count(*) > 1;

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
		when "" then "Nan"
        when "01" then "Nan"
        when "02" then "Nan"
		when "99" then item_etc
	else item_code
    end
	) as "sup_item" from stores_db;

-- column 순서 정렬
ALTER TABLE stores_db1 MODIFY COLUMN idx varchar(128) first;
ALTER TABLE stores_db1 MODIFY COLUMN area varchar(128) AFTER idx;
ALTER TABLE stores_db1 MODIFY COLUMN name varchar(128) AFTER area;
ALTER TABLE stores_db1 MODIFY COLUMN addr1 varchar(128) AFTER name;
ALTER TABLE stores_db1 MODIFY COLUMN addr2 varchar(128) AFTER addr1;
ALTER TABLE stores_db1 MODIFY COLUMN zipcode varchar(128) AFTER addr2;
ALTER TABLE stores_db1 MODIFY COLUMN open_info varchar(128) AFTER zipcode;
ALTER TABLE stores_db1 MODIFY COLUMN close_info varchar(128) AFTER open_info;
ALTER TABLE stores_db1 MODIFY COLUMN type varchar(128) AFTER close_info;
ALTER TABLE stores_db1 MODIFY COLUMN target1_code varchar(128) AFTER type;
ALTER TABLE stores_db1 MODIFY COLUMN target1_etc varchar(128) AFTER target1_code;
ALTER TABLE stores_db1 MODIFY COLUMN target2_code varchar(128) AFTER target1_etc;
ALTER TABLE stores_db1 MODIFY COLUMN target2_etc varchar(128) AFTER target2_code;
ALTER TABLE stores_db1 MODIFY COLUMN item_code varchar(128) AFTER target2_etc;
ALTER TABLE stores_db1 MODIFY COLUMN item_etc varchar(128) AFTER item_code;
ALTER TABLE stores_db1 MODIFY COLUMN lat varchar(128) AFTER item_etc;
ALTER TABLE stores_db1 MODIFY COLUMN lng varchar(128) AFTER lat;
ALTER TABLE stores_db1 MODIFY COLUMN img_name varchar(128) AFTER lng;

-- 지역별, 주소별 정렬하기
SELECT * from stores_db1
order by field(area,"경기","서울") desc, addr1 asc,
         field(sup_obj,"소방관","독거노인","결식아동") desc,
		 field(sup_num, target1_etc,"동반 2인","동반 1인");