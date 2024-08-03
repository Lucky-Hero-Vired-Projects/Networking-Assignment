# sub-domain-check.py, Explaination


## Features
1. Checks the status (Up/Down) of subdomains in json file.
2. Monitors the JSON file for updates and reloads the subdomains when the file is modified.
3. Displays the status of subdomains in the tabular format.
4. Script will runs continuously, updating the status every minute.

## Requirements
1. Python 3.x
2. requests 
3. tabulate
4. json
5. time

Install all required packages using pip
 ```
   pip3 install <package-name>
```

## Create the JSON File

Creating a file named as subdomains.json in the same directory as the script exits.
```
   {
    "subdomains": [
      "http://google.com",
      "http://sub1.example.com",
      "http://sub2.example.com",
      "https://www.cricbuzz.com",
      "http://awssomeweb.com",
      "https://vlearnv.herovired.com",
      "https://www.amazon.in"
    ]
  }
```
## Flow chart steps of python script
1. Import all required packages
2. Creating a class

    a. declare self, json file, ....

    b. Loading the subdomains.json file

    c. check for updates in json file

    d. status checking using request package

    e. displaying the status o/p

    d. infinite loop function to check status

3. calling class with required file

### Run the Script (sub-domain-check.py)

Execute the script using the following command:
```
   python3 subdomain_status_checker.py
   ```

The O/P will display in tabular format and update status in every 60 seconds. If the subdomains.json file is modified, the script will automatically reload the subdomains and check their status again.

#### Output of script
```
Networking-Assignment git:(main) ✗ python3 sub-domain-check.py
+-------------------------------+--------+
|           Subdomain           | Status |
+-------------------------------+--------+
|       http://google.com       |  Down  |
|    http://sub1.example.com    |  Down  |
|    http://sub2.example.com    |  Down  |
|   https://www.cricbuzz.com    |   Up   |
|     http://awssomeweb.com     |  Down  |
| https://vlearnv.herovired.com |   Up   |
|    https://www.amazon.in/     |  Down  |
+-------------------------------+--------+
Subdomains list updated.
+-------------------------------+--------+
|           Subdomain           | Status |
+-------------------------------+--------+
|       http://google.com       |  Down  |
|    http://sub1.example.com    |  Down  |
|    http://sub2.example.com    |  Down  |
|   https://www.cricbuzz.com    |   Up   |
|     http://awssomeweb.com     |  Down  |
| https://vlearnv.herovired.com |   Up   |
|     https://www.amazon.in     |  Down  |
+-------------------------------+--------+
```

## Note
1. Ensure that the subdomains in the JSON file are valid URLs.
2. The script uses a HEAD request to check the status of each subdomain. If the subdomain responds with a status code other than 200, it is marked as "Down".
3. The script checks for updates to the subdomains.json file every minute. If the file is modified, the subdomains are reloaded and the status is checked again.