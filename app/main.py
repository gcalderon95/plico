from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.registro import router as registro_router
from app.routes.login import router as login_router
from app.routes.medicion import router as mediciones_router


app = FastAPI()

app.include_router(registro_router, prefix="", tags=["auth"])
app.include_router(login_router, prefix="", tags=["auth"])
app.include_router(mediciones_router, prefix="", tags=["mediciones"])

# Middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"msg": "Backend funcionando correctamente"}
