from math import pi, log10
from models.constants import GRAVITY
from models.user import UserModel
from db import db
import sqlite3

average_roughness = {
    'steel': {
        'sheet_metal_new': {
            'ft': 1.6E-4,
            'm': 5.0E-2
        },
        'stainless_new': {
            'ft': 7.0E-6,
            'm': 2.0E-3
        },
        'commercial_new': {
            'ft': 1.50E-4,
            'm': 4.60E-2
        },
        'riveted': {
            'ft': 1.0E-2,
            'm': 3.0
        },
        'rusted': {
            'ft': 7.0E-3,
            'm': 2.0
        }
    },
    'iron': {
        'cast_new': {
            'ft': 8.50E-4,
            'm': 2.60E-1
        },
        'wrought_new': {
            'ft': 1.50E-4,
            'm': 4.60E-2
        },
        'galvanized_new': {
            'ft': 5.0E-4,
            'm': 1.50E-1
        },
        'asphalted_cast': {
            'ft': 4.00E-4,
            'm': 1.20E-1
        }

    },
    'brass': {
        'drawn_new': {
            'ft': 7.0E-6,
            'm': 2.0E-3
        }
    },
    'plastic': {
        'drawn_tubing': {
            'ft': 5.0E-6,
            'm': 1.50E-3
        }
    },
    'glass': {
        'ft': 0,
        'm': 0
    },
    'concrete': {
        'smoothed': {
            'ft': 1.30E-4,
            'm': 4.0E-2
        },
        'rough': {
            'ft': 7.00E-3,
            'm': 2.0
        }
    },
    'rubber': {
        'smoothed': {
            'ft': 3.30E-5,
            'm': 1.0E-2
        }
    },
    'wood': {
        'stave': {
            'ft': 1.60E-3,
            'm': 5.0E-1
        }
    }
}


class HeadLossModel(db.Model):
    __tablename__ = "head_losses"

    id = db.Column(db.Integer, primary_key=True)
    density = db.Column(db.Float)
    kinematic_viscosity = db.Column(db.Float)
    pipe_diameter = db.Column(db.Float)
    volumetric_flow_rate = db.Column(db.Float)
    pipe_material = db.Column(db.String)
    material_condition = db.Column(db.String)
    pipe_length = db.Column(db.Float)

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    user = db.relationship("UserModel")

    def __init__(
            self,
            fluid_density,
            kinematic_viscosity,
            pipe_diameter,
            pipe_material,
            material_condition,
            volumetric_flow_rate,
            pipe_length,
            user_id,
    ):
        self.fluid_density = fluid_density
        self.kinematic_viscosity = kinematic_viscosity
        self.pipe_diameter = pipe_diameter
        self.volumetric_flow_rate = volumetric_flow_rate
        self.average_roughness = average_roughness[pipe_material][material_condition][
            'm'] if pipe_material != 'glass' else average_roughness[pipe_material]['m']
        self.pipe_length = pipe_length
        self.user_id = user_id

    @classmethod
    def calculate_cross_sectional_area(cls, pipe_diameter):
        return (pi * (pipe_diameter ** 2)) / 4

    @classmethod
    def calculate_fluid_velocity(cls, volumetric_flow_rate, area):
        return volumetric_flow_rate / area

    @classmethod
    def calculate_reynolds_number(
            cls, pipe_diameter, kinematic_viscosity, fluid_velocity
    ):
        return (pipe_diameter * fluid_velocity) / kinematic_viscosity

    @classmethod
    def reynolds_number_regime(cls, reynolds_number):
        if reynolds_number < 2300:
            return "laminar"
        elif reynolds_number > 2600:
            return "turbulent"
        else:
            return "transitional"

    @classmethod
    def calculate_relative_roughness(cls, average_roughness, pipe_diameter):
        return average_roughness / pipe_diameter

    @classmethod
    def calculate_friction_factor(cls, relative_roughness, reynolds_number):
        aux = -4 * log10((relative_roughness / 3.7) - (5.02 / reynolds_number) * log10(
            (relative_roughness / 3.7) + (13 / reynolds_number)))
        return 1 / (aux ** 2)

    @classmethod
    def calculate_head_loss(cls, friction_factor, pipe_length, pipe_diameter, fluid_velocity):
        return 2 * friction_factor * (pipe_length / pipe_diameter) * ((fluid_velocity ** 2) / GRAVITY)

    @classmethod
    def json(
            cls,
            cross_sectional_area,
            fluid_velocity,
            reynolds_number,
            reynolds_number_regime,
            relative_roughness,
            friction_factor,
            head_loss,
    ):
        """
        Recebe os parametros e retorna o mesmo em formato JSON.
        """
        return {
            "cross_sectional_area": cross_sectional_area,
            "fluid_velocity": fluid_velocity,
            "reynolds_number": reynolds_number,
            "reynolds_number_regime": reynolds_number_regime,
            "relative_roughness": relative_roughness,
            "friction_factor": friction_factor,
            "head_loss": head_loss,
        }

    def calculate_all(self):
        """
        Returns all calculated values on JSON format.
        """
        area = self.calculate_cross_sectional_area(self.pipe_diameter)

        velocity = self.calculate_fluid_velocity(self.volumetric_flow_rate, area)

        reynolds_number = self.calculate_reynolds_number(
            self.pipe_diameter, self.kinematic_viscosity, velocity
        )

        reynolds_number_regime = self.reynolds_number_regime(reynolds_number)

        relative_roughness = self.calculate_relative_roughness(
            self.average_roughness, self.pipe_diameter
        )

        friction_factor = self.calculate_friction_factor(
            relative_roughness, reynolds_number
        )

        head_loss = self.calculate_head_loss(
            friction_factor, self.pipe_length, self.pipe_diameter, velocity
        )

        return self.json(
            area,
            velocity,
            reynolds_number,
            reynolds_number_regime,
            relative_roughness,
            friction_factor,
            head_loss,
        )

    @classmethod
    def search_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
