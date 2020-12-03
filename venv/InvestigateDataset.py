# Investigate a dataset project for Udacity
# I chose No-show appointments dataset
# Began 0900 on 17-11-2020

'''
This dataset collects information
from 100k medical appointments in
Brazil and is focused on the question
of whether or not patients show up
for their appointment. A number of
characteristics about the patient are
included in each row.
● ‘ScheduledDay’ tells us on
what day the patient set up their
appointment.
● ‘Neighborhood’ indicates the
location of the hospital.
● ‘Scholarship’ indicates
whether or not the patient is
enrolled in Brasilian welfare
program Bolsa Família.
● Be careful about the encoding
of the last column: it says ‘No’ if
the patient showed up to their
appointment, and ‘Yes’ if they
did not show up
'''

#module block
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Universal Variable Block
med_cond = ['Alcoholism','Diabetes','Handicap','Hypertension']
med_cond_list = ['Alcoholism','Diabetes','Handcap','Hipertension']
age_grps = [19,30,40,50,60,70,80] #this list is our cut offs
age_lables = ['1-20','21-30','31-40','41-50','51-60','61-70','71-80', '81+' ]
weekDays = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
sn_legend = ['No Show', 'Show']

# Definition Block

def ret_nunique(DataFrame):
    """Runs dataframe.nunique on the input and returns it.

    Parameters:
        Dataframe (pandas.DataFrame): The Dataframe that you are trying to get a return on.
    """
    return DataFrame.nunique()


def bar_plots(list1,list2,N,xlabs,ylabs,legend,*Title):
    """Produces a bar plot of two variables, with N linked columns, add x,y labels, legend and optional Title.

    Parameters:
        List 1(list): Dataframe Column or List to graph
        List 2(list): Dataframe Column or List to graph
        N     (int) : Number of bars in each List, must be the same.
        xlabs (list): Label for X Axis
        ylabs (str) : Label for Y Axis
        Legend(list): Legend for graph
        Title (str) : Optional Title for graph
    """
    width = .5              #Width of hte bars
    N_arr = np.arange(N)    #Arrange the bars

    fig, bcht = plt.subplots()
    bar1 = bcht.bar(N_arr, list1, width, color='blue')
    bar2 = bcht.bar(N_arr+width,list2,width,color='green')
    bcht.set_xticks(N_arr+width /2)
    try:
        bcht.set_title(Title[0])
    except:
        bcht.set_title("UNTITLED")
    bcht.set_xticklabels(xlabs)
    bcht.legend(legend)
    bcht.set_ylabel(ylabs)

    return plt.show()

def ret_sum(DATAFRAME,COLUMNN,*string):
    """Returns the sum of a given DataFrame. Can be used with either String or Int/Float types.

    Parameters:
        DATAFRAME (pandas.dataframe) : The dataframe you are calling
        COLUMNN   (str)              : The Column from the dataframe
        string    (str)              : A string variable for the count(optional)
    """
    try:
        COLUMNNN = str(COLUMNN)
        return sum(DATAFRAME[COLUMNN].str.count(string[0]))
    except:
        return sum(DATAFRAME[COLUMNN])

def app_per(DATAFRAME):
    """Produces a percentage from the given dataframe as a proportion of the total Appointments

    Parameters:
        DATAFRAME (pandas.DataFrame) : The Dataframe you are comparing.
    """
    return 100*DATAFRAME.shape[0]/df.shape[0]


# Produces a settingwithcopywarning: This is expected for now and review of the code shows it is correct. should probably

# read file and formatting block
df = pd.read_csv(r'I:\Python\PycharmProjects\udacityproject1\noshowappointments-kagglev2-may-2016.csv')
df = df[df.Age > 0]    #Clears out ages -1 and 0
df['AppointmentDay'] = df.AppointmentDay.str.split('T',1, expand=True)   #Cleans up the date for easier use
df['AppointmentDay'] = pd.to_datetime(df['AppointmentDay'])

#Patient ID shows only 62299 distinct Ids.

PId_dup = df[df['PatientId'].duplicated(keep=False)]   #Dataframe consisting of only those people with multiple appointments
PId_dup_ns = PId_dup.groupby('No-show').get_group("Yes") # A look at the number of people who had appointments and had cancelled and showed up later.
PId_dup_s = PId_dup.groupby('No-show').get_group("No")  # A look at the number of people who made appointments and did show up for at least one of them

