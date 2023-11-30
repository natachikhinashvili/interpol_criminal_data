from pydantic import BaseModel


class Criminal(BaseModel):
    date_of_birth:str
    nationalities:str
    entity_id:str
    forename:str
    name:str
    image:str
    