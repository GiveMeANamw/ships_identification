import pymysql
import data_operations as db

def search_info(cur, query):
    try:
        cur.execute(query)
        results = cur.fetchall()
        if results:  # 检查结果是否为空
            res = str(results[0][0])
        else:
            res = ""  # 如果结果为空，返回相应的消息
    except pymysql.Error as err:
        print(f"Error executing query: {err}")
        res = "Error executing query"  # 处理其他异常情况
    return res


if __name__=="__main__":
    conn=db.connect_to_database()
    cur=db.create_cursor(conn)
    Login_User='admi'
    query_pw = f"SELECT password FROM user_info WHERE user_name='{Login_User}'"
    query_un = f"SELECT user_name FROM user_info WHERE user_name='{Login_User}'"
    res1=search_info(cur,query_pw)
    res2=search_info(cur,query_un)
    print(res1)
    print(res2)