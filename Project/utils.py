import pickle
import json
import config
import numpy as np

class Online_Marketing():
    def __init__(self,Marketing_Spend, Administration, Transport, Area):
        self.Marketing_Spend=Marketing_Spend
        self.Administration=Administration
        self.Transport=Transport
        self.Area=Area

    def load_model(self):
        with open(config.Model_PKL,"rb") as f:
            self.model_pkl=pickle.load(f)

        with open(config.Model_JSON,"r") as f:
            self.json_data=json.load(f)


    def get_Profit(self):
        self.load_model()

        t_array=np.zeros(len(self.json_data["columns"]))
        t_array[0]=self.Marketing_Spend
        t_array[1]=self.Administration
        t_array[2]=self.Transport
        t_array[3]=self.json_data["Area"][self.Area]

        print("Test_Array: ",t_array)

        profit=np.around(self.model_pkl.predict([t_array]),2)[0]
        return profit