from math import pi, log10
from scipy import constants


def calculate_cross_sectional_data(pipe_diameter):
    return (pipe_diameter ** 2) * (pi / 4)


def calculate_fluid_velocity(volumetric_flow_rate, area):
    return volumetric_flow_rate / area


def calculate_reynolds_number(pipe_diameter, kinematic_viscosity, fluid_velocity):
    return (pipe_diameter * fluid_velocity) / kinematic_viscosity


def get_reynolds_number_regime(reynolds_number):
    if reynolds_number < 2300:
        return "laminar"
    elif reynolds_number > 2600:
        return "turbulent"
    else:
        return "transitional"


def calculate_relative_roughness(average_roughness, pipe_diameter):
    return average_roughness / pipe_diameter


def calculate_friction_factor(relative_roughness, reynolds_number):
    equation_p1 = -4 * log10(
        (relative_roughness / 3.7)
        - (5.02 / reynolds_number)
        * log10((relative_roughness / 3.7) + (13 / reynolds_number))
    )
    return 1 / (equation_p1 ** 2)


def calculate_head_loss(friction_factor, pipe_length, pipe_diameter, fluid_velocity):
    return (
        2
        * friction_factor
        * (pipe_length / pipe_diameter)
        * ((fluid_velocity ** 2) / constants.g)
    )
