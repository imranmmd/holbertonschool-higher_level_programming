-- izmirin daglarinda cicekler acar
SELECT score, COUNT(*) AS number FROM second_table
GROUP BY score
ORDER BY number DESC;
