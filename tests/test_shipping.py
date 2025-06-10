from main import calculate_shipping_cost
from src.shipping_costs import get_distance


def test_default_shipping_type():
    # Arbitrary but valid coordinates
    from_coords = (0, 0)
    to_coords = (1, 1)

    result = calculate_shipping_cost(from_coords, to_coords)

    assert isinstance(result, str), "The result is not a text string."
    assert result.startswith("$"), "The result does not start with '$'."

    # Convert to number to see if it is within the expected range wtf
    try:
        price_float = float(result.replace("$", ""))
    except ValueError:
        assert False, f"No se pudo convertir '{result}' a número."

    assert 350 < price_float < 370, f"El precio {price_float} está fuera del rango esperado."


def test_distance_cdmx_to_nyc():
    cdmx = (19.4326, -99.1332)
    nyc = (40.7128, -74.0060)
    distance = get_distance(*cdmx, *nyc)

    assert isinstance(distance, float)
    assert 3300 < distance < 3400
