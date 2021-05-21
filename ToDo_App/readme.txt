5/19/21- Ashley
------------------------------------------------
make sure virtual env is active
cd into the project folder
install this in terminal: pip install google-api-python-client

superuser created
username: admin
password: adminpassword

username: johndoe
password: adminpassword

username: sallysue
password: adminpassword


5/20/21- Ashley 
-------------------------------------------------
Forgot to create branch but I hadn't done anything yet besides delete what I thought was an extra folder in the templates folder (which i ended up putting back LOL) Went ahead and pushed it to master. Then created a branch  named ashley

updated task_list.html
created DetailView, CreateView, DeleteView, UpdateView, FormView
created more templates
created/completed login/registration with templates

*I noticed he had in the Task model "complete" and you put "status"- I do think status is better but that will need to be changed eventually to a charfield as a booleanfield would not make sense but we can update that when its necessary. I'll leave it for now. 

created another user in the admin panel so you could see different accounts to compare- login info listed above below the superuser login info; created another user sallysue to test registration- info up above as well

Left Off at 1:32:10 in the youtube video- at this point the login/registration is up and running, as well as view task detail, edit and delete functions. 

5/21/21- Ashley
I added the grocery list templates- basically made it the same as the tasks list. Ideally, I think the complete "button" should be on the front side and not have to go into the "update"form just to check it. And also ideally, I'd like to add items to the list without having to redirect to the page where you add an item. That would be time consuming. So I'll try to figure out how we can do that. 

I updated some CSS...I thought it might be nice to stick with that gradient feature and just let each tab be a different color. 

I think I might have messed up the container or something somehow...The colored box at the top is not the full width of the app but we can figure that out later as well.

I'm not entirely sure how we should do the meal planner tab...I was just wanting it to be pretty simple...Where it's a list of the week days, like this: 
Sunday: Write a meal here
Monday: Spaghetti w/ Salad
Tuesday: Steak and Broccoli
Wednesday: etc..
Thursday:
Friday:
Saturday:

It's like a hidden text box where they can write in what they want to eat for that day. I didn't want to make it complicated where they have to choose from a recipe box or anything like that- although that is maybe something that could come later. I purposefully wanted this to specifically be something to just input what you're planning on making. What do you think? or if you have a better idea..i'm all ears.

Lastly, my nav bar is supposed to only highlight the tab that's clicked. Only the Tasks and the Grocery list tabs are workable right now. but you should see that when you click on Grocery list- the tasks tab stays highlighted. I had it working at one point and I'm not sure what I did wrong so I'll have to figure it out. If you have time and want to- you can go to bootstrap website and find their nav and tabs components to read about it and see what I did= that's where I got the code from. 

Sorry my notes are so long! Let me know if you need anything else. 





