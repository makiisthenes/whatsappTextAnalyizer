<center>
<h1><img id='what' src='https://www.stickpng.com/assets/images/580b57fcd9996e24bc43c543.png' width='50px' style='vertical-align: center;'>Whatsapp Text Analyiser [BETA] </h1>
</center>
<br>
<em>This python script will be able to take texts and analyise these things::</em>
  <br><b>Between person A and B, will be able to:</b>
    <ul>
    <li> Find out how many messages where sent by person A and B;</li>
    <li> Of these messages, the percentage of actual texts and images/stickers.</li>
    <li> The amount of emojis used by each person.</li>
    <li> The amount of times, user has initiated a conversation first.</li>
    </ul>
    <hr>
    <b>Currently still in deveopment:</b>
    <ul>
    <li> [UPDATED, now works.] The type of emoji specifically and how many times(beta).</li>
    <li> [UPDATED, now works.] The ability to save analysis.log in directory.</li>
    <li> [still in develpment] The time between messages send and averages, mean and standard devations data.</li>
    <li> [still in develpment] Graphical Analytical Representation of Chat (graphs and pie charts).</li>
    </ul>
    <i>The points above are currently being worked on.</i><br>
    <hr>
    <b>Future updates: --> Update 1.01</b>
    <ul>
    <li>Recognise message time frames.</li>
    <li>Use of Machine Learning Algorithms to determine subject of messages, similar to grammarly.</li>
    <li>Implementation of spelling checks in messages. ~ pyspellchecker 0.5.3</li>
    <li>Average message length, word length and average no of words.</li>
    <li>Determing whether you should initiate conversations more times.</li>
    <li>Determining whether you are sending too many messages.</li>
    <li>Response time of users from message.</li>
    </ul>
<i>This update will focus on timing and type of messages sent from both users.</i><br><hr>
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
<a href='https://www.imyfone.com/ios-data-recovery/export-whatsapp-chat-from-iphone/' target='_blank'>[External Link To Guide]</a><br>
<hr>
<h3>main.py Usage</h4>
To use, all you have to do is install dependancies found in requirements.txt<br>
Use "pip install -r requirements.txt" to install dependancies.<br>
Now from command line,<br>
CD to directory where <b>whatsappTextAnalyizer is stored<br>
usually found somewhere like "C:\Users\USER\Downloads\whatsappTextAnalyizer-master"<br>
and type python main.py FILE_PATH_TO_EXPORT.<br>
This will output an analysis statment...<br>
At the end it gives you the option to save this analysis, please be aware it will overwrite previously saved analysis.<br>
<hr>
<h4>Errors</h4>
If an error has occured its probably to do with the PATH_TO_FILE.<br>
Make sure that you have copied the whole complete directory path to the export file.<br>
If the problem still persists I found it useful to run it on Pycharm IDLE...<br>
<hr>
<h4>Contact Me and donations</h4>
To contact me,<br>
40126030@uxbridge.ac.uk<br> 
<br>
// Thanks and enjoy :) <br>
 Made by Michael Peres.
  
