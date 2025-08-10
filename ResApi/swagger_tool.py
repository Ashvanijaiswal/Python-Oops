import json
import requests

BASE_URL = "http://localhost:8080/api/"
AUTH_URL = "https://<server:port>/authservice/oath/token?grant_type=client_credentials"
AUTH_HEADER = {"Authorization": "Basic <HashValue>"}
ID_STORE = {}
ENTITY_MAP = {
    "workflows":      ("workflows/save", "workflowId"),
    "datasources":    ("datasources/save", "dataSourceId"),
    "filetemplates":  ("filetemplates/save", "fileTemplateId"),
    "datasourceflds":  ("datasourceflds/save", "dataSourceFldId"),
    "destinationtables": ("destinationtables/save", "destinationTableId")
    # Add more mappings as needed
}

def get_bearer_token():
    resp = requests.post(AUTH_URL, headers=AUTH_HEADER, verify=False)
    resp.raise_for_status()
    return resp.json()["access_token"]

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

def call_api(endpoint, payload, id_key, store_key_pattern, token):
    url = BASE_URL + endpoint
    headers = {"Authorization": f"Bearer {token}"}
    resp = requests.post(url, json=payload, headers=headers, verify=False)
    resp.raise_for_status()
    data = resp.json()
    generated_id = data.get(id_key)
    ID_STORE[store_key_pattern] = generated_id
    print(f"Stored IDs: {ID_STORE}")


def main():
    token = get_bearer_token()
    with open("input.json") as f:
        config = json.load(f)

    for key in config:
        if key in ENTITY_MAP:
            endpoint, id_key = ENTITY_MAP[key]
            items = replace_placeholders(config[key])
            for i, item in enumerate(items):
                call_api(endpoint, item, id_key, f"{id_key}-{i}",token)

if __name__ == "__main__":
    main()