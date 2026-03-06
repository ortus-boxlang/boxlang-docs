#!/usr/bin/env python3
"""
BIF Metadata Extractor for BoxLang Documentation

This script extracts metadata from BoxLang BIF (Built-In Function) Java files
and generates documentation. It is designed to be reusable across different
BoxLang modules for consistent documentation generation.

Usage:
    python3 bif_metadata_extractor.py <bifs_dir> <output_dir> [--template <template_file>]

Example:
    python3 bif_metadata_extractor.py \
        /path/to/bifs \
        /path/to/output \
        --template /path/to/template.md pablo was here 
"""

import re
import sys
import json
from pathlib import Path
from typing import Dict, List, Optional, Tuple


class BIFMetadataExtractor:
    """Extracts metadata from BoxLang BIF Java files"""

    def __init__(self):
        self.bifs = {}

    def extract_from_file(self, java_file: Path) -> Dict:
        """Extract BIF metadata from a Java file"""
        with open(java_file, 'r', encoding='utf-8') as f:
            content = f.read()

        metadata = {
            'name': java_file.stem,
            'filename': f"{java_file.stem}.md",
            'description': '',
            'arguments': [],
            'method_signature': '',
            'returns': '',
            'class_path': '',
            'raw_javadoc': ''
        }

        # Extract class name from file
        class_match = re.search(r'public class (\w+)', content)
        if class_match:
            metadata['class_name'] = class_match.group(1)

        # Extract @BoxBIF description
        box_bif_match = re.search(r'@BoxBIF\(\s*description\s*=\s*"([^"]+)"', content)
        if box_bif_match:
            metadata['description'] = box_bif_match.group(1)

        # Extract the entire javadoc comment for _invoke method
        javadoc_match = re.search(
            r'/\*\*\s*(.*?)\s*\*/\s*public Object _invoke',
            content,
            re.DOTALL
        )
        if javadoc_match:
            javadoc_text = javadoc_match.group(1)
            metadata['raw_javadoc'] = javadoc_text

            # Extract @argument entries
            arg_pattern = r'@argument\.(\w+)\s+(.+?)(?=@argument|@return|$)'
            arg_matches = re.findall(arg_pattern, javadoc_text, re.DOTALL)

            for arg_name, arg_desc in arg_matches:
                # Clean up multiline descriptions
                arg_desc = ' '.join(arg_desc.split())
                metadata['arguments'].append({
                    'name': arg_name,
                    'description': arg_desc.strip(),
                    'type': 'any',
                    'required': 'false',
                    'default': ''
                })

            # Extract @return
            return_match = re.search(r'@return\s+(.+?)(?=@|\Z)', javadoc_text, re.DOTALL)
            if return_match:
                metadata['returns'] = ' '.join(return_match.group(1).split()).strip()

        # Extract declared arguments for better type information
        self._extract_declared_arguments(content, metadata)

        # Build method signature
        arg_names = [f"{arg['name']}=[any]" for arg in metadata['arguments']]
        metadata['method_signature'] = f"{metadata['name']}({', '.join(arg_names)})"

        return metadata

    def _extract_declared_arguments(self, content: str, metadata: Dict) -> None:
        """Extract argument type information from declaredArguments"""
        args_section = re.search(
            r'declaredArguments\s*=\s*new Argument\[\]\s*{([^}]+?(?:new Argument[^}]*?})?)}',
            content,
            re.DOTALL
        )

        if not args_section:
            return

        args_text = args_section.group(1)

        # Parse each Argument declaration
        # Pattern: new Argument( required, type, Key.of("name"), [default] )
        arg_decls = re.findall(
            r'new Argument\(\s*([^)]+)\)',
            args_text
        )

        for i, decl in enumerate(arg_decls):
            parts = [p.strip() for p in decl.split(',')]

            if i < len(metadata['arguments']):
                # Update argument with type info
                if len(parts) >= 2:
                    # Extract required status
                    req = parts[0].lower() == 'true'
                    metadata['arguments'][i]['required'] = 'true' if req else 'false'

                    # Extract type
                    type_match = re.search(r'Argument\.(\w+)', parts[1])
                    if type_match:
                        metadata['arguments'][i]['type'] = type_match.group(1)

                # Extract default value if present
                if len(parts) >= 4:
                    default_val = parts[3].strip()
                    # Remove quotes if present
                    if default_val.startswith('"') and default_val.endswith('"'):
                        default_val = default_val[1:-1]
                    metadata['arguments'][i]['default'] = default_val

    def extract_all(self, bifs_dir: Path) -> Dict[str, Dict]:
        """Extract metadata from all BIF files in a directory"""
        bif_files = sorted(bifs_dir.glob("*.java"))
        print(f"Found {len(bif_files)} BIF files in {bifs_dir}")

        for java_file in bif_files:
            try:
                metadata = self.extract_from_file(java_file)
                self.bifs[metadata['name']] = metadata
                print(f"  ✓ {metadata['name']}")
            except Exception as e:
                print(f"  ✗ {java_file.name}: {e}")

        return self.bifs

    def get_metadata(self, bif_name: str) -> Optional[Dict]:
        """Get metadata for a specific BIF"""
        return self.bifs.get(bif_name)

    def to_json(self, output_file: Path) -> None:
        """Export all metadata to JSON file"""
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(self.bifs, f, indent=2)
        print(f"Exported metadata to {output_file}")


