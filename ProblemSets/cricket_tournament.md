# PSET: Analyze the roaster of cricket tournament, having Team Name, Matches Played, No Of Wins, No Of Loss as the analyze output.


### DDL:
```SQL
CREATE TABLE icc_world_cup
(
    team_1 Varchar(20),
    team_2 Varchar(20),
    einner Varchar(20)
);
INSERT INTO icc_world_cup values('India','SL','India');
INSERT INTO icc_world_cup values('SL','Aus','Aus');
INSERT INTO icc_world_cup values('SA','Eng','Eng');
INSERT INTO icc_world_cup values('Eng','NZ','NZ');
INSERT INTO icc_world_cup values('Aus','India','India');
```


### Solution:

#### SQL:
1. Brute Force
```SQL
WITH 
    cte_all AS (
        SELECT team_1 AS team 
        FROM icc_world_cup 
        UNION ALL 
        SELECT team_2 AS team 
        FROM icc_world_cup
    ), 
    cte_uniq AS (
        SELECT team, COUNT(1) AS total_count 
        FROM cte_all 
        GROUP BY team
    ), 
    cte_win AS (
        SELECT winner, COUNT(1) AS win_count 
        FROM icc_world_cup 
        GROUP BY winner
    ), 
    cte_loss AS (
        SELECT IF(winner = team_1, team_2, team_1) AS losser,count(1) AS loss_count 
        FROM icc_world_cup 
        GROUP BY losser
    ) 
SELECT c.team, c.total_count AS matches_played, IFNULL(w.win_count,0) AS win_count, IFNULL(l.loss_count,0) AS loss_count 
FROM cte_uniq c 
    LEFT join cte_win w 
        ON c.team=w.winner 
            LEFT JOIN cte_loss l 
                ON l.losser = c.team 
ORDER BY win_count DESC, loss_count ASC; 
```

2. Optimized
```SQL
SELECT team_name, count(1) AS no_of_matches_played, SUM(win_flag) AS no_of_matches_won, COUNT(1) - SUM(win_flag) AS no_of_losses
FROM(
    SELECT team_1 AS team_name, CASE WHEN team_1=winner THEN 1 ELSE 0 END AS win_flag
    FROM icc_world_cup
    UNION ALL
    SELECT team_2 AS team_name, CASE WHEN team_2=winner THEN 1 ELSE 0 END AS win_flag
    FROM icc_world_cup
) A
GROUP BY team_name
ORDER BY no_of_matches_won DESC;
```


3. CASE WHEN Optimized
```SQL
WITH temp AS (
    SELECT team_1 AS team, winner 
    FROM icc_world_cup 
    UNION ALL
    SELECT team_2 AS team, winner 
    FROM icc_world_cup
) 
SELECT 
    team, 
    COUNT(1) AS no_of_matches_played, 
    SUM(CASE WHEN winner = team THEN 1 ELSE 0 END) AS no_of_matches_won, 
    SUM(CASE WHEN winner <> team THEN 1 ELSE 0 END) AS no_of_matches_lost 
FROM temp 
GROUP BY team;
```

4. IF Optimized
```SQL
WITH temp AS (
    SELECT team_1 AS team, winner 
    FROM icc_world_cup 
    UNION ALL
    SELECT team_2 AS team, winner 
    FROM icc_world_cup
) 
SELECT 
    team, 
    COUNT(1) AS no_of_matches_played, 
    SUM(IF(winner = team, 1,0)) AS no_of_matches_won, 
    SUM(IF(winner <> team,1,0)) AS no_of_matches_lost 
FROM temp 
GROUP BY team;
```

5. **Additional Question :** Write No of draws too.
```SQL
WITH temp AS (
    SELECT team_1 AS team, winner 
    FROM icc_world_cup 
    UNION ALL
    SELECT team_2 AS team, winner 
    FROM icc_world_cup
) 
SELECT 
    team, 
    COUNT(1) AS no_of_matches_played, 
    SUM(IF(winner = team, 1,0)) AS no_of_matches_won, 
    SUM(IF(winner <> team AND winner != 'DRAW',1,0)) AS no_of_matches_lost,
    SUM(IF(winner = 'DRAW', 1, 0)) AS no_of_draw
FROM temp 
GROUP BY team;
```

6. **Additional Questions:** Calculate % of match won and lost (most easy and optimised approach)

```SQL
WITH temp AS (
    SELECT team_1 AS team, winner 
    FROM icc_world_cup 
    UNION ALL
    SELECT team_2 AS team, winner 
    FROM icc_world_cup
) 
SELECT 
    team, 
    COUNT(1) AS no_of_matches_played, 
    SUM(IF(winner = team, 1,0)) AS no_of_matches_won, 
    SUM(IF(winner <> team AND winner != 'DRAW',1,0)) AS no_of_matches_lost,
    SUM(IF(winner = 'DRAW', 1, 0)) AS no_of_draw,
    ROUND((SUM(IF(winner = team, 1,0))/COUNT(team))*100,2) AS won_match_percentage,
    ROUND((SUM(IF(winner <> team AND winner != 'DRAW',1,0))/COUNT(team))*100,2) AS won_match_percentage
FROM temp 
GROUP BY team;
```