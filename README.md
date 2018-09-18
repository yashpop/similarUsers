# similarUsers
This project is related to [PluralSight](https://www.pluralsight.com/) and has all rights reserved.

## Recommendation Systems

It is very important in current scenario to recommend the products to users or users to products or even users to users (for networking, colloborations) and products-products (for product cateegorization and deals/ofers).

- This project is for the User-User recommendation

## Final application - Process followed (other than different explorations done)
1. Every users have many **interests** - so explored this
2. **Correlation** is the main key to understand how well users have similar interests
3. All users who follow might not take the **assessment** , and who took assessment might not succeed
4. Created a simple **Flask** application
  - Asks for an integer input of user_id/user_handle
  - Has to be a maximum of 5 digits
  - takes in the user_id and returns a tabular structure of similar users
5. The model currently runs based on the course_viewed and assessement taken along with courses_available


# Data discovery
To understand about the, data, data mining and inferential statistics are important. So Key findings are :

  - Courses that users were interested are all available in the course_tag dataset
  - Few assessments that were taken are not in the original course_tag dataset
  - The highest possible number of views or possible subscriptions to courses was around 833
  - The least number of interests/subscriptions = 1
  - 50% of the people were atleast interested in 5 courses
  - The maximum marks observed was around 300 = mean+~3*sigma*
  - Some Courses didnot have the course_tags

# Further implementation, drawbacks for the current system
1. Current model runs the entire algorithm on the fly - Time constraint
  - This can be dealt easily in case of ston=ring the analyzed documents into a DB,
  - so whenever user is chosen, immediate results are directly queried from the DB
  - For large scale we can use Teradata, Hive, Spark processing
2. System works well if the user has taken the assessment also
  - For new users the same recommendation can be done if the user has expressed some interests and subscribed for some courses
  - For completely new users the recommendations can be given based on the user interests alone
  - If the user doesnt even have the interests data, then we can recommend most popular and least popular **both** sets
    - Further this can be improved based on feedbacks


*time taken: 8 hours*

# How to run the file
- **requirements**
  - 4GB RAM, Python 2.7 or recent
  - Data files in respective paths as specified
- Install python
- Create virtual environment of python in Pluralsight folder/directory
  - python virtualenv <env_name>
- run pip requirements.txt
- run *flask run*
  - This creates the virtual host running in local machine
- open browser and type localhost:5000/index
- enter a user id number
- watch the result (takes 1 minute)
  
