# python---challenge
Module 3 Due Monday by 11:59pm

Pybank:
  I first started off with importing what we have been doing in class. Then I added the os.path.join and tried to open it. It took a while since I initially had "..","Resources", "budget_data.csv" which was giving me an error. I figured out that the ".." indicated to go back in the parent directory and that I didn't need it anymore.  I then went to trying to find the total number of months included in the dataset which I was figuring I would need the len() function. After trying to figure it out I couldn't find why so I ended up putting that question into google. It became apparent to me that I could find the homework for this course from others on GitHub who had taken the class before. I figured I might want to use them as reference if I was really stuck but I went to https://www.chegg.com/homework-help/questions-and-answers/task-create-python-script-analyzes-records-calculate-following-values-total-number-months--q116921602 which ended up being the same as those GitHub links. I looked at the code to see where I was going wrong though and figured out that I needed to create a list by doing = [] and then I could add things to that list by .append. Then I just needed to make a for loop to run though the first column excluding the header, since that is not a month. This made my len() function work and I was able to get the answer printed. Looking back on the activities in class I did come across the census_solution.py in lesson 3.2 which did this as well.
  I then worked on summing the second row. I figured I would need to specify that the second row are numbers and since they are integers I knew we used the int() function in class and I would probably need it. I started by repeating the process and doing another for loop but I kept getting 0 for the answer. I noticed that that website had them together and so I did that and that fixed my problem.
  The first thing I though about doing for this task is using an average function. I imported the mean from the statistics function but I was not getting anywhere close the the correct answer. I then realized that they were looking for the difference from month to month so I knew I would need a x - (x+1) type of deal like we did for the VBA script, though that was checking if they weren't equal. I created an empty array again and appended that difference in the variable amount. Then I would just have to use sum()/len() to get the average change every month.
  For the max and min change in a month I just had to do the max of that list of the difference of months stored as amount. The real challenge was trying to get the month of that increase and decrease. How to get back the month this happened I didn't really know how to do. I noticed they used index which I do remember using in class. After looking back at the activities it seems house_of_pies_bonus_solution.py in lesson 3.2 used this as well. Looking into it more I was able to understand that amount (the change in months) indexed for either the max or min amount. Then I would need the upper bound for the month change. Then tying everything back to the months variable that was based on the months column let me get that correct month for both.
  The last part was easy, I just googled how to write a file in python and how to get a new line from these two sites: https://www.w3schools.com/python/python_file_write.asp and https://www.freecodecamp.org/news/print-newline-in-python/#:~:text=Using%20the%20escape%20character%20%5Cn,use%20a%20different%20escape%20sequence.

PyPoll
  https://www.javatpoint.com/numpy-unique for getting the unquie values of a column.
  https://www.guru99.com/python-list-count.html#:~:text=Summary-,The%20count()%20is%20a%20built%2Din%20function%20in%20Python,method%20returns%20an%20integer%20value for counting.
