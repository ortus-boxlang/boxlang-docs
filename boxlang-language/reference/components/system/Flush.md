
# Component: `Flush`

I include a template into the current template

## Component Signature

```
<bx:Flush  />
```

### Attributes

This tag does not accept any attributes

## Examples

### Simple Script Example

Outputs 'foo' to the browser approximately 1 second before 'bar'

<a href="https://try.boxlang.io/?code=eJwrL8osSfUvLSkoLdFQULJJySyzS8vPt9EHMZQUNK25kiqs0nJKizOsuYpzUlMLNBQMDQwMQBLlmDqTEouQdAIAZEwcow%3D%3D" target="_blank">Run Example</a>

```java
writeOutput( "<div>foo</div>" );
bx:flush;
sleep( 1000 );
writeOutput( "<div>bar</div>" );

```


### Simple Tag Example

Outputs 'foo' to the browser approximately 1 second before 'bar'


```java
<div>foo</div> 
 <bx:flush/> <bx:sleep time="1000"/> 
 <div>bar</div>
```


