---
icon: message
description: Pre-built MCP prompts that guide AI clients through common diagnostic and administrative workflows.
---

# 🧠 MCP Prompts

The server registers **32 pre-built MCP prompts** that guide AI clients through common diagnostic and administrative workflows. Each prompt instructs the AI agent which tools to call and in what order, and provides system-level context for interpreting results.

Prompts are organized into the following categories:

| Category | Page | Prompts |
| --- | --- | --- |
| Operations & Monitoring | [Operations & Monitoring](operations-and-monitoring.md) | 6 |
| Diagnostics & Auditing | [Diagnostics & Auditing](diagnostics-and-auditing.md) | 12 |
| Developer & Data | [Developer & Data](developer-and-data.md) | 6 |
| Infrastructure & Incident | [Infrastructure & Incident](infrastructure-and-incident.md) | 8 |

---

## Getting a Prompt

Prompts are retrieved via JSON-RPC 2.0:

```bash
curl -s http://localhost:8080/~bxmcp/boxlang.bxm \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer your-token" \
  -d '{"jsonrpc":"2.0","method":"prompts/get","params":{"name":"prompt_name","arguments":{}},"id":"1"}'
```

See the [Protocol Reference](../protocol.md) for complete details.
