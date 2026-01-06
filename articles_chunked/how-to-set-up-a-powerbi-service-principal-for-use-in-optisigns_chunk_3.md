Article URL: https://support.optisigns.com/hc/en-us/articles/32860569148819-How-to-Set-Up-a-PowerBI-Service-Principal-for-Use-in-OptiSigns
Topic: How To Set Up A Powerbi Service Principal For Use In Optisigns

## Authenticating OptiSigns via Service Principal

In order to authenticate your PowerBI on OptiSigns via service principal, you’ll need four pieces of information:

1. Name of the service principal
2. Application (client) ID
3. Directory (tenant) ID
4. Application (client) secret

Since we’ve already created an Entra app in Azure, we already have access to the first three pieces of information. These can be found under **App Registrations** back in Azure.

!where to find app registration information in microsoft azure (https://support.optisigns.com/hc/article_attachments/32860569095571)

In this example, the values have been blurred, but on your Azure portal, these should be visible.

The only piece of information you won’t have is the client secret. To get that, click **Manage → Certificates & Secrets → Client Secrets → New Client Secret**

**!how to create new client secret in microsoft azure (https://support.optisigns.com/hc/article_attachments/32860569099411)**

Next, set the **Description** and **Expiry**, then click **Add**.

!how to add a client secret (https://support.optisigns.com/hc/article_attachments/32860569100947)

The **Value** present is the last piece of information you need.

Now, head into the OptiSigns app. Click your **Profile name → More → Integrations.**

!where to find integrations tab in optisigns (https://support.optisigns.com/hc/article_attachments/32860610434451)

A screen like the one below will appear. Click **Add Azure Service Principal.**

!how to add service principal in optisigns (https://support.optisigns.com/hc/article_attachments/32860569109011)

When the popup appears, collect the information mentioned above from Microsoft Azure and input it into OptiSigns. The values match up like this:

!inputting all the powerbi service principal information into optisigns (https://support.optisigns.com/hc/article_attachments/32860610442771)

Once all the information is input correctly, hit **Save**. Now your Service Principal is saved to the OptiSigns portal.

---