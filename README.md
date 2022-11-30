# html
python html writer with CSS and custom JS support

USE:
<code>
from PyperText.html import Script
from PyperText.htmlButton import Button
#from PyperText.html{WIDGET} import WIDGET; ex from PyperText.htmlEntry import Entry; variations shared in file
myScript=Script("myfile.html")
myButton=Button()
myButton.setText("This is a button")
myScript.addWidget(myButton)
myScript.createAndWrite()
</code>