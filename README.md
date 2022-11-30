# html
python html writer with CSS and custom JS support

USE:
<code><br>
from PyperText.html import Script<br>
from PyperText.htmlButton import Button<br>
#from PyperText.html{WIDGET} import WIDGET; ex from PyperText.htmlEntry import Entry; variations shared in file<br>
myScript=Script("myfile.html")<br>
myButton=Button()<br>
myButton.setText("This is a button")<br>
myScript.addWidget(myButton)<br>
myScript.createAndWrite()<br>
</code>