1. This is my First Practical Program.
2. it was made to run at startup and delete temporary files every half- and full hour!
3. However it both /temp-del.py/ and /countdown.py/ have to be first moved into the binary folder with the command "sudo mv temp-del.py countdown.py /bin"
4. Then you have to add it as a startup service. To do this you have to type in the command "crontab -e".
5. Once you executed the Command a file should have opened.
6. At the very end of the file you have to add a new line and write "@reboot python3 /bin/temp_del.py &" the & symbol tells your computer to see it as a background program so not to interfere with your GUI.
7. Once saved you can check if the file has been succesfully updated with "crontab -l" there look for the line of code you added
8. If the file was successfully updated you are now ready to reboot your Computer with the "reboot" Command.
9. Once rebooted your temporary files will be deleted every half- and full hour.
10. Thank you for using my program!
