'''FastApi learning'''
from typing import Optional
import uvicorn
import fastapi

app = fastapi.FastAPI()


@app.get('/')
def calculate(x: int, y: int, z: Optional[int] = None):
    if z == 0:
        return fastapi.Response(content="{'error': 'Error: z can not be 0'}",
                                media_type='application/json',
                                status_code=400)

    value = x + y

    if z:
        value = (x + y) / z

    return {
        'value': value
    }


uvicorn.run(app, host="0.0.0.0", port=8888)
