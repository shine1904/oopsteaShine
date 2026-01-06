Article URL: https://support.optisigns.com/hc/en-us/articles/32860569148819-How-to-Set-Up-a-PowerBI-Service-Principal-for-Use-in-OptiSigns
Topic: How To Set Up A Powerbi Service Principal For Use In Optisigns

## Enable PowerBI Service Admin Settings

Follow this link to the PowerBI Admin Portal (https://app.powerbi.com/admin-portal/capacities?experience=power-bi).

Once there, click **Tenant Settings**. Then, scroll down to **Developer Settings**.

!finding developer settings in tenant settings within powerbi admin portal (https://support.optisigns.com/hc/article_attachments/32860610420627)

Enable the **Embed Content in Apps Settings**, as below:

!how to enable embed content in apps (https://support.optisigns.com/hc/article_attachments/32860610421779)

In this example, we’ve set this embed to apply permissions to the entire organization. However, you can restrict access to specific security groups based on your needs. These security settings can be changed as per your requirements.

Next, **Enable Service principals can create workspaces, connections, and deployment pipelines** and **Enable Service Principals can call Fabric public APIs**, as below:

!image (28)(1).png (https://support.optisigns.com/hc/article_attachments/42225175622675)

Like before, we’ve applied these to the entire organization. Just like the last step, you can restrict access to specific security groups based on your needs.

### Add the Service Principal to a Workspace

Now we need to assign service principal access to the workspaces you want to show in your PowerBI reports.

In the admin portal, click **Workspaces**. You’ll want to go to the workspace you want to assign service principal access to. Click the workspace, then hit **Access**.

!how to grant service principal access powerbi (https://support.optisigns.com/hc/article_attachments/32860610425107)

Add the service principal you created in the last step as a member of the workspace.

!how to add service principal as a member of powerbi workspace (https://support.optisigns.com/hc/article_attachments/32860569093139)

---