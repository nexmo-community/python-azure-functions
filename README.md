# Handling Phone Calls with Azure Functions & Python

This project contains sample code for the Nexmo Blog post "Handling Phone Calls with Azure Functions & Python"

I recommend you follow the blog post (which has not yet been published) to find out how to write and run this code! In the meantime, you can run the functions by installing Python 3.6,  [Azure Functions Core Tools](https://docs.microsoft.com/en-us/azure/azure-functions/functions-run-local) and running the following command:

```shell
# Create a python3.6 virtualenv:
python3.6 -m venv venv

# Activate the venv:
source venv/bin/activate

# Install dependencies:
python -m pip install -r requirements.txt

# Start the local Azure Functions server:
func host start
```
