from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.decomposition import PCA
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
import pandas as pd 
from sklearn.neighbors import KNeighborsClassifier
import os


def gridSearch():
    csv_map_path = dir(dir(dir(os.path.abspath(__file__)))) + os.sep + 'data' + os.sep + "fire_archive_M6_96619.csv"
    df = pd.read_csv(csv_map_path)
    df = df[[ "latitude", "longitude", "scan", "track", "acq_time", "frp", "type" ]]
    X = df.drop("type", axis=1)
    y = df["type"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.8, random_state=42)

    reg_log = Pipeline(steps=[
        ('pca', PCA(n_components=0.9, random_state=42)),
        ('classifier', SVC())])

    logistic_params = {'classifier': [LogisticRegression()]}
    random_forest_params = {'classifier': [KNeighborsClassifier()]}
    svm_params = {'classifier': [SVC()]}

    search_space = [
        logistic_params,
        random_forest_params,
        svm_params]

    clf = GridSearchCV(estimator = reg_log,
                    param_grid = search_space,
                    cv = 2,
                    verbose=1,
                    n_jobs=-1)

    return clf 

clf = gridSearch() 

def best_scores():
    clf.fit(X, y)
    return clf.best_estimator_ , clf.best_score_

