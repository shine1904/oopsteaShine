Article URL: https://support.optisigns.com/hc/en-us/articles/40736654972563-OptiSigns-Pro-ProMax-Player-Troubleshooting-Guide
Topic: Optisigns Pro Promax Player Troubleshooting Guide

## Security Settings and Advanced Feature Troubleshooting

The Pro and ProMax Players offer advanced security settings and features that are indispensable for an enterprise environment. Below are the most common and helpful suggestions we have when trying to enable some of these more advanced settings.

See our **Pro/Pro Max Player Advanced Features** (https://support.optisigns.com/hc/en-us/articles/35577511423635-OptiSigns-Pro-Player-Advanced-Features) article for information on setting these up.

### Using the Device Log

There are two ways to use the **Device Log** feature:

1. By plugging in an external device to the player, then hitting the **Device Log** button on the **About** menu. This will bring up a box letting you know the log has been exported to the external device:

!device log export confirmation (https://support.optisigns.com/hc/article_attachments/40736654921235)

2. By using the ***collectDeviceLog*** **Remote Command** (https://support.optisigns.com/hc/en-us/articles/4408658251027-How-to-use-Remote-Command-Execution-Windows-Linux) from the OptiSigns portal. This will provide a download link that you can use to obtain the log:

!execute remote command device log (https://support.optisigns.com/hc/article_attachments/40736684875283)

This can be extremely helpful for troubleshooting any issues that might have occurred when the device was not being closely monitored.

### Static IP

When setting up a Static IP, make sure you’ve selected the appropriate static IP setting, depending on whether you’re using a WLAN or Ethernet connection.

!static IP wlanip vs ethip (https://support.optisigns.com/hc/article_attachments/40736684876691)

Next, ensure you’ve input the correct information in the IP Address, Default Gateway, Subnet Mask, and DNS Server fields.

!static ip options (https://support.optisigns.com/hc/article_attachments/40736654945427)

See our **Advanced Settings for the Pro/ProMax Player** (https://support.optisigns.com/hc/en-us/articles/35577511423635-OptiSigns-Pro-Player-Advanced-Features) article for more information.

### Internal Website and Certificates

For installation on a Gen 3 Pro or ProMax Player, your certificate must have a **.crt** extension. However, it is important that this certificate is signed and contains your public key. These are usually generated as **.pem** files. You’ll need to rename your certificate (.pem) file and change its extension to **.crt** for your internal website to properly display.

!certificate file option (https://support.optisigns.com/hc/article_attachments/40736684879635)

See our article on **how to install a root certificate and set up your internal website display** (https://support.optisigns.com/hc/en-us/articles/35184720136595-How-to-Install-a-Root-Certificate-and-Display-an-Internal-Website-on-Screens) for more information.

---