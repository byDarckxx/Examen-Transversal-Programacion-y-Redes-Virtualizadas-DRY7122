import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "cLDFJwQy8ZK8oZ75dld5AH2ukSiLs2O5"

while True:
    orig = input("Ciudad de Origen: ")
    if orig == "quit" or orig == "q" or orig == "Q" :
        break
    dest = input("Ciudad de Destino: ")
    if dest == "quit" or dest == "q" or dest == "Q":
        break
    url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})
    print("URL: " + (url))
    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]
    if json_status == 0:
        print("API Status: " + str(json_status) + " = A successful route call.\n")
        print("=============================================")
        print("Direcciones desde " + (orig) + " hacia " + (dest))
        print("Duración del viaje (HH:MM:SS):  " + (json_data["route"]["formattedTime"]))
        print("Distancia (Kilómetros):         " + str("{:.3f}".format((json_data["route"]["distance"])*1.61)))
    #       print("Combustible Usado (Ltr):        " + str((json_data["route"]["fuelUsed"])*3.78))
        print("=============================================")
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)"))
        print("=============================================\n")
    elif json_status == 402:
        print("**********************************************")
        print("Status Code: " + str(json_status) + "; Ingreso de datos erroneo para una o ambas locaciones.")
        print("**********************************************\n")
    elif json_status == 611:
        print("**********************************************")
        print("Status Code: " + str(json_status) + "; Datos faltantes para una o ambas locaciones.")
        print("**********************************************\n")
    else:
        print("************************************************************************")
        print("For Staus Code: " + str(json_status) + "; Refer to:")
        print("https://developer.mapquest.com/documentation/directions-api/status-codes")
        print("************************************************************************\n")
    