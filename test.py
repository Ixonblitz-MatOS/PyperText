from src.PyperText.html import Script
from src.PyperText.htmlEntry import Entry
myScript=Script("test.html")
myScript.addCustomHeader("lang=\"en\"")
myEntry=Entry()
myEntry.setValue("Val")
myScript.addWidget(myEntry)
myScript.createAndWrite()