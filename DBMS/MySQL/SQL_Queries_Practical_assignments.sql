create database TOPS01;
use TOPS01;
/*
1. find customers who are either from the city 'NewYork' or
who do not have a grade greater than 100. Return customer_id, cust_name, city, grade, and salesman_id
*/
SELECT * FROM customer WHERE city = "NewYork" or grade > 100;
/*
2. find all the customers in ‘New York’ city who have a gradevalue above 100. 
Return customer_id, cust_name, city, grade, and salesman_id.
*/
SELECT * FROM customer WHERE city = "NewYork" AND grade > 100;
/*
3. displays order number, purchase amount, and the
achieved and unachieved percentage (%) for those orders that exceed 50% of the target value of 6000.
*/
SELECT ord_no,purch_amt,
    ROUND((purch_amt / 6000.0) * 100, 2) AS achieved_percentage,
    ROUND(100 - ((purch_amt / 6000.0) * 100), 2) AS unachieved_percentage
FROM orders WHERE (purch_amt / 6000.0) * 100 > 50;
/*
4. calculate the total purchase amount of all orders. Returntotal purchase amount 
*/
SELECT sum(purch_amt) from orders;
/*
5. find the highest purchase amount ordered by each customer.
Return customer ID, maximum purchase amount.
*/
SELECT customer_id, max(purch_amt) FROM orders GROUP BY customer_id;
/*
6. calculate the average product price. Return average product
price.
*/
SELECT avg(pro_price) FROM products;
/*
7. find those employees whose department is located at ‘Toronto’.
 Return first name, last name, employee ID, job ID
*/
-- for above query view is already provided as emp_details_view

CREATE VIEW emp_details_view AS SELECT e.employee_id,
	e.job_id,e.manager_id,e.department_id,d.location_id,l.country_id,
	e.first_name,e.last_name,e.salary,e.commission_pct,d.department_name,j.job_title,
	l.city,l.state_province,c.country_name,r.region_name
FROM employees e,
	departments d,jobs j,locations l,countries c,regions r
WHERE e.department_id = d.department_id
	AND d.location_id = l.location_id
	AND l.country_id = c.country_id
	AND c.region_id = r.region_id
	AND j.job_id = e.job_id;


use tops02;
SELECT * FROM emp_details_view WHERE city = "Toronto";
/*
8. find those employees whose salary is lower than that of
employees whose job title is "MK_MAN". Exclude employees of the Job title
‘MK_MAN’. Return employee ID, first name, last name, job ID.
*/
SELECT employee_id, first_name, last_name,job_id FROM employees WHERE 
salary < 
(
SELECT min(salary) FROM employees WHERE job_id = "MK_MAN"
) AND job_id != "MK_MAN";

/*
9. find all those employees who work in department ID 80 or
40. Return first name, last name, department number and department name.
*/
SELECT first_name,last_name,department_id, department_name FROM emp_details_view 
WHERE department_id = 80 or department_id = 40;
/*
10. calculate the average salary, the number of employees
receiving commissions in that department. Return department name, average
salary and number of employees.
*/
SELECT d.department_name, avg(salary) as Avg_Sal, count(e.commission_pct) AS com_emp 
FROM employees e JOIN departments d ON e.department_id = d.department_id GROUP BY d.department_name;

/*
11. find out which employees have the same designation as the
employee whose ID is 169. Return first name, last name, department ID and job
ID.
*/
SELECT first_name,last_name, department_id, job_id FROM emp_details_view WHERE
job_title = (
SELECT job_title FROM emp_details_view WHERE employee_id = 169
);
/*
12. find those employees who earn more than the average salary.
Return employee ID, first name, last name.
*/ 
SELECT employee_id, first_name, last_name FROM emp_details_view WHERE salary > (
SELECT avg(salary) FROM emp_details_view
);

/*
13. find all those employees who work in the Finance
department. Return department ID, name (first), job ID and department name.
*/
SELECT department_id, first_name, job_id, department_name FROM emp_details_view WHERE department_name = "Finance";
/*
14. find the employees who earn less
than the employee of ID 182. Return first name, last name and salary.
*/
SELECT first_name, last_name, salary FROM emp_details_view WHERE salary <  
(
    SELECT salary FROM emp_details_view WHERE employee_id = 182
);

/*
15. 
Create a stored procedure CountEmployeesByDept that returns the number of
employees in each department
*/
DELIMITER //
CREATE PROCEDURE CountEmployeesByDept()
BEGIN
    SELECT department_id,department_name, COUNT(*) AS EmployeeCount
    FROM emp_details_view
    GROUP BY department_id;
END //
DELIMITER ;

/*
16. Create a stored procedure AddNewEmployee that adds a new employee to the
database.
*/
DELIMITER //
CREATE PROCEDURE AddNewEmployee(
	IN employee_id int, IN first_name text,IN last_name text, IN email Text, 
    IN phone_number text, in hire_date date, in job_id int , in salary float, in commission_pct int,
    in manager_id int, in department_id int
)
BEGIN
		INSERT INTO employees VALUES 
        (employee_id, first_name, last_name, email, phone_number, 
        hire_date, job_id, salary, commission_pct, manager_id, department_id);
END //
DELIMITER ;

/*
17. Create a stored procedure DeleteEmployeesByDept that removes all employees from a specific department
*/
DELIMITER //
CREATE PROCEDURE DeleteEmployeesByDept(IN p_DepartmentID INT)
BEGIN
    DELETE FROM Employees
    WHERE DepartmentID = p_DepartmentID;
END //
DELIMITER ;

/*
18. Create a stored procedure GetTopPaidEmployees that retrieves the highest-paid
employee in each department.
*/
DELIMITER //
CREATE PROCEDURE GetTopPaidEmployees()
BEGIN
    SELECT *
    FROM emp_details_view e
    WHERE salary = (
        SELECT MAX(salary)
        FROM emp_details_view
        WHERE department_id = e.department_id
    );
END //
DELIMITER ;

/*
19. Create a stored procedure PromoteEmployee that increases an employee’s salary
and changes their job role.
*/
DELIMITER //
CREATE PROCEDURE PromoteEmployee(
    IN p_EmployeeID INT,
    IN p_NewSalary DECIMAL(10,2),
    IN p_NewJobID VARCHAR(10)
)
BEGIN
    UPDATE Employees
    SET salary = p_NewSalary,
        job_id = p_NewJobID
    WHERE employee_id = p_EmployeeID;
END //
DELIMITER ;

/*
20. Create a stored procedure AssignManagerToDepartment that assigns a new
manager to all employees in a specific department.
*/
DELIMITER //
CREATE PROCEDURE AssignManagerToDepartment(
    IN department_id INT,
    IN manager_id INT
)
BEGIN
    UPDATE Employees
    SET manager_id = manager_id
    WHERE department_id = department_id;
END //
DELIMITER ;
