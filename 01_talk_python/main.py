import uvicorn
import fastapi

app = fastapi.FastAPI()


@app.get('/')
def calculate():
    return {
        'value': 4
    }


uvicorn.run(app, host="0.0.0.0", port=8888)
