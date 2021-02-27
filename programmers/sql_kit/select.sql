-- 상위 n개 레코드
SELECT NAME from ANIMAL_INS order by DATETIME limit 1;

-- 여러 기준으로 정렬하기
SELECT ANIMAL_ID, NAME, DATETIME from ANIMAL_INS order by NAME asc, DATETIME desc;

-- 동물의 아이디와 이름
SELECT ANIMAL_ID, NAME from ANIMAL_INS order by ANIMAL_ID;

-- 어린 동물 찾기
SELECT ANIMAL_ID, NAME from ANIMAL_INS where INTAKE_CONDITION != "Aged" order by ANIMAL_ID;

-- 아픈 동물 찾기
SELECT ANIMAL_ID, NAME from ANIMAL_INS where INTAKE_CONDITION = "Sick";

-- 역순 정렬하기
SELECT NAME, DATETIME from ANIMAL_INS order by ANIMAL_ID desc;

-- 모든 레코드 조회하기
SELECT * from ANIMAL_INS order by ANIMAL_ID;