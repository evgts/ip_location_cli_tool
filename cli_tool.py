import sys
import json
import requests


def ip_location_cli_tool():
    """
    IP Address location CLI tool
    :return: json: {'ip': 'xxx.xxx.xxx.xxx', 'latitude': x, 'longitude': y}
    eg: {'ip': '134.201.250.155', 'latitude': 34.0655517578125, 'longitude': -118.24053955078125}
    """
    # IP Address is a required argument
    # e.g.: 134.201.250.155
    if len(sys.argv) < 2:
        print("Expected command line arguments: "
              "<IP Address> <Config File Path (optional)> <Output File Path (optional)>")
        return
    else:
        ip_address = sys.argv[1]

    # Config File
    if len(sys.argv) < 3 or sys.argv[2] == "-":
        conf_file_path = "config.json"
    else:
        conf_file_path = sys.argv[2]

    with open(conf_file_path) as config_file:
        config = json.load(config_file)

    # Output File
    if len(sys.argv) < 4:
        output_file_path = config["output_file_path"]
    else:
        output_file_path = sys.argv[3]

    # IPStack https://ipstack.com/documentation API request
    response = requests.get(f"{config['protocol']}://api.ipstack.com/{ip_address}?access_key={config['api_key']}")

    j_response = response.json()
    if "latitude" in j_response and "longitude" in j_response:
        ip_location = {"ip": ip_address,
                       "latitude": j_response["latitude"],
                       "longitude": j_response["longitude"]}
    else:
        ip_location = j_response

    print(ip_location)

    with open(output_file_path, "w") as output_file:
        output_file.write(json.dumps(ip_location))


if __name__ == "__main__":
    ip_location_cli_tool()
