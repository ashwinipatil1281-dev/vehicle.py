def vehicle_details(vId, vname, price, yop):
    result = (
        f"vId: {vId}\n"
        f"vname: {vname}\n"
        f"Price: {price}\n"
        f"YOP: {yop}"
    )
    return result


if __name__ == "__main__":
   
    print(vehicle_details("P102", "BMW", 100000, 2025))