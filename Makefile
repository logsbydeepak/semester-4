format-py:
	uv format

format-sql:
	find . -name "*.sql" | xargs bunx sql-formatter --fix --language mysql
