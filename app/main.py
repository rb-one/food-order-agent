from fastapi import FastAPI
from app.routes.auth import router as auth_router

app = FastAPI()

# Include routers
app.include_router(auth_router, prefix="/auth", tags=["Authentication"])


@app.get("/")
def read_root():
    return {"message": "Welcome to the Food Ordering API!"}
