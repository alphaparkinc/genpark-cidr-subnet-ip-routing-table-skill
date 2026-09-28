"""CIDR Subnet & Longest Prefix Match (LPM) Routing Table.
100% Python Standard Library.
"""

class CIDRRouter:
    """Longest Prefix Match (LPM) IP routing table engine."""
    def __init__(self):
        self.routes = []

    @staticmethod
    def ip_to_int(ip_str: str) -> int:
        parts = [int(p) for p in ip_str.split(".")]
        return (parts[0] << 24) | (parts[1] << 16) | (parts[2] << 8) | parts[3]

    @staticmethod
    def int_to_ip(ip_int: int) -> str:
        return f"{(ip_int >> 24) & 0xFF}.{(ip_int >> 16) & 0xFF}.{(ip_int >> 8) & 0xFF}.{ip_int & 0xFF}"

    def add_route(self, cidr: str, next_hop: str):
        ip_part, mask_part = cidr.split("/")
        mask_bits = int(mask_part)
        ip_int = self.ip_to_int(ip_part)
        mask = (0xFFFFFFFF << (32 - mask_bits)) & 0xFFFFFFFF if mask_bits > 0 else 0
        network = ip_int & mask
        self.routes.append((mask_bits, network, mask, next_hop, cidr))
        self.routes.sort(key=lambda x: x[0], reverse=True)

    def route(self, ip_str: str) -> dict:
        target_int = self.ip_to_int(ip_str)
        for mask_bits, network, mask, next_hop, cidr in self.routes:
            if (target_int & mask) == network:
                return {
                    "destination": ip_str,
                    "matched_cidr": cidr,
                    "next_hop": next_hop,
                    "prefix_len": mask_bits
                }
        return {"destination": ip_str, "matched_cidr": "default", "next_hop": "drop", "prefix_len": 0}
