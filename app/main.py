from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  # ✅ ADD THIS

from app.db.database import engine
from app.db.base import Base

from app.routes.auth import router as auth_router
from app.routes.projects import router as project_router
from app.routes.tasks import router as task_router
from app.routes.dashboard import router as dashboard_router
import os

PORT = int(os.getenv("PORT", 8000))

app = FastAPI()

# ✅ ADD CORS HERE (IMPORTANT POSITION)
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# create tables
Base.metadata.create_all(bind=engine)

# include routers
app.include_router(auth_router)
app.include_router(project_router)
app.include_router(task_router)
app.include_router(dashboard_router)


@app.get("/")
def home():
    return {"message": "Backend running successfully"}