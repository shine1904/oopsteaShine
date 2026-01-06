Article URL: https://support.optisigns.com/hc/en-us/articles/35184720136595-How-to-Install-a-Root-Certificate-and-Display-an-Internal-Website-on-Screens
Topic: How To Install A Root Certificate And Display An Internal Website On Screens

Article URL: https://support.optisigns.com/hc/en-us/articles/35184720136595-How-to-Install-a-Root-Certificate-and-Display-an-Internal-Website-on-Screens
--- DOCUMENT START ---

# How to Install a Root Certificate and Display an Internal Website on Screens

### In this article, we will explain how to install a root certificate on your devices to set up an internal website for use with OptiSigns.

* [Installing a Root Certificate on an OptiSigns Gen 3 Pro Player](#ProPlayer)
* [Installing a Root Certificate on a Linux/Ubuntu Device](#Ubuntu)
* [Installing a Root Certificate on a Windows Device](#Windows)
  + [Open the Microsoft Management Console (MMC)](#MMC)
  + [Add the Certificates Snap-in](#Snap-In)
  + [Import the Certificate](#Import)
  + [Verify the Installation](#Verify)
  + [Command Line Installation](#Command1)
* [Installing a Root Certificate on a MacOS Device](#MacOS)  
  + [Install Certificate](#Install)
  + [Command Line Installation](#Command2)
* [Installing a Root Certificate on Chrome-Based Web Browsers](#Chrome)
* [Setting Up an Internal Website for Use on OptiSigns Using the Website App](#InternalWebsite)
  + [Using Web Scripting to Bypass Logins](#WebScripting)

OptiSigns digital signage software is an extremely valuable tool for internal communication, capable of displaying internal memos, communications, and announcements across numerous locations and offices. Messaging can be tailored to specific audiences, scheduled, and automatically synced to data sources.

With all these capabilities, it stands to reason that some want to incorporate OptiSigns into their intranet, or internal website. These can be displayed on your screens using the OptiSigns Website app, or Advanced Website app in some cases.

However, in order to do this, you’ll need a trusted, self-signed root certificate installed on the platform you choose to run it on. Here, we’ll show you how to get that installed.

Please note that you’ll need to obtain a trusted certificate yourself. This will need to be some sort of key, usually denoted by a **.pem** file extension.

In this article, we will walk you through two main steps:

1. Installing a root certificate on your device of choice (OptiSigns Pro Player, Ubuntu, Windows, MacOS, or Chrome browser)
2. Configuring a Website app to display your internal website

|  |
| --- |
| **NOTE** |
| Before you start, make sure you’re connected to the same network as the server you’re trying to access. |

|  |
| --- |
| **Please note that Android devices are not supported at this time.** |

---