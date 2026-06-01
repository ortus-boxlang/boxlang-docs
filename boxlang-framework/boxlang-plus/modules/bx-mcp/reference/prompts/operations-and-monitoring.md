---
icon: heart-pulse
description: Pre-built prompts for runtime health checks, system audits, performance troubleshooting, and deployment validation.
---

# ⚡ Operations & Monitoring Prompts

| Prompt | Description | Arguments |
| --- | --- | --- |
| `runtime_health_check` | Comprehensive health check: memory, caches, datasources, executors, modules | — |
| `full_system_audit` | End-to-end audit of every subsystem (JVM, threads, web server, caches, datasources, modules, schedulers, executors, logging, watchers) | — |
| `performance_troubleshooting` | Interactive diagnostic guide for a given symptom (slow responses, high memory, CPU spikes, thread pool exhaustion) | `symptom` *(required)* |
| `diagnose_memory_pressure` | JVM memory diagnosis: heap, non-heap, pools, GC activity; identifies leaks and misconfiguration | `threshold` *(optional, default: 80)* |
| `executor_saturation_check` | Async executor pool saturation, queue buildup, and rejected tasks | — |
| `deployment_validation` | Validate a deployment after a new release or module update: confirms runtime started cleanly, expected modules loaded, datasources reachable, executor pools healthy, and web server accepting traffic | `expectedModules` *(optional)* |
