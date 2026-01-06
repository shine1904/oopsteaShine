Article URL: https://support.optisigns.com/hc/en-us/articles/46299245284243-OptiKiosk-50-Setup-and-Troubleshooting-Guide
Topic: Optikiosk 50 Setup And Troubleshooting Guide

## Troubleshooting

Your first stop when running into a problem with the OptiKiosk should be the **Troubleshooting Page**. This is an option on the side menu.

To access it, swipe right on the left edge of your screen to open the side menu of the OptiSigns app. Navigate to **Troubleshooting** under the **Advanced** **Options** section.

![](https://support.optisigns.com/hc/article_attachments/46301404715795)

Now you can view detailed information about the app’s status and connectivity to assist with troubleshooting.

![](https://support.optisigns.com/hc/article_attachments/46301404716819)

* **Check Internet Connection**: Verifies whether the device has an active internet connection.
* **Check Connection to API Services**: Tests the device's connection to OptiSigns services.
  + Note: If this check fails, it may be due to a firewall blocking the connection. Refer to our Whitelist Article (https://support.optisigns.com/hc/en-us/articles/360047275934) for the required URLs and ports.
* **Check File Downloading**: Confirms the status of downloadable files (e.g., images, videos) being downloaded to the device.
* **Network Information**: Displays the current network the device is connected to.
  + WiFi/Ethernet Details: Includes IP Address, SSID, Signal Strength, Channel, Connection Type, and MAC Address.
* **Device Information:**
  + Screen Name, Pairing Code, Screen Resolution, OptiSigns App Version, OptiSigns MDM App Version, OS Version, Manufacturer, Model, Serial Number
  + Heartbeat/Polling Interval: Indicates how frequently the device communicates with OptiSigns servers and the last received signal.
* **Running Time:** Shows how long the OptiSigns app has been running on the device.
* **Storage:** Displays used and total storage capacity.
* **Memory:** Displays used and total memory capacity.
* **System Time:** Shows the current system time on the device.
* **System Time Zone:** Displays the time zone configured on the device.
* **Assigned Content Type:** Indicates the type of content the device is playing (e.g., Asset, Playlist, Schedule).
* **Assigned Content Name:** Provides the name of the content being displayed.
* **Device Created Date:** Displays the date the device was activated.
* **Operational Schedule Assigned:** Shows whether an operational schedule is assigned (Y/N).
* **Mute Status:** Displays the current audio status of the device.
* **Heavy Content Status:** Indicates whether the device is handling heavy content (e.g., 4+ zones or SplitScreen with 4K video) (Y/N). This will usually result in lag.

### **Hardware Troubleshooting**

Here, we will cover the most common hardware troubleshooting issues our support team encounters.

#### **Network Troubleshooting**

This is, by far, the most common issue people encounter. Devices experiencing network issues typically appear “Offline” in the OptiSigns portal, even when they are powered on and have content assigned to them.

![](https://support.optisigns.com/hc/article_attachments/46299811073427)

**To identify and resolve network issues:**

* Create a mobile hotspot, then have your OptiKiosk connect with it. A successful connection indicates a problem with your general Wi-Fi connection.
* Try a different network. You may need to move the device to get connected. A successful connection indicates a problem with your general Wi-Fi connection.
* If you have firewalls, make sure OptiSigns is whitelisted. Refer to our Whitelist Article (https://support.optisigns.com/hc/en-us/articles/360047275934) for the required URLs and ports.
* Plug in an Ethernet cable to see if it can still connect.
* After trying to connect with these methods, Factory Reset the device, then perform initial setup again.
* If the device still cannot connect to any network, contact our support team (https://support.optisigns.com/hc/en-us/articles/35626165056787-How-to-Contact-OptiSigns-Support).

#### **Blank Screen Troubleshooting**

If your device and screen are on, but only displays a black screen:

* Network issues, see above.
* Check to make sure there is a Playlist or Asset assigned to your screen.
* Make sure your Timezones and Schedules match, including your Operational Schedule and normal schedule.
* Check your firewall settings, and ensure you’ve Whitelisted OptiSigns IP addresses and ports (https://support.optisigns.com/hc/en-us/articles/360047275934-Whitelist-OptiSigns-IP-addresses-ports).
* Check your Operational Schedule, and verify its power settings are not set to Off. If an Operational Schedule’s power settings are set to Off, it will remain off during the designed time.

If the device is still not displaying content after you’ve checked these, try a Factory Reset.

#### **App Freezes, Video Assets Not Playing Full Video, or Asset Not Loaded Fully**

To handle any of these issues, hit the Refresh & Relaunch option, then reboot. You may need to Factory Reset if the problem persists.

#### **Performing a Factory Reset**

**Soft Reset**

If your kiosk is still operable, you can perform a soft factory reset directly from the system settings:

1. Open the **Settings** app.
2. Scroll down and select System.
3. Tap Reset options.
4. Choose Erase all data (factory reset).
5. Confirm your choice to begin the reset.

This will erase all data from the kiosk’s internal storage, including Google accounts, system and app data, downloaded apps, music, photos, and any other user content. After the reset is complete, the device will restart with its original factory settings.

---