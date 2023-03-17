################################################
# This script will register all .json files in #
# the current working directory to the API.    #
# Move this script to the directory with the   #
# .json files and run it.                      #
################################################
import glob, json, requests, os

def register(path = "patterns", api_url = "http://localhost:8000/patterns", debug = False):

    if not path.startswith("/"):
        path = "/" + path
    if not path.endswith("/*.json"):
        if path.endswith("*.json"):
            path = path[:-5] + "/*.json"
        else:
            path += "/*.json"

    if debug:
        print("Searching for patterns in:", os.getcwd() + path)

    # Load all .json files in the cwd
    files = glob.glob(os.getcwd() + path)

    # Create the dictionary
    d = {
        "patterns": []
    }

    # For each file load the data and add it to the dictionary
    for file in files:
        if debug:
            print("Registering pattern: ", file)
        data = json.load(open(file))

        # Add the data to the dictionary
        d['patterns'].append({
            "pattern_name": file.replace('.json', '').replace("\\", "/").split("/")[-1],
            "pattern": data
        })


    # Make a post request to the API
    r = requests.post(api_url, json=d)
    print("Pattern register code (200 = success):", r.status_code)

    # Print all registered patterns
    r = requests.get(api_url)
    print("Registered patterns:", r.json())

if __name__ == "__main__":
    register()