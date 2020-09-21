# Write your MySQL query statement below
UPDATE 
    salary
SET 
    sex = CASE 
    WHEN sex = 'm' 
        THEN 'f' 
        ELSE 'm'
        END;


# | id | name | sex | salary |
# |----|------|-----|--------|
# | 1  | A    | m   | 2500   |
# | 2  | B    | f   | 1500   |
# | 3  | C    | m   | 5500   |
# | 4  | D    | f   | 500    |

# After running your update statement, the above salary table should have the following rows:

# | id | name | sex | salary |
# |----|------|-----|--------|
# | 1  | A    | f   | 2500   |
# | 2  | B    | m   | 1500   |
# | 3  | C    | f   | 5500   |
# | 4  | D    | m   | 500    |

