#__date__ = 2022-02-01
#!/usr/bin/python3.8
'''
    cretated by Domingo Utrera 
    Refresh siigo token
    
'''
import datetime as dtm
import requests as req
import dbConnect  as con
import json 
import ast
import uuid 

today = dtm.datetime.now()
db_con = con.connect('postgres')

#cambiar esta logica para que verifoque el token que esta en la BD si esta vencido sino traerlo 
def getToken():
    cursor = db_con.cursor()
    sql_query = "select * from siigo_parameters;"
    cursor.execute(sql_query)
    parameters = cursor.fetchall()

    for param in parameters:
        values = json.dumps(param[1])
        headers = ast.literal_eval("{"+str(param[2])+"}")
        link = str(param[3])
    
    response_token = req.post(link, data=values, headers=headers)
    
    if response_token.status_code==200:
        response_ok = response_token.json()
        return response_ok
    else:
        print(response_token.status_code)
        print(response_token.text)
        return response_token.text

def existsToken():
    sql_query = f""" SELECT * FROM siigo_tokens WHERE expiration_date > '{today}';"""
    cursor = db_con.cursor()
    cursor.execute(sql_query)
    have_token = cursor.fetchone()
    
    if have_token == None:
        siigo_token = getToken()
        token_generated = str(siigo_token.get('access_token'))
        expires_in = int(siigo_token.get('expires_in'))
        token_type = str(siigo_token.get('token_type'))
        scope = str(siigo_token.get('scope'))
        start_date = today
        expiration_date = today + dtm.timedelta(seconds = expires_in)
        sql_insert = f"""
                      INSERT INTO siigo_tokens(token_generated, expires_in, token_type ,token_uuid, "scope", start_date, expiration_date) 
                      VALUES('{token_generated}', {expires_in},'{token_type}','{uuid.uuid4()}','{scope}','{start_date}', '{expiration_date}'); 
                      """
        
        try:
            cursor.execute(sql_insert)
            db_con.commit()
            sql_query = "SELECT token_generated FROM siigo_tokens WHERE id= (SELECT max(id) FROM siigo_tokens)"
            cursor.execute(sql_query)
            reusult_token = cursor.fetchone()
            exist_token = reusult_token[0]
            return exist_token
        
        except db_con.Error as error:
            print(sql_insert)
            print(error)
            db_con.rollback()
            return False
    
    elif have_token is not None:
        exist_token = have_token[1]
        return exist_token
    
if __name__=="__main__":
    token = existsToken()
    print(token)