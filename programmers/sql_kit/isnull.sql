-- 이름이 없는 동물의 아이디
select ANIMAL_ID from ANIMAL_INS where NAME is null order by ANIMAL_ID asc;

-- 이름이 있는 동물의 아이디
select ANIMAL_ID from ANIMAL_INS where NAME is not null order by ANIMAL_ID asc;

-- NULL 처리하기
select ANIMAL_TYPE, ifnull(NAME, "No name"), SEX_UPON_INTAKE from ANIMAL_INS;