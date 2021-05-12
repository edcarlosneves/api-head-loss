from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.head_loss import HeadLossModel
from schemas.head_loss import HeadLossSchema
from libs.strings import gettext

head_loss_schema = HeadLossSchema()


class HeadLoss(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument(
        "density", type=float, required=True, help="density is not defined."
    )

    parser.add_argument(
        "kinematic_viscosity",
        type=float,
        required=True,
        help="kinematic_viscosity is not defined.",
    )

    parser.add_argument(
        "pipe_diameter", type=float, required=True, help="pipe_diameter is not defined."
    )

    parser.add_argument(
        "volumetric_flow_rate",
        type=float,
        required=True,
        help="volumetric_flow_rate is not defined.",
    )

    # parser.add_argument(
    #     "average_roughness",
    #     type=float,
    #     required=True,
    #     help="average_roughness is not defined.",
    # )

    parser.add_argument(
        "pipe_material",
        type=str,
        required=True,
        help="pipe_material is not defined.",
    )

    parser.add_argument(
        "material_condition",
        type=str,
        required=True,
        help="material_condition is not defined.",
    )

    parser.add_argument(
        "pipe_length", type=float, required=True, help="pipe_length is not defined."
    )

    parser.add_argument(
        "user_id", type=int, required=True, help="user_id is not defined."
    )

    @jwt_required()
    def post(self):
        data = HeadLoss.parser.parse_args()

        density = data["density"]
        kinematic_viscosity = data["kinematic_viscosity"]
        pipe_diameter = data["pipe_diameter"]
        volumetric_flow_rate = data["volumetric_flow_rate"]
        pipe_material = data["pipe_material"]
        material_condition = data["material_condition"]
        pipe_length = data["pipe_length"]
        user_id = data["user_id"]

        head_loss = HeadLossModel(
            density,
            kinematic_viscosity,
            pipe_diameter,
            pipe_material,
            material_condition,
            volumetric_flow_rate,
            pipe_length,
            user_id,
        )
        head_loss.save_to_db()

        return head_loss.calculate_all()


class GetHeadLoss(Resource):
    @jwt_required()
    def get(self, analysis_id):
        head_loss = HeadLossModel.search_by_id(analysis_id)
        if head_loss:
            return head_loss_schema.dump(head_loss)
        return {"message": gettext("analysis_not_found")}

        # return perdacarga.json()
