from fastapi import FastAPI
import requests as req
import getHeaders as hder
from getUrl import getUrl
app = FastAPI()

#get list of all products
@app.get("/products/{code}")
async def get_products_by_code(code):
    headers = hder.getHeaders()
    url = getUrl("get_products_list", "postgres")
    respuesta = req.get(f'{url}{code}', headers=headers)
    response_body = respuesta.json()
    return response_body

#get one product by id
@app.get("/products/{product_id}")
async def get_product_id(product_id):
    headers = {
            'Content-Type': 'application/json',
            'Authorization': 'eyJhbGciOiJSUzI1NiIsImtpZCI6IkFFNjY0RkJCMkY4OUMwQjhEOTgxMTYwQTVBMEVEMjhCNjk3MDkzQUNSUzI1NiIsInR5cCI6ImF0K2p3dCIsIng1dCI6InJtWlB1eS1Kd0xqWmdSWUtXZzdTaTJsd2s2dyJ9.eyJuYmYiOjE2NDM2Mzg5NTIsImV4cCI6MTY0MzcyNTM1MiwiaXNzIjoiaHR0cDovL21zLXNlY3VyaXR5c2VydmljZTo1MDAwIiwiYXVkIjoiaHR0cDovL21zLXNlY3VyaXR5c2VydmljZTo1MDAwL3Jlc291cmNlcyIsImNsaWVudF9pZCI6IlNpaWdvQVBJIiwic3ViIjoiNTM3MDM2IiwiYXV0aF90aW1lIjoxNjQzNjM4OTUyLCJpZHAiOiJsb2NhbCIsIm5hbWUiOiJpbmZvQGluZ2VuaW9za29rb3JvLmNvbSIsIm1haWxfc2lpZ28iOiJpbmZvQGluZ2VuaW9za29rb3JvLmNvbSIsImNsb3VkX3RlbmFudF9jb21wYW55X2tleSI6IktPS09STyIsInVzZXJzX2lkIjoiMzE3ODYiLCJ0ZW5hbnRfaWQiOiIweDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMTg0MzM0IiwidXNlcl9saWNlbnNlX3R5cGUiOiIwIiwicGxhbl90eXBlIjoiMTQiLCJ0ZW5hbnRfc3RhdGUiOiIxIiwibXVsdGl0ZW5hbnRfaWQiOiI5MSIsImNvbXBhbmllcyI6IjAiLCJhcGlfc3Vic2NyaXB0aW9uX2tleSI6IjI5MWVlZThmZGZiYjQ2ZTM4NjgxMTE3MTgyMGM2ZDM4IiwiYWNjb3VudGFudCI6ImZhbHNlIiwianRpIjoiQzk5OURGRDc4REQzQUI0NkFEQzgyRUQ0M0FEM0QzOEUiLCJpYXQiOjE2NDM2Mzg5NTIsInNjb3BlIjpbIlNpaWdvQVBJIl0sImFtciI6WyJjdXN0b20iXX0.lc3_9ZBsm8_aUTHbjsCZbETa1Rwi8fB5zygOpIFCmBZA1nSxr-iumqGQozdWG2mGP6hMvMjfMF7zI1SK_bDsdrrSzGFLoW-qSVuJy5U6KRlJnmqUlARjlv5dx7nrT-UqW-6VYuTKQC9YjpkiOQZD3bSFzpId5MyVNWEK_OL1XYBxwdf8Oh54TT9luB9xX1aA2aSlpfMv-bDqaT--UppfBg49_-GXwlkv_eEYwYrJO7ev6d0X-hL61Taf1C7r2dhBbjlmt8Zyj12V9SGqklNG_uk6FgNSb5KQ0HBKdcGFACCSuHXaE52dYj9WcxFkpxPPNpdOL6feUweR_Lhu9gdPLw'
            }
    respuesta = req.get(f'https://api.siigo.com/v1/products/{product_id}', headers=headers)
    response_body = respuesta.json()
    return response_body

