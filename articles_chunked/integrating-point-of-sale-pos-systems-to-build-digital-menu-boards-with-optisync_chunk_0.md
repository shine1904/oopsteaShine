Article URL: https://support.optisigns.com/hc/en-us/articles/31860170199955-Integrating-Point-of-Sale-POS-Systems-to-Build-Digital-Menu-Boards-with-OptiSync
Topic: Integrating Point Of Sale Pos Systems To Build Digital Menu Boards With Optisync

Article URL: https://support.optisigns.com/hc/en-us/articles/31860170199955-Integrating-Point-of-Sale-POS-Systems-to-Build-Digital-Menu-Boards-with-OptiSync
--- DOCUMENT START ---

# Integrating Point-of-Sale (POS) Systems to Build Digital Menu Boards with OptiSync

### OptiSync allows you to create dynamic digital menus through API integration. Your POS systems can interface directly with OptiSigns to automatically update prices, track inventory, and more.

* [How to Integrate POS Systems Through API Requests](#Section%201)  
  + [Get API URL Endpoint and Set Up API Request DataSource](#Section%202)
  + [Additional Information on API Authentication](#Section%203)
  + [Handling Multiple Stores or POS Locations](#Section%204)
  + [How to Use Post-Request Processing to Convert API Data](#Section%205)
* [How to Build Digital Menu Boards in Designer with OptiSync](#Section%206)  
  + [Using DataSources and Repeaters](#Section%207)
  + [Element Mapping](#Section%208)  
    - [Adding Text Elements to Your Menu](#Section%209)
    - [Creating Strike Throughs and Sold Out Warnings](#Section%2010)
* [Pushing a Digital Menu Board to a Screen](#Section11)

In this article, we will create a real Digital Menu Board (DMB) integrated with a Clover POS system. The DMB pulls product info from Clover and display it onscreen. When an item is not available, it will display as "SOLD OUT."

|  |
| --- |
| **NOTE** |
| API Integration is only available with a **Pro Plus** plan or higher. |

---