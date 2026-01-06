Article URL: https://support.optisigns.com/hc/en-us/articles/33382537925267-Making-a-Video-Wall-with-OptiSigns-Video-Wall-App
Topic: Making A Video Wall With Optisigns Video Wall App

## Setting Up a Video Wall App

To use a video wall, you’ll need to set it up through the Video Wall app. To do that, navigate to **Files/Assets → Apps**, then select **Video Wall Content**:

**!picture of several app options within optisigns web browser with arrow pointing at Video Wall app (https://support.optisigns.com/hc/article_attachments/33382537891219)**

You’ll be prompted to select the number of screens and their orientation:

![](https://support.optisigns.com/hc/article_attachments/40326717838739)

|  |
| --- |
| **NOTE** |
| **4 Screens**are only available using the **OptiSigns ProMax Player.**The regular Pro Player can handle 2 or 3 screens. |

Once selected, you’ll have a couple options: you can build a basic video wall, or create a continuous one.

---

### Creating a Basic Video Wall

To create a basic video wall, select the number of screens and their orientation. Once you’ve done so, you’ll see the following:

!open video wall app with zone options on left and screen layout on right (https://support.optisigns.com/hc/article_attachments/33382521810835)

Notice that each screen is known as a **Zone**, mapped to the HDMI ports on your OptiSigns Pro Player. Make sure your screens are arranged in the order displayed here, as it cannot be changed.

There are a few options to note:

**Name** - The name of your Video Wall App.

**Zone Name** - The name of the designated zone. Depending on which option you picked, there will be two or three zones. These default to the name of the HDMI port on the OptiSigns Pro Player.

**Type** - The Type of content to display. You’ll choose from **Asset**, **Playlist**, or **Schedule**, then choose the piece of content you want to display.

Clicking the **Gear** icon will lead you to this screen:

!picture of video wall configs menu with audio zone and primary zone options (https://support.optisigns.com/hc/article_attachments/33382521817235)

**Audio Zone** - Lets you choose which screen the audio will come from. This can be **All**, or any one of the **HDMI ports**you've assigned a screen to.

**Primary Zone** - Setting one of your screens as a Primary Zone will provide a better experience or smoother content transition when you need to coordinate contents in different zones and put use the video wall app in a playlist.

* For example, if the primary zone is utilizing Playlist A, Playlist B and its video wall asset will respect the duration of Playlist A's asset. It will only transition to the next item when the asset in the Primary Zone's playlist is complete, rather than follow the duration setting of the video wall asset placed in Playlist B. This is a great way to avoid videos being cut off early.

For more information on these zones, see our guide on Advanced Playlist Item Playback Control and Campaign Management. (https://support.optisigns.com/hc/en-us/articles/22474034993043-Advanced-Playlist-Item-Playback-Control-Campaign-Management)

Should you choose content and assign it to your screens in this way, your video wall will function almost like a split screen, with each screen displaying different content or repeating images:

!example of a multi-zone video wall, 2x1 (https://support.optisigns.com/hc/article_attachments/33382521820819)

---

### Merging Screens to Create a Continuous Image or Video

To create one continuous image, the screens will need to be merged.

To do this, click the **Merge Screens** button:

!image of 3x1 video wall with arrow pointing at merge screens button (https://support.optisigns.com/hc/article_attachments/33382537910675)

Then, select the screens you’d like to merge:

!image with two of three screens selected and an arrow pointing toward merge option (https://support.optisigns.com/hc/article_attachments/33382537912083)

These two screens will now be merged, and considered the same Zone:

!image of one larger screen next to a smaller screen to represent two merged zones (https://support.optisigns.com/hc/article_attachments/33382521823891)

You can continue merging screens if you have a third to create a video wall that looks like the image below, with one continuous image.

!optisigns three screen video wall displaying mountains and a lake (https://support.optisigns.com/hc/article_attachments/33501752188563)

In order to unmerge screens, select the merged screens, hit the **Merge Screens** button again, then hit the two arrows going out from each other:

!image showing arrow pointing toward unmerge screen option (https://support.optisigns.com/hc/article_attachments/33382521829907)

This will separate the screens into separate Zones once again.

Once you’ve finished setting up the Video Wall app, hit **Save**. This will store it as an Asset. As an Asset, you can push it to a screen directly, add it to a Playlist, or schedule it to play at any time.

---

### Creating Custom Resolutions

Sometimes, you might have an unusual resolution, or want to chain multiple screens together to register as a single screen.

To support this, it's possible to input a custom resolution. Here's how.

First, find your Pro Player screen with the Video Wall add-on applied. Go to **Advanced** → **More** → **Video Wall.** You may need to activate it. When activated, this will appear:

![](https://support.optisigns.com/hc/article_attachments/47300715377555)

Click **Change**, then hit any option. A resolution should be displayed, like this:

![](https://support.optisigns.com/hc/article_attachments/47300715380883)

To input a custom resolution, simply replace the numbers in the box with the resolution you would like to display.

---

### Forcing Rotation to Portrait or Landscape

If you have a non-standard video wall setup, you may wish to force the display to either Portrait or Landscape mode. To do this, find your Pro Player screen with the Video Wall add-on applied. Then, go to **Advanced** → **More** → **Video Wall.** You may need to activate it. When activated, this will appear:

![](https://support.optisigns.com/hc/article_attachments/47300715377555)

Click **Change**, then hit any option. Your chosen resolution should be displayed. Then:

**For Portrait:**

Append ":P" to the end of the resolution string:

![](https://support.optisigns.com/hc/article_attachments/47300715383699)

**For Landscape:**

Append ":L" to the end of the resolution string:

![](https://support.optisigns.com/hc/article_attachments/47300715387027)

Your video will now display in the requested mode.

---