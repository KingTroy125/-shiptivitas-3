-- TYPE YOUR SQL QUERY BELOW

-- PART 1: Daily Active Users Analysis
WITH user_metrics AS (
    SELECT 
        date(timestamp) as day,
        COUNT(DISTINCT user_id) as daily_active_users,
        CASE 
            WHEN date(timestamp) < '2018-06-02' THEN 'Before Kanban'
            ELSE 'After Kanban'
        END as period
    FROM user_actions
    GROUP BY date(timestamp)
)
SELECT 
    period,
    AVG(daily_active_users) as avg_daily_users,
    MIN(daily_active_users) as min_users,
    MAX(daily_active_users) as max_users
FROM user_metrics
GROUP BY period;

-- PART 2: Status Changes Analysis
WITH card_metrics AS (
    SELECT 
        date(timestamp) as day,
        card_id,
        COUNT(*) as status_changes,
        CASE 
            WHEN date(timestamp) < '2018-06-02' THEN 'Before Kanban'
            ELSE 'After Kanban'
        END as period
    FROM status_changes
    GROUP BY date(timestamp), card_id
)
SELECT 
    period,
    AVG(status_changes) as avg_status_changes_per_card,
    SUM(status_changes) as total_status_changes
FROM card_metrics
GROUP BY period;





