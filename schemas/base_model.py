from datetime import datetime
from types import UnionType
from typing import (
    Any,
    Callable,
    Dict,
    Optional,
    Self,
    Type,
    Union,
    get_args,
    get_origin,
)

from pydantic import BaseModel, ConfigDict, field_serializer, model_serializer


def is_optional_datetime(annotation: Any) -> bool:
    if annotation == datetime:
        return True
    if get_origin(annotation) is UnionType:
        args = get_args(annotation)
        return len(args) == 2 and datetime in args and type(None) in args
    return False


class DiscoveryBaseModel(BaseModel):
    @model_serializer(mode="wrap")
    def serialize(
        self, original_serializer: Callable[[Self], dict[str, Any]]
    ) -> dict[str, Any]:
        if hasattr(self, "model_fields"):
            for field_name, field_info in self.model_fields.items():
                if is_optional_datetime(field_info.annotation):
                    value = getattr(self, field_name)
                    if value is not None:
                        setattr(self, field_name, self.datetime_serializer(value))

        result = original_serializer(self)

        return result

    def datetime_serializer(self, dt: datetime):
        try:
            return int(dt.timestamp() * 1e3)
        except Exception as e:
            print(f"Error serializing datetime: {e}")
            return dt

    class Config:
        from_attributes = True

        @staticmethod
        def json_schema_extra(schema: Dict[str, Any], model: Type) -> None:
            if "properties" in schema:
                for key in schema["properties"].keys():
                    prop = schema["properties"][key]
                    if "format" in prop and prop["format"] == "date-time":
                        schema["properties"][key] = {"type": "integer"}
