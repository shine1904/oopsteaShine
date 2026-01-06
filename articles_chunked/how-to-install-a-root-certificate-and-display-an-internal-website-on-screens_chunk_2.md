Article URL: https://support.optisigns.com/hc/en-us/articles/35184720136595-How-to-Install-a-Root-Certificate-and-Display-an-Internal-Website-on-Screens
Topic: How To Install A Root Certificate And Display An Internal Website On Screens

## Installing a Root Certificate on OptiSigns Gen 2 Pro Players and Linux/Ubuntu Devices

To install a root certificate on a Linux or Ubuntu device, you’ll need to make heavy use of the **Terminal.**

To begin, take your trusted, signed certificate (.pem file) and place it in the /usr/share/ca-certificates folder.

![](https://support.optisigns.com/hc/article_attachments/35184720058515)

|  |
| --- |
| **NOTE** |
| You will need to rename your **.pem** file to make it a **.crt** file, or else this will not work. |

After the certificate has been moved and renamed, you’ll need to refresh the installed certificates and hashes. Open your **Terminal** and type in this command:

```
sudo update-ca-certificates
```

Once this command is executed, it should say that it has installed 1 (or more) new certificate.

![](https://support.optisigns.com/hc/article_attachments/35184720067475)

This means the certificate has been added to the operating system and signed certificates will be trusted.

Now, you’ll want to install the certificate in the Chromium store using this command:

```
certutil -A -n "ROOT-CA" -t "TCu,Cu,Tu" -i /usr/share/ca-certificates/[name-of-cert].crt -d sql:/home/[user]/.pki/nssdb
```

The Linux-based OptiSigns app uses Chromium, so this will allow the certificate to pass through the OptiSigns app.

Now reboot your device.

Congratulations! You’ve successfully installed a root certificate on Ubuntu.

---