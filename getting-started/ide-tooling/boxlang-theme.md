---
description: Beautiful VS Code themes specifically designed for BoxLang development with dark neon and light muted variations
icon: palette
---

# BoxLang Theme Extension

Clean, modern themes designed specifically for BoxLang development. This extension provides two carefully crafted color schemes that enhance your BoxLang coding experience with optimal syntax highlighting and visual appeal.

## 🎨 Available Themes

### BoxLang Dark (Neon)

![BoxLang Dark Neon](https://github.com/ortus-boxlang/vscode-boxlang-theme/blob/development/screenshots/boxlang-dark.png?raw=true)

High-contrast dark theme featuring vibrant neon colors with pink, purple, and cyan accents. Optimized for extended coding sessions while maintaining visual appeal and code readability.

### BoxLang Light (Muted)

![BoxLang Light Muted](https://github.com/ortus-boxlang/vscode-boxlang-theme/blob/development/screenshots/boxlang-light.png?raw=true)

Subtle light theme with soft teal and green backgrounds, perfect for daytime development. Features muted accent colors that reduce eye strain during long coding sessions.

## ✨ Key Features

- **BoxLang Optimized** - Specifically designed for BoxLang syntax highlighting and component recognition
- **Semantic Highlighting** - Enhanced token colors for better code understanding
- **Bracket Pair Colorization** - Distinct colors for matching brackets and parentheses
- **Complete UI Theming** - Consistent colors across editor, sidebar, terminal, and all VS Code interfaces
- **Component Support** - Special highlighting for BoxLang components (`<bx:component>` tags)
- **Eye-friendly** - Carefully selected contrast ratios for comfortable viewing

## 📦 Installation

### VS Code Marketplace

Install from the [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=ortus-solutions.vscode-boxlang-theme):

1. Open VS Code and go to Extensions (`Ctrl+Shift+X` / `Cmd+Shift+X`)
2. Search for "BoxLang Theme"
3. Click **Install**
4. Go to **File → Preferences → Color Theme** and select your preferred BoxLang theme

### OpenVSX Registry

For VS Code compatible editors like **Cursor**, **Windsurf**, **VSCodium**, install from [OpenVSX Registry](https://open-vsx.org/extension/ortus-solutions/vscode-boxlang-theme).

### Command Line Installation

```bash
# VS Code
code --install-extension ortus-solutions.vscode-boxlang-theme

# VS Code compatible editors
cursor --install-extension ortus-solutions.vscode-boxlang-theme
```

## 🎯 Recommended Settings

Enable these VS Code settings for the best theme experience:

```json
{
  "editor.semanticHighlighting.enabled": true,
  "editor.bracketPairColorization.enabled": true,
  "editor.guides.bracketPairs": "active",
  "editor.fontFamily": "Fira Code, 'Cascadia Code', Consolas, 'Courier New'",
  "editor.fontLigatures": true,
  "editor.fontSize": 14,
  "editor.lineHeight": 1.5
}
```

## 🔧 Theme Selection

After installation, activate your preferred theme:

1. **Windows/Linux**: `Ctrl+K`, `Ctrl+T` or `File → Preferences → Color Theme`
2. **macOS**: `Cmd+K`, `Cmd+T` or `Code → Preferences → Color Theme`
3. Select either:
   - **BoxLang Dark (Neon)** - For high contrast dark experience
   - **BoxLang Light (Muted)** - For comfortable light experience

## 🛠️ Development & Contributing

### GitHub Repository

- **Source Code**: [https://github.com/ortus-boxlang/vscode-boxlang-theme](https://github.com/ortus-boxlang/vscode-boxlang-theme)
- **Report Issues**: [GitHub Issues](https://github.com/ortus-boxlang/vscode-boxlang-theme/issues)

### Contributing Guidelines

1. Fork the repository
2. Create a feature branch
3. Edit theme JSON files in the `themes/` directory
4. Run `npm run build` to validate changes
5. Test themes using `npm run dev:host`
6. Submit a pull request with screenshots

{% hint style="info" %}
**Note**: When reporting visual issues, please include your VS Code version, operating system, and screenshots for faster resolution.
{% endhint %}
