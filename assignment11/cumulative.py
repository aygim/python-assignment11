import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

conn = sqlite3.connect('./db/lesson.db')

query = """
SELECT o.order_id, SUM(p.price * l.quantity) AS total_price FROM orders o
JOIN line_items l ON o.order_id = l.order_id
JOIN products p ON l.product_id = p.product_id
GROUP BY o.order_id
ORDER BY o.order_id;
"""

df = pd.read_sql_query(query, conn)
conn.close()

print(df.head())

df['cumulative'] = df['total_price'].cumsum()

df.plot(x='order_id', y='cumulative', marker='o', linestyle='-', color='green')
plt.title('Cumulative Revenue over orders')
plt.xlabel('Order_id')
plt.ylabel('Cumulative')
plt.grid(True)


plt.show()

# 