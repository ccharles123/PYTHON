import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/")
def get_list():
    return [1, 2, 3]

#con el siguiente comando puedes devolver una pagina web
@app.get("/contact", response_class=HTMLResponse)
def get_list():
    return """
    <h1>¡Hola! Soy una pagina</h1>
    <p>Soy un parrafo</p>
    """

#vamos a correr nuestra funcion getCategory de nuestro module store
def run():
    store.getCategories()


if __name__ == "__main__":
    run()