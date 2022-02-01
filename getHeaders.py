#__date__ = 2022-02-01
#!/usr/bin/python3.8
'''
    cretated by Domingo Utrera 
    Headers for siigo_api 
'''
import refreshToken as rftk

def getHeaders():
    token = rftk.getToken()
    headers = {'Content-Type': 'application/json','Authorization':token['access_token']}
    return headers

if __name__== "__main__":
    headers = getHeaders()
    print(headers)