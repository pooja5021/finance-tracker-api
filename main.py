from fastapi import FastAPI
from database import Base, engine
from routers import users, transactions, analytics

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Finance Tracker API")

app.include_router(users.router)
app.include_router(transactions.router)
app.include_router(analytics.router)

@app.get("/")
def root():
    return {"message": "API is running "}