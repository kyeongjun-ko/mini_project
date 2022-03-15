import pymysql


def open_close():

    free = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='bit123', db='free', charset='utf8')

    cursor = free.cursor(pymysql.cursors.DictCursor)

    cursor.execute("""SELECT store_name FROM gupsik_hours
    WHERE weekday LIKE concat('%', dayofweek(now()), '%') AND open_hour < now() AND close_hour > now() """)

    result = cursor.fetchall()
    # print(result, type(result))
    opens = []
    for i in range(len(result)):
        opens.append(result[i]['store_name'])

    return opens


# print(open_close())