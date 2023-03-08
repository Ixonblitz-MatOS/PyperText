# html
python html writer with CSS and custom JS support

USE:<br>
<code>from PyperText.html import Script</code><br>
<code>from PyperText.htmlButton import Button</code><br>
<code>#from PyperText.html{WIDGET} import WIDGET; ex from PyperText.htmlEntry import Entry; variations shared in file</code><br>
<code>myScript=Script("myfile.html")</code><br>
<code>myButton=Button()</code><br>
<code>myButton.setText("This is a button")</code><br>
<code>myScript.addWidget(myButton)</code><br>
<code>myScript.createAndWrite()</code><br>
