import json

def parse_openapi_spec(content):
    spec = json.loads(content)
    paths = spec.get("paths", {})
    endpoint_info = []

    for path, methods in paths.items():
        for method, meta in methods.items():
            summary = meta.get("summary", "")
            params = meta.get("parameters", [])
            endpoint_info.append({
                "path": path,
                "method": method.upper(),
                "summary": summary,
                "params": params,
            })
    return endpoint_info
