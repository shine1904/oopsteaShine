Article URL: https://support.optisigns.com/hc/en-us/articles/35184720136595-How-to-Install-a-Root-Certificate-and-Display-an-Internal-Website-on-Screens
Topic: How To Install A Root Certificate And Display An Internal Website On Screens

## Installing a Root Certificate on an OptiSigns Gen3 Pro Player

In order to get your root certificate onto an OptiSigns Pro Digital Signage Player, you’ll need to manually add it. Find where your certificate is stored, then download it to a USB or MicroSD card. Plug the card into the Pro Player.

|  |
| --- |
| **IMPORTANT** |
| For installation on a Gen 3 Pro Player, your certificate must have a **.crt** extension. However, it is important that this certificate is signed and contains your public key. These are usually generated as **.pem** files. You’ll need to rename your certificate (.pem) file and change its extension to **.crt** for your internal website to properly display. |

Now, open your OptiSigns player menu. Go to **About → Advanced Settings**.

**![](https://support.optisigns.com/hc/article_attachments/35184705322515)**

Here, you’ll see a field called **Certificate File**.

![](https://support.optisigns.com/hc/article_attachments/35184705339539)

Simply locate your certificate on your USB or MicroSD card and select it. The certificate will automatically be downloaded to the appropriate location. This will allow your OptiSigns player to display your internal website.

---