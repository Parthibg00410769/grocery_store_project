def get_uoms(connection):
    cursor = connection.cursor()
    query = "SELECT * from uom"
    cursor.execute(query)

    response = []
    for (uom_id, uom_name) in cursor:
        response.append({
            'uom_id': uom_id,
            'uom_name': uom_name
        })
    return response
def insert_new_uom(connection, new_uom):
    cursor = connection.cursor()
    query  = "INSERT INTO uom (uom_id, uom_name) VALUES (%s, %s)"
    data = (new_uom['uom_id'], new_uom['uom_name'])
    cursor.execute(query, data)
    connection.commit()

    return cursor.lastrowid



if __name__=='__main__':
    from sql_connection import get_sql_connection
    connection = get_sql_connection()
    print(get_uoms(connection))
    print(insert_new_uom(connection, {
        'uom_id': '6',
        'uom_name': 'box'
    }))