SELECT * FROM employee 

SELECT * FROM category c 

SELECT * from subCategory sc

SELECT * FROM product p 

select sc.description as Name_SubCategory, c.description as Name_Category from subCategory sc 
inner join category c 
on sc.idCategory = c.id 
order by sc.description asc;

select p.description as Name_Produto, sc.description as Name_SubCategory, c.description as Name_Category from product p 
inner join subCategory sc  
on p.idSubCategory = sc.id 
inner join category c 
on sc.idCategory = c.id 
order by p.description  asc;