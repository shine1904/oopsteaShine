Article URL: https://support.optisigns.com/hc/en-us/articles/39250660729747-How-to-Use-the-Tableau-App
Topic: How To Use The Tableau App

## Step 3: Create a Tableau Asset and Assign it to a Screen

Now that we’ve got the Tableau integration set up, it’s time to create a Tableau asset. This asset determines how your report will show up on your screens.

|  |
| --- |
| **NOTE** |
| See [**Note 2**](#Note2) if your workbook contains Broad Views. |

First, find the report you’d like to display. Hit **Share:**

![](https://support.optisigns.com/hc/article_attachments/39364492002579)

On the Share View window, hit **Copy Link**:

!share view copy link tableau (https://support.optisigns.com/hc/article_attachments/39250613936275)

Now go back to the OptiSigns portal and hit **Files/Assets** → **Apps:**

!optisigns files/assets tab app (https://support.optisigns.com/hc/article_attachments/39250613937555)

Now find the **Tableau** app.

!tableau app optisigns (https://support.optisigns.com/hc/article_attachments/39250660711955)

Clicking the app will open this window:

![](https://support.optisigns.com/hc/article_attachments/39597827693203)

* **Name -** The name of your Asset. This is used entirely in OptiSigns and can be anything you like.
* **Tableau Shared Report URL -** This is where you’ll input the Share URL you copied earlier.
* **Update Interval -** Denotes how often the app will sync, measured in seconds.
* **Authenticate with Connected App Integration -** Tick this box if you want to use Private reports. Since we set this up in [Steps 1](#Step1) and [2](#Step2), we recommend ticking this box. If you skipped those steps and only want to use Public reports, no need to check the box.

|  |
| --- |
| **NOTE** |
| Tableau Cloud only allows 600 Update Interval requests per user/hour. See [**Note 3**](#Note3) for more information and solutions on how to handle this. |

Now it's time to authenticate your Shared Report URL with an appropriate Connected App Integration you set up earlier:

![](https://support.optisigns.com/hc/article_attachments/39597827694099)

* **Connected App Integration -** Select the integration [you set up in Step 2](#Step2) in this box.

Once you input the **Tableau Shared Report URL** and have selected your Integration, hit **Save** and your report should appear as a Preview:

![](https://support.optisigns.com/hc/article_attachments/39597827695763)

Once you have tailored it to your liking, you can **Close** it. This will create a Tableau asset that can be added to a Playlist or directly assigned to a screen:

![](https://support.optisigns.com/hc/article_attachments/39597853567251)

In order to display different tabs of a report, select the tab you'd like to view on Tableau site, then hit **Share**, same way as before:

!tableau report share (https://support.optisigns.com/hc/article_attachments/39250660703635)

You'll then create a new Asset with that Share link as the **Site URL**:

![](https://support.optisigns.com/hc/article_attachments/39597827698067)

To display all the tabs in a report on a screen, these Assets can be placed in a Playlist (https://support.optisigns.com/hc/en-us/articles/28295104605843-How-to-Create-Use-Playlists) to show the complete report.