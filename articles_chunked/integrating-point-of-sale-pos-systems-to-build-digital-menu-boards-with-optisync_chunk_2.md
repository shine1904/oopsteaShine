Article URL: https://support.optisigns.com/hc/en-us/articles/31860170199955-Integrating-Point-of-Sale-POS-Systems-to-Build-Digital-Menu-Boards-with-OptiSync
Topic: Integrating Point Of Sale Pos Systems To Build Digital Menu Boards With Optisync

## How to Build Digital Menu Boards in Designer with OptiSync

In order to create a DMB with data from your POS system, the API Request will need to be registered as a DataSource. This allows data elements to be added to OptiSigns' Designer app (https://support.optisigns.com/hc/en-us/articles/4404151402899-How-to-use-OptiSigns-Template-Designer-app-to-make-your-Digital-Signs-in-minutes), where it can be formatted and incorporated into any visual design you'd like to display.

The Designer app and templates can be used to do the formatting, and mapping the element to the data from the API data source. Any text box or image element can be mapped in Designer. When you map an image element, the URL of the image will be replaced at run time.

---

### Using DataSources and Repeaters

To get started, find your design or create a new one in the **Files/Assets** tab.

With the design open, click **"DataSource"** in the left hand column. Then, click **"Add DataSource"** to add an API data source to the design.

!firefox_ebkICMVoVf.jpg (https://support.optisigns.com/hc/article_attachments/43051537966355)

Scroll down to where it says **"API Gateway Collection"** and click it.

!firefox_mCdtjleFse - Copy.png (https://support.optisigns.com/hc/article_attachments/31936613189523)

You can also set up a one-time Gateway with the *API Gateway* command if you need a one-off design with no pre- or post-request processing. In our example, however, we are, so we'll use Gateway Collection.

You should see this screen:

!firefox_xXJk2r7wuv - Copy.png (https://support.optisigns.com/hc/article_attachments/31936613193747)

* **Name -** The name of the DataSource. This is internally facing and will not be shown on your screens.
* **Select APIs -** Here you'll select from the API Gateways you've already set up in earlier steps. You can select just one, or multiple. If multiple are selected, the API DataSource will automatically aggregate them.
* **Update Interval -** How often to send requests back to the API for updates. Select from None (never call the API back), 30 minutes, 60 minutes, or every 6 hours. If you Enable WebHook on your API Request and input the provided URL in your API, this Update Interval will change to near real-time.

Hit **Save**, and the DataSource is created.

It should appear in the left column under **"Used in this design".**It will definitely appear in the **"Other DataSources"** section. You may need to refresh the page for it to appear.

![](https://support.optisigns.com/hc/article_attachments/31937799814163)

### Element Mapping

Now that you've got your API DataSource has been created, we're ready to map the data. In this example, we will show you how to make a DMB with the ability to strike through product names and display the phrase "SOLD OUT" when the item is out of stock.

#### Adding Text Elements to a Digital Menu Board

First, create your design. You can create your menu within our Designer app.

!firefox_g87oDmb7i3.jpg (https://support.optisigns.com/hc/article_attachments/43051537968787)

The easiest way to set up a DMB is with a **Data Repeater**. For a full breakdown of a Repeater's capabilities, see this article (https://support.optisigns.com/hc/en-us/articles/29217646663187). Here, we'll stick to teaching how to add information from your POS system.

To set up a Repeater, click **"Repeaters" → Add Blank Repeater**.

![](https://support.optisigns.com/hc/article_attachments/43051537970195)

With the Repeater selected, click **Settings**. Then select **Connect to DataSource** on the Side Menu.

!firefox_yX20kMKstf.jpg (https://support.optisigns.com/hc/article_attachments/43051537971219)

Select the DataSource you set up in the last set under **"Other DataSources"**.

You'll be taken back to the last pane with your DataSource now selected. Now, click **Edit** or double click the selected Repeater to head to the Repeater Editor. This is like a design-within-a-design, specifically for your Repeater (menu) items. With text selected, click the arrow on the left.

![](https://support.optisigns.com/hc/article_attachments/32078326973331)

That brings up the DataSource tab. Click on the DataSource Used in this Design and you'll see something like this:

![](https://support.optisigns.com/hc/article_attachments/31968058948371)

In this example, we want to display the name and the price, with the possibility of saying "SOLD OUT"

By creating text and dragging data points to it, we can create a menu item like this:

![](https://support.optisigns.com/hc/article_attachments/32060268861331)

This was created by finding data points from the API and dragging them into the desired text boxes. In this case, we only wish to display the "name" and "price," so those values were what we dragged into a blank or existing text box.

If your numbers need extra formatting, click on the number, then hit **Settings.**

**![](https://support.optisigns.com/hc/article_attachments/32077278901139)**

Click **Advanced Options →** **"Display Format"** and choose **"Number,"** then click **"Number Format"** and select the formatting you'd like. This will allow you to add dollar signs to your prices, with other options.

!ShareX_q0ybaobi0E.png (https://support.optisigns.com/hc/article_attachments/32060268867859)

Make sure to hit **Update** to make your new number format display.

!mraS5gfp1n.png (https://support.optisigns.com/hc/article_attachments/32060273056019)

The value of a repeater is that it will copy the format of this one cell, then replace the data points with others from your API. Done correctly, your menu should look something like this:

![](https://support.optisigns.com/hc/article_attachments/32077278906643)

The Repeater will pull as many data points as you have set up on your API. In this example, we've made a menu with 9 items, but with proper design you can put as many items as you'd like, with dynamic descriptions as well. If you have more items than what you've set to show on your screen at any one time, the items on the menu will rotate through them until they have all displayed.

#### Creating Strike Throughs and Sold Out Warnings

In the above example, we show a Sold Out warning. However, we don't want to display that all the time - only when the item isn't available. With OptiSync, this can be accomplished thanks to the Post-request processing we did earlier. Our code created this **"soldout: 0"** data. This is tied to our **"available"** data:

![](https://support.optisigns.com/hc/article_attachments/32077278913043)

When the "available" data reads "true," the "soldout" data reads 0. When your POS system detects items are unavailable, the "available" data will read "false". This will make the "soldout" data read 1.

We can use this knowledge to set up our Sold Out warnings and strike throughs to only appear when items are not available.

Going back to our Repeater Editor, we can click on a piece of text we want to strike through and hit **Settings**:

![](https://support.optisigns.com/hc/article_attachments/32077293399315)

In the Settings tab, hit **Advanced Options**.

![](https://support.optisigns.com/hc/article_attachments/32077801189779)

Under Advanced Options, hit **Property Mapping**.

![](https://support.optisigns.com/hc/article_attachments/31968071408915)

Two values will show up: **Property** and **Value**.

![](https://support.optisigns.com/hc/article_attachments/31968059040275)

Under Property, choose **Linethrough**.

![](https://support.optisigns.com/hc/article_attachments/31968450832915)

Under Value, choose **.soldout.** Before the "." will be the name of your API Request.

**![](https://support.optisigns.com/hc/article_attachments/32077293403411)**

This sets the text to be crossed out when the "soldout" data reads 1.

We can repeat this with the Sold Out reading, except instead of Linethrough, choose **Visible**.

![](https://support.optisigns.com/hc/article_attachments/31968463038227)

This will make the Sold Out text only appear when the "visible" data reads 1 - in other words, when your product is sold out.

Your final menu ought to look something like this:

![](https://support.optisigns.com/hc/article_attachments/32077820105875)

Finally, you're ready to Name and **Save** your Design.