from pandas.tools.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import SGDClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
dataset = pandas.read_csv('tn.csv') 
array = dataset.values
X = array[:,0:30]
Y = array[:,30]
validation_size = 0.2
seed = 7
scoring = 'accuracy'
X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size=validation_size, random_state=seed)


models = []
models.append(('LR', LogisticRegression()))
models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('KNN', KNeighborsClassifier()))
results = []
names = []
prevMean = 0
counter = 0
for name, model in models:
    counter += 1
    kfold = model_selection.KFold(n_splits=10, random_state=seed)
    cv_results = model_selection.cross_val_score(model, X_train, Y_train, cv=kfold, scoring=scoring)
    results.append(cv_results)
    names.append(name)
    msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std()) 
    if (cv_results.mean() > prevMean):
        if name == 'LR':
            algoUse = 1
        elif name == 'LDA':
            algoUse = 2
        else:
            algoUse = 3 
        prevMean = cv_results.mean()
algo = LinearDiscriminantAnalysis()
algoName = ''
algoType = ''
if algoUse == 1:
    algo = LogisticRegression()
    algoName = 'Logistic Regression'
    algoType = 'Linear'
elif algoUse == 2:
    knn = LinearDiscriminantAnalysis()
    algoName = 'Linear Distriminant Analysis'
    algoType = 'Linear'
elif algoUse == 3:
    knn = KNeighborsClassifier()
    algoName = 'K Neighbor Classifier'
    algoType = 'Non-Linear'
algo = LinearDiscriminantAnalysis()
algo.fit(X_train, Y_train)
predictions = algo.predict(X_validation)
matrix = classification_report(Y_validation, predictions)
print('\nThis data set was identified as best suited for the '+algoName+' algorithm. Using this \033[92m'+algoType+' algorithm, Panthera had a '+str((accuracy_score(Y_validation, predictions)*100))+'% accuracy\033[0m in correctly identifying credit card transactions as either legitimate or fraudulent in this entire dataset.\n\n')
print('Final statistics on data:\n\n')
target_names = ['Legitimate Transaction', 'Fraudulent Transaction']
print(classification_report(Y_validation, predictions,target_names=target_names))

