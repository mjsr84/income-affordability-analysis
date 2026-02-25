import psycopg

conn = psycopg.connect(
    host="localhost",
    port=5433,
    dbname="analysis_lab",
    user="postgres",
    password="Jenkins84"
)

cur = conn.cursor()
cur.execute("SELECT version();")

print(cur.fetchone())

cur.close()
conn.close()