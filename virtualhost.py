#!/usr/bin/env python
import os

os.system("clear")

print("Ingrese el nombre de su domino")
domain=input()

index="index.html"
directory="/var/www/"

print("su domino sera almacenado en el siguiente directorio /var/www")
os.system("sudo mkdir -p "+directory+"/"+domain+"/"+index)

print("Asignando permisos")
os.system("sudo chmod -R 755 "+directory+domain)

print("ajustando la landing page")



landing=open(directory+"/"+domain+"/"+index)
landing.write("<!DOCTYPE html><html lang='en'><head><meta charset='UTF-8'><title>Virtual Hosts Created Successfully!</title><style>html{background-color: #508bc9;color: #fff;font-family: sans-serif, arial;}.container{width: 80%;margin: auto auto;}.inl{text-align: center;}.inl img{border-radius: 10px;}a{color: #f2d8ab;}</style></head><body><div class='container'><h1>Virtual Hosts Created Successfully!</h1><p><b>Apache Virtual Hosts Generator</b> has successfully created a virtual host in your server.<br>We can code it better! Join at <a href='https://github.com/rakibtg/Apache-Virtual-Hosts-Creator' target='_blank'>GitHub</a><br>Created by <a href='https://www.twitter.com/rakibtg' target='_blank'>Hasan</a></p><div class='divider'><div class='inl'><h1>Let's celebrate!</h1><img src='http://i.imgur.com/vCbBhwy.gif' alt='Scene from Spider Man Movie (C) Spider Man Movie ..'></div></div></div></body></html>")
landing.close()



#virtual host
#virtual=open("/etc/apache2/sites-available/"+domain+".conf", "w")
#virtual.write("<VirtualHost *:80>\nServerAdmin localserver@localhost\nServerName "+domain+"\nServerAlias www."+domain+"\nDocumentRoot "+directory+domain+"\nErrorLog ${APACHE_LOG_DIR}/error.log\nCustomLog ${APACHE_LOG_DIR}/access.log combined\n</VirtualHost>")
#virtual.close()
#os.system("sudo systemctl restart apache2")


#host
#host=open("/etc/hosts")
#host.write=("192.168.17.9\nadmin.com"))
#host.close=() 

#print("configuracion hosts")
#os.system("sudo sed -i -e\n192.168.1.42" +domain+"\' \"/etc/hosts\"")
#print("\nSuccess! Please visit http://"+domain+"/ from any web browser\n\n")

