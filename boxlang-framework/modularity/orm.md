---
description: >-
  The BoxLang ORM module allows your BoxLang application to integrate with the
  powerful Hibernate ORM
icon: database
---

# ORM

### BoxLang ORM <a href="#boxlang-orm" id="boxlang-orm"></a>

The [BoxLang ORM module](https://github.com/ortus-boxlang/bx-orm) allows your BoxLang application to integrate with the powerful [Hibernate ORM](https://hibernate.org/orm/). With Hibernate, you can interact with your database records in an object oriented fashion, using a BoxLang class to denote each record and simple getters and setters for each field value:

```groovy
@entityName( "Auto" ) 
@persistent
class {

  property name="id" type="string" fieldtype="id" ormtype="string";
  property name="make" type="string";
  property name="model" type="string";

  function onPreInsert(){
      log.info( "Inserting new Auto: #getMake()# #getModel()#" );
 }
}
```

BoxLang ORM also enables transactional persistence, where an error during a save will roll back the entire transaction to prevent leaving the database in a broken state:

```groovy
transaction{
    try{
        entitySave(
            entityNew( "Purchase", {
                productID : "123-expensive-watch",
                purchaseTime : now(),
                customerID : customer.getId()
            })
        );
        var cartProducts = entityLoad( "CartProduct", customer.getID() );
        entityDelete( cartProducts );
    } catch ( any e ){
        // don't clear the user's cart if the purchase failed
        transactionRollback();
        rethrow;
    }
}
```

### Hibernate Version Support <a href="#hibernate-version-support" id="hibernate-version-support"></a>

bx-orm bundles Hibernate `5.6.15.FINAL`.

### Features In A Nutshell <a href="#features-in-a-nutshell" id="features-in-a-nutshell"></a>

* Add Object Relational Mapping to any boxlang app with Hibernate ORM
* Use native built-in-functions (BIFs) to update and persist entities to the database (`entityNew()`, `entitySave()`, `ormFlush()`, etc.)
* Supports 80+ database dialects, from `SQLServer2005` to `MySQL8` and `PostgreSQL`
* Generate your mapping XML once and never again with the `autoGenMap=false` ORM configuration setting
* React to entity changes with pre and post event listeners such as `onPreInsert()`, `onPreUpdate()` and `onPreDelete()`
* Over 20 native BIFs:
  * `EntityDelete()`
  * `EntityLoad()`
  * `EntityLoadByExample()`
  * `EntityLoadByPK()`
  * `EntityMerge()`
  * `EntityNameArray()`
  * `EntityNameList()`
  * `EntityNew()`
  * `EntityReload()`
  * `EntitySave()`
  * `EntityToQuery()`
  * `ORMClearSession()`
  * `ORMCloseAllSessions()`
  * `ORMEvictCollection()`
  * `ORMEvictEntity()`
  * `ORMEvictQueries()`
  * `ORMExecuteQuery()`
  * `ORMFlush()`
  * `ORMGetSession()`
  * `ORMGetSessionFactory()`
  * `ORMReload()`

### Documentation

This module has quite an extensive documentation, so check out our book on it: [https://bxorm.ortusbooks.com/](https://bxorm.ortusbooks.com/)

{% embed url="https://bxorm.ortusbooks.com/" %}

### GitHub Repository and Reporting Issues <a href="#github-repository-and-reporting-issues" id="github-repository-and-reporting-issues"></a>

Visit the [GitHub repository](https://github.com/ortus-boxlang/bx-orm) for the latest source code and our [ORM docs](https://bxorm.ortusbooks.com/readme/release-history) for docs and release notes. You can also file a bug report or improvement suggestion via [Jira](https://ortussolutions.atlassian.net/secure/CreateIssueDetails!init.jspa?pid=13359\&components=27026\&issuetype=1).
