Article URL: https://support.optisigns.com/hc/en-us/articles/38062664690195-Tagging-in-OptiSigns
Topic: Tagging In Optisigns

## Screen Tagging

Your screens can be tagged in much the same way as an asset. This has a number of different uses:

* Organizing numerous screens, by location, type of screen, etc.
* Grouping sets of screens together for quick pushes of assets or playlists
* Allowing Emergency Messages/CAP Alerts to appear on certain screens with specific tags
* Enabling Remote Commands to be able to alter the content displayed on multiple screens at once

You can add as many different tags as you want to a screen. Please note that these screen tags are separate from those tags you may have applied to your assets. For more information on tagging assets, see the [**Asset Tagging**](#AssetTagging) section later in this article.

To tag your screens, select the screens, then hit **Edit**.

![](https://support.optisigns.com/hc/article_attachments/38062664586387)

This will bring up the **Edit Group of Screens** tab.

![](https://support.optisigns.com/hc/article_attachments/38062664590355)

In the “Tags” section, you can click the field and you’ll be able to select from existing tags, or create a new one.

![](https://support.optisigns.com/hc/article_attachments/38062653681811)

### Pushing to Multiple Screens

The most commonly used feature of screen tagging is the ability to push content - be that an asset, playlist, or schedule - to multiple screens at once.

To do this, find the piece of content you wish to push, then click the **Three Dots**:

![](https://support.optisigns.com/hc/article_attachments/38062664596115)

This will open up the Options menu. Click **Push to Screens**. You’ll see the Push to Screens tab:

![](https://support.optisigns.com/hc/article_attachments/38062664602003)

Here, select the **Target** to say “Tags”:

![](https://support.optisigns.com/hc/article_attachments/38062664604691)

You can then select the Tags from your previously created Screen Tags.

![](https://support.optisigns.com/hc/article_attachments/38062653695891)

When done, hit **Push**. Your content will now display on any Online screens that have the tag you selected. This is a method OptiSigns uses to change what displays on numerous screens at once, and can be used to drastically speed up deployments.

### Tag Rules

With Tag Rules, it's possible to set a network of Tags for an Asset to display on.

For example, let's say you want an advertisement to play only in customer-facing screens, but only in certain locations. You can combine these screens into a single Tag Rule, then push content to only those screens.

To do this, select the **Target**to say **Tag Rules**on the Push to Screens tab:

!firefox_Cnp46Hnyhc.jpg (https://support.optisigns.com/hc/article_attachments/39406606002195)

Hit **New:**

**!firefox_GcChrnf831.jpg (https://support.optisigns.com/hc/article_attachments/39406610743827)**

This will bring up the Screen Tag Rule screen:

!rpA5cqMfxw.jpg (https://support.optisigns.com/hc/article_attachments/39406606004371)

Here, you have the ability to **Include**or **Exclude**certain tags using and/or logic commands. You can add **Rules**or **Rulesets**to make these as elaborate as you like:

!firefox_XiHCAOKT8K.jpg (https://support.optisigns.com/hc/article_attachments/39406606006547)

When you're ready to go, simply click on any Field and you'll be prompted to Add a tag via a dropdown menu:

!firefox_VwCzrxr0yH.jpg (https://support.optisigns.com/hc/article_attachments/39406606007699)

Now you're ready to include or exclude any tags you'd like. When you're finished, hit **Save**.

You'll then be able to select this Tag Rule on the Push to Screens tab, and use it across your assets.

### Tagging for Remote Commands

Screen tags can also be used by OptiSigns Remote Commands to send direct commands to multiple screens at a time. This can be anything from forcing an update to changing the content displaying on screen.

|  |
| --- |
| **NOTE** |
| Remote Commands can only be used by **Pro Plus** subscribers or above. |

For more information on how to send Remote Commands via tag, see our article on **Remote Command Execution** (https://support.optisigns.com/hc/en-us/articles/4408658251027-How-to-use-Remote-Command-Execution-Windows-Linux).

---