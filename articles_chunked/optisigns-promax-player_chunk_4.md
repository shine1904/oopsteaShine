Article URL: https://support.optisigns.com/hc/en-us/articles/38680194603155-OptiSigns-ProMax-Player
Topic: Optisigns Promax Player

## How to Set Up the OptiSigns ProMax Digital Signage Player

1. [Connecting Device to your TV](#TV)
2. [Configuring Wi-Fi Settings](#Configuring)
   * [Optional: Connecting to a Non-Broadcast SSID](#Connecting)
3. [Setting Up Security Protocol](#Setting)
4. [Checking the Device's Detailed Information](#Checking)
5. [Troubleshooting](#Troubleshooting)

### Connecting Device to Your TV

1. **Connect the power adapter** to the DC-In port on the ProMax Player and **plug the adapter** into a power outlet.
2. **Plug the TV HDMI cable** to the **center HDMI port** on the ProMax Player (Use DP port for 8K output).
3. ***Optional:*** Secure the device to the back of TV using a T-mount.

!optisigns promax player whats in the box (https://support.optisigns.com/hc/article_attachments/38921124181651)

Now, we will cover how to set up and connect your OptiSigns ProMax Player to Wi-Fi, ensuring that your device has a stable internet connection right from the start.

|  |
| --- |
| Note: If you are connecting through LAN, you can skip this guide and follow this guide to set up your screen (https://support.optisigns.com/hc/en-us/articles/360016374813). |

---

### Configuring Wi-Fi Settings

Upon first boot (*make sure there is no LAN connected*), the OptiSigns ProMax Player will prompt you to configure your Wi-Fi settings using Mobile Admin app or manually, as shown in the image below:

!welcome to optisigns screen (https://support.optisigns.com/hc/article_attachments/39538703606419)

To perform manual Wi-Fi setup connect keyboard and muse(optional) and hit the Enter key to fill out Wi-Fi details, as shown on the screenshot below, first you choose Wi-Fi SSID and also on the bottom you can see device MAC and Hostname:

!device wifi settings (https://support.optisigns.com/hc/article_attachments/39538671757715)

After choosing SSID, you can choose security type and enter credentials. (If you choose WPA-Enterprise with TLS make sure your certificate is in .pem format)

!device wifi settings ssid (https://support.optisigns.com/hc/article_attachments/39538703611667)

Here’s what each field means and what you need to do:

* **WIFI SSID**: Select the name of the Wi-Fi network you want to connect to from the dropdown list.
* **WIFI Password**: Enter the password for the selected Wi-Fi network. You can click on the eye icon to show or hide the password as you type.
* **WIFI Security**: This dropdown lets you choose the type of security protocol your Wi-Fi network uses. By default, this is set to WPA2-PSK, which is the most common and secure option.

Once you have entered all the required information, click on the "**CONNECT**" button to link your OptiSigns Pro Player to the Wi-Fi network.

### Optional: Connecting to a Non-Broadcast SSID

If your Wi-Fi network does not broadcast its SSID (network name), you will need to manually enter the network information to connect your OptiSigns Pro Player. When you reach the Wi-Fi setup screen, follow these additional steps:

1. **Access the Wi-Fi SSID Dropdown**: Click on the dropdown menu labeled "WIFI SSID" to see the list of available networks. As shown in the image below, there is an option at the top labeled "Hidden Wifi...". Select this option if your network is not visible in the list.
2. **Enter Your Hidden SSID**: After selecting "Hidden Wifi...", you will be prompted to manually enter the name (SSID) of your Wi-Fi network. Ensure that the SSID is typed correctly, as this is case-sensitive.

!hidden wifi non-broadcast ssid (https://support.optisigns.com/hc/article_attachments/39538703613331)

### Setting Up Security Protocol

You’ll need to select the appropriate Wi-Fi security protocol that matches your network configuration. The security protocol determines how your Wi-Fi network is protected and how devices communicate securely. The image below shows the available options:

!setting up wifi security protocol (https://support.optisigns.com/hc/article_attachments/39538703615635)

Here’s a brief overview of each option:

* **NONE**:
  + **Description**: This option indicates that the Wi-Fi network has no security, meaning no password is required to connect.
  + **Usage**: This is uncommon for most networks as it leaves your network vulnerable to unauthorized access. It's generally recommended to avoid using unsecured networks for your digital signage.
* **WPA2-PSK**:
  + **Description**: WPA2-PSK (Wi-Fi Protected Access 2 - Pre-Shared Key) is the most widely used security protocol for Wi-Fi networks. It provides strong encryption and requires a password to connect.
  + **Usage**: This is the default and most recommended option for both home and business networks due to its balance of security and compatibility.
* **WPA2-Enterprise**:
  + **Description**: WPA2-Enterprise is a more advanced security protocol often used in corporate environments. It requires a RADIUS server for authentication, offering individual credentials for users rather than a single shared password.
  + **Usage**: If your network is managed by an IT department with a RADIUS server, this is the option you’ll need to choose.
* **WPA3-Personal**:
  + **Description**: WPA3-Personal is the latest Wi-Fi security protocol, offering enhanced protection against brute-force attacks and stronger encryption than WPA2. It also simplifies the process of connecting devices without a display, like IoT devices.
  + **Usage**: Use this option if your network supports WPA3, providing the highest level of security for your digital signage setup.

|  |
| --- |
| Note: Make sure to select the security protocol that corresponds with your network settings. If you're unsure which one to choose, consult your network administrator or refer to your router’s settings. |

After selecting the appropriate Wi-Fi security protocol, proceed by entering your network’s password and click on the "**CONNECT**" button to complete the Wi-Fi setup.

---