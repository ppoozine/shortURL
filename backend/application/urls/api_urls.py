from ..apis import url

def init_apis(app):
    app.include_router(url.router, tags=["Url"], prefix="/api")