# Bar chart to compare duplicate patients data
pidbar1 = ret_nunique(PId_dup['PatientId'])
pidbar2 = ret_nunique(PId_dup_ns['AppointmentID'])
pidbar3 = ret_nunique(PId_dup_s['AppointmentID'])

plt.bar([1,2,3], height=[pidbar1,pidbar2,pidbar3], width=.5, color=['green','red','blue'], tick_label=['Total Patients', 'Appointments not kept', 'Appointments kept'])
plt.title('Patients with multiple appointments')
plt.ylabel('Patients')
plt.show(block=True)
# split df into 2 dataframes one for each "No-show" == 'Yes' and 'No'

noshow = df.groupby('No-show')
df_n = noshow.get_group("No")  # df of people who did show up for appointments
df_y = noshow.get_group("Yes") #df of people who did not show up to appointments

# Starting with a look into potential gender differences among the two listed genders.
females_ns = ret_sum(df_y,'Gender','F')
males_ns = sum(df_y['Gender'].str.count('M'))
total_ns = females_ns + males_ns
females_s = sum(df_n['Gender'].str.count('F'))
males_s = sum(df_n['Gender'].str.count('M'))
total_s = females_s + males_s
m_f_p_h = [females_ns,females_s,males_ns,males_s]
plt.bar([1,2,3,4], height=m_f_p_h, width=.5, color=['pink','cyan','red', 'blue'], tick_label=['f_ns', 'f_s', 'm_ns', 'm_s'])
plt.title('Female and Male show vs no show')
plt.ylabel('Patients')
plt.show(block=True)
prop_f_ns = females_ns/(females_s+females_ns)           #proportion of female no shows to all women
prop_m_ns = males_ns/(males_s+males_ns)                 #Proportion of male no shows to all men
ftom = (prop_f_ns, prop_m_ns)                           #female to male ratio


# Create age groups list

df_n['Age'].hist()
df_y['Age'].hist()
plt.legend(['show','no-show'])
plt.title('No shows by age')
plt.xlabel('Age')
plt.ylabel('Patients')
plt.show()
# Proportions of Ages
s_val = df['Age'].value_counts() #value counts dataframe for number of times each age appears in the original dataframe
s_val_y = df_y['Age'].value_counts()
s_rat = s_val_y/s_val
s_rat.plot(kind='line')
plt.title('Ratio of no show to total in Age')
plt.margins(x=0,y=0)
plt.ylabel('Patients')
plt.xlabel('Age')
plt.show()

# Appointment Day data search
# do certain days have more no shows than other days

days_label = ['Monday','Tuesday', 'Wednesday','Thursday', 'Friday', 'Saturday']
df_y_days = pd.DataFrame(columns=['days'])
df_n_days = pd.DataFrame(columns=['days'])
df_y_days['days'] = df_y.AppointmentDay.dt.day_name().value_counts()
df_n_days['days'] = df_n.AppointmentDay.dt.day_name().value_counts()
df_d_sum = df_y_days['days']+df_n_days['days']
day_week_lst = [df_y_days.days.loc['Monday']/df_d_sum.loc['Monday'],df_y_days.days.loc['Tuesday']/df_d_sum.loc['Tuesday'],
                df_y_days.days.loc['Wednesday']/df_d_sum.loc['Wednesday'],df_y_days.days.loc['Thursday']/df_d_sum.loc['Thursday'],
                df_y_days.days.loc['Friday']/df_d_sum.loc['Friday'],df_y_days.days.loc['Saturday']/df_d_sum.loc['Saturday']]
day_week_lst_n = [df_n_days.days.loc['Monday']/df_d_sum.loc['Monday'],df_n_days.days.loc['Tuesday']/df_d_sum.loc['Tuesday'],
                  df_n_days.days.loc['Wednesday']/df_d_sum.loc['Wednesday'],df_n_days.days.loc['Thursday']/df_d_sum.loc['Thursday'],
                  df_n_days.days.loc['Friday']/df_d_sum.loc['Friday'],df_n_days.days.loc['Saturday']/df_d_sum.loc['Saturday']]
