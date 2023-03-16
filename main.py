import json
import datetime
fechaActual = datetime.datetime.now()
fechaActual2 = datetime.datetime.strftime(fechaActual, '%b %d/%m/%Y %C:%M:%S %A')
print(fechaActual2)

def Divi (x,y):
  return int(x) / int(y)

def Suma (x,y):
  return int(x) + int(y)

def Resta (x,y):
  return int(x) - int(y)


def Multi (x,y):
  return int(x) * int(y)

Opers = {
  "Div":Divi,
  "Sum":Suma,
  "Res":Resta,
  "Mul":Multi,
}

data="""{
"Function":"Mul",
"Params":{"x":3,"y":3}
}"""

payload=json.loads(data)
f=payload["Function"]

callback = Opers.get (f, None)
with open("Data.log",mode="a") as f:
    res=callback(**payload["Params"])
    f.write(f"{fechaActual2} resultado: {res} argumentos: {payload}\n")