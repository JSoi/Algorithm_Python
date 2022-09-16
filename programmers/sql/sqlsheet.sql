/**
  https://school.programmers.co.kr/learn/courses/30/lessons/59042
  없어진 기록 찾기
 */
-- RIGHT OUTER JOIN
SELECT OUTS.ANIMAL_ID, OUTS.NAME
FROM ANIMAL_INS AS INS
         RIGHT OUTER JOIN ANIMAL_OUTS AS OUTS ON INS.ANIMAL_ID = OUTS.ANIMAL_ID
WHERE INS.DATETIME IS NULL

-- LEFT OUTER JOIN
SELECT OUTS.ANIMAL_ID, OUTS.NAME
FROM ANIMAL_OUTS AS OUTS
         LEFT OUTER JOIN ANIMAL_INS AS INS ON INS.ANIMAL_ID = OUTS.ANIMAL_ID
WHERE INS.DATETIME IS NULL

/**
  https://school.programmers.co.kr/learn/courses/30/lessons/59406
  동물 수 구하기
 */
SELECT COUNT(*) AS `count`
FROM ANIMAL_INS

/**
  https://school.programmers.co.kr/learn/courses/30/lessons/59408
  중복 제거하기
 */
SELECT COUNT(NEWTABLE.NAME) AS `count`
FROM (SELECT DISTINCT NAME FROM ANIMAL_INS WHERE NAME IS NOT NULL GROUP BY NAME) NEWTABLE;

/*
https://school.programmers.co.kr/learn/courses/30/lessons/59038
최솟값 구하기
 */
SELECT DATETIME AS `시간`
FROM ANIMAL_INS
WHERE DATETIME = (SELECT MIN(DATETIME) FROM ANIMAL_INS)

/*
https://school.programmers.co.kr/learn/courses/30/lessons/59047
이름에 EL 들어가는 동물 찾기
 */
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE UPPER(NAME) LIKE '%EL%'
  AND ANIMAL_TYPE = 'Dog'
ORDER BY NAME

/*
https://school.programmers.co.kr/learn/courses/30/lessons/59410
NULL 처리하기
 */
SELECT ANIMAL_TYPE, IFNULL(NAME, "No name") AS NAME, SEX_UPON_INTAKE
FROM ANIMAL_INS
ORDER BY ANIMAL_ID;


