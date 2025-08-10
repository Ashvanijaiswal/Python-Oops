import json
import requests

BASE_URL = "http://localhost:8080/api/"
ID_STORE = {}


def replace_placeholders(obj):
    """Recursively replace placeholders in a dictionary or list."""
    if isinstance(obj, dict):
        return {k: replace_placeholders(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [replace_placeholders(item) for item in obj]
    elif isinstance(obj, str) and obj.startswith("{") and obj.endswith("}"):
        key = obj.strip("{}")
        return ID_STORE.get(key, obj)  # Replace if found, else keep as is
    else:
        return obj

def call_api(endpoint, payload, id_key, store_key_pattern):
    """Send POST request and store generated ID."""
    url = BASE_URL + endpoint
    resp = requests.post(url, json=payload, verify=False)  # verify=False for self-signed certs
    resp.raise_for_status()
    data = resp.json()
    generated_id = data.get(id_key)

    if isinstance(payload, list):
        for i, item in enumerate(payload):
            ID_STORE[store_key_pattern.format(i)] = generated_id if len(payload) == 1 else data[i][id_key]
    else:
        ID_STORE[store_key_pattern] = generated_id

    print(f"Stored IDs: {ID_STORE}")

def main():
    with open("input.json") as f:
        config = json.load(f)

    # Step 1: workflows (insert one by one)
    workflows = replace_placeholders(config["workflows"])
    for i, workflow in enumerate(workflows):
        call_api("workflows/save", workflow, "workflowId", f"workflowId-{i}")

    # Step 2: datasources (replace placeholders after workflows)
    datasources = replace_placeholders(config["datasources"])
    for i, datasource in enumerate(datasources):
        call_api("datasources/save", datasource, "dataSourceId", f"dataSourceId-{i}")

    # Step 3: filetemplates (replace placeholders after datasources)
    filetemplates = replace_placeholders(config["filetemplates"])
    for i, filetemplate in enumerate(filetemplates):
        call_api("filetemplates/save", filetemplate, "fileTemplateId", f"fileTemplateId-{i}")

if __name__ == "__main__":
    main()