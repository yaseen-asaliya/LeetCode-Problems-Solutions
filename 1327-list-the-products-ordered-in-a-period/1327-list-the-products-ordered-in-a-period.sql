# Write your MySQL query statement below

select p.product_name, sum(o.unit) as unit from Products p inner join Orders o on p.product_id = o.product_id 
where order_date LIKE '2020-02-%'
group by o.product_id 
having sum(o.unit) >= 100;


