import json
import sys
from client import CIDRRouter

router = CIDRRouter()
router.add_route("0.0.0.0/0", "default_gateway")
router.add_route("10.0.0.0/8", "corp_internal")
router.add_route("192.168.0.0/16", "local_lan")

def handle_request(req):
    method = req.get("method")
    params = req.get("params", {})
    req_id = req.get("id")

    if method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "tools": [
                    {
                        "name": "lookup_route",
                        "description": "Perform longest prefix match IP routing lookup",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "ip_address": {"type": "string"}
                            },
                            "required": ["ip_address"]
                        }
                    },
                    {
                        "name": "add_route",
                        "description": "Add CIDR route entry to router table",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "cidr": {"type": "string"},
                                "next_hop": {"type": "string"}
                            },
                            "required": ["cidr", "next_hop"]
                        }
                    }
                ]
            }
        }
    elif method == "tools/call":
        name = params.get("name")
        args = params.get("arguments", {})
        if name == "lookup_route":
            match = router.route(args["ip_address"])
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {"content": [{"type": "text", "text": json.dumps(match)}]}
            }
        elif name == "add_route":
            router.add_route(args["cidr"], args["next_hop"])
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {"content": [{"type": "text", "text": "Route added"}]}
            }
    return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": "Method not found"}}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            req = json.loads(line)
            res = handle_request(req)
            sys.stdout.write(json.dumps(res) + "\n")
            sys.stdout.flush()
        except Exception as e:
            err = {"jsonrpc": "2.0", "id": None, "error": {"code": -32700, "message": str(e)}}
            sys.stdout.write(json.dumps(err) + "\n")
            sys.stdout.flush()

if __name__ == "__main__":
    main()
