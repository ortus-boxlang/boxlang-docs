[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `CLIGetArgs`

This method will parse the cli arguments and return a struct of the following:
 <ul>
 <li><code>options</code> - A struct of the options</li>
 <li><code>positionals</code> - An array of the positional arguments</li>
 </ul>

<p>
 The options can be provided in the following formats:
 <ul>
 <li><code>--option</code> - A boolean option</li>
 <li><code>--option=value</code> - An option with a value</li>
 <li><code>--option="value"</code> - An option with a quoted value</li>
 <li><code>--option='value'</code> - An option with a quoted value</li>
 <li><code>-o=value</code> - A shorthand option with a value</li>
 <li><code>-o</code> - A shorthand boolean option</li>
 <li><code>--!option</code> - A negation option</li>
 </ul>

 <p>
 For example, the following cli arguments:

 <pre>
 --debug --!verbose --bundles=Spec -o='/path/to/file' -v my/path/template
 </pre>

 <p>
 Will be parsed into the following struct:

 <pre>
 {
 "options" :  {
    	"debug": true,
   	"verbose": false,
  	"bundles": "Spec",
 	   	"o": "/path/to/file",
 	   	"v": true
 },
 "positionals": [ "my/path/template" ]
 </pre>

 <h2>Some Ground Rules</h2>
 <ul>
 <li>Options are prefixed with --</li>
 <li>Shorthand options are prefixed with -</li>
 <li>Options can be negated with --! or --no-</li>
 <li>Options can have values separated by =</li>
 <li>Values can be quoted with single or double quotes</li>
 <li>Repeated options will override the previous value</li>
 </ul>

## Method Signature

```
CLIGetArgs()
```

### Arguments

This function does not accept any arguments

## Examples

### Get parsed command-line arguments

```java
args = cliGetArgs();
writeOutput( isStruct( args ) );

```

Result: true

## Related

  * [CLIClear](./CLIClear.md)
  * [CLIExit](./CLIExit.md)
  * [CLIRead](./CLIRead.md)
