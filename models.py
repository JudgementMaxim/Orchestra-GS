from pydantic import BaseModel
from enum import Enum
from typing import Literal, Union
from pydantic import Field

class ProviderType(str, Enum):
    container = "container"
    process = "process"

class Resources(BaseModel):
    memory: str
    cpu: str

class BaseSettings(BaseModel):
    args: list[str] = []
    env: dict[str, str] = {}
    ports: list[str] = []

class ProcessorSettings(BaseSettings):
    type: Literal["process"]
    executable: str

class ContainerSettings(BaseSettings):
    type: Literal["container"]
    image: str

class ServerConfig(BaseModel):
    id: str
    type: ProviderType
    enabled: bool
    resources: Resources
    settings: Union[ProcessorSettings, ContainerSettings] = Field(discriminator="type")