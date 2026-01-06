Article URL: https://support.optisigns.com/hc/en-us/articles/32839794222099-Display-Salesforce-Dashboards-with-MFA-using-Web-Scripting
Topic: Display Salesforce Dashboards With Mfa Using Web Scripting

## Setting Up MFA

|  |
| --- |
| *If you don't already have MFA set up for your Salesforce account, please visit their support article: **Multi-Factor Authentication for Salesforce Orgs. (https://help.salesforce.com/s/articleView?id=sf.security_overview_2fa.htm&type=5)*** |

Next, go to your account settings > My Personal Information > Advanced User Details

From there, click **"Connect"** on "**App Registration: One-Time Password Authenticator**"

!Salesforce account settings and setting up authenticator app (https://support.optisigns.com/hc/article_attachments/35528791304211)

When Salesforce prompts you to connect an Authenticator App, **DO NOT** immediately scan the QR code.

Click "**I Can't Scan the QR Code**".

!Salesforce setting up authenticator app. Select 'I can't scan the QR code' (https://support.optisigns.com/hc/article_attachments/35528807336979)

**Copy and paste the alphanumeric string** displayed underneath "Key". **Save this key** somewhere secure, like the Notepad app.

* This is ***necessary*** for the web scripting process later.

Next, enter that setup key in your authenticator app, then enter the verification code into Salesforce, and connect!

!Save the setup key that Salesforce provides you. (https://support.optisigns.com/hc/article_attachments/35528807340691)

**Your MFA is now set up!**

---