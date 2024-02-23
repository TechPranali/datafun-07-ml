from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

# Load the digits dataset
digits = load_digits()

# Split into training and test set
X_train, X_test, y_train, y_test = train_test_split(digits.data, digits.target, random_state=0)

# Initialize the classifier
knn = KNeighborsClassifier()

# Fit the classifier to the data
knn.fit(X_train, y_train)

# Predict the test data
y_pred = knn.predict(X_test)

# Calculate the confusion matrix
cm = confusion_matrix(y_test, y_pred)

# Plot the confusion matrix
plt.figure(figsize=(10, 7))
sns.heatmap(cm, annot=True, cmap='nipy_spectral_r')
plt.xlabel('Predicted')
plt.ylabel('True')
plt.show()
