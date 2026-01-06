Article URL: https://support.optisigns.com/hc/en-us/articles/32860569148819-How-to-Set-Up-a-PowerBI-Service-Principal-for-Use-in-OptiSigns
Topic: How To Set Up A Powerbi Service Principal For Use In Optisigns

Article URL: https://support.optisigns.com/hc/en-us/articles/32860569148819-How-to-Set-Up-a-PowerBI-Service-Principal-for-Use-in-OptiSigns
--- DOCUMENT START ---

# How to Set Up a PowerBI Service Principal for Use in OptiSigns

### In this article, we will walk you through the process of setting up a service principal for PowerBI in Microsoft Azure, and connecting it to OptiSigns.

* [Creating an Entra App in Microsoft Azure](#Create)
* [Enable PowerBI Service Admin Settings](#Enable)
  + [Add the Service Principal to a Workspace](#Add)
* [Authenticating OptiSigns via Service Principal](#Auth)
* [Getting PowerBI onto a Screen](#Get)

Using a PowerBI service principal with app registration is a preferred option for companies with strict information security rules that don't want to use individual user accounts for PowerBI integration.

This reduces headaches in situations when:

* There is a position or permission change of a user and authentication needs to be performed again by a different user.
* A prolonged authentication token period cannot be set for individual users, and you will need to reauthorize and refresh the token every couple of months.

Using a PowerBI service principal, the authentication tokens are associated with a registered app instead of a user. This allows you to set a longer validity time for the authentication token and avoids more frequent re-authorization. Using service principal with App registration for Power BI integration is supported well with OptiSigns.

|  |
| --- |
| **NOTE:** This feature is only available to customers on an **Enterprise** plan. |

---