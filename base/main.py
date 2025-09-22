from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get('/')
def index():
    return {
        'message': 'Home page'
    }


if __name__ == '__main__':
    uvicorn.run('base.main:app', reload=True)
