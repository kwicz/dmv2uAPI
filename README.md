# _dmv2u API_

#### By _**K. Wicz**_


## Description

_A Python/Flask program that serves up data from the DMV2U database._


## Setup/Installation Requirements

### 1.  Install Python
* Go to the [Python website](https://www.python.org/downloads/) and click the button that says `Download version 3.X.X`.
* Run the Python installer.
* Confirm Python successfully installed by opening your terminal and running:
```sh
python --version
pip --version
```
* If the output for these commands includes a version number, Python is installed and available from the command line.

### 2. Install Flask
* Navigate to your command line and run
```sh
pip install flask
```
* You should see some output ending in a notification that Flask has been installed successfully.

### 3. Clone this repository

Enter the following commands in Terminal (macOS) or PowerShell (Windows):
```sh
cd desktop
git clone https://github.com/kwicz/dmv2uAPI
cd dmv2uAPI
```

### 4. Launch the project in your browser
In your terminal, type:
```sh
python app.py 
```
Hold ```command``` while clicking the link in your local terminal to your local address, which should be:
```sh
http://127.0.0.1:5000
```


## DMV2U API Endpoints
_Once you have installed this program, you can use these endpoints on your local host in your browser._

Base URL: ```https://localhost:5000```

#### HTTP Requests
```sh
GET api/v1/plates/all
GET api/v1/plates?{parameters}
```
#### Path Parameters
| Parameter | Type | Description |
| :---: | :---: | --- |
| id | integer | Returns match by ID.
| date | YYYY-MM-DD |   |
| prev_date | string |  |
| status | string | "Assigned", "Available", or "Restricted"  |
| string | string |  |

#### Example Queries
To search by IDs:
```sh
https://localhost:5000/api/v1/plates?id={id}
```
To search by status:
```sh
https://localhost:5000/api/v1/plates?status={status}
```
```sh
https://localhost:5000/api/v1/plates?string={string}
```

## Support and contact details

_Have a bug or an issue with this application? [Open a new issue](https://github.com/kwicz/dmv2u/issues) here on GitHub._

## Technologies Used
* _Python 3.8.1_
* _Flask_
* _SQLite_

## License

[MIT License](https://choosealicense.com/licenses/mit/)

Copyright (c) 2020 **_K Wicz_**