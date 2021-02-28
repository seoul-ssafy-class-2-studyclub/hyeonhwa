-- 고양이와 개는 몇 마리 있을까
SELECT ANIMAL_TYPE, count(ANIMAL_TYPE) as count FROM ANIMAL_INS GROUP BY ANIMAL_TYPE order by ANIMAL_TYPE asc;

-- 동명 동물 수 찾기
SELECT NAME, count(NAME) as count from ANIMAL_INS group by NAME having count(NAME) >= 2 order by NAME asc;

-- 입양 시각 구하기 1
select hour(DATETIME) HOUR, count(DATETIME) COUNT from ANIMAL_OUTS group by hour(DATETIME) having HOUR >= 9 and HOUR <= 19 order by HOUR asc;

-- 입양 시각 구하기 2
set @hour = -1;
select (@hour := @hour + 1) as HOUR, (select count(*) from ANIMAL_OUTS where hour(DATETIME) = @hour) as COUNT from ANIMAL_OUTS where @hour < 23;