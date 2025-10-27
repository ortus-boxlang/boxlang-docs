# BoxLang Documentation Project Instructions

## Project Overview

This repository contains the comprehensive documentation for **BoxLang** - a modern dynamic JVM language. The documentation is built using **GitBook** and follows a structured approach to documenting language features, framework capabilities, and developer tooling.

## Architecture & Organization

### Core Structure

- **`boxlang-language/`** - Core language documentation (syntax, BIFs, components)
- **`boxlang-framework/`** - Framework features (async programming, caching, modularity)
- **`getting-started/`** - Installation, configuration, IDE tooling
- **`extra-credit/`** - Advanced topics (DI, MVC, testing)
- **`readme/`** - Project meta information, contributing guidelines

### Documentation Types

1. **Language Reference** - Organized by functional categories (`arrays.md`, `strings.md`, `io/`, `jdbc/`)
2. **Framework Guides** - Feature-focused with practical examples (`async-pipelines.md`, `scheduled-tasks.md`)
3. **Modular Components** - Plugin/module documentation (`modularity/ai.md`, `modularity/pdf.md`)

## File Conventions

### Frontmatter Structure
Every documentation file uses YAML frontmatter with specific patterns:

```yaml
---
description: Brief, descriptive summary for SEO/navigation
icon: gitbook-icon-name  # From GitBook icon library
---
```

### Content Patterns

- **Emojis in headings** for visual hierarchy: `## 🚀 Getting Started`
- **Table-based API references** with consistent columns (Method, Purpose, Returns, Usage)
- **Code examples** in `js`/`java` blocks (BoxLang syntax highlighting) until BoxLang is offered by GitBook.  Use `xml` or `html` for markup examples.
- **Callouts** for important notes, warnings, and tips using GitBook's hint system
- **GitBook callouts** using `{% hint style="info|warning|danger|success" %}`
- **Markdown spacing** - All headers must be surrounded by blank lines (before and after). All code blocks must be surrounded by blank lines (before and after the fences).

### Navigation Integration

- **`SUMMARY.md`** defines the complete table of contents structure
- Cross-references use `{% content-ref url="relative/path.md" %}`
- External embeds with `{% embed url="..." %}`

## Documentation Workflows

### Content Creation Patterns
1. **Start with frontmatter** - Always include description and appropriate icon
2. **Use consistent heading hierarchy** - H1 (title), H2 (major sections), H3 (subsections)
3. **Include practical examples** - Every feature should have working code samples
4. **Cross-link related content** - Reference other docs for comprehensive coverage

### Reference Documentation
- **BIF documentation** follows pattern: Purpose → Syntax → Parameters → Examples
- **Component docs** include class structure, methods, and usage patterns
- **Framework features** combine conceptual explanation with practical implementation

### Special Content Types
- **Time units reference** - Centralized in `async-pipelines.md` for all async documentation
- **Configuration examples** - Use JSON/YAML blocks with proper syntax highlighting
- **API tables** - Consistent column structure across all reference materials

## Language-Specific Patterns

### BoxLang Syntax Conventions
- Use `js` syntax highlighting for BoxLang code blocks
- Function calls: `functionName( arg1, arg2 )`
- Structure access: `struct.key` or `struct[ "key" ]`
- Template syntax: `<bx:component>` for XML-style components
- Script syntax: Standard BoxLang scripting patterns
- **Closures vs Lambdas**:
  - Use **lambdas** (`->`) for deterministic functions that ONLY work with local variables or arguments passed to them
  - Use **closures** (`=>`) for functions that access variables from enclosing scope OR call external functions/BIFs
  - Example lambda: `array.map( ( item ) -> item * 2 )` (only uses the item argument)
  - Example closure: `array.filter( ( item ) => item > threshold )` (accesses threshold from outer scope)
  - Example closure: `() => loadUserFromDatabase( 123 )` (calls external function)

### Async Programming Documentation
- **Executors** - Thread pool management and configuration
- **BoxFutures** - Promise-like async programming patterns
- **Scheduled Tasks** - Cron-like scheduling with fluent API
- **Parallel Computations** - Collection processing and async operations

## GitBook Integration

### GitBook MCP Server

This project uses the GitBook Model Context Protocol (MCP) server for enhanced documentation capabilities. The MCP server provides access to GitBook's documentation and best practices.

**Reference:** [GitBook MCP Documentation](https://gitbook.com/docs/~gitbook/mcp)

Use the GitBook MCP to:
- Learn GitBook-specific syntax and features
- Understand code block formatting and options
- Access GitBook blocks and components documentation
- Follow GitBook best practices for content creation

### Styling Elements
- **Hint blocks** for callouts: `{% hint style="type" %}content{% endhint %}`
  - Available styles: `info`, `warning`, `danger`, `success`
  - Reference: [GitBook Hint Blocks](https://gitbook.com/docs/creating-content/blocks/hint)
- **Content references** for internal navigation
- **Embed blocks** for external resources
- **Table components** with GitBook-specific formatting
- **Code blocks** with syntax highlighting and optional features (line numbers, overflow handling)

### File Organization
- **README.md files** serve as section introductions
- **Reference materials** organized by functional categories
- **Progressive disclosure** - overview → details → examples → advanced patterns

## Contributing Guidelines

### Content Standards
- **Comprehensive examples** - Every feature needs working code samples
- **Cross-platform considerations** - Note OS-specific behaviors where relevant
- **Error handling patterns** - Include exception handling in examples
- **Performance considerations** - Document resource implications

### Documentation Maintenance
- **Version compatibility** - Note BoxLang version requirements
- **External link validation** - Ensure embedded content remains accessible
- **Code example testing** - Verify all code samples work with current BoxLang
- **Cross-reference accuracy** - Maintain valid internal links

This documentation serves as both user guide and developer reference, emphasizing practical usage patterns while maintaining comprehensive API coverage.
