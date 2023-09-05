from datetime import datetime


def insert_order(connection, order):
    cursor = connection.cursor()
    order_query = "INSERT INTO orders (customer_name, total, datetime) VALUES (%s,%s,%s)"
    order_data = (order['customer_name'], order['total'], datetime.now())

    cursor.execute(order_query, order_data)
    order_id = cursor.lastrowid

    connection.commit()
    return order_id

if __name__=='__main__':
    from sql_connection import get_sql_connection
    connection = get_sql_connection()
    print(insert_order(connection, {
        'customer_name': 'Lora',
        'total': '455',
        'datetime': datetime.now(),
        'order_details':[
            {
                'product_id': '1',
                'quantity': '3',
                'total_price': '300'
            },
            {
                'product_id': '2',
                'quantity': '2',
                'total_price': '800'
            }
        ]

    }))