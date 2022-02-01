#__date__ = 2022-01-24
#!/usr/bin/python3.8
'''
    cretated by Domingo Utrera 
    Get the url to siigo_api
 
'''
import dbConnect as con

def getUrl(end_point, connect_type):
    db_con = con.connect(connect_type)
    cursor = db_con.cursor()
    sql_query = f"SELECT url FROM siigo_end_points WHERE description like '%{end_point}%'"
    cursor.execute(sql_query)
    reusult_url = cursor.fetchone()
    url = reusult_url[0]
    return url
