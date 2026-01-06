Article URL: https://support.optisigns.com/hc/en-us/articles/35184720136595-How-to-Install-a-Root-Certificate-and-Display-an-Internal-Website-on-Screens
Topic: How To Install A Root Certificate And Display An Internal Website On Screens

## Installing a Root Certificate on a MacOS Device

To prepare for the installation, make sure your device is connected to the same network of host servers you plan to use. Also, make sure your certificate is in a folder (the Download folder will work) on the device installing the certificates.

### Install Certificate

To begin, open **Keychain Access**. This is normally located in the “Other” folder in the launchpad.

![](https://support.optisigns.com/hc/article_attachments/35184720101907)

Select the System tab within the menu on the left. If you see a padlock icon next to the System folder, right click to unlock and enter the system password.

![](https://support.optisigns.com/hc/article_attachments/35184720103571)

![](https://support.optisigns.com/hc/article_attachments/35184720107027)

Open the folder where your certificate is stored. Drag and drop the certificate into the system folder in Keychain Access. If a red x is displayed next to the certificate like below, keep following along. Otherwise, you’re done.

![](https://support.optisigns.com/hc/article_attachments/35184705380883)

Right click the certificate and select “get info”

![](https://support.optisigns.com/hc/article_attachments/35184705382291)

Select “Trust”.

![](https://support.optisigns.com/hc/article_attachments/35184720114579)

Select “Always Trust”. This means your computer will always trust this certificate to keep your connection secure.

![](https://support.optisigns.com/hc/article_attachments/35184705386771)

Exit and you will be prompted with entering password. Enter the system password.

Your certificate is now installed. You will now be able to access the local website.

### Command Line Installation

On MacOS, you can also use the Terminal to directly install the Certificate. Simply type in these commands:

**Use the following command to add a certificate:**

```
sudo security add-trusted-cert -d -r trustRoot -k /Library/Keychains/System.keychain “new-root-certificate”
```

**Use the following command to remove a certificate:**

```
sudo security delete-certificate -c "name of existing certificate"
```

---