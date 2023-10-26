# Requirements
* Python 3
* Install requests:
```commandline
pip install requests
```
or
```commandline
pip install -r requirements.txt
```

# Configuration
Default configuration file: config.json
```json
{
  "output_file_path": "ip_location.json",
  "api_key": "<api key>",
  "protocol": "http"
}
```
* Update configuration file with valid api_key from your account.
* Change output_file_path if needed.
* If your Plan supports HTTPS Encryption, update protocol to https. This will allow secure access to the API.

# CLI Usage
```commandline
python cli_tool.py <IP Address>
```
- default config file: config.json
- default output file: ip_location.json (can be changed in config)

or
```commandline
python cli_tool.py <IP Address> <Config File Path>
```
* default output file: ip_location.json (can be changed in config)

or
```commandline
python cli_tool.py <IP Address> <Config File Path> <Output File Path>
```

or
```commandline
python cli_tool.py <IP Address> - <Output File Path>
```
* default config file used: config.json

# Docker
Update Dockerfile with correct parameters: IP Address etc.
```text
CMD [ "python", "./cli_tool.py", "<IP Address>" ]
```
Navigate to the project directory. Build Docker image:
```commandline
docker build -t ip_cli_app .
```
Run:
```commandline
docker run -it --rm ip_cli_app
```
