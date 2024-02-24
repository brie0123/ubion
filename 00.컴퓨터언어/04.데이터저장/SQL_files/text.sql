select * from sqldb.usertbl;
select userID, Name from usertbl where birthYear >= 1970 or height >= 182;

select name, height from usertbl where height >= 180 and height <= 183;
select name, height from usertbl where height between 180 and 183;

select name, addr from usertbl where addr = '경남' or '전남' or '경북';
select name, addr from usertbl where addr in ('경남','전남','전북');