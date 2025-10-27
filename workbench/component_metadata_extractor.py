#!/usr/bin/env python3
"""
Component Metadata Extractor for BoxLang Documentation

This script extracts metadata from BoxLang Component Java files
and generates documentation. It is designed to be reusable across different
BoxLang modules for consistent documentation generation.

Usage:
    python3 component_metadata_extractor.py <components_dir> <output_dir> [--template <template_file>]

Example:
    python3 component_metadata_extractor.py \
        /path/to/components \
        /path/to/output \
        --template /path/to/template.md
"""

import re
import sys
import json
from pathlib import Path
from typing import Dict, List, Optional, Tuple


class ComponentMetadataExtractor:
    """Extracts metadata from BoxLang Component Java files"""

    def __init__(self):
        self.components = {}

    def extract_from_file(self, java_file: Path) -> Dict:
        """Extract Component metadata from a Java file"""
        with open(java_file, 'r', encoding='utf-8') as f:
            content = f.read()

        metadata = {
            'name': java_file.stem,
            'filename': f"{java_file.stem}.md",
            'description': '',
            'attributes': [],
            'class_javadoc': '',
            'supported_actions': [],
            'raw_javadoc': ''
        }

        # Extract class name from file
        class_match = re.search(r'public class (\w+)', content)
        if class_match:
            metadata['class_name'] = class_match.group(1)

        # Extract @BoxComponent annotation details
        box_comp_match = re.search(
            r'@BoxComponent\(\s*([^)]+(?:\([^)]*\)[^)]*)*)\s*\)',
            content,
            re.DOTALL
        )
        if box_comp_match:
            comp_attrs = box_comp_match.group(1)

            # Extract description
            desc_match = re.search(r'description\s*=\s*"([^"]+)"', comp_attrs)
            if desc_match:
                metadata['description'] = desc_match.group(1)

            # Extract other component properties
            allows_body = re.search(r'allowsBody\s*=\s*(\w+)', comp_attrs)
            requires_body = re.search(r'requiresBody\s*=\s*(\w+)', comp_attrs)

            if allows_body:
                metadata['allows_body'] = allows_body.group(1)
            if requires_body:
                metadata['requires_body'] = requires_body.group(1)

        # Extract class-level javadoc
        class_javadoc = re.search(
            r'/\*\*\s*(.*?)\s*\*/\s*@BoxComponent',
            content,
            re.DOTALL
        )
        if class_javadoc:
            javadoc_text = class_javadoc.group(1)
            metadata['raw_javadoc'] = javadoc_text
            metadata['class_javadoc'] = self._clean_javadoc(javadoc_text)

            # Extract supported actions from javadoc
            actions = re.findall(r'-\s*(\w+):\s*(.+?)(?=\n\s*-|\Z)', javadoc_text)
            for action_name, action_desc in actions:
                metadata['supported_actions'].append({
                    'name': action_name,
                    'description': action_desc.strip()
                })

        # Extract declared attributes
        self._extract_declared_attributes(content, metadata)

        return metadata

    def _extract_declared_attributes(self, content: str, metadata: Dict) -> None:
        """Extract attribute information from declaredAttributes"""
        attrs_section = re.search(
            r'declaredAttributes\s*=\s*new Attribute\[\]\s*{([^}]+?(?:new Attribute[^}]*?})?)}',
            content,
            re.DOTALL
        )

        if not attrs_section:
            return

        attrs_text = attrs_section.group(1)

        # Parse each Attribute declaration
        # Pattern: new Attribute( Key.of("name"), "type", [defaultValue] )
        attr_decls = re.findall(
            r'new Attribute\(\s*([^)]+(?:\([^)]*\)[^)]*)*)\)',
            attrs_text
        )

        for decl in attr_decls:
            attr_info = self._parse_attribute_declaration(decl)
            if attr_info:
                metadata['attributes'].append(attr_info)

    def _parse_attribute_declaration(self, decl: str) -> Optional[Dict]:
        """Parse a single attribute declaration"""
        parts = [p.strip() for p in decl.split(',')]

        if len(parts) < 1:
            return None

        # Extract attribute name
        name_match = re.search(r'Key\.of\("([^"]+)"\)|KeyDictionary\.(\w+)', parts[0])
        if not name_match:
            name_match = re.search(r'"([^"]+)"', parts[0])

        attr_name = name_match.group(1) if name_match and name_match.group(1) else (
            name_match.group(2).lower() if name_match and name_match.group(2) else 'unknown'
        )

        attr_info = {
            'name': attr_name,
            'type': 'any',
            'required': 'false',
            'default': ''
        }

        # Extract type (second parameter)
        if len(parts) >= 2:
            type_str = parts[1].strip().strip('"')
            attr_info['type'] = type_str

        # Extract default value (third parameter)
        if len(parts) >= 3:
            default_val = parts[2].strip()
            # Remove quotes if present
            if default_val.startswith('"') and default_val.endswith('"'):
                default_val = default_val[1:-1]
            attr_info['default'] = default_val

        return attr_info

    def _clean_javadoc(self, javadoc: str) -> str:
        """Clean and format javadoc text"""
        # Remove leading * characters and extra whitespace
        lines = []
        for line in javadoc.split('\n'):
            # Remove leading asterisks and whitespace
            line = re.sub(r'^\s*\*\s?', '', line).strip()
            # Skip empty lines and filter out license text
            if line and not line.startswith('[BoxLang]') and not line.startswith('Copyright'):
                # Stop at "Supported actions" line to avoid including that section
                if line.startswith('Supported actions'):
                    break
                lines.append(line)
        return ' '.join(lines[:3])  # Return first 3 sentences max

    def extract_all(self, components_dir: Path) -> Dict[str, Dict]:
        """Extract metadata from all component files in a directory"""
        component_files = sorted(components_dir.glob("*.java"))
        print(f"Found {len(component_files)} component files in {components_dir}")

        for java_file in component_files:
            try:
                metadata = self.extract_from_file(java_file)
                self.components[metadata['name']] = metadata
                print(f"  ✓ {metadata['name']}")
            except Exception as e:
                print(f"  ✗ {java_file.name}: {e}")

        return self.components

    def get_metadata(self, component_name: str) -> Optional[Dict]:
        """Get metadata for a specific component"""
        return self.components.get(component_name)

    def to_json(self, output_file: Path) -> None:
        """Export all metadata to JSON file"""
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(self.components, f, indent=2)
        print(f"Exported metadata to {output_file}")


