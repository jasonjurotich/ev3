# ev3
Everything you need to set up and program a Lego ev3. https://www.ev3dev.org/ is based on a siplified version of Debian 9 (linux) which allows you to ssh into the ev3 brick and program it. Keep in mind that the processor is VERY simple and slow. You should only install what you really need. Trying to update or upgrade everything will take a long time, so it is best to aviod it. 


## SETTING UP THE EV3 THE FIRST TIME
- First you need to have a micro sd card with 4 GB minimum.  
- Try to avoid XC as sometimes these will not work but you can try them anyway. 
- https://amzn.to/2raL0q8
- Then, you need to download the image from here
- http://bit.ly/2KvU28f
- You should download snapshot-ev3dev-stretch-ev3-generic-2019-10-23.img.xz
- You should then change it to zip with this page: https://extract.me/
- Once it is downloaded as a zip, you open up the Chrome Recovery Utility on your Chromebook: http://bit.ly/2OmmGty
- In the upper right-hand corner, click on the cog (settings) and choose "Use local image" and choose the zip file
- On the next screen choose your micro sd card that you previously connected to your Chromebook. 
- Click on the blue bottons in the lower right hand corner until the image is written. 
- When it is done, close the Recovery Utility and then go to your files app on the Chromebook to eject the sd card, do NOT just pull it out. 
- When that is ready, just plug the sd card into the ev3 brick while the brick is off (do not try and put it in when it is on). 
- Press the center button on the ev3 to start up the ev3 Brick with the ev3dev operating system.

## USING WIFI
- You can use wifi with the ev3 so as to ssh into it. 
- you MUST use this wifi adapter: EDiMAX EW-7811Un WLAN 150
- https://amzn.to/37mrwiW
- After pluggin in the adpater and turning on the ev3 with ev3dev, go to Wireless and Networks > Wi-Fi > Power on
- Then clic on scan and choose your Network, and then put in the password. 
- It will not work with webpage wifi access. The wifi network must be simple and either open or with a simple password.
- The IP address will be on the top of the ev3 screen when you are connected. 
- The IP address is private and NOT public, so you can either connect on the local network or you will have to use reverse SSH if you want to connect remotely. 

## USING GOOGLE CLOUD PLATFORM (GCP) TO SSH INTO THE EV3
- You must have a GCP project open and active.
- You must have a Compute Engine VM instance up and running. https://youtu.be/sHtEtk0dYiA
- You must have previously entered by SSH into the ev3 on the local network 
- To enter by ssh you put ssh robot@localIP in your terminal ("localIP" is the IP address on top of the ev3 screen like 192.168.1.1)
- Do this on your Chromebook which alread has linux installed. https://youtu.be/EIAqPsyAMCw
- The password is maker
- Then, you create the SSH keys by putting ssh-keygen (just press enter various times after that until it finishes. 
- Then, put cat ~/.ssh/id_rsa.pub to find and copy the public key. 
- in your GCP, go to the VM instance and click on the name, then click on edit, and then down below, click on edit ssh keys
- paste the public key, put a space, and then put the name of the user that you see when you enter into the GCP normally. 
- back in the local ssh where you are inside your ev3, first make sure you can ssh normally into the GCP vm instance. 
- ssh jason@PUBLICIPGCP (jason should be your user when you enter normally into the GCP, and the ip is the public IP of the vm instance. 
- If that works then log out (type exit) and then put ssh -R 6000:localhost:22 jason@PUBLICIPGCP
- If that lets you enter, then leave that open (or active in the background) and in the GCP terminal put ssh -p 6000 robot@localhost and you should have access to your ev3 by ssh remotely. 
- BE VERY CAREFULL NOT TO HAVE OTHER PREVIOUS CONFIGURATIONS ON THE EV3 OR GCP OTHERWISE THIS WILL NOT WORK.





