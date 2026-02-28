from titanapi import TitanAPI

titan = TitanAPI()
app = titan.fastapi

@titan.task
async def send_email(user_id: str):
    print(f"Sending email to {user_id}")

@app.get("/trigger")
async def trigger():
    await send_email.delay(user_id="abc")
    return {"status": "queued"}