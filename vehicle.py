def vehicle_details(vId,vname.price,yop):
    result=(
        f"vId: {vId}\n"
        f"vname: {vname}\n"
        f"Price: {price}\n"
        f"YOP: {yop}\n"
    )
    return result

if __name__ == "__main__":
 print(vehicle_details(103 , BMW, 10000, 2025))

