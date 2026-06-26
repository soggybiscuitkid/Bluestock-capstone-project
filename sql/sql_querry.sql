-- 1 Top 5 funds by AUM

SELECT *
FROM aum
ORDER BY aum DESC
LIMIT 5;

------------------------------------------------

-- 2 Average NAV by month

SELECT
strftime('%Y-%m',date) AS month,
AVG(nav)
FROM nav_history
GROUP BY month;

------------------------------------------------

-- 3 SIP YoY growth

SELECT
year,
SUM(amount)
FROM investor_transactions
WHERE transaction_type='SIP'
GROUP BY year;

------------------------------------------------

-- 4 Transactions by state

SELECT
state,
COUNT(*)
FROM investor_transactions
GROUP BY state;

------------------------------------------------

-- 5 Funds expense ratio < 1%

SELECT *
FROM scheme_performance
WHERE expense_ratio < 1;

------------------------------------------------

-- 6 Highest 5 year returns

SELECT *
FROM scheme_performance
ORDER BY return_5yr DESC
LIMIT 10;

------------------------------------------------

-- 7 Average NAV fund house wise

SELECT
fund_house,
AVG(nav)
FROM nav_history n
JOIN fund_master f
ON n.amfi_code=f.amfi_code
GROUP BY fund_house;

------------------------------------------------

-- 8 Total redemption amount

SELECT
SUM(amount)
FROM investor_transactions
WHERE transaction_type='Redemption';

------------------------------------------------

-- 9 Number of funds per category

SELECT
category,
COUNT(*)
FROM fund_master
GROUP BY category;

------------------------------------------------

-- 10 Highest AUM fund house

SELECT
fund_house,
SUM(aum)
FROM aum
GROUP BY fund_house
ORDER BY SUM(aum) DESC
LIMIT 1;