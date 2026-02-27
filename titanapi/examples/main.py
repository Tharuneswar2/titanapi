from titanapi.app import TitanAPI

app = TitanAPI(
    distributed=True,
    ai=True,
)

@app.get("/")
async def root():
    return {"message": "TitanAPI running"}