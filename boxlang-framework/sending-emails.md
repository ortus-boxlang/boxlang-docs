# Sending Emails

BoxLang gives you the `mail` tag/construct to easily send email in text or HTML format without ceremony. Just register your mail servers in the administrators or the `Application.bx` and you are ready to start sending emails in a jiffy!

```java
mail(
  subject="Your Order",
  from="myshop@ortus.com",
  to="whatever@gmail.com,another@gmail.com",
  bcc="orders@ortus.com"
  type="HTML"
){
  // body of the email.
  writeOutput( 'Hi there,' );
  writeOutput( 'This mail is sent to confirm that we have received your order.' );
};
```

### Query Binding

You can even bind the mail construct with a query, and the engine will send as many emails as rows in the query for you:

```java
var qData = userService.getNewUsers();
mail(
  subject="Welcome to FORGEBOX!",
  from="myshop@ortus.com",
  to="#qData.email#",
  query=qData
){
  writeOutput( "
    Dear #qData.name#,

    Welcome to your FORGEBOX account! Play and just do it!
  ")
};
```

### Sending Attachments

You can also send attachments to your email destinations very easily using the `mimeattach` attribute or via the child `mailparam()` construct, which allows you to send multiple attachments or headers.

```java
mail(
  subject="Your Order",
  from="myshop@ortus.com",
  to="whatever@gmail.com,another@gmail.com",
  bcc="orders@ortus.com"
  mimeattach=expandPath( "/my/path/attach.pdf" );
){
  // body of the email.
  writeOutput( 'Hi there,' );
  writeOutput( 'This mail is sent to confirm that we have received your order.' );
};

mail( subject="Attachments", to="you@domain.com", from="me@domain.com" ) {
	mailparam( name="Reply-To", value="me@domain.com" );
	mailparam( file="c:\files\readme.txt" );
	mailparam( file="c:\files\logo.gif" );
}
```
