---
description: Solutions for common module development issues
icon: bug
---

# Troubleshooting

Solutions for common issues when developing BoxLang modules.

<details>
<summary>Module not loading / not found</summary>

**Symptoms:** Module doesn't appear in the registry, BIFs aren't available.

**Checklist:**

1. **Verify `box.json` `moduleName`** — Ensure `boxlang.moduleName` is set correctly
   ```json
   { "boxlang": { "moduleName": "myModule" } }
   ```

2. **Check module path** — The module directory must be in a scanned location (default: `./modules/` or as configured in `modulesDirectory`)

3. **Check `enabled` flag** — `this.enabled = true` in ModuleConfig.bx, not overridden to `false` in runtime config

4. **Check for descriptor conflicts** — If both ModuleConfig.bx and Java IModuleConfig exist, Java wins and BX is ignored

5. **Verify ModuleConfig.bx exists** at the module root

6. **If the module is nested inside another** — check the containing module too. A disabled or failed parent skips every module nested inside it, since their class loaders chain to its own. Its parent may also have disabled it via `this.modules`. See [Module Inception](module-inception.md)

7. **If the module is a JAR** — it must expose an `IModuleConfig` through `META-INF/services/ortus.boxlang.runtime.modules.IModuleConfig`. A JAR without one is disabled with a warning. Note the module is named after the JAR file unless `@BoxModule( name )` says otherwise

8. **Check logs** — Enable debug logging for the module service:
   ```json
   { "logging": { "loggers": { "modules": { "level": "DEBUG" } } } }
   ```

</details>

<details>
<summary>Class not found when using @moduleName</summary>

**Symptoms:** `import models.MyClass@myModule` throws "Class not found".

**Solutions:**

1. **Verify the module is loaded and activated** — `@moduleName` only works for active modules
   ```js
   boxRuntime.getModuleService().hasModule( "myModule" )
   ```

2. **Check the class path** — Path is relative to the module root
   ```js
   // Module root: /path/to/myModule/
   // Class at:    /path/to/myModule/models/MyClass.bx
   // Import:      import models.MyClass@myModule ✅
   ```

3. **For Java classes**, verify they're in the module's JAR or `libs/` folder

4. **Check ServiceLoader config** for Java classes — ensure the class is listed in the correct services file

</details>

<details>
<summary>BIF not callable after module load</summary>

**Symptoms:** Module loads without errors, but BIFs aren't available.

**Solutions:**

1. **For BoxLang BIFs** — Files must be in the `bifs/` folder at the module root
2. **For Java BIFs** — Class must be `@BoxBIF` annotated AND listed in `META-INF/services/ortus.boxlang.runtime.bifs.BIF`
3. **Check naming conventions** — The member function name is derived from the class name (e.g., `SetAdd` → `add`)
4. **Check for registration errors** in the module service log

</details>

<details>
<summary>Dependency not activating</summary>

**Symptoms:** Module declares `this.dependencies = [ "otherModule" ]` but `otherModule` isn't activating first.

**Solutions:**

1. **Verify the dependency module is discoverable** — It must be in a scanned module path
2. **Check dependency name** — Must match the registered module name (from `box.json` `boxlang.moduleName` or directory name)
3. **Dependencies are activated recursively** — If the dependency fails, its dependents won't activate either
4. **Missing dependencies don't prevent activation** — They log a warning but allow the module to proceed

</details>

<details>
<summary>Version incompatibility error</summary>

**Symptoms:** `"Module [X] requires BoxLang version [Y] but we are running [Z]"`

**Solutions:**

1. **Update BoxLang** to match or exceed the module's `minimumVersion`
2. **Update `minimumVersion`** in your `box.json` to match the runtime you're targeting
3. **Development mode** — BoxLang `0.x.x` versions skip version checks

</details>

<details>
<summary>Class loader / JAR conflict</summary>

**Symptoms:** `NoClassDefFoundError`, `ClassNotFoundException`, or unexpected behavior from a library.

**Solutions:**

1. **Check for conflicting JARs** — Use `./gradlew dependencies` to inspect the dependency tree
2. **Shadow conflicting dependencies** — The shadow JAR plugin can relocate packages to avoid conflicts
3. **Isolate your classes** — Ensure compiled classes use the `modules.{moduleName}` package prefix
4. **Move JARs to `libs/`** — External JARs in `libs/` are loaded with module-level isolation
5. **Check the containing module** — A [nested module](module-inception.md) inherits its parent's class loader, so a conflicting JAR in the parent's `libs/` is visible to it. Sibling modules are still isolated from each other
6. **Walk the chain correctly** — Module loaders track their parent themselves, so `getParent()` returns `null`. Use `DynamicClassLoader.getDynamicParent()` when inspecting the hierarchy

</details>

<details>
<summary>Interceptor not firing</summary>

**Symptoms:** Registered an interceptor but event methods aren't being called.

**Solutions:**

1. **Verify interceptor registration** — In `configure()`:
   ```js
   interceptors = [
       { class: "interceptors.MyListener", properties: {} }
   ]
   ```
2. **Check class path** — The class path is relative to the module root
3. **Check event names** — Method names must match the event name exactly (e.g., `onRequestStart`, not `onrequeststart`)
4. **For Java interceptors** — Implement `IInterceptor`, use `@InterceptionPoint`, and register via ServiceLoader

</details>

<details>
<summary>onUnload cleanup not running</summary>

**Symptoms:** Module resources aren't cleaned up on module unload or runtime shutdown.

**Solutions:**

1. **Wrap cleanup in try/catch** — An unhandled exception in `onUnload()` will abort cleanup
   ```js
   function onUnload() {
       try { cleanupResource1() } catch ( e ) { log.warn( "Cleanup failed", e ) }
       try { cleanupResource2() } catch ( e ) { log.warn( "Cleanup failed", e ) }
   }
   ```
2. **Check unload order** — Modules are unloaded in reverse activation order
3. **Verify unload is called** — Add a log statement to confirm `onUnload()` executes

</details>

<details>
<summary>Public assets returning 404</summary>

**Symptoms:** Files in `public/` folder aren't accessible via HTTP.

**Solutions:**

1. **Verify the file path** — `public/css/style.css` → URL: `/bxModules/myModule/public/css/style.css`
2. **Check custom mapping** — If `this.publicMapping` is overridden, use the custom URL path
3. **Ensure module is activated** — Public mappings are only available after activation
4. **Check web server configuration** — Ensure the `/bxModules/` path isn't blocked

</details>

## Getting Help

If you're still stuck:

1. **Check the logs** — Enable debug logging for more details
2. **Reference real modules** — Study open-source modules at [github.com/ortus-boxlang](https://github.com/orgs/ortus-boxlang/repositories?q=bx-)
3. **Use GitHub Issues** — Search for similar issues in the BoxLang repository
4. **Community** — Reach out on the BoxLang community channels
