# Troubleshooting Slow Postgres Query

## Systematic Approach:

### 1. Analyze Query Performance
- Use `EXPLAIN ANALYZE` to view the execution plan.
- Check for missing indexes.
- Look for sequential scans.
- Analyze join conditions.

### 2. Check Database Statistics
- Review table size and row counts.
- Analyze index usage statistics.
- Check buffer cache hit ratio.
- Investigate lock waiting and deadlocks.

### 3. Review Query Optimization
- Rewrite subqueries if necessary.
- Optimize `JOIN` conditions.
- Consider using materialized views.
- Ensure a proper indexing strategy.

### 4. System-Level Checks
- Monitor I/O performance.
- Check memory usage.
- Verify connection pooling.
- Review PostgreSQL configuration.
