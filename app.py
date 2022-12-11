from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.exception_handler(500)
async def internal_server_error_exception_handler(request, exception):
    return JSONResponse(
        status_code=500,
        content={
            'errors': exception.errors() if hasattr(exception, 'errors') else [],
            'exception_str': str(exception)
        }
    )
