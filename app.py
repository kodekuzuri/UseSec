from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap
from consent import ConsentForm, create_form
from flask import redirect, url_for
from flask import request
from hashlib import md5 as hash_fn

from wtforms import StringField, SubmitField, BooleanField, RadioField

users = {}
user_list = ['Parth Jindal', 'Neha Dalmia', 'Suhas Jain',
             'Pranav Rajput', 'Rajat Bachawat', 'Animesh Jha']


questions = {
    "q1" : {
        "question" : "How long have you been using a smartphone?",
        "response_type": "radio",
        "options" : ["Around a few months", "Around a year", "Around 2 years", "Around 3 years", "More than 3 years"],
    },
}
"""
    "q2" : {
        "question": "What operating system do you currently use (to make payments from Google pay)?",
        "response_type": "radio",
        "options" : ["Android", "iOS", "Prefer not to Answer"],
    },

    "q3" : {
        "question": "Before installing an application on your smartphone, how often do you read the application provider's privacy policy for using the application?",
        "response_type": "radio",
        "options" : ["Always", "Sometimes", "Never", "I am not sure"],
    },

    "q4" : {
        "question": "What do you usually do when applications ask for permissions after installation?",
        "response_type": "radio",
        "options" : ["Almost always deny", "Allow what is required for basic functionality ", "Almost always allow", "I am not sure"],
    },

    "q5" : {
        "question": "Which of the following Google applications do you use (utilize at least once a week) in your smartphone? ",
        "response_type": "checkbox",
        "options" : ["Chrome Browser", "Google Voice Assistant", "GMail", "Google Calendar", "Google Meet", "Youtube / Youtube Music", "Android Auto", "Google Drive", "Google Office Apps (docs/sheets/slides)", "Google Maps"],
    },

    "q6" : {
        "question": "Can you please select what kind of data you consider private on your smartphone?" ,
        "response_type": "radio",
        "options" : ["Call records" , "Location", "Photos and videos ", "Names of installed applications", "Documents", "Audio/call recordings", "Browser history"],
    },

    "q7" : {
        "question" : "Since how long have you been using Google Pay on your smartphone?",
        "response_type": "radio",
        "options" : ["Around a few months", "Around a year", "Around 2 years", "Around 3 years", "More than 3 years"],
    }, 

    "q8" : {
        "question" : "How often do you use Google Pay on your smartphone?",
        "response_type": "radio",
        "options" : ["A couple of times a day", "Once a day", "A couple of times per week", "Once a week", "A couple of times per month", "A couple of times every 3 months", "Less than once every 3 months"],
    }, 

    "q9" : {
        "question" : "Approximately how long ago did you link your bank account to Google Pay?",
        "response_type": "radio",
        "options" : ["A few weeks", "A few months", "Around a year", "Around 2 years", "Around 3 years", "More than 3 years"],
    }, 

    "q10" : {
        "question" : "[If answered “A couple of times a week” or higher] What qualities of Google Pay encourage you to use it frequently on your smartphone? Select all that apply.",
        "response_type": "checkbox",
        "options" : ["Making transactions with it is faster than other modes of payment", "You earn rewards from it", "You find it easy to use", "Others"],
    },

    "q11" : {
        "question" : "[If answered lower than “A couple of times a week”] What qualities of Google Pay discourage you to use it frequently on your smartphone? Select all that apply.",
        "response_type": "checkbox",
        "options" : ["Making transactions with it is slower than other modes of payment", "You find it difficult to use", "You fear about your privacy" , "You fear about getting scammed online", "Other"],
    },    
    
    "q12" : {
        "question" : "Which of the following payment apps have you used? Select all that apply.", 
        "response_type": "checkbox",
        "options" : ["PhonePe", "PayTM", "Amazon Pay" , "None of These"],
    },

"""



    
"""
    "q2" : {
        "question": "What operating system do you currently use (to make payments from Google pay)?",
        "response_type": "radio",
        "options" : ["Android", "iOS", "Prefer not to Answer"],
    },

    "q3" : {
        "question": "Before installing an application on your smartphone, how often do you read the application provider's privacy policy for using the application?",
        "response_type": "radio",
        "options" : ["Always", "Sometimes", "Never", "I am not sure"],
    },

    "q4" : {
        "question": "What do you usually do when applications ask for permissions after installation?",
        "response_type": "radio",
        "options" : ["Almost always deny", "Allow what is required for basic functionality ", "Almost always allow", "I am not sure"],
    },

    "q5" : {
        "question": "Which of the following Google applications do you use (utilize at least once a week) in your smartphone? ",
        "response_type": "checkbox",
        "options" : ["Chrome Browser", "Google Voice Assistant", "GMail", "Google Calendar", "Google Meet", "Youtube / Youtube Music", "Android Auto", "Google Drive", "Google Office Apps (docs/sheets/slides)", "Google Maps"],
    },

    "q6" : {
        "question": "Can you please select what kind of data you consider private on your smartphone?" ,
        "response_type": "radio",
        "options" : ["Call records" , "Location", "Photos and videos ", "Names of installed applications", "Documents", "Audio/call recordings", "Browser history"],
    },

    "q7" : {
        "question" : "Since how long have you been using Google Pay on your smartphone?",
        "response_type": "radio",
        "options" : ["Around a few months", "Around a year", "Around 2 years", "Around 3 years", "More than 3 years"],
    }, 

    "q8" : {
        "question" : "How often do you use Google Pay on your smartphone?",
        "response_type": "radio",
        "options" : ["A couple of times a day", "Once a day", "A couple of times per week", "Once a week", "A couple of times per month", "A couple of times every 3 months", "Less than once every 3 months"],
    }, 

    "q9" : {
        "question" : "Approximately how long ago did you link your bank account to Google Pay?",
        "response_type": "radio",
        "options" : ["A few weeks", "A few months", "Around a year", "Around 2 years", "Around 3 years", "More than 3 years"],
    }, 

    "q10" : {
        "question" : "[If answered “A couple of times a week” or higher] What qualities of Google Pay encourage you to use it frequently on your smartphone? Select all that apply.",
        "response_type": "checkbox",
        "options" : ["Making transactions with it is faster than other modes of payment", "You earn rewards from it", "You find it easy to use", "Others"],
    },

    "q11" : {
        "question" : "[If answered lower than “A couple of times a week”] What qualities of Google Pay discourage you to use it frequently on your smartphone? Select all that apply.",
        "response_type": "checkbox",
        "options" : ["Making transactions with it is slower than other modes of payment", "You find it difficult to use", "You fear about your privacy" , "You fear about getting scammed online", "Other"],
    },    
    
    "q12" : {
        "question" : "Which of the following payment apps have you used? Select all that apply.", 
        "response_type": "checkbox",
        "options" : ["PhonePe", "PayTM", "Amazon Pay" , "None of These"],
    },

    "q13" : {
        "question" : "[If answered anything but “None of these”] Do you prefer using Google Pay over the payment apps that you have used?",
        "response" : "radio",
        "options" : ["Yes", "No"],
    },

    "q14" : {
        "question" : "[If answered “Yes”] Why do you prefer using Google Pay over the other payment apps that you have used? Select all that apply.",
        "response" : "radio",
        "options" : ["You find Google Pay easier to use", "You find making transactions with Google Pay to be faster", "Payment failure rates are lower on Google Pay", "You prefer using Google apps", "Other"],
    },

    "q15" : {
        "question" : "[If answered “No”] Why do you prefer using other payment apps over Google Pay? Select all that apply.",
        "response" : "checkbox",
        "options" : ["You find Google Pay more difficult to use", "You find making transactions with Google Pay to be slower", "Payment failure rates are higher on Google Pay",
        "You do not prefer using Google apps", "Other"],
    },

    "q16" : {
        "question" : "Which of the following purposes do you use Google Pay for? Select all that apply.",
        "response" : "checkbox",
        "options" : ["Sending money","Receiving money","Group Expenses","Availing rewards", "Other"],
    }, 

    "q17" : {
        "question" : "Among the following, whom do you generally send money to? Select all that apply.",
        "response" : "checkbox",
        "options" : ["Friends", "Vendors", "E-Commerce Websites or Apps", "Food Delivery Websites or Apps", "Food Delivery Websites or Apps", "Periodically Billed Services (like electricity or mobile network provider)", "Other", "Do not wish to disclose"],
    },

    "q18" : {
        "question" : "On average, what range do your transactions via Google Pay lie in?",
        "response" : "checkbox",
        "options" :  ["Less than Rs. 100", "Rs. 100 to Rs. 1000", "Rs. 1000 to Rs. 10000", "Rs. 10000 to Rs. 50000", "Rs. 50000 or higher", "Do not wish to disclose"],
    } ,

    "q19" : {
        "question" : "From which of the following locations do you remember having made transactions using Google Pay? Select all that apply.",
        "response" : "checkbox",
        "options" : ["Home", "Work", "Shopping Mall", "Restaurant", "Do not wish to disclose"],
    },

    "q20" : {
        "question" : "At what times of the day do you usually make transactions using Google Pay? Select all that apply.",
        "response" : "checkbox",
        "options" : ["Morning (06:00 AM to 12:00 PM)", "Afternoon (12:00 PM to 04:00 PM)", "Evening (04:00 PM to 08:00 PM)", "Night (08:00 PM to 11:00 PM)", "Late Night (11:00 PM to 02:00 AM)", "I do not remember", "Do not wish to disclose"],
    },

    "q21" : {
        "question" : "On a scale of 1 to 5, with 1 being the least and 5 being the most, how much do you trust Google that it would not use your data for malicious purposes?",
        "response" : "radio",
        "options" : ["1", "2", "3", "4", "5"],
    },

    "q22" : {
        "question" : "Which of the following do you remember sharing or giving permission for at the time of setting up Google Pay on your smartphone? Select all that apply",
        "response" : "checkbox",
        "options" : ["Basic personal information (such as name, birthday and phone number)", "Access to your location history", "Bank account details", "Access to your contacts", "Access to your photo gallery"],
    },

    "q23" : {
        "question" : "Do you think Google Pay stores the amount of the transaction?",
        "response" : "radio",
        "options" : ["Yes", "No", "I am not sure"],
    },

    "q24" : {
        "question" : "Do you think Google Pay stores the UPI ID of the other party that took part in the transaction?",
        "response" : "radio",
        "options" : ["Yes", "No", "I am not sure"],
    },
    
    "q25" : {
        "question" : "Do you think Google Pay stores the bank account number of the other party that took part in the transaction?",
        "response" : "radio",
        "options" : ["Yes", "No", "I am not sure"],
    },
    
    "q26" : {
        "question" : "Do you think Google Pay stores the name of the other party that took part in the transaction?",
        "response" : "radio",
        "options" : ["Yes", "No", "I am not sure"],
    },

    "q27" : {
        "question" : "Do you think Google Pay stores the date and time at which the transaction was made?",
        "response" : "radio",
        "options" : ["Yes", "No", "I am not sure"],
    },

    "q28" : {
        "question" : "Do you think Google Pay stores the data about which companies' vouchers (coupons) you have been rewarded?",
        "response" : "radio",
        "options" : ["Yes", "No", "I am not sure"],
    },   
    
    "q29" : {
        "question" : "Do you think Google Pay stores the data about which vouchers you have redeemed?",
        "response" : "radio",
        "options" : ["Yes", "No", "I am not sure"],
    },    
    
    "q30" : {
        "question" : "Do you think Google Pay stores the data about your group expenses?",
        "response" : "radio",
        "options" : ["Yes", "No", "I am not sure"],
    },    
    
    "q31" : {
        "question" : "Do you think Google uses data collected from Google Pay to show you targeted ads?",
        "response" : "radio",
        "options" : ["Yes", "No", "I am not sure"],
    },    
    
    "q32" : {
        "question" : "Do you think Google Pay has the ability to make a transaction without your consent?",
        "response" : "radio",
        "options" : ["Yes", "No", "I am not sure"],
    },    
    
    "q33" : {
        "question" : "Do you think Google will provide your Google Pay data to a government agency (like Enforcement Directorate/Income Tax Department) if pressured?",
        "response" : "radio",
        "options" : ["Yes", "No", "I am not sure"],
    },    
    
    "q34" : {
        "question" : "Do you think there exists an option to automatically delete data stored by a specific Google application after a fixed time?",
        "response" : "radio",
        "options" : ["Yes", "No", "I am not sure"],
    },

    "q35" : {
        "question" : "Do you think Google Pay stores your data indefinitely on its storage facilities (i.e. does not delete it after a fixed time) by default?",
        "response" : "radio",
        "options" : ["Yes", "No", "I am not sure"],
    },

    "q36" : {
        "question" : "Do you think Google Pay uses your data for purposes other than improving its user experience?",
        "response" : "radio",
        "options" : ["Yes", "No", "I am not sure"],
    },

    "q37" : {
        "question" : "Do you think Google removes all personally identifiable information before storing your data in its storage facilities?",
        "response" : "radio",
        "options" : ["Yes", "No", "I am not sure"],
    },

    "q38" : {
        "question" : "I believe Google should be more proactive in notifying the users about the Google Pay data dashboard.",
        "response" : "radio",
        "options" : ["Very Uncomfortable", "Uncomfortable", "Neutral", "Comfortable", "Very Comfortable"],
    },

    "q39" : {
        "question" : "I believe Google should be more proactive in notifying the users exactly what data it collects from Google Pay",
        "response" : "radio",
        "options" : ["Very Uncomfortable", "Uncomfortable", "Neutral", "Comfortable", "Very Comfortable"],
    },

    "q40" : {
        "question" : "I believe Google should be more proactive in notifying the users what purposes the Google Pay data collected from them is used for.",
        "response" : "radio",
        "options" : ["Very Uncomfortable", "Uncomfortable", "Neutral", "Comfortable", "Very Comfortable"],
    },

    "q41" : {
        "question" : "I believe Google should allow me to decide what data about my transactions it collects (if it collects it at all).",
        "response" : "radio",
        "options" : ["Very Uncomfortable", "Uncomfortable", "Neutral", "Comfortable", "Very Comfortable"],
    },

    "q42" : {
        "question" : "I believe Google should allow me to decide what data about my vouchers (coupons), rewards or gift cards it collects (if it collects it at all).",
        "response" : "radio",
        "options" : ["Very Uncomfortable", "Uncomfortable", "Neutral", "Comfortable", "Very Comfortable"],
    },

    "q43" : {
        "question" : "I believe Google should allow me to decide what data about my group expenses on Google Pay it collects (if it collects it at all).",
        "response" : "radio",
        "options" : ["Very Uncomfortable", "Uncomfortable", "Neutral", "Comfortable", "Very Comfortable"],
    },

    "q44" : {
        "question" : "I believe Google should allow managing the data collected by an application in that specific application itself.",
        "response" : "radio",
        "options" : ["Very Uncomfortable", "Uncomfortable", "Neutral", "Comfortable", "Very Comfortable"],
    },

    "q45" : {
        "question" : "I believe there should be an option to automatically delete data older than a certain time period.",
        "response" : "radio",
        "options" : ["Very Uncomfortable", "Uncomfortable", "Neutral", "Comfortable", "Very Comfortable"],
    },

    "q46" : {
        "question" : "I believe Google should collect data primarily to enhance user experience.",
        "response" : "radio",
        "options" : ["Very Uncomfortable", "Uncomfortable", "Neutral", "Comfortable", "Very Comfortable"],
    },

    "q47" : {
        "question" : "I believe there should be an option to delete selected portions of the transaction data I consider to be sensitive.",
        "response" : "radio",
        "options" : ["Very Uncomfortable", "Uncomfortable", "Neutral", "Comfortable", "Very Comfortable"],
    },

    "q48" : {
        "question" : "I believe Google should be more liberal with the data it collects to give a more personalised experience.",
        "response" : "radio",
        "options" : ["Very Uncomfortable", "Uncomfortable", "Neutral", "Comfortable", "Very Comfortable"],
    },

    "q49" : {
        "question" : "I would be okay with Google using my data for any purpose as long as it removes personally identifiable information from the data.",
        "response" : "radio",
        "options" : ["Very Uncomfortable", "Uncomfortable", "Neutral", "Comfortable", "Very Comfortable"],
    },

    "q50" : {
        "question" : "I would be okay with Google using my data for any purpose as long as it does not share it with government agencies or political parties.",
        "response" : "radio",
        "options" : ["Very Uncomfortable", "Uncomfortable", "Neutral", "Comfortable", "Very Comfortable"],
    },
    
    "q51" : {
        "question" : "Do you know about Google Data Dashboard?",
        "response_type": "radio",
        "options" : ["Yes", "No"],
    }, 
   
    "q52" : {
        "question" : "[Yes] Which features of the Google Data Dashboard have you utilised?",
        "response" : "radio",
        "options" : ["Download collected data", "Delete all data", "Delete selected sensitive data", "Change privacy settings", "Other"],
    },

    "q53" : {
        "question" : "[No] Do you think you would have benefited if you had known about it earlier?",
        "response" : "radio",
        "options" : ["Yes", "No"],
    },

    "q54" : {
        "question" : "[No] Now that you know about it, which actions are you most likely to perform in the future (for any Google application)?",
        "response" : "radio",
        "options" : ["Download collected data", "Delete all data", "Delete selected sensitive data", "Change privacy settings", "Other", "Not change anything", "I am not sure"],
    },

    "q55" : {
        "question" : "Knowing about the functionality of the personalisation feature, which setting will you like to keep it at?",
        "response" : "radio",
        "options" : ["On", "Off", "I am not sure"],
    },

    "q56" : {
        "question" : "Do you feel that tech companies, in general, tend to make it harder for users to access their collected data?",
        "response" : "radio",
        "options" : ["Yes", "No", "Maybe"],
    },

    "q57" : {
        "question" : "Have you ever gone through Google's privacy policy?",
        "response" : "radio",
        "options" : ["On", "Off", "I am not sure"],
    },

    "q58" : {
        "question" : "On a scale of 1 to 5, with 1 being the least and 5 being the most, how much do you trust Google that it would not use your data for malicious purposes, after participating in this study?",
        "response" : "radio",
        "options" : ["1", "2", "3", "4", "5"],
    },
       
    "q59" : {
        "question" : "With what gender do you identify?",
        "response" : "radio",
        "options" : ["Male", "Female", "Non_Binary", "Prefer not to answer"],
    },

    "q60" : {
        "question" : "What is your age?",
        "response" : "radio",
        "options" : ["Younger than 18", "18-24", "25-34", "35-44", "45-54", "55-64", "64 or older", "I don't know", "Prefer not to say"],
    },

    "q61" : {
        "question" : "What is the highest degree or level of school you have completed?",
        "response" : "radio",
        "options" : ["No formal education", "Nursery school to 8th grade", "Some high school, no diploma", "High school graduate, diploma or the equivalent", "Some college credit, no degree", "Trade, technical, or vocational training", "Associate's degree", "Bachelor's degree", "Master's degree", "Professional degree", "Doctorate degree", "Prefer not to answer"],
    },

    "q62" : {
        "question" : "What is your employment status?",
        "response" : "radio",
        "options" : ["Student", "Full-time employed", "Part-time employed", "Not employed", "Retired", "Prefer not to answer"],
    },

    "q63" : {
        "question" : "Are you majoring in or do you have a degree or job in computer science, computer engineering, information technology, or a related field?",
        "response" : "radio",
        "options" : ["Yes", "No", "Prefer not to answer"],
    },
}
"""

