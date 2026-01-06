Article URL: https://support.optisigns.com/hc/en-us/articles/31695220475283-Configuring-Mass-Deployment-with-Jamf-Pro-MDM-on-Apple-Devices
Topic: Configuring Mass Deployment With Jamf Pro Mdm On Apple Devices

## Step 2: OptiSigns App Enrollment with Jamf Pro MDM

Before deploying the app to devices, you can preconfigure it to have your device automatically enrolled into your OptiSigns account.

* This is not required, but if you are managing a large number of devices, this will make the deployment much easier.

To do this, navigate to the **mobile device apps section** in Jamf MDM → Click on the **OptiSigns Digital Signage app →** Select the **App Configuration** section → Complete the configuration as shown below:

!chrome_xqP0Dfxy2g.png (https://support.optisigns.com/hc/article_attachments/36280396747283)

Let's go through each section of the configuration:

!chrome_QVJc5ejA6j.png (https://support.optisigns.com/hc/article_attachments/36280396752915)

1. **serialNo:** Serial number of the device, you can map this to a variable from your MDM.
2. **accountId:** This is your OptiSigns Account ID, you need to enter it manually.

Account ID can be found inside the OptiSigns portal, by visiting the **Screens tab (https://app.optisigns.com/app/screenManagement)** → Finding the screen you'd like→ Clicking **Edit Screens** → Click **Advanced** → Click **More** → Click on the "**i**" button

!chrome_yBWo4GT2Dw.png (https://support.optisigns.com/hc/article_attachments/31704324281107)

This will open your **Device Info**:

!chrome_81PqujFdUR.png (https://support.optisigns.com/hc/article_attachments/31704337896467)

3. **screenName** - This is the screen name that will appear on the OptiSigns portal, as shown in the screenshot below. Normally this is mapped to a variable from your MDM.

!chrome_ffRQifJKS2.png (https://support.optisigns.com/hc/article_attachments/31736820764819)