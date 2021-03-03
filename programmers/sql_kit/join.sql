-- 없어진 기록 찾기
select b.ANIMAL_ID, b.NAME from ANIMAL_INS as a right join ANIMAL_OUTS as b on a.ANIMAL_ID = b.ANIMAL_ID where a.ANIMAL_ID is null;

-- 있었는데요 없었습니다
select a.ANIMAL_ID, a.NAME from ANIMAL_INS as a join ANIMAL_OUTS as b on a.ANIMAL_ID = b.ANIMAL_ID where a.DATETIME > b.DATETIME order by a.DATETIME;

-- 오랜 기간 보호한 동물1
select a.NAME, a.DATETIME from ANIMAL_INS as a left join ANIMAL_OUTS as b on a.ANIMAL_ID = b.ANIMAL_ID where b.ANIMAL_ID is null order by a.DATETIME limit 3;

-- 보호소에서 중성화한 동물
select b.ANIMAL_ID, b.ANIMAL_TYPE, b.NAME from ANIMAL_OUTS as b join ANIMAL_INS as a on a.ANIMAL_ID = b.ANIMAL_ID where a.SEX_UPON_INTAKE != b.SEX_UPON_OUTCOME order by b.ANIMAL_ID;