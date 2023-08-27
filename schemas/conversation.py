from typing import Optional
from pydantic import BaseModel, Field

class WppConversation(BaseModel):
    celphone: str = Field(min_length=10, max_length=13)
    message: str = Field(min_length=1, max_length=500)
    history: Optional[list] = Field(default=None)

    class Config:
        schema_extra = {
            "example": {
                "celphone": "3127423350",
                "message": "¿Cómo podemos utilizar nuestros datos de redes sociales para identificar nuevas oportunidades de mercado?",
                "history": [
                    {"role": "user", "content": "Hola"}, 
                    {"role": "assistant", "content": "Hola, como te puedo ayudar?"},
                    {"role": "user", "content":"¿Cómo podemos utilizar nuestros datos de redes sociales para identificar nuevas oportunidades de mercado?"}
                    ]
            }
        }