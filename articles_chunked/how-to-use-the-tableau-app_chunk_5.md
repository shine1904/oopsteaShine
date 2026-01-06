Article URL: https://support.optisigns.com/hc/en-us/articles/39250660729747-How-to-Use-the-Tableau-App
Topic: How To Use The Tableau App

## Additional Notes

#### Note 1

Content display may vary based on device type and screen resolution.

#### Note 2

**If your workbook contains broad views:**

* + - Create Custom Views on the Tableau site and use the Custom View's URL as the Shared Report URL.![](https://support.optisigns.com/hc/article_attachments/39597853568787)
    - Set the View Size to either **Fit Width**, **Fit Height**, or **Entire View**:  
      ![](https://support.optisigns.com/hc/article_attachments/39597827704979)

#### Note 3:

Tableau currently limits (https://help.tableau.com/current/online/en-us/to_site_capacity.htm) its maximum number of refresh requests to 600 per hour/user. This means you'll want to be careful on how you set the "Update Interval," especially if you have numerous devices wanting to display Tableau reports.

We have several recommendations on how to handle this with multiple devices:

1. Set the Update Interval to match the number of devices. For example, if you have 50 devices, you can have a maximum Update Interval of 5 minutes (300 s) for a single report. With more devices this Update Interval will need to be longer, with less, it can be shorter.
2. For using Reports in a Playlist, the Report will update each time it is played. You'll need to set the proper duration, factoring in the number of reports and the number of devices. For example, if you have 10 reports on a single playlist across 5 devices, you can have a Playlist duration of 5 minutes (300 s).
3. To scale beyond these limitations, you'll need to create more connected apps under different Tableau Cloud users. Each Tableau Cloud user will have 600 requests an hour.

### That’s all!

OptiSigns is the leader in digital signage software (https://www.optisigns.com/). If you have any additional questions, concerns or any feedback about OptiSigns, feel free to reach out to our support team at support@optisigns.com (support@optisigns.com).

--- DOCUMENT END ---
For more details, please visit: Article URL: https://support.optisigns.com/hc/en-us/articles/39250660729747-How-to-Use-the-Tableau-App