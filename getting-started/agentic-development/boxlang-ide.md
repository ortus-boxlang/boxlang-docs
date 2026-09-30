---
description: >-
  Use the BoxLang IDE extension with AI agents for language intelligence,
  debugging, and agentic coding in VS Code.
icon: laptop-code
---

# BoxLang IDE

The [BoxLang IDE extension](../ide-tooling/boxlang-ide.md) gives you and your agent the same language intelligence: code insight, diagnostics, formatting, and a debugger. It works in VS Code and compatible editors such as Cursor, Windsurf, and VSCodium.

## 🧰 Install

```bash
code --install-extension ortus-solutions.vscode-boxlang-developer-pack
```

The developer pack includes the language support, the BoxLang theme, TestBox support, and CommandBox integration.

## 🤖 How It Helps Agentic Development

* **Agentic coding in the editor.** Chat with `@boxlang` for explanations, generation, and help with your BoxLang code.
* **Language intelligence.** Diagnostics and code insight catch mistakes in agent-written code early.
* **Debugging.** The [BoxLang debugger](../ide-tooling/boxlang-debugger/README.md) lets you step through code an agent wrote.
* **Works with your agent.** Use it alongside Copilot, Claude Code, Cursor, or another agent, with your project's `AGENTS.md`, skills, and MCP servers.

## 🛠️ Command Line Tooling Agents Can Use

Agents can also validate their work from the terminal:

* [Syntax Check](validate-your-code.md) (`boxlang check`) to confirm code parses
* [Formatter](../ide-tooling/boxlang-formatter.md) to apply consistent style
* [AST](../ide-tooling/boxlang-ast.md) to inspect how code is parsed
* [CFML Feature Audit](../ide-tooling/cfml-feature-audit.md) and [CFML Transpiler](../ide-tooling/cfml-to-boxlang-transpiler.md) for modernization work

{% content-ref url="../ide-tooling/boxlang-ide.md" %}
[boxlang-ide.md](../ide-tooling/boxlang-ide.md)
{% endcontent-ref %}
