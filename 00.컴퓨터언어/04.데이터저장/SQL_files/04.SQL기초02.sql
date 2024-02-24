select name, height from usertbl where name like '김%';
select name, height from usertbl where name like '_종신';
select name, height from usertbl where height > 177; -- # 177은 데이터 중 김경호의 키를 의미함. 그러나 177이라는 구체적인 숫자를 적어넣으면 추후 김경호의 키 데이터가 바뀌었을 때 제대로 동작하지 않을 수 있음. 이런 경우 서브쿼리를 쓴다
select name, height from usertbl where height > (select height from usertbl where Name = '김경호');

-- select name,height from usertbl where height >= (select height from usertbl where addr = '경남'). -> 에러 뜸

select name,height from usertbl where height >= any (select height from usertbl where addr = '경남');
/* 지역이 경남인 사람이 둘 있는데 그 사람들의 키가 173,170임. 173 이상이거나 170 이상인 조건에 맞는 데이터 출력됨 -> 170 이상인 데이터가 다 나옴 */

select name, height from usertbl where height >= all (select height from usertbl where addr = '경남');

select name, height from usertbl where height = any (select height from usertbl where addr = '경남');

select name,height from usertbl where height in (select height from usertbl where addr = '경남');

select name, mDate from usertbl order by mDate desc;
select name, height from usertbl order by height desc, name asc;
select name, height from usertbl order by height desc;

select addr from usertbl order by addr;
select distinct addr from usertbl;

use employees;
select emp_no, hire_date from employees order by hire_date asc limit 5;

select emp_no, hire_date from employees order by hire_date asc limit 0,5 -- 'limit 5 offset 0'과 동일한 문장

use sqldb;
create table buytbl2 (select * from buytbl);
select * from buytbl2;

create table buytbl3 (select userID, prodName from buytbl);
select * from buytbl3;

select userID as `사용자 아이디`, SUM(amount) as `총 구매 개수`from buytbl group by userID;
select userID as `사용자 아이디`, sum(price * amount) as `구매액 총합` from buytbl group by userID;

select avg(amount) as'평균 구매 개수' from buytbl;
select userID as `사용자 아이디`, avg(amount) as' 평균 구매 개수' from buytbl group by userID;

select name, max(height), min(height) from usertbl; -- 이렇게 했는데 안 나옴
select name, Max(height), min(height) from usertbl group by name; -- 이래도 안 나옴

select name, height 
from usertbl 
where (height = (select max(height) from usertbl) or height = (select min(height) from usertbl));

select count(*) from usertbl;
select count(mobile1) as '휴대폰이 있는 사용자' from usertbl;

select userID, sum(price*amount) as '총 구매액' from buytbl group by userID;

select userID, sum(price*amount) as '총 구매액' from buytbl where sum(price*amount) > 1000 group by userID; -- 에러 ** 집계 함수 sum, min, max 등은 where 절에 들어갈 수 없다.

select userId, sum(price*amount) as '총 구매액' from buytbl group by userID having sum(price*amount) > 1000;

select userId, sum(price*amount) as '총 구매' from buytbl group by userID having sum(price*amount) > 1000 order by sum(price*amount) asc;

select num,groupName, sum(price*amount) as '비용' from buytbl group by groupName,num with rollup; -- with rollup -> groupName과 num별 소합계를 내줌

select groupName, sum(price*amount) as '비용' from buytbl group by groupName with rollup; -- with rollup -> groupName별 소합계를 내줌

use sqldb;
create table testTbl2 (id int auto_increment primary key, userName char(3), age int);
insert into testTbl2 values (NULL, '지민',25);
insert into testTbl2 values(NULL, '유나',22);
insert into testTbl2 values(NULL, '유경',21);
select * from testTbl2;

alter table testTbl2 auto_increment = 100;
insert into testTbl2 values (NULL,'찬미',23);
select * from testTbl2;

use sqldb;
create table testTbl3
(id int auto_increment primary key,
userName char(3),
age int);
alter table testTbl3 auto_increment=1000;
set @@auto_increment_increment=3;
insert into testTbl3 values(NULL,'나연',20);
insert into testTbl3 values(NULL,'정연',18);
insert into testTbl3 values(NULL,'모모',19);
select * from testTbl3;

use sqldb;
create table testTbl4 (id int, Fname varchar(50), Lname varchar(50));
insert into testTbl4 select emp_no, first_name, last_name from employees.employees;

select * from testTbl4;

use sqldb;
create table testTbl5 (select emp_no, first_name, last_name from employees.employees);

update testTbl4
set Lname = '없음'
where Fname = 'Kyoichi';

select Lname,Fname from testTbl4 where Fname = 'Kyoichi';

use sqldb;
update buytbl set price = price * 1.5

use sqldb;
delete from testTbl4 where Fname = 'Kyoichi' limit 5;

-- python이랑 sql