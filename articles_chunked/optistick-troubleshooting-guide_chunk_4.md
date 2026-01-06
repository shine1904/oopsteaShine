Article URL: https://support.optisigns.com/hc/en-us/articles/40147900639891-OptiStick-Troubleshooting-Guide
Topic: Optistick Troubleshooting Guide

## Hardware Troubleshooting

Here we will cover the most common hardware troubleshooting issues our support team encounters.

### Network Troubleshooting

|  |  |
| --- | --- |
| **GEN 2** | **GEN 3** |
| 2.4 GHz WiFi only | 2.4 GHz and 5 GHz WiFi |
| WiFi 5 and below | WiFi 5 and below |
| No Ethernet | Ethernet Capable |

The OptiStick is not compatible with 802.1x Enterprise networks or WPA3 WiFi security.

To identify and resolve network issues:

* Create a mobile hotspot, then have your OptiStick connect with it. A successful connection indicates a problem with your general Wi-Fi connection.
* Try a different network. You may need to move the device to get connected. A successful connection indicates a problem with your general Wi-Fi connection.
* Plug in an Ethernet cable to see if it can still connect.

To see what network you’re connected to, go to the Side Menu and hit **Exit**. This will close the OptiSigns app.

!exit optisigns app (https://support.optisigns.com/hc/article_attachments/40147917441555)

Next, open the menu on the side using the remote. If connected to a network, it should appear here. If not, you'll need to set that back up.

!access network optisigns player (https://support.optisigns.com/hc/article_attachments/40147900613907)

### Power Troubleshooting

One of the most common causes of device instability is not using the provided power adapters and cables.

If your device has any sort of intermittent power issues, ***please ensure it is not being powered by the USB port on your screen***. The USB port does not provide enough power to the device to keep it running under all conditions.

In the event there is no available power outlet nearby and the USB port is your only option, keep your content load light - meaning, no videos, no large files, etc.

### HDMI & TV Connection Troubleshooting

If you’re having problems connecting your OptiStick to your HDMI port or TV, here are some steps to try:

* Try a different HDMI port on your screen
* Try to connect the OptiStick directly to your TV without the HDMI extended
* Try a different TV or monitor to see if it will work at all

If none of these work, contact our support team at support@optisigns.com (support@optisigns.com).

### Remote Control Troubleshooting

The OptiStick Player ships with a Remote Control. Which remote control you have depends on the version of your player, but they largely function the same with a few slight differences.

**Gen 3 Remote:**

**!gen 3 remote control (https://support.optisigns.com/hc/article_attachments/40147917443347)**

|  |
| --- |
| **NOTE** |
| To pair or re-pair this remote, hold the **Back**and **Home**buttons. |

**Gen 2 Remote:**

!gen 2 remote control (https://support.optisigns.com/hc/article_attachments/40147900615827)

|  |
| --- |
| **NOTE** |
| To pair or re-pair this remote, hold the **Return**and **OK**buttons. |

OptiSigns Players also support the **Mobile Admin App** (https://support.optisigns.com/hc/en-us/articles/30003143806099-How-to-Use-the-OptiSigns-Mobile-Admin-App) as a Remote Control. This is our ***top recommendation,*** as not only does it function as a true remote control (allowing you to control your players from anywhere), but it has numerous other features as well.

If your remote control is having issues:

* Ensure batteries have been installed inside your remote control, and that they are not dead
* Re-pair your remote control with the player
* Try a plug-in USB keyboard or mouse
* Use the Mobile Admin app to set up Wi-Fi, or as a remote control itself

### Blank Screen Troubleshooting

If your device and screen are on, but only displays a black screen:

* Network issues, [**see above**](#Network).
* Check to make sure there is a Playlist or Asset assigned to your screen.
* Make sure your Timezones and Schedules match, including your Operational Schedule and normal schedule.
* Check your firewall settings, and ensure you’ve **Whitelisted OptiSigns IP addresses and ports** (https://support.optisigns.com/hc/en-us/articles/360047275934-Whitelist-OptiSigns-IP-addresses-ports).
* Check your Operational Schedule, and verify its power settings are not set to Off. If an Operation Schedule’s power settings are set to Off, it will remain off during the designed time.

If the device is still not displaying content after you’ve checked these, check our [**Content Playback Troubleshooting**](#ContentPlayback) section, then try a **Factory Reset**.

### Changing Device Time Zone

When **setting a schedule** (https://support.optisigns.com/hc/en-us/articles/360016981853-Create-and-Using-Schedules-with-OptiSigns), it's critical that the portal and device share the same time zone. If the time zones are not identical, it can cause your schedule to start at a different time than you'd like. The issue is usually the device's time zone.

To do this, you'll need to change it. Start by pressing the **Home button**on your remote (or hit **Exit App** from the Side Menu), and navigate to the **Settings** menu.

!settings menu (https://support.optisigns.com/hc/article_attachments/41497198237971)

Select **Device Preferences**.

!device preferences option android side menu (https://support.optisigns.com/hc/article_attachments/41497175224851)

Select **Date & Time**.

!date & time option android side menu (https://support.optisigns.com/hc/article_attachments/41497198242323)

Select **Set time zone**.

!select time zone option android side menu (https://support.optisigns.com/hc/article_attachments/41497198243347)

For some reason, Android devices lead with Midway Island, in the middle of the Pacific (some things in life are best left a mystery). Navigate to your preferred time zone and select it.

!time zone options android (https://support.optisigns.com/hc/article_attachments/41497198244627)

Now your device and schedule should sync properly.

|  |
| --- |
| **NOTE** |
| These steps can be performed remotely using the **Mobile Admin App**or through **MDM Commands**. The OptiStick needs to be connected and online for these commands to go through. |

### How to Factory Reset the OptiStick

You can factory reset your OptiStick Player if the system is not functioning properly or the OptiStick system will not load.

There are two ways to do a factory reset.

#### Soft Reset

A soft reset can be performed if the system is still accessible and operational. This will erase all the data on the device, and may help improve performance and fix some issues.

On the Home screen, go to **Settings**. Hit **Device Preferences,** then choose **About**. Finally, choose **Factory Reset.**

!factory reset settings (https://support.optisigns.com/hc/article_attachments/40147900617363)

It will ask if you’re sure you’d like to perform this function. If you are, hit **OK**. The soft factory reset will take place.

#### Hard Reset

When certain Android system files are corrupted, the device will not be able to boot into the Android system. In this case, you will need to perform a hard reset.

To perform one, you’ll need a small tool. Think paperclip, needle, or SIM card pin. Then, ensure the device is completely powered off and the USB power cable is unplugged from the device.

Next, use your small tool to press into the small hole on the side of the device. Hold it, then plug in the power cable while the tool is still pressing the button in the small hole.

!optisigns gen 3 player hard reset hole (https://support.optisigns.com/hc/article_attachments/40147900618259)

The system will then boot into recovery mode. You can use the button to navigate between selections and will need to press and hold for 1-2 secs to confirm selection. Choose **wipe data/factory reset**, and the factory reset will start.

!boot mode wipe data option (https://support.optisigns.com/hc/article_attachments/40147900620563)

Then choose **Factory data reset:**

**!boot mode factory data reset option (https://support.optisigns.com/hc/article_attachments/40147917447443)**

Once the process is complete, you’ll see a **Data Wipe Complete** message at the bottom of the screen. From there, select **Reboot System Now** to finish.

!boot mode reboot system now option (https://support.optisigns.com/hc/article_attachments/40147917449235)

Your OptiStick will be fully factory reset.

---