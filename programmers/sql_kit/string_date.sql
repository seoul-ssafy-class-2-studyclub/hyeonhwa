-- 루시와 엘라 찾기
select ANIMAL_ID, NAME, SEX_UPON_INTAKE from ANIMAL_INS where NAME in ("Lucy", "Ella", "Pickle", "Rogan", "Sabrina", "Mitty") order by ANIMAL_ID

-- 이름에 el이 들어가는 동물 찾기
select ANIMAL_ID, NAME from ANIMAL_INS where NAME like "%EL%" and ANIMAL_TYPE = "Dog" order by NAME;

-- 중성화 여부 파악하기
select ANIMAL_ID, NAME, case when SEX_UPON_INTAKE like "%Neutered%" or SEX_UPON_INTAKE like "%Spayed%" then "O" else "X" end as "중성화" from ANIMAL_INS order by ANIMAL_ID;

-- 오랜 기간 보호한 동물2
select a.ANIMAL_ID, a.NAME from ANIMAL_INS as a, ANIMAL_OUTS as b where a.ANIMAL_ID = b.ANIMAL_ID order by datediff(a.DATETIME, b.DATETIME) limit 2;

-- DATETIME에서 DATE로 형 변환
select ANIMAL_ID, NAME, date_format(DATETIME, "%Y-%m-%d") as "날짜" from ANIMAL_INS order by ANIMAL_ID;