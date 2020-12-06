from ma import ma
from models.head_loss import HeadLossModel


class HeadLossSchema(ma.SQLAlchemySchema):
    class Meta:
        model = HeadLossModel
