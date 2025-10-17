import pickle
import pandas
import matplotlib
import seaborn as sns


with open("10-diamonds","rb") as f:
    save_data = pickle.load(f)


model = save_data["model"]
encoder = save_data["encoder"]
scaler = save_data["scaler"]