from starlette.responses import FileResponse

def main_service():
    return FileResponse('src/static/main.html')