CREATE database PROJECT;
USE PROJECT;
SELECT * FROM hr;

alter table HR
change column ï»¿id emp_id varchar(20)null;

describe hr;

select birthdate from hr;

update hr
SET  birthdate = case
when  birthdate like '%/%' then date_format(str_to_date(birthdate,'%m/%d/%Y'),'%Y-%m-%d')
when  birthdate like '%-%' then date_format(str_to_date(birthdate,'%m-%d-%Y'),'%Y-%m-%d')
else null
end;

select birthdate from hr;


alter table HR
modify birthdate date;

update hr
SET  hire_date = case
when  hire_date like '%/%' then date_format(str_to_date(hire_date,'%m/%d/%Y'),'%Y-%m-%d')
when  hire_date like '%-%' then date_format(str_to_date(hire_date,'%m-%d-%Y'),'%Y-%m-%d')
else null
end;
select hire_date from hr;

alter table hr
modify column hire_date date;

select termdate from hr;

update hr
set termdate = date(str_to_date(termdate,'%Y-%m-%d %H:%i:%s UTC'))
where termdate is not null and termdate !=' ';
select termdate from hr;

ALTER TABLE hr
MODIFY COLUMN termdate DATE;

ALTER table HR ADD column Age int;  
update hr
set Age = timestampdiff(year,birthdate, curdate());

select birthdate,age from hr;

select 
min(age)as youngest,
max(age)as oldest
from hr;

select count(*) as child_labour from hr
where age < 18;

SET SQL_MODE='';

-- 1.what is the gender breakdown of employees in the company?

select gender,count(*) as count
from hr
where age >= 18 and termdate ='0000-00-00'
group by gender;

-- 2.what is the race/ethnicity breakdown of employees in the company?

select race,count(*)as count
from hr
where age>=18 and termdate='0000-00-00'
group by race
order by count(*)desc;

-- 3. what is the age distribution of employees in the company?

select 
min(age) as youngest,
max(age) as oldest
from hr
where age>=18 and termdate='0000-00-00';

describe hr;
SELECT
 CASE
  WHEN AGE >=18 AND AGE <=24 THEN '18-24'
  WHEN AGE >=25 AND AGE <=34 THEN '25-34'
  WHEN AGE >=35 AND AGE <=44 THEN '35-44'
  WHEN AGE >=45 AND AGE <=54 THEN '45-54'
  WHEN AGE >=55 AND AGE <=64 THEN '55-64'
  ELSE '65+'
END AS age_group,
count(*) as count
from hr
where age>=18 and termdate='0000-00-00'
group by age_group
order by age_group;

SELECT
 CASE
  WHEN AGE >=18 AND AGE <=24 THEN '18-24'
  WHEN AGE >=25 AND AGE <=34 THEN '25-34'
  WHEN AGE >=35 AND AGE <=44 THEN '35-44'
  WHEN AGE >=45 AND AGE <=54 THEN '45-54'
  WHEN AGE >=55 AND AGE <=64 THEN '55-64'
  ELSE '65+'
END AS age_group,
count(*) as count,gender
from hr
where age>=18 and termdate='0000-00-00'
group by age_group,gender
order by age_group,gender;

-- 4.how many employees work at headquarters versus remote locations?

select location,count(*) as count
from hr
where age>=18 and termdate='0000-00-00'
group by location;

-- 5.what is the  average length of employees who have been terminated?
select
round(avg(datediff(termdate,hire_date))/365,0)as average_lenth_employment
from hr
where termdate<=curdate() and termdate<>'0000-00-00' and age>=18;

-- 6.How does gender distribution vary across and job titles?

select department,gender,count(*) as count from hr
where age>=18 and termdate='0000-00-00'
group by department,gender
order by department;

-- 7.what is the distribution of job titles across the company?

select jobtitle,count(*) as count 
from hr
where age >=18 and termdate='0000-00-00'
group by jobtitle
order by jobtitle desc;

-- which department has the highest turnoverrate?

select * from hr;

select department,
total_count,
termination_count,
termination_count/total_count as termination_rate
from(
  select department,
  count(*)as total_count,
  sum(case when termdate<>'0000-00-00'and termdate<=curdate()then 1 else 0 end)as termination_count
  from hr
  where age >=18
  group by department
  )as subquery
order by termination_rate desc;

-- 9.what is the distribution of employees across locations by city and state?

select location_state,count(*)as count
 from hr
 where age >=18 and termdate='0000-00-00'
 group by location_state
 order by count desc;
 
 -- 10.how has the company's employees count changed over time based on hire and term dates?
 select
 year,
 hires,
 terminations,
 hires-terminations as net_change,
 round((hires-terminations)/hires*100,2) as net_change_percent
 from(
	select 
    year(hire_date) as year,
    count(*) as hires,
    sum(case when termdate <> '0000-00-00' and termdate <= curdate() then 1 else 0 end)as terminations
    from hr
    where age >=18
    group by year(hire_date)
)as subquery
order by year asc;

-- 11.what is the tenure distribution for each department?
select department,round(avg(datediff(termdate,hire_date)/365),0) as avg_tenure
from hr
where age >=18 and termdate <>'0000-00-00' and termdate <= curdate()
group by department;
    