days_title = 'Days of the week vs Show and No-show appointments'
bar_plots(day_week_lst_n,day_week_lst,6,days_label,'Patients',['Show','NoShow'],days_title)

# See if Neighborhood has any impact on the results

df_n_h = df_n['Neighbourhood'].value_counts()
df_y_h = df_y['Neighbourhood'].value_counts()
df_h_lab = df_n_h.index.tolist()                        #Labels for the chart
df_h_s = sum(df_y_h)+sum(df_n_h)
df_h_ny = df_n_h.to_frame()
df_h_ny = df_h_ny.rename(columns={'Neighbourhood' :'Neighborhood_Showed' })
df_h_ny['Neighborhood no show'] = df_y_h.to_frame().Neighbourhood
df_h_ny['Neighborhood no show'] = df_h_ny['Neighborhood no show'].fillna(0).astype(int)
df_h_ny.plot.bar(stacked=False)
plt.title('Appointments vs. Neighborhood')
plt.show()

df_h_ny['Ratio'] = df_h_ny['Neighborhood no show']/(df_h_ny['Neighborhood no show'] + df_h_ny['Neighborhood_Showed'])
desc_h = df_h_ny.describe()
df_h_ny_2sd_m = df_h_ny[df_h_ny['Ratio'] > (desc_h.iloc[1,2]+desc_h.iloc[2,2])]
df_h_ny_2sd_l = df_h_ny[df_h_ny['Ratio'] < (desc_h.iloc[1,2]-desc_h.iloc[2,2])]
df_h_ny_2sd_ml = df_h_ny_2sd_m.append(df_h_ny_2sd_l)
df_h_ny_2sd_ml['Ratio'].plot.bar()
plt.tight_layout()
plt.title('Appointments in Neighborhoods more than 1 sd away from mean')
plt.ylabel('Appointments')
plt.show()

# Comparing Medical Conditions to No Shows

mc_list_S = []
mc_list_NS = []
for ailment in med_cond_list:
    mc_list_S.append(ret_sum(df_n,ailment))
    mc_list_NS.append(ret_sum(df_y,ailment))
mc_title = ['Medical Condition Show vs. No-Show']
bar_plots(mc_list_S,mc_list_NS,4,med_cond,'patients',sn_legend,mc_title)

#comparing scholarship values to no show

df_S_y = df[['Scholarship','No-show']][(df.Scholarship == 1)&(df['No-show'] =='Yes')]
df_S_n = df[['Scholarship','No-show']][(df.Scholarship == 1)&(df['No-show'] == 'No')]
bar_plots(app_per(df_S_y), app_per(df_S_n),1,['Show vs. No-Show'],'Percent total Appointments', sn_legend,
          "Ratio of Scholarship vs no-show to total appointments")
#compare SMS

df_SMS_y = df_y.SMS_received.describe()
df_SMS_n = df_n.SMS_received.describe()
plt.bar([0,1],[100*df_SMS_y['mean'],100*df_SMS_n['mean']],.5, color=['red','yellow'])
plt.title('SMS percentage')
plt.ylabel('Percent recieved SMS')
plt.xticks([0,1],sn_legend)
plt.show()

#Multivariable on Age and Scholarship
df_mva_y = df[['Age','Scholarship','No-show']][(df['Scholarship']==1) & (df['Age']<= 25) & (df['No-show'] == 'Yes')]
df_mva_yo = df[['Age','Scholarship','No-show']][(df['Scholarship']==1) & (df['Age']>= 25) & (df['No-show'] == 'Yes')]
df_mva_yns = df[['Age','Scholarship','No-show']][(df['Scholarship']==0) & (df['Age']<= 25) & (df['No-show'] == 'Yes')]
plt.bar([0,1,2],[app_per(df_mva_y),app_per(df_mva_yo),app_per(df_mva_yns)],width=.5, color=['cyan','yellow','red'])
plt.title('Age, Bolsa Familia, and No-showing to appointments')
plt.ylabel('Percentage of Appointments')
plt.xticks([0,1,2],['Bolsa Familia under 25','Bolsa Familia over 25', 'No BF, under 25'])
plt.show()

