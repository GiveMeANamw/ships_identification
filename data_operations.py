import pymysql

# 连接到 MySQL 数据库
def connect_to_database():
    try:
        conn = pymysql.connect(
            host='localhost',  # 数据库服务器地址
            user='root',  # 数据库用户名
            password='yay200202',  # 数据库密码
            database='ships_vision',  # 数据库名
            charset='utf8mb4'  # 字符集（兼容更多的文字）
        )
        print("Connect successfully")
        return conn
    except pymysql.Error as err:
        print(f"Error: {err}")
        return None

# 创建游标对象
def create_cursor(conn):
    try:
        cursor = conn.cursor()
        return cursor
    except pymysql.Error as err:
        print(f"Error creating cursor: {err}")
        return None

# 执行 SQL 查询
def execute_query(cursor, query):
    try:
        cursor.execute(query)
        results = cursor.fetchall()
        for row in results:
            print(row)  # 打印每一行数据
    except pymysql.Error as err:
        print(f"Error executing query: {err}")

# 插入数据
def insert_data(cursor, query, values):
    try:
        cursor.execute(query, values)
        cursor.connection.commit()
        print("Insert successful!")
        return True
    except pymysql.Error as err:
        cursor.connection.rollback()
        print(f"Error inserting data: {err}")
    return False

# 关闭游标和连接
def close_connection(cursor, conn):
    cursor.close()
    conn.close()
    print("close successfully")

if __name__ == "__main__":
    connection = connect_to_database()
    if connection:
        print("Connected Successfully")
        query = "SELECT * FROM ships_vision"
        cursor = create_cursor(connection)
        print("executing query")
        execute_query(cursor, query)

        # 插入数据示例
        # insert_query = "INSERT INTO ships_vision (ImgFileName, ships_name) VALUES (%s, %s)"
        #
        # data_to_insert = ("value1", "value2")
        query = f"INSERT INTO ships_vision (ImgFileName, ships_name, center_x, center_y, bound_width, bound_height, ResultImgFilePath,ResultTXTFilePath VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        data_to_insert = ('p1', 'names[int(cls)]',float(2))

        insert_data(cursor, query, data_to_insert)

        close_connection(cursor, connection)
    else:
        print("Failed to connect to the database.")
