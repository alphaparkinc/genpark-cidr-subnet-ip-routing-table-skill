# genpark-cidr-subnet-ip-routing-table-skill

[![GitHub Stars](https://img.shields.io/github/stars/alphaparkinc/genpark-cidr-subnet-ip-routing-table-skill?style=social)](https://github.com/alphaparkinc/genpark-cidr-subnet-ip-routing-table-skill)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Zero External Dependencies](https://img.shields.io/badge/dependencies-0%20(pure%20standard%20library)-brightgreen.svg)](client.py)
[![MCP Ready](https://img.shields.io/badge/MCP-Ready-purple.svg)](mcp_server.py)

> **CIDR IP prefix routing table with Longest Prefix Match (LPM) and subnet decomposition**

Part of the **GenPark Autonomous Agent Matrix**, developed for production AI agents operating across local and distributed enterprise networks.

---

## 🏗️ Architecture

```mermaid
flowchart TD
    A[Agent Application / Network Stack] --> B[genpark-cidr-subnet-ip-routing-table-skill]
    B --> C[Pure Python Standard Library Engine]
    C --> D[Validated Network Output / Route Vector]
    B --> E[MCP Protocol Endpoint stdio]
    E --> F[Cursor / Claude Desktop / Windsurf Integration]
```

## 🚀 Quickstart

### Native Python Execution
```bash
python example_usage.py
```

### Standard Library Verification
```python
from client import *
```

### MCP Server (Claude Desktop / Cursor)
```json
{
  "mcpServers": {
    "genpark-cidr-subnet-ip-routing-table-skill": {
      "command": "python",
      "args": ["-m", "genpark_cidr_subnet_ip_routing_table_skill.mcp_server"]
    }
  }
}
```

## 📄 License
MIT License.