def hash_users():
    for i, user in enumerate(user_list):
        hash_val = hash_fn(str(i).encode()).hexdigest()
        hash_val = hash_val[:8]
        users[hash_val] = user


app = Flask(__name__)
app.config['SECRET_KEY'] = 'C2HWGVoMGfNTBsrYQg8EcMrdTimkZfAb'
Bootstrap(app)


@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template("home.html", name="Parth", date="12/12/2019")


@app.route("/hello")
def hello_world():
    return 'hello world'


@app.route("/hello/<name>")
def varfunc(name):
    return 'Hello %s, Adios !' % name

@app.route("/gateway/<name>", methods = ['GET', 'POST'])
def inbetween(name):
    form = QuickForm()
    if request.method == 'POST':
        if form.is_submitted():
            pass
        else:
            pass
    return render_template('guide.html') #, first_sentence = "This is meant to be a guide for %s made by pranav\n" % name)


@app.route("/hello/<name>/final")
def varfun2(name):
    return "Hope to see you soon %s !" % name

@app.route('/survey/<id>', methods=['GET', 'POST'])
def index(id):
    name = users[id]
    form = ConsentForm()
    if request.method == 'POST':
        if form.is_submitted():
            if form.accept.data == "Yes":
                return redirect(url_for('survey2', id=id))
            else:
                return redirect(url_for('varfunc', name=name))
    return render_template('consent_form.html', form=form, name=name)


@app.route("/survey2/<id>", methods=['GET', 'POST'])
def survey2(id):
    if (request.method == 'POST'):
        return redirect(url_for('inbetween', name=users[id]))
    form, fields = create_form(questions=questions)
    return render_template('survey2.html', form=form, questions=fields)


@app.route("/survey3/<id>", methods = ['GET', 'POST'])
def specific_survey(id):
    name = users[id]
    #specific_survey_questions = generate_q_list()
    specific_survey_questions = {}
    if (request.method == 'POST'):
            return redirect(url_for('varfunc2',name = name))
    form, fields = create_form(questions = specific_survey_questions)
    return render_template('specific_survey.html', form=form, name=fields)



if __name__ == '__main__':
    hash_users()
    print(users)
    app.run(debug=True)