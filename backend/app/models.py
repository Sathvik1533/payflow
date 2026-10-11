import uuid
from datetime import datetime

from sqlalchemy import DateTime,String,func
from sqlalchemy.dialects.postgresql import JSONB,UUID
from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column

class Base(DeclarativeBase):
    pass

class PaymentEvent(Base):
    __tablename__="payment_events"

    id:Mapped[uuid.UUID]=mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        )
    provider_event_id:Mapped[str | None]=mapped_column(
            String(255),
            nullable=True,
        )
    event_type:Mapped[str]=mapped_column(
            String(100),
            nullable=False,
        )
    payload:Mapped[dict]=mapped_column(
            JSONB,
            nullable=False,
        )
    received_at:Mapped[datetime]=mapped_column(
            DateTime(timezone=True),
            server_default=func.now(),
            nullable=False,
        )
    