-- 최댓값 구하기
SELECT DATETIME from ANIMAL_INS order by DATETIME desc limit 1;

-- 최솟값 구하기
SELECT DATETIME FROM ANIMAL_INS ORDER BY DATETIME ASC limit 1;

-- 동물 수 구하기
SELECT count(*) FROM ANIMAL_INS;

-- 중복 제거하기
SELECT count(distinct NAME) FROM ANIMAL_INS where NAME is not null;