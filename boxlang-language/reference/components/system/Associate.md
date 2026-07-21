
# Component: `Associate`

Allows subtag data to be saved with a base tag.

## Component Signature

```
<bx:Associate baseTag=[string]
dataCollection=[string] />
```

### Attributes


| Atrribute | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `baseTag` | `string` | `true` | The base tag to associate the data with |  |
| `dataCollection` | `string` | `false` | The collection of data to associate with the base tag | `AssocAttribs` |

## Examples

### Associate data with a parent custom tag

Passes attribute data from a child tag to its parent custom tag.

```java
<!--- Parent custom tag: mymenu.bx --->
<bx:mymenu>
    <bx:menuitem label="Home" href="/">
    <bx:menuitem label="About" href="/about">
</bx:mymenu>

<!--- Inside mymenu.bx, the associate data is available --->
<bx:loop array="#attributes.assocAttribs#" index="item">
    <a href="#item.href#">#item.label#</a>
</bx:loop>

```

### Use a custom data collection name

```java
<bx:parenttag>
    <bx:childtag>
        <bx:associate baseTag="parenttag" dataCollection="items">
    </bx:childtag>
</bx:parenttag>

```
