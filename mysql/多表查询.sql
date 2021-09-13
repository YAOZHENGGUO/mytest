-- 1. 查出至少有一个员工的部门。显示部门编号、部门名称、部门位置、部门人数。
SELECT 
  t1.`deptno`,
  t1.`dname`,
  t1.`loc`,
  t2.cn 
FROM
  t_dept t1,
  (SELECT 
    deptno,
    COUNT(*) cn 
  FROM
    t_employees 
  GROUP BY deptno 
  HAVING cn >= 1) t2 
WHERE t1.deptno = t2.deptno ;

-- 3.列出所有员工的姓名及其直接上级的姓名。
SELECT 
  t1.`ename`,
  t2.`ename` 
FROM
  t_employees t1,
  t_employees t2 
WHERE t1.`MGR` = t2.`empno` ;

-- 4. 列出受雇日期早于直接上级的所有员工的编号、姓名、部门名称。
SELECT 
  t1.`empno`,
  t1.`ename`,
  t3.`deptno` 
FROM
  t_employees t1,
  t_employees t2,
  t_dept t3 
WHERE t1.`MGR` = t2.`empno` 
  AND t1.`hiredate` < t2.`hiredate` 
  AND t1.`deptno` = t3.`deptno` ;

-- 5.列出部门名称和这些部门的员工信息，同时列出那些没有员工的部门。
SELECT 
  * 
FROM
  t_employees t1 
  RIGHT JOIN t_dept t2 
    ON t1.`deptno` = t2.`deptno` ;

-- 7. 列出最低薪金大于15000的各种工作及从事此工作的员工人数。
SELECT 
  job,
  COUNT(*) 
FROM
  t_employees 
GROUP BY job 
HAVING MIN(sal) > 15000 ;

-- 8. 列出在公关部工作的员工的姓名，假定不知道公关部的部门编号。
SELECT 
  t1.`ename` 
FROM
  t_employees t1 
WHERE t1.`deptno` = 
  (SELECT 
    deptno 
  FROM
    t_dept t2 
  WHERE t2.`dname` = '公关部') ;

-- 9. 列出薪金高于公司平均薪金的所有员工信息，所在部门名称，上级领导，工资等级。
SELECT 
  t1.*,
  t3.`dname`,
  t2.`ename` 
FROM
  t_employees t1 
  LEFT OUTER JOIN t_dept t3 
    ON t1.`deptno` = t3.`deptno` 
  LEFT OUTER JOIN t_employees t2 
    ON t1.`MGR` = t2.`empno` 
WHERE t1.`sal` > 
  (SELECT 
    AVG(sal) 
  FROM
    t_employees) ;

-- 10.列出与张飞从事相同工作的所有员工及部门名称。
SELECT 
  t1.`ename`,
  t2.`dname` 
FROM
  t_employees t1,
  t_dept t2 
WHERE t1.`deptno` = t2.`deptno` 
  AND job = 
  (SELECT 
    job 
  FROM
    t_employees 
  WHERE ename = '张飞') ;

-- 11.列出薪金高于在部门30工作的所有员工的薪金的员工姓名和薪金、部门名称。
SELECT 
  t1.`ename`,
  t1.`sal`,
  t2.`dname` 
FROM
  t_employees t1,
  t_dept t2 
WHERE t1.`deptno` = t2.`deptno` 
  AND sal > ALL 
  (SELECT 
    sal 
  FROM
    t_employees 
  WHERE deptno = 30) ;