Article URL: https://support.optisigns.com/hc/en-us/articles/44890229616403-Using-an-Enterprise-Network-802-1x-with-OptiSigns
Topic: Using An Enterprise Network 802 1X With Optisigns

## Supported Devices

* OptiSigns Pro Player (https://www.optisigns.com/product/hardware/pro-digital-signage-player) or ProMax Player (https://www.optisigns.com/product/hardware/promax-digital-signage-player)
* Windows
* Linux

Note that this does not include the OptiStick, nor other devices such as Raspberry Pi. These do not support Enterprise networks at this time.

The scope of this article will limit itself to getting OptiSigns to work on OptiSigns devices. For Windows and Linux, connect the device to your network as normal and be sure OptiSigns has been **whitelisted through your organization's firewall** (https://support.optisigns.com/hc/en-us/articles/360047275934-Whitelist-OptiSigns-IP-addresses-ports)**.**

|  |
| --- |
| **IMPORTANT** |
| You'll need to know whether or not you're using **PEAP** or **EAP-TTLS** for your network security protocol. This will determine what sort of certificate to set up on the OptiSigns device. |

---