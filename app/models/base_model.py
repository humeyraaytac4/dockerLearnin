import sqlalchemy
from sqlalchemy.orm import registry

mapper_registry = registry()
Base = mapper_registry.generate_base()

target_metadata = mapper_registry.metadata