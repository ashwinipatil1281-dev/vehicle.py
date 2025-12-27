from vehicle import vehicle_details
def test_vehicle_details():
    expected_output=(
        "vId: 103\n"
        "vname: BMW\n"
        "Price: 10000\n"
        "YOP: 2025\n"
    )
    assert (vehicle_details("P102","BMW",10000,2025))