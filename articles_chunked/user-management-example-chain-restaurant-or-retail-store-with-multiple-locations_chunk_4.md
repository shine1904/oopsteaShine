Article URL: https://support.optisigns.com/hc/en-us/articles/43657735780627-User-Management-Example-Chain-Restaurant-or-Retail-Store-with-Multiple-Locations
Topic: User Management Example Chain Restaurant Or Retail Store With Multiple Locations

## Set Up Folder-Level Security

Now that we’ve made our Teams, it’s time to set up Folder Level security. We only want to grant access to screens that the users on the Team will actually use, and no more.

To do this, go to your **Screens** tab. Find the Folder you want to set permissions for. In this case, we’ll start with the **Pacific** folder at the top of the structure. Click the **Three Dots →  Change Permissions:**

!find change permission tab on folder (https://support.optisigns.com/hc/article_attachments/43657783484051)

The **Change Security** screen will appear. Click underneath where it says “Everyone on this team” and a list of Teams will appear. In our example, we’ll choose the **Pacific Region** team.

!how to change security permissions (https://support.optisigns.com/hc/article_attachments/43657783485715)

Now only the Pacific Region Team and the Default Team will have access to this folder. You can also choose whether to make this Folder and its subfolders Editable or View-only:

!edit and view permissions for folder (https://support.optisigns.com/hc/article_attachments/43657783486099)

Any folders created inside a folder will automatically inherit its permissions. However, if you’ve already created a folder and then change the parent folder permissions, those child folders will not inherit them.

### Complete Folder-Level Security Example

OptiSigns uses a top-down setup, meaning that the highest-level folders will need the most Teams with permissions.

To illustrate this, let’s go back to our example. Here is a partial nested setup:

!complete folder nesting setup (https://support.optisigns.com/hc/article_attachments/43657735762323)

Each layer will require fewer and fewer permissions. For example, here is the permission structure we’d want for the **Pacific** folder:

!regional level folder permissions example (https://support.optisigns.com/hc/article_attachments/43657783490451)

Note how ***every Team operating in the region*** has permissions for this folder.

As we go deeper into the nesting, we can eliminate teams that do not need certain permissions. For example, here are the Teams needing **California** folder permissions:

!state level folder security example (https://support.optisigns.com/hc/article_attachments/43657735765779)

Notice how we’ve filtered out the other State-level teams. This means that members of the Oregon or Washington teams will be able to enter the Pacific folder, but would ***not even see*** the California one.

Going a step further, here are the City/County level permissions we’d want on the **Los Angeles** folder:

!city level folder security example (https://support.optisigns.com/hc/article_attachments/43657783497363)

Here, we’ve filtered out Eagle Mountain (the other city-level team we’ve set up), but kept all the teams corresponding to Los Angeles area store locations. Going down to the **Cosmos Space Center** folder will complete the picture:

!store location folder security example (https://support.optisigns.com/hc/article_attachments/43657783497875)

All the other store locations have been filtered out. If we were to look at another store location, we’d exchange the Cosmos Space Center team for the team corresponding to that store. This way, the people assigned to the lowest level teams will only have access to the single folder that applies to them, but members of “higher level” teams will be able to see all the stores in their respective level.

|  |
| --- |
| **NOTE** |
| Another option: it is possible to restrict folder access to users within the Default Team. This is a good option if you want your regional managers to have more access. |

This can be applied across OptiSigns, and it is possible to create similar nesting within the **Files/Assets**, **Playlists**, and **Schedules** area of the Portal:

!add folder in files/assets area (https://support.optisigns.com/hc/article_attachments/43657735771923)

!add folders in playlist and schedule area (https://support.optisigns.com/hc/article_attachments/43657783499411)

For simplicity, we recommend mirroring the same setup in each of these areas. This way, higher-level teams can share content, playlists, or schedules with many lower-level teams, but lower-level teams cannot share with each other.

Lastly, when creating a New Folder, these permissions can be set by clicking the **Advanced** button:

!new folder advanced opened (https://support.optisigns.com/hc/article_attachments/43657783500051)

---