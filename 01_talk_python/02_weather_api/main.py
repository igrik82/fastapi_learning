'''Weather app'''
import uvicorn
import fastapi


app = fastapi.FastAPI()


@app.get('/')
def index():
    return {
        'index': 'Hello from weather app!'
    }


if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8888)
