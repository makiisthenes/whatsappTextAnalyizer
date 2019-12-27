<center>
<h1><img id='what' src='https://www.stickpng.com/assets/images/580b57fcd9996e24bc43c543.png' width='50px' style='vertical-align: center;'>Whatsapp Text Analyiser</h1>
</center>
<br>
<em>This python script will be able to take texts and analyise these things::</em>
<hr>
  <br><b>Between person A and B, will be able to:</b>
    <ul>
    <li> Find out how many messages where sent by person A and B;</li>
    <li> Of these messages, the percentage of actual texts and images/stickers.</li>
    <li> The amount of emojis used by each person.</li>
    <li> [still in develpment] The type of emoji specifically and how many times.</li>
    <li> The amount of times, user has initiated a conversation first.</li>
    </ul>
<h3>Setup</h3>
<hr>
In order to use for the first time, script requires some parameters...<br>
--> Obtaining the text data for whatsapp chat...<br>
To obtain the whatsapp text file, you must access this on the mobile application.<br>
There are currently two different versions of Whatsapp running. iOS and Andriod.
<hr>
<h4>Exporting Chats using Andriod Whatsapp:</h4>
<i> 1) First go on desired chat you want to be analyised and tap the 3 dots.</i>
<img src='https://raw.githubusercontent.com/makiisthenes/whatsappTextAnalyizer/master/export_pics/Screenshot_20191227-142052_WhatsApp.jpg' width='400px'>
<i> 2) Then press on 'More >'...</i>
<img src='https://raw.githubusercontent.com/makiisthenes/whatsappTextAnalyizer/master/export_pics/Screenshot_20191227-142058_WhatsApp.jpg'>
<i> 3) Then press on 'Export Chat'...</i>
<img src='https://raw.githubusercontent.com/makiisthenes/whatsappTextAnalyizer/master/export_pics/Screenshot_20191227-142101_WhatsApp.jpg'>
<i> 4) Dont export meda ... </i>
<img src='https://raw.githubusercontent.com/makiisthenes/whatsappTextAnalyizer/master/export_pics/Screenshot_20191227-142121_WhatsApp.jpg'>
And then send to an email and obtain the txt file that can be analyised.
<hr>
<h4>Exporting Chats using iOS Whatsapp:</h4>
<hr>
--> Person A and Person B tags found in txt file...<br>
  These include person A and person B tags, to obtain them you can either use <b>setup.py</b><br>
  or manually set the variables...,<br>
  <b>1)<b/> By going to directory where <b>whatsappTextAnalyizer</b> is stored<br>
  usually found somewhere like "C:\Users\USER\Downloads\whatsappTextAnalyizer-master"<br>
  and type python setup.py <FILE_PATH_TO_EXPORT>.

