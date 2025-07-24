import datetime as dt
import json
from typing import Any, Callable, Optional

from sqlalchemy import JSON, DateTime, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class DateTimeJSON(JSON):
    """
    Modify behavior for serialization of datetime type
    """

    def bind_processor(self, dialect) -> Optional[Callable[[Any], Any]]:
        super().bind_processor(dialect)

        def process(value: Any) -> Any:
            if value is None:
                return None
            return json.dumps(value, default=_converter)

        return process


def _converter(value: Any) -> str | None:
    if isinstance(value, dt.datetime):
        return value.__str__()
    if isinstance(value, dt.date):
        return value.__str__()
    return None


class Base(DeclarativeBase):
    type_annotation_map = {dict[str, Any]: DateTimeJSON}


class LifeTimeMixin:
    created_at: Mapped[dt.datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
    )
    updated_at: Mapped[dt.datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
        onupdate=dt.datetime.now,
    )
