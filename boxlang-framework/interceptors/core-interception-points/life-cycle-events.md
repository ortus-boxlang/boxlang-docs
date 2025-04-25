# Life-cycle Events

These events occur during the lifecycle of components (CFCs) and built-in functions (BIFs).

| Event Name              | Data | Description                                               |
| ----------------------- | :--: | --------------------------------------------------------- |
| `onBIFInstance`         |      | Triggered when a BIF is instantiated.                     |
| `onBIFInvocation`       |      | Triggered when a BIF is invoked.                          |
| `onComponentInstance`   |      | Triggered when a component is instantiated.               |
| `onComponentInvocation` |      | Triggered when a component method is invoked.             |
| `onFileComponentAction` |      | Triggered on lifecycle actions for file-based components. |
| `onCreateObjectRequest` |      | Triggered when a `createObject()` call is made.           |
