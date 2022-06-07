from fastapi import FastAPI
from pydantic import BaseModel


class Usuario(BaseModel):
    id: int
    name: str
    age: int
    city: str


infoList = [
    Usuario(id=1, user="renans", name="Renan", age=22, city="Taubaté"),
    Usuario(id=2, user="paulin", name="Paulo", age=27, city="São José"),

]

# fast api diretorio
app = FastAPI()



@app.get('/user/')
def allUsers():
    return infoList

@app.get('/user/{id_usuario}')
def infoId(id_usuario: int):
    for Usuario in infoList:
        if Usuario.id == id_usuario:
            return Usuario


@app.post('/user/add')
def addInfo(user: Usuario):
    infoList.append(user)
    return infoList

@app.delete('/user/delete/{id_usuario}')
def deleteUser(id_usuario: int):
    for Usuario in infoList:
        if Usuario.id == id_usuario:
            infoList.remove(Usuario)
            return {"Message": "Delete successful"}

