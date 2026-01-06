Article URL: https://support.optisigns.com/hc/en-us/articles/39250660729747-How-to-Use-the-Tableau-App
Topic: How To Use The Tableau App

## Step 1: Set Up OptiSigns as a Connected App in Tableau Cloud

To view Private reports in OptiSigns, it needs to be set up as a **Connected App** in Tableau Cloud. If you’re only interested in displaying Public reports, this step can be skipped - however, we ***highly recommend*** it, as setting up this integration will allow you to use it for any future reports you want to display from this account. If you are only interested in displaying Public reports, though, feel free to [skip to step 3](#Step3).

To begin, find your **Settings** tab within Tableau. Once there, click **Connected Apps** → **New Connected App**.

!new connected app tableau (https://support.optisigns.com/hc/article_attachments/39250613919635)

Select **Direct Trust**.

!direct trust dropdown tableau (https://support.optisigns.com/hc/article_attachments/39250613922451)

You’ll open the Create Connected App window. Here, you can give your connected app a name (we recommend “OptiSigns” so you know it’s for us), restrict its access, and provide allowed domains. For the purposes of this example, we’ll apply it to “All projects” and “All domains.”

!create connected app window tableau (https://support.optisigns.com/hc/article_attachments/39250613923987)

Once created, it will appear in a list of Connected Apps. Select the app.

On this screen, you'll want to **Enable** the OptiSigns app by hitting the **Three Dots**. Then, you'll want to hit **Generate New Secret**:

!Screenshot 2025-03-22 at 5.27.26 PM.jpg (https://support.optisigns.com/hc/article_attachments/39672709375507)

The blurred out values are your **Secret ID, Secret Value, and Client ID**. These values will be critical to setting up your integration with OptiSigns, so keep this tab open.

With this information and the app Enabled in Tableau, we can configure the integration in OptiSigns.

---