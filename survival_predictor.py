from tkinter import *
import tkinter.messagebox
import pandas as pd
import pickle

class SurvivalPredictor:
    def __init__(self):
        self.model_file = "svc_model.sav"

        self.window = Tk()
        self.window.geometry('600x600')
        self.window.title("Would you have survived in Titanic?")

        self.heading = Label(text="Your Data", width=20, font=("bold", 20))
        self.heading.pack()

        self.title_text = Label(text="Title:")
        self.firstname_text = Label(text="First Name:")
        self.lastname_text = Label(text="Last Name:")
        self.gender_text = Label(text="Gender:")
        self.age_text = Label(text="Age:")
        self.pclass_text = Label(text="Passenger Class (1, 2, or 3):")

        self.title_text.place(x=15, y=70)
        self.firstname_text.place(x=15, y=140)
        self.lastname_text.place(x=15, y=210)
        self.gender_text.place(x=15, y=280)
        self.age_text.place(x=15, y=350)
        self.pclass_text.place(x=15, y=420)

        self.title = StringVar()
        self.firstname = StringVar()
        self.lastname = StringVar()
        self.gender = StringVar()
        self.age = IntVar()
        self.pclass = IntVar()

        self.title_entry = Entry(textvariable=self.title, width=20)
        self.firstname_entry = Entry(textvariable=self.firstname, width=30)
        self.lastname_entry = Entry(textvariable=self.lastname, width=30)
        self.gender_entry = Entry(textvariable=self.gender, width=20)
        self.age_entry = Entry(textvariable=self.age, width=10)
        self.pclass_entry = Entry(textvariable=self.pclass, width=10)

        self.title_entry.place(x=15, y=100)
        self.firstname_entry.place(x=15, y=170)
        self.lastname_entry.place(x=15, y=240)
        self.gender_entry.place(x=15, y=310)
        self.age_entry.place(x=15, y=380)
        self.pclass_entry.place(x=15, y=450)

        submit = Button(self.window, text='Submit', width=10, command=self.process)
        submit.place(x=15, y=550)

    def process(self):
        print("enter process")
        title = self.title.get()
        firstname = self.firstname.get()
        lastname = self.lastname.get()
        gender = self.gender.get()
        age = self.age.get()
        pclass = self.pclass.get()

        sample_input = pd.read_csv("sample_input.csv")

        # setting passenger title
        if title.lower() == "mr":
            sample_input['name_title_Mr'] = 1
        elif title.lower() == "mrs":
            sample_input['name_title_Mrs'] = 1
        elif title.lower() == "miss":
            sample_input['name_title_Miss'] = 1
        elif title.lower() == "sir":
            sample_input['name_title_Sir'] = 1
        elif title.lower() == "master":
            sample_input['name_title_Master'] = 1
        else:
            sample_input['name_title_Mr'] = 0


        # setting passenger age
        if 0 < age > 20:
            sample_input['Age'] = -1
        elif 20 < age > 40:
            sample_input['Age'] = 0
        elif 40 < age > 60:
            sample_input['Age'] = 1
        elif age > 60:
            sample_input['Age'] = 2

        # setting the passenger class
        if pclass == 1:
            sample_input['Pclass_1'] = 1
        elif pclass == 2:
            sample_input['Pclass_2'] = 1
        elif pclass == 3:
            sample_input['Pclass_3'] = 1
        else:
            sample_input['Pclass_1'] = 0
            sample_input['Pclass_2'] = 0
            sample_input['Pclass_3'] = 0

        # setting passenger gender
        if gender.lower() == 'male':
            sample_input['Sex_male'] = 1
        elif gender.lower() == 'female':
            sample_input['Sex_female'] = 1
        else:
            sample_input['Sex_male'] = 0
            sample_input['Sex_female'] = 0

        # get prediction from the model
        prediction = self.get_prediction(sample_input)

        message = "No Info Yet!!"
        if prediction == 0:
            message = "Sorry, You would NOT have Survived!! :("
        elif prediction == 1:
            message = "Hurray, You would have Survived!! :D"

        tkinter.messagebox.showinfo(title=f"Hi, {firstname}",
                                    message=f"Hi, {firstname}. {message}")


    def get_prediction(self, sample_input):
        load_model = pickle.load(open(self.model_file, 'rb'))
        prediction = load_model.predict(sample_input)

        return prediction

    def run(self):
        self.window.mainloop()


def main():
    survival_predictor = SurvivalPredictor()
    survival_predictor.run()


if __name__ == '__main__':
    main()
