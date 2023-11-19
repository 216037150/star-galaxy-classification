#Read data file
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#RF classifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score, f1_score

# matrics to test the model
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import cross_val_score
from sklearn import metrics


from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier