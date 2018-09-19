from __future__ import print_function
from app import app
from flask import render_template,flash, redirect
import pandas as pd
import numpy as np
import os
import webbrowser
from flask import jsonify


from forms import UserEntry

@app.route("/index",methods=['GET','POST'])
def index():
    form = UserEntry()
    if form.validate_on_submit():
        user_handle = form.user_handle.data
        #print(user_handle)
        a = Application()
        similar_users = a.retrieve_data(user_handle)
        if similar_users is None:
            return "Hello New User {}, please take our assessment at Pluralsight for better results".format(user_handle)
        else:
            flash("requested for user : {}".format(form.user_handle.data))
            return view_data_in_browser(similar_users)
    return render_template('index.html',title='Home',form=form)

@app.route("/display/<user_handle>",methods=['GET','POST'])
def display(user_handle):
    try:
        user_handle=int(user_handle)
    except:
        return jsonify(Error="Please make sure of user ID is number")
    a = Application()
    similar_users = a.retrieve_data(user_handle)
    if similar_users is None:
        return "New User : Hello New User {}, please take our assessment at Pluralsight for better results".format(user_handle)
    else:
        #flash("requested for user : {}".format(user_handle))
        return view_data_in_browser(similar_users)
    return render_template('index.html',title='Home',form=form)


def view_data_in_browser(data):
    if type(data)==list:
        #html_str = list_to_html(html_data)
        data = pd.Series(data).to_frame()
        file = 'html_data_list.html'
        data.columns = ['similar_users_available']
    else:
        file = 'html_data.html'

    html_str = data.to_html()
    '''
    with open(file,'w') as f:
        f.write(html_str)
    #file_name = os.path.abspath(file)
    #webbrowser.open("file://{}".format(file_name))
    '''
    return html_str

def list_to_html(elements):
        string = "<ul>\n"
        for s in elements:
            string += "<li>" + str(s) + "</li>\n"
        string += "</ul>"
        return string

class Application:
    global user_course_views
    user_course_views = pd.read_csv('./app/data_files_ml_engineer/user_course_views.csv')
    global user_interests
    user_interests = pd.read_csv('./app/data_files_ml_engineer/user_interests.csv')
    global user_assessment_scores
    user_assessment_scores = pd.read_csv('./app/data_files_ml_engineer/user_assessment_scores.csv')
    global course_tags
    course_tags = pd.read_csv('./app/data_files_ml_engineer/course_tags.csv')


    def __init__(self):
        '''read the files provided in to dataframes'''
        print('Class Invoked')

    def retrieve_data(self,user_handle):
        print
        if user_handle not in list(user_assessment_scores.user_handle):
            return None
        ratings = self.get_assessment_ratings()

        course_genres = set(course_tags.course_tags)
        #print(len(course_genres),' course_genres/course_tags.course_tags available')
        courses = set(course_tags.course_id)
        #print(len(courses),' courses available')
        assessment_tags = set(user_assessment_scores.assessment_tag)
        #print(len(assessment_tags),' : assessement_tags')
        #print(assessment_tags.issubset(course_genres),' assessment tags is subset of course_tags.course_tags/course_genres')
        user_level,user_views_crosstab = self.get_viewer_ratings(courses)

        return self.process_data(user_views_crosstab,user_handle,user_level,ratings)





    def process_data(self, user_views_crosstab, user,user_level,ratings):
        #user = int(raw_input('please enter user id :'))
        #drop multi index
        user_views_crosstab.columns = user_views_crosstab.columns.droplevel()
        user_view_ratings = user_views_crosstab[user]
        #user_view_ratings[user_view_ratings>0]
        correlated_users = user_views_crosstab.corrwith(user_view_ratings)
        correlated_users_df = pd.DataFrame(correlated_users,columns=['correlated'])
        correlated_users_df.dropna(inplace=True)
        correlated_users_summary = correlated_users_df.join(user_level['rating_count'])
        users=list(correlated_users_summary.index)
        print(correlated_users_summary.shape)
        similar_users = pd.DataFrame(users,columns=['user_handle'])
        similar_users_summary = pd.merge(similar_users,ratings,on='user_handle')
        #similar_users_summary
        #return list(similar_users_summary.user_handle.unique())
        return similar_users_summary




    def get_viewer_ratings(self,courses):
        rating_views,courses_available = self._viewer_ratings(courses)
        user_level = pd.DataFrame(rating_views.groupby('user_handle')['level_id'].mean())
        user_level['rating_count'] = pd.DataFrame(rating_views.groupby('user_handle')['level_id'].count())
        user_views_crosstab = pd.pivot_table(rating_views,columns='user_handle',index='course_ids')
        return user_level,user_views_crosstab

    def _viewer_ratings(self,courses):
        course_available_dict={}
        course_available_dict_reverse={}
        courses_available = list(courses)
        for key,value in enumerate(courses_available):
            course_available_dict[key]=value
            course_available_dict_reverse[value]=key

        user_course_views['course_ids']=user_course_views.course_id.map(course_available_dict_reverse)
        user_course_views['level_id']=user_course_views.level.map({'Beginner':1,'Intermediate':2,'Advanced':3})
        rating_views = user_course_views[['user_handle','course_ids','level_id']]

        rating_views.drop_duplicates(inplace=True)

        courses_available = pd.DataFrame.from_dict(course_available_dict,orient='index')
        #courses_available.reset_index(inplace=True)
        courses_available.columns=['course']

        return rating_views,courses_available


    def get_assessment_ratings(self):
        ## for ratings
        ratings = user_assessment_scores.copy()
        #print(ratings.head())
        # Drop the date column to draw average scores for user on asessment tags,
        # incase if users took assessment multiple times
        ratings.drop(['user_assessment_date'],axis = 1, inplace = True)
        grouped = ratings.groupby(['user_handle','assessment_tag'])
        ratings1=grouped.agg('mean')
        print(ratings.shape)

        for indice in ratings.index:
            if 0<=ratings.ix[indice,2]<=50:
                ratings.ix[indice,'rating']=1

            if 51<=ratings.ix[indice,2]<=100:
                ratings.ix[indice,'rating']=2

            elif 101<=ratings.ix[indice,2]<=151:
                ratings.ix[indice,'rating']=3

            if 151<=ratings.ix[indice,2]<=200:
                ratings.ix[indice,'rating']=4

            if 201<=ratings.ix[indice,2]<=250:
                ratings.ix[indice,'rating']=5

            if 251<=ratings.ix[indice,2]<=300:
                ratings.ix[indice,'rating']=6


        return ratings



if __name__=="__main__":
    app.run(debug=True)
