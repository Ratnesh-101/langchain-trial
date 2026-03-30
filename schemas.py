from pydantic import BaseModel

class Context(BaseModel):
    user_id: str

class ResponseFormat(BaseModel):
    summary: str
    temperature_celcius: float
    temperature_fahrenheit: float
    humidity: float