create database dannys_diner;

use dannys_diner;

drop database dannys_diner;
create table sales(
customer_id varchar(1),
order_date date,
product_id int
);
insert into sales values('A', '2021-01-01', 1);
insert into sales values('A', '2021-01-01', 2);
insert into sales values('A', '2021-01-07', 2);
insert into sales values('A', '2021-01-10', 3);
insert into sales values('A', '2021-01-11', 3);
insert into sales values('A', '2021-01-11', 3);
insert into sales values('B', '2021-01-01', 2);
insert into sales values('B', '2021-01-02', 2);
insert into sales values('B', '2021-01-04', 1);
insert into sales values('B', '2021-01-11', 1);
insert into sales values('B', '2021-01-16', 3);
insert into sales values('B', '2021-02-01', 3);
insert into sales values('C', '2021-01-01', 3);
insert into sales values('C', '2021-01-01', 3);
insert into sales values('C', '2021-01-07', 3);

select * from sales;

create table menu(
product_id int,
product_name varchar(5),
price int
);
insert into menu values(1, 'sushi', 10);
insert into menu values(2, 'curry', 15);
insert into menu values(3, 'ramen', 12);

select * from menu;

create table members(
customer_id varchar(1),
join_date date
);
insert into members
(customer_id,join_date)
values
('A', '2021-01-07'),
('B', '2021-01-09');

select * from members;

-- 1.what is the total amount each customer spend at the restaurant?

select s.customer_id,sum(m.price) as total_spent
from sales as s
join menu as m
on s.product_id = m.product_id
group by s.customer_id;

-- 2.How many days each customer visited the restaurent?

select s.customer_id,count(distinct s.order_date) as days_visited
from sales s 
group by s.customer_id;

-- 3.what was the first item from the menu purched by each customer?


with customer_first_purchase as(
 select s.customer_id,min(s.order_date)as first_purchase_date
 from sales as s
 group by s.customer_id
 )
 select distinct cfp.customer_id,cfp.first_purchase_date,m.product_name
 from customer_first_purchase as cfp
 join sales as s on s.customer_id=cfp.customer_id
 and cfp.first_purchase_date=s.order_date
 join menu as m on s.product_id = m.product_id;
 
 -- 4.what is the most purchased item on the menu and how many times was it purchased by customer?
 
 select m.product_name,count(*) as total_purchased 
 from menu as m
 join sales as s on s.product_id = m.product_id
 group by m.product_name
 order by total_purchased desc
 limit 1;
 
 
 -- 5. Which item was the most popular for each customer?
 WITH CUSTOMER_POPULARITY AS(
SELECT S.CUSTOMER_ID,M.PRODUCT_NAME,COUNT(*) AS TOTAL_COUNT,
dense_rank() OVER (PARTITION BY S.CUSTOMER_ID ORDER BY COUNT(*) DESC) AS RANKS
FROM SALES AS S
JOIN MENU AS M ON S.PRODUCT_ID = M.PRODUCT_ID
GROUP BY S.CUSTOMER_ID,M.PRODUCT_NAME
)
select CP.CUSTOMER_ID,CP.PRODUCT_NAME,CP.TOTAL_COUNT
FROM CUSTOMER_POPULARITY AS CP
WHERE RANKS=1;

-- 6.Which item was purchased first by the customer after they became a member?

WITH FIRST_PURCHASE_AFTER_MEMBER AS (
	SELECT S.CUSTOMER_ID,MIN(S.ORDER_DATE) AS FIRST_PURCHASED_DATE
	FROM SALES AS S
	JOIN MEMBERS AS MB ON S.CUSTOMER_ID = MB.CUSTOMER_ID
	where S.ORDER_DATE >= MB.JOIN_DATE
	group by S.CUSTOMER_ID
)
SELECT  FPAM.CUSTOMER_ID, M. PRODUCT_NAME 
FROM FIRST_PURCHASE_AFTER_MEMBER AS FPAM
JOIN SALES AS S ON S.CUSTOMER_ID = FPAM.CUSTOMER_ID
AND S.ORDER_DATE = FPAM.FIRST_PURCHASED_DATE
JOIN MENU AS M ON S.PRODUCT_ID = M. PRODUCT_ID
order by S.CUSTOMER_ID asc;

-- 7. Which item was purchased just before the cutomer became a member?
WITH LAST_PURCHASE_BEFORE_MEMBERSHIP AS (
	SELECT S.CUSTOMER_ID,max(S.ORDER_DATE) AS LAST_PURCHASED_DATE
	FROM SALES AS S
	JOIN MEMBERS AS MB ON S.CUSTOMER_ID = MB.CUSTOMER_ID
	where S.ORDER_DATE < MB.JOIN_DATE
	group by S.CUSTOMER_ID
)
SELECT LPBM.CUSTOMER_ID,M.PRODUCT_NAME
FROM LAST_PURCHASE_BEFORE_MEMBERSHIP AS LPBM
JOIN SALES AS S ON LPBM.CUSTOMER_ID = S.CUSTOMER_ID
AND S.ORDER_DATE = LPBM.LAST_PURCHASED_DATE
JOIN MENU AS M ON M.PRODUCT_ID =S.PRODUCT_ID
order by S.CUSTOMER_ID asc;

-- 8.What is the total items and amount spent each member before they become a member?

select s.customer_id,count(*) as total_item,sum(m.price)as total_amount
from sales as s
join menu as m on s.product_id = m.product_id
join members as mb on s.customer_id = mb.customer_id
where s.order_date < join_date
group by s.customer_id
order by s.customer_id asc;

-- 9.If each $1 spent equates to 10 points and sushi has a 2X points multiplier - how many points would each customer have?

select s.customer_id,sum(
	case
		when m.product_name='sushi'then m.price*20
        else m.price*10 end)as total_points
from sales as s
join menu as m on m.product_id= s.product_id
group by s.customer_id;

/*  10. In the first week after a customer joins the program (including their join date)
they earn 2X points on all items,not just sushi
how many points do customer a and b have at the end of january? */
select s.customer_id,sum(
	case
		when s.order_date between mb.join_date and DATEADD(day,7,mb.join_date)
        then m.price*20
        when m.product_name='sushi' then m.price*20
        else m.price*10 end)as total_points
from sales as s
join menu as m on m.product_id= s.product_id
left join members as mb on s.customer_id=mb.customer_id
where s.customer_id in ('a','b') AND s.order_date <='2021-01-31'
group by s.customer_id;

-- 11. Recreate the table output using the available data?

select s.customer_id,s.order_date,m.product_name,m.price,
	case
		when s.order_date >= mb.join_date then 'Y'
        else 'N'end as members
from sales as s
join menu as m on s.product_id = m.product_id
left join members as mb on s.customer_id =mb.customer_id
order by s.customer_id,s.order_date;

-- 12.ranking all the thinks

with customer_date as (
	select s.customer_id,s.order_date,m.product_name,m.price,
		case
			when s.order_date < mb.join_date then 'NO'
			when s.order_date >= mb.join_date then 'YES'
			ELSE 'NO' END AS members
	from sales as s
	join menu as m on s.product_id= m. product_id
	left join members as mb on mb.customer_id = s.customer_id
	order by s.customer_id,s.order_date
)
select *,
	CASE
		WHEN members='no' then null
        else rank() over(partition by s.customer_id,members order by s.order_date)
        end as ranking
from customer_date as cd
order by s.customer_id,s.order_date;