class ComponentMarkdownGenerator:
    """Generates Markdown documentation from Component metadata"""

    DEFAULT_TEMPLATE = """[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the component class)

# Component: `<{name}>`

{description}

## Supported Actions

{actions_section}

## Attributes

{attributes_table}

## Examples



## Related

"""

    def __init__(self, template: Optional[str] = None):
        self.template = template or self.DEFAULT_TEMPLATE

    def generate(self, metadata: Dict) -> str:
        """Generate Markdown from Component metadata"""
        # Build actions section
        actions_section = self._generate_actions_section(metadata['supported_actions'])

        # Build attributes table
        attr_table = self._generate_attributes_table(metadata['attributes'])

        # Format description - prefer @BoxComponent description
        description = metadata['description'].strip()
        if not description and metadata['class_javadoc']:
            description = metadata['class_javadoc']
        if not description:
            description = f"The {metadata['name']} component provides functionality for BoxLang applications."

        # Generate markdown
        markdown = self.template.format(
            name=metadata['name'],
            description=description,
            actions_section=actions_section,
            attributes_table=attr_table
        )

        return markdown

    def _generate_actions_section(self, actions: List[Dict]) -> str:
        """Generate actions section"""
        if not actions:
            return "No actions defined."

        section = ""
        for action in actions:
            section += f"- **`{action['name']}`** - {action['description']}\n"

        return section.rstrip()

    def _generate_attributes_table(self, attributes: List[Dict]) -> str:
        """Generate markdown table for attributes"""
        if not attributes:
            return "No attributes."

        table = "| Attribute | Type | Required | Description | Default |\n"
        table += "|-----------|------|----------|-------------|----------|\n"

        for attr in attributes:
            name = attr['name']
            attr_type = attr.get('type', 'any')
            required = attr.get('required', 'false')
            description = attr.get('description', '')
            default = attr.get('default', '')

            # Clean up description
            if description:
                description = ' '.join(description.split())

            table += f"| `{name}` | `{attr_type}` | `{required}` | {description} | {default} |\n"

        return table


class ComponentDocumentationGenerator:
    """Main class to orchestrate component documentation generation"""

    def __init__(self):
        self.extractor = ComponentMetadataExtractor()
        self.generator = ComponentMarkdownGenerator()

    def generate_docs(
        self,
        components_dir: Path,
        output_dir: Path,
        template_file: Optional[Path] = None,
        export_metadata: bool = False
    ) -> None:
        """Generate documentation for all components"""
        # Extract metadata
        print(f"\n📊 Extracting metadata from {components_dir}...")
        self.extractor.extract_all(components_dir)

        # Load custom template if provided
        if template_file and template_file.exists():
            print(f"\n📄 Loading custom template from {template_file}")
            with open(template_file, 'r', encoding='utf-8') as f:
                self.generator.template = f.read()

        # Create output directory
        output_dir.mkdir(parents=True, exist_ok=True)

        # Generate markdown files
        print(f"\n✍️  Generating documentation to {output_dir}...\n")
        for component_name, metadata in self.extractor.components.items():
            markdown = self.generator.generate(metadata)

            md_file = output_dir / metadata['filename']
            with open(md_file, 'w', encoding='utf-8') as f:
                f.write(markdown)

            print(f"  ✓ {md_file.name}")

        # Export metadata if requested
        if export_metadata:
            metadata_file = output_dir / "component_metadata.json"
            self.extractor.to_json(metadata_file)

        print(f"\n✅ Generated {len(self.extractor.components)} documentation files!")


def main():
    """Main entry point"""
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)

    components_dir = Path(sys.argv[1])
    output_dir = Path(sys.argv[2])
    template_file = None
    export_metadata = False

    # Parse optional arguments
    for i, arg in enumerate(sys.argv[3:]):
        if arg == '--template' and i + 4 < len(sys.argv):
            template_file = Path(sys.argv[i + 4])
        elif arg == '--export-metadata':
            export_metadata = True

    # Validate directories
    if not components_dir.exists():
        print(f"❌ Error: Components directory not found: {components_dir}")
        sys.exit(1)

    # Generate documentation
    generator = ComponentDocumentationGenerator()
    generator.generate_docs(components_dir, output_dir, template_file, export_metadata)


if __name__ == '__main__':
    main()
