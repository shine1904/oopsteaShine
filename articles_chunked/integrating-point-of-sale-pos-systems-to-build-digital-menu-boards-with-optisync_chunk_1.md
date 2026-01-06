Article URL: https://support.optisigns.com/hc/en-us/articles/31860170199955-Integrating-Point-of-Sale-POS-Systems-to-Build-Digital-Menu-Boards-with-OptiSync
Topic: Integrating Point Of Sale Pos Systems To Build Digital Menu Boards With Optisync

## How to Integrate POS Systems Through API Requests

Most POS systems have an API library which OptiSigns can use to get the relevant data from the system programmatically. This API can return menu items, item price, availability, and more.

With OptiSync, we can link APIs to the OptiSigns portal and push the data to screens as a Digital Menu Board (DMB) or any other type of screen you'd like without the need of human intervention.

!api optisigns integration diagram (https://support.optisigns.com/hc/article_attachments/31860108901523)

This article will focus on these POS specific wrinkles, and the process of mapping POS data to assets and pushing them to screens.

|  |
| --- |
| **IMPORTANT** |
| In order to integrate a POS system, you'll need to first set up an API Gateway request. A complete guide for how to do that can be found here (https://support.optisigns.com/hc/en-us/articles/22875592994195-How-to-Integrate-API-and-Publish-API-Data-via-OptiSync). |

---

### Get API Endpoint URL and Set Up API Request DataSource

We have a comprehensive guide (https://support.optisigns.com/hc/en-us/articles/22875592994195-How-to-Integrate-API-and-Publish-API-Data-via-OptiSync) on how to set up your API gateway request. We recommend following this guide until your initial request is set up.

Bare minimum, you'll need an API endpoint URL and an API Authentication token.

### Additional Information on API Authentication

For most token based authentication, setting up the authentication token with the key store is normally all that's required for an API request. But certain APIs (such as Toast) will require additional calls to get the authentication token for each request, this can be handled through pre-request processing. To see how to handle that, see our article on Toast APIs (https://support.optisigns.com/hc/en-us/articles/31113088917907-How-to-use-Toast-API-data-with-OptiSigns).

### Handling Multiple Stores or POS Locations

Once you've got your basic API Gateway request set up, there are a few additional steps you'll want to perform if you have multiple locations for your screens. These different locations may have different menus, or different specials for that day, or even different pricing depending on various factors.

POS systems normally require separate license for each location. Your POS system API may provide different store ID in the API endpoint or using different authentication token. For larger deployment with multiple stores, you can use substitution parameters to handle that with OptiSigns.

There are two ways to handle multiple POS locations:

1. Set up individual API requests for each of your POS locations, changing the value in the URL endpoint each time and mapping them to each of your screens individually. If you only have a few locations where your POS system is used, this will work just fine.
2. *(Recommended)*Configuring each screen to send its storeID to the API call, allowing a single API request to provide data to multiple screens. For anything more than two or three screens, we recommend this method.

Here's how to handle option 2.

To get started, find the screen you wish to edit.

!edit screen (https://support.optisigns.com/hc/article_attachments/31893086724755)

Click **Advanced** **→** **More** **→** **Device Additional Attributes.**

!device additional attributes on edit screen (https://support.optisigns.com/hc/article_attachments/31893080684563)

Two fields will show up, **Key** and **Value**.  
!device additional attributes key value (https://support.optisigns.com/hc/article_attachments/32043124363155)

* **Key** - A parameter that will be used during the API call to substitute for your store's value. This will replace part of your API URL endpoint.
* **Value** - Represents the unique code associated with the store or location you wish to pass through to your API.

In this example, we'll pretend the parameter you are changing is called "merchantID". The value inputted will need to be obtained on your end as it will be unique.

Now, go back to the API request config page. Substitute the merchantID in the API endpoint with the Key name you previously defined.

#### **clover url request**

When the API request is triggered on the device, it will take the value from the device and substitute it at runtime. For each screen, you'll want to perform these same steps, keeping the Key name the same while changing the Value. This will allow you to push different data to different screens off a single API Request.

### How to Use Post-Request Processing to Convert API Data

When retrieving data from your POS system, it may not initially show up exactly the way you'd like, or you might want to add some functionality, such as the ability to display SOLD OUT for items out of stock.

For example, prices may display as whole numbers (i.e. 1299 instead of $12.99). That's where the "Post-request" tab comes in - this allows changes to be made to the data after it comes in. This will require some basic coding to use.

Take the example of the price display from earlier. How would we convert a number like 1299 to display as $12.99, and make that piece of code extensible to any similar display errors (e.g. 1899 instead of $18.99)?

![](https://support.optisigns.com/hc/article_attachments/31893086743187)

For this common example, this piece of JavaScript code should solve your issue.

```
let {data, headers, status} = os.context.get("response");  
temp_data = data.elements  
for (let object of temp_data) {  
        object.price = '$' + (object.price*.01);  
        if (object.available == true)  
              {object.soldout=0;}  
            else {object.soldout=1;}  
    }  
return temp_data
```

This will fix the returned data, allowing it to display properly. It will also allow for creation of SOLD OUT and strike through for when items are out of stock.

![](https://support.optisigns.com/hc/article_attachments/32060273039763)

|  |
| --- |
| **NOTE:** Enabling and configuring a WebHook allows near real-time updating of the data pulled from your API. If you plan to keep track of store inventory using your digital signs, we recommend setting one up. You will need to input the provided WebHook key into your API to set this up. |

 

---