from client import CIDRRouter

def main():
    r = CIDRRouter()
    r.add_route("0.0.0.0/0", "default_gateway")
    r.add_route("192.168.0.0/16", "switch_lan")
    r.add_route("192.168.1.0/24", "vlan_office")

    print(r.route("192.168.1.55"))  # Matches 192.168.1.0/24
    print(r.route("192.168.20.1"))  # Matches 192.168.0.0/16
    print(r.route("8.8.8.8"))       # Matches default_gateway

if __name__ == "__main__":
    main()
