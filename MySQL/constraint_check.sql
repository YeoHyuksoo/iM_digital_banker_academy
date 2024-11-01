use employees;

desc dept_emp;
desc employees;
desc departments;

select * from information_schema.table_constraints
	where table_name = "dept_emp";
    
select * from information_schema.table_constraints
	where table_name = "employees";

select * from information_schema.table_constraints
	where constraint_schema = "employees";
    
    


    