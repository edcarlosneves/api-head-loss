from math import pi, log10
from scipy import constants


def get_reynolds_number_regime(reynolds_number):
    if reynolds_number < 2300:
        return "laminar"
    elif reynolds_number > 2600:
        return "turbulent"
    else:
        return "transitional"


def calculate_cross_sectional_area(pipe_diameter):
    return (pipe_diameter ** 2) * (pi / 4)


def calculate_fluid_velocity(pipe_diameter, volumetric_flow_rate):
    area = calculate_cross_sectional_area(pipe_diameter)
    return volumetric_flow_rate / area


def calculate_reynolds_number(pipe_diameter, kinematic_viscosity, volumetric_flow_rate):
    flud_velocity = calculate_fluid_velocity(pipe_diameter, volumetric_flow_rate)
    return (pipe_diameter * flud_velocity) / kinematic_viscosity


def calculate_average_roughness(pipe_material, material_condition):
    return AVERAGE_ROUGHNESS_DATA[pipe_material][material_condition]["m"]


def calculate_relative_roughness(pipe_diameter, pipe_material, material_condition):
    average_roughness = calculate_average_roughness(pipe_material, material_condition)
    return average_roughness / pipe_diameter


def calculate_friction_factor(
    pipe_diameter,
    kinematic_viscosity,
    volumetric_flow_rate,
    pipe_material,
    material_condition,
):
    relative_roughness = calculate_relative_roughness(
        pipe_diameter, pipe_material, material_condition
    )
    reynolds_number = calculate_reynolds_number(
        pipe_diameter, kinematic_viscosity, volumetric_flow_rate
    )
    equation_p1 = -4 * log10(
        (relative_roughness / 3.7)
        - (5.02 / reynolds_number)
        * log10((relative_roughness / 3.7) + (13 / reynolds_number))
    )
    return 1 / (equation_p1 ** 2)


def calculate_head_loss(
    pipe_length,
    pipe_diameter,
    kinematic_viscosity,
    volumetric_flow_rate,
    pipe_material,
    material_condition,
):
    fluid_velocity = calculate_fluid_velocity(pipe_diameter, volumetric_flow_rate)
    friction_factor = calculate_friction_factor(
        pipe_diameter,
        kinematic_viscosity,
        volumetric_flow_rate,
        pipe_material,
        material_condition,
    )
    return (
        2
        * friction_factor
        * (pipe_length / pipe_diameter)
        * ((fluid_velocity ** 2) / constants.g)
    )