class MarkdownGenerator:
    """Generates Markdown documentation from BIF metadata"""

    DEFAULT_TEMPLATE = """[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `{name}`

{description}

## Method Signature

```
{method_signature}
```

### Arguments

{arguments_table}

## Examples



## Related

"""

    def __init__(self, template: Optional[str] = None):
        self.template = template or self.DEFAULT_TEMPLATE

    def generate(self, metadata: Dict) -> str:
        """Generate Markdown from BIF metadata"""
        # Build arguments table
        arg_table = self._generate_arguments_table(metadata['arguments'])

        # Format description (ensure it's a single line or properly formatted)
        description = metadata['description'].strip()

        # Generate markdown
        markdown = self.template.format(
            name=metadata['name'],
            description=description,
            method_signature=metadata['method_signature'],
            arguments_table=arg_table
        )

        return markdown

    def _generate_arguments_table(self, arguments: List[Dict]) -> str:
        """Generate markdown table for arguments"""
        if not arguments:
            return "No arguments."

        table = "| Argument | Type | Required | Description | Default |\n"
        table += "|----------|------|----------|-------------|----------|\n"

        for arg in arguments:
            name = arg['name']
            arg_type = arg.get('type', 'any')
            required = arg.get('required', 'false')
            description = arg.get('description', '')
            default = arg.get('default', '')

            # Clean up description
            description = ' '.join(description.split())

            table += f"| `{name}` | `{arg_type}` | `{required}` | {description} | {default} |\n"

        return table


class DocumentationGenerator:
    """Main class to orchestrate documentation generation"""

    def __init__(self):
        self.extractor = BIFMetadataExtractor()
        self.generator = MarkdownGenerator()

    def generate_docs(
        self,
        bifs_dir: Path,
        output_dir: Path,
        template_file: Optional[Path] = None,
        export_metadata: bool = False
    ) -> None:
        """Generate documentation for all BIFs"""
        # Extract metadata
        print(f"\n📊 Extracting metadata from {bifs_dir}...")
        self.extractor.extract_all(bifs_dir)

        # Load custom template if provided
        if template_file and template_file.exists():
            print(f"\n📄 Loading custom template from {template_file}")
            with open(template_file, 'r', encoding='utf-8') as f:
                self.generator.template = f.read()

        # Create output directory
        output_dir.mkdir(parents=True, exist_ok=True)

        # Generate markdown files
        print(f"\n✍️  Generating documentation to {output_dir}...\n")
        for bif_name, metadata in self.extractor.bifs.items():
            markdown = self.generator.generate(metadata)

            md_file = output_dir / metadata['filename']
            with open(md_file, 'w', encoding='utf-8') as f:
                f.write(markdown)

            print(f"  ✓ {md_file.name}")

        # Export metadata if requested
        if export_metadata:
            metadata_file = output_dir / "bif_metadata.json"
            self.extractor.to_json(metadata_file)

        print(f"\n✅ Generated {len(self.extractor.bifs)} documentation files!")


def main():
    """Main entry point"""
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)

    bifs_dir = Path(sys.argv[1])
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
    if not bifs_dir.exists():
        print(f"❌ Error: BIFs directory not found: {bifs_dir}")
        sys.exit(1)

    # Generate documentation
    generator = DocumentationGenerator()
    generator.generate_docs(bifs_dir, output_dir, template_file, export_metadata)


if __name__ == '__main__':
    main()
