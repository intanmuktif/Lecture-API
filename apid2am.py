# import package
from fastapi import FastAPI, Request, Header, HTTPException
import pandas as pd

# membuat data frame
df = pd.DataFrame()

# mengisi data
df['Username'] = ['Undertaker', 'Rey Mysterio', 'Edge']
df['Location'] = ['Texas', 'Mexico', 'Colorado']

# Password API
API_KEY = "intanmuktif2001"

# buat object
app = FastAPI()

# membuat function + url (endpoint)

# endpoint untuk retrieve data = 1 parameter url
# http://www.domain.com
# @app.get("/") #akses seluruh data
# @app.get("/surveys")

# endpoint get all data from df
@app.get("/data/{loc}")
def handlerDf(loc):
    # filter
    result = df.query(f"Location == '{loc}'")
    
    return result.to_dict(orient="records")


# Membuat function harus berdekatan
# @app.get("/")
# def handlerData(request : Request ):
#     # get req headers
#     headers = request.headers

#     return {
#         "message" : "this is fastapi data",
#         "owner" : "Intan Mukti Pebriana",
#         "headers" : headers
#     }

# ENDPOINT SECRET
# @app.get("/secret")
# def handlerSecret(password: str = Header(None)):
#     # Kondisi cek api key
#     if password != API_KEY or password == None:
#         return {
#             "error" : "Anda tidak bisa mengakses endpoint ini"
#         }

#     return{
#         "secret" : "hanya saya dan tuhan yang tahu"
    # }

# Menggunakan Exception
# @app.get("/secret")
# def handlerSecret(password: str = Header(None)):
#     # Kondisi cek api key
#     if password != API_KEY or password == None:
#         raise HTTPException(detail="Password salah!", status_code=401)

#     return{
#         "secret" : "hanya saya dan tuhan yang tahu"
#     }
