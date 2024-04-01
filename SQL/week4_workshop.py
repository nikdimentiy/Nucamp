# Constants
FIG_SIZE = (10, 5)

# %% Setup Cell
import psycopg2
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

con = psycopg2.connect("dbname=week4 user=postgres host=localhost port=5432")


def sql_to_df(sql_query: str):
    """Execute SQL query and return result set as a pandas DataFrame."""
    try:
        return pd.read_sql(sql_query, con)
    except psycopg2.Error as e:
        print("Error executing SQL query:", e)
        return None


# %% Task 1 Cell

def task1():
    """Visualize artworks count by department."""
    title = "Artworks by Department"
    query = '''
        SELECT department, COUNT(department) FROM moma_works
        GROUP BY department ORDER BY COUNT DESC
    '''
    dataframe = sql_to_df(query)
    if dataframe is not None:
        fig, axes = plt.subplots(figsize=FIG_SIZE)
        axes.set_title(title, fontsize=14)

        xpos = np.arange(len(dataframe))
        axes.bar(xpos, dataframe["count"], width=0.50)
        axes.set_xticks(xpos)
        axes.set_xticklabels(dataframe["department"])
        axes.set_ylabel("Count", fontsize=12)
        plt.setp(axes.get_xticklabels(), rotation=30, horizontalalignment='right')

        plt.show()


task1()

# %% Task 2 Cell

def task2():
    """Visualize artworks count by classification."""
    title = "Artworks by Classification"
    query = '''
        SELECT classification, COUNT(classification) FROM moma_works
        GROUP BY classification ORDER BY COUNT DESC
    '''
    dataframe = sql_to_df(query)
    if dataframe is not None:
        fig, axes = plt.subplots(figsize=FIG_SIZE)
        axes.set_title(title, fontsize=14)

        xpos = np.arange(len(dataframe))
        axes.bar(xpos, dataframe["count"], width=0.50)
        axes.set_xticks(xpos)
        axes.set_xticklabels(dataframe["classification"])
        axes.set_ylabel("Count", fontsize=12)
        plt.setp(axes.get_xticklabels(), rotation=30, horizontalalignment='right')

        plt.show()


task2()

# %% Task 3 Cell

def task3():
    """Visualize artists count by nationality."""
    title = "Artists by Nationality"
    query = '''
        SELECT info -> 'nationality' AS nationality, COUNT(info -> 'nationality') FROM moma_artists
        GROUP BY nationality ORDER BY COUNT DESC
    '''
    dataframe = sql_to_df(query)
    if dataframe is not None:
        fig, axes = plt.subplots(figsize=FIG_SIZE)
        axes.set_title(title, fontsize=14)

        xpos = np.arange(len(dataframe))
        axes.bar(xpos, dataframe["count"], width=0.50)
        axes.set_xticks(xpos)
        axes.set_xticklabels(dataframe["nationality"])
        axes.set_ylabel("Count", fontsize=12)

        plt.show()


task3()

# %% Task 4 Cell

def task4():
    """Visualize artists count by gender."""
    title = "Artists by Gender"
    query = ''' 
    SELECT UPPER(info ->> 'gender') AS gender, COUNT(info -> 'gender') FROM moma_artists
    WHERE info ->> 'gender' IS NOT NULL
    GROUP BY gender ORDER BY gender
    '''
    dataframe = sql_to_df(query)
    if dataframe is not None:
        fig, axes = plt.subplots(figsize=FIG_SIZE)
        axes.set_title(title, fontsize=14)

        fig.set_facecolor('white')
        axes.pie(
            x=dataframe["count"],
            labels=dataframe["gender"],
            autopct='%1.1f%%',
            colors=['lightcoral', 'skyblue', 'lavender']
        )
        axes.axis('equal')

        plt.show()


task4()

# %% Task 5 Cell: Describe this chart

def task5():
    """Visualize daily acquisition count."""
    title = "Daily Acquisition by Date"
    query = """
            WITH daily_acquisition_count AS (
                SELECT date_acquired, COUNT(*) FROM moma_works 
                WHERE date_acquired IS NOT NULL 
                GROUP BY date_acquired
            )
            SELECT date_acquired, SUM(count) 
            OVER (ORDER BY date_acquired) FROM daily_acquisition_count;
            """
    dataframe = sql_to_df(query)
    if dataframe is not None:
        fig, axes = plt.subplots(figsize=FIG_SIZE)
        axes.set_title(title, fontsize=14)

        xpos = np.arange(len(dataframe))
        axes.bar(xpos, dataframe["sum"], width=0.50)
        axes.set_xticks([
            0,
            len(dataframe) // 2,
            len(dataframe)
        ])
        axes.set_xticklabels(dataframe.iloc[[
            0,
            len(dataframe) // 2,
            -1
        ]]["date_acquired"])
        axes.set_ylabel("Count", fontsize=12)

        plt.show()


task5()
