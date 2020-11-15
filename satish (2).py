import pandas as pd
dataset_name='raw_cdr_data.csv'
df=pd.read_csv(dataset_name,header= None, low_memory=False)

print(df[9].sample(4).tolist())

#list of string
data=["20190620032717.906","20190620052652.52",'','20190620052735.207']
import re
print(re.match("^\d" , str(data[2])))

data=["20190620032717.906","20190620052652.52",'','20190620052735.207']
regex=re.compile("\d{1,8}")
a=regex.findall(str(data[0]))

print(type(a))
print(len(a))
print(a[0])
print(a[1])
print(a)

import numpy as np
data=["20190620032717.906","20190620052652.52",'','20190620052735.207']
def datetime_divider(data):
    for index in range (len(data)):
        if (re.match("^\d",str(data[index]))):
            regex=re.compile("\d{1,8}")
            a=regex.findall(str(data[index]))
            data[index]=[a[0],a[1]]
        else:
            data [index] = [np.nan,np.nan]
    return data

data=["20190620032717.906","20190620052652.52",'','20190620052735.207']
print(datetime_divider(data))

data=["20190620032717.906","20190620052652.52",'','20190620052735.207']
print(*datetime_divider(data))

data=["20190620032717.906","20190620052652.52",'','20190620052735.207']
result=zip(*datetime_divider(data))
print(list(result))


data=["20190620032717.906","20190620052652.52",'','20190620052735.207']
date,time=zip(*datetime_divider(data))

print(date)
print(time)




def date_modifier (data):
    for index in range(len(data)):
        if(re.match("^\d", str(data[index]))):
            year=str(data[index][:4])
            month=str(data[index][4:6])
            day=str(data[index][6:])
            data[index]="-".join([year,month,day])
            
        else:
            data[index]=np.nan
    return data
data=['20190620','20190620',np.nan,'20190620']
result=date_modifier(data)
print(result)

def time_modifier(data):
    for index in range(len(data)):
        if(re.match("^\d", str(data[index]))):
            hours=int(data[index][:2])
            minutes=data[index][2:4]
            sec=data[index][4:]
            
            if (hours>=12):
                if hours==12:
                    hr=str(hours)
                else:
                    hr=str(hours-12)
                meridiem="PM"
            else:
               if hours==0:
                   hr=str(12)
               else:
                    hr=str(hours)
               meridiem="AM"
        data[index]=":".join([hr,minutes,sec])+""+meridiem
    else:
          
          data[index]=np.nan
          return data
      
data=['032717', '052652', np.nan, '052735']
result=time_modifier(data)
print(result)

df[5]
df[5].unique()
df[5].value_counts(dropna=False)

df[267]
df[267].unique()

df[312]
df[312].unique()


def replace_simple_with_standard_terminology(dataframe):
    dataframe[5]=dataframe[5].replace('Originating','Outgoing')
    dataframe[5]=dataframe[5].replace('Terminating','Incoming')
    
    dataframe[267]=dataframe[267].replace('Success','Voice Portal')
    dataframe[312]=dataframe[312].replace('Shared Call Appearence','Secondary Devices')
    return dataframe
    
    
import numpy as np
def remove_unwanted_data(datacolumn):
    for index in range(len(datacolumn)):
        if (datacolumn[index]=='Primary Device' or datacolumn[index]=='Secondary Device'):
            continue
        else:
            datacolumn[index]=np.nan
    return datacolumn


df[[147,312,267]]
df[147].unique()
df[147].value_counts(dropna=False)





import numpy as np
def combine_All_Services(data1,data2,data3):
    for index in range(len(data1)):
        if (data1[index] is np.nan):
            if(data2[index] is not np.nan and data3[index] is not np.nan):
                data1[index]=str(data2[index])
            elif(data2[index] is not np.nan):
                data1[index]=data2[index]
            else:
                data1[index]=data3[index]
        else:
            continue
    return data1

def call_time_fetcher(data):
    for index in range(len(data)):
        data[index] = str(data[index])
        if data[index]!='nan':
            year=data[index][:4]
            month=data[index][4:6]
            day=data[index][6:8]
            hours=data[index][8:10]
            minutes=data[index][10:12]
            seconds=str(round(float(data[index][12:])))
            if int(seconds)>=60:
                seconds=int(seconds)-60
                minutes=int(minutes)+1
            if int(minutes)>=60:
                hours=int(hours)+1
                minutes=int(minutes)-60
            data[index]=f"{year}-{month}-{day} {hours}:{minutes}:{seconds}"
        else:
            data[index]=np.nan
    return data
            
            
        






import numpy as np
import pandas as pd
import datetime
import re

#there was some indentation issue 
def hourly_range(data):
    for index in range(len(data)):
        data[index]=str(data[index])
        if data[index]!="nan":
            if re.search("PM",data[index]):
                time_data=re.findall("\d+", data[index])
                if time_data[0]!="12":
                    time_data=int(time_data[0]+12)
                else:
                    time_data=time_data[0]
            else:
                time_data=re.findall("\d+", data[index])
                if int(time_data[0])==12:
                    time_data=f"0{int(time_data[0])-12}"
                else:
                    time_data=time_data[0]
            data[index]=f"{time_data}:00-{time_data}:59"
        else:
            data[index]=np.nan
                                 
    return data



data=['3:27:17AM', '5:26:52AM', 'nan','5:27:35AM']
result=hourly_range(data)
print(result)



def weekly_range(data):
    for index in range(len(data)):
        data[index] = str(data[index])
        if data[index]!="nan":
            year,month,day=[int(x) for x in data[index].split("-")]
            result=datetime.date(year,month,day)
            data[index]=result.strftime("%A")
        else:
            data[index]=np.nan
    return data
data=['2019-06-20','2019-06-20','nan','2019-06-20']
result=weekly_range(data)
print(result)



import pandas as pd
import webbrowser
import dash
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_core_components as dcc

import plotly.graph_objects as go
import plotly.express as px

import dash_bootstrap_components as dbc
import dash_table as dt
import re

app=dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
project_name=None


def load_data():
    
    
    call_dataset_name="Call_data.csv"
    service_dataset_name="Service_data.csv"
    device_dataset_name="Device_data.csv"
    
    global call_data
    call_data=pd.read_csv(call_dataset_name)
    
    global service_data
    service_data=pd.read_csv(service_dataset_name)
    
    global device_data
    device_data=pd.read_csv(device_dataset_name)


    
    global start_date_list
    temp_list=sorted(  call_data["date"].dropna().unique().tolist()   )
    start_date_list=[ {"label":str(i) , "value":str(i) } for i in temp_list]
    
    
    global end_date_list
    end_date_list=start_date_list
    
   
    temp_list=["Hourly","Daywise","Weekly"]
    global report_type_list
    #wrong variable name was used 
    report_type_list=[ {"label":str(i), "value":str(i) } for i in temp_list]
    
   




def open_browser():
    webbrowser.open_new('http://127.0.0.1:8050/')
    
    
def create_app_ui():
    main_layout=html.Div(
    [
    html.H1('CDR Analysis with Insights', id='Main_title'),
    
    dcc.Tabs(id="Tabs", value="tab-1",children=[
    dcc.Tab(label="Call Analytics tool", id="Call Analytics tool", value="tab-1", children=[
    html.Br(),
    html.Br(),
    
    
    dcc.Dropdown(
        id='start-date-dropdown',
        options=start_date_list,
        placeholder='Select starting Date here',
        value='2019-06-20'
        ),
    
    
    dcc.Dropdown(
        id='end-date-dropdown',
              options=end_date_list,
              placeholder='Select ending date here',
              value='2019-06-25'
        ),
    
    
    dcc.Dropdown(
                   id='group-dropdown',
                   placeholder='Select Group here',  
                   multi=True
        ),
    
    
    dcc.Dropdown(
                  id='Report-type-dropdown',
                  options=report_type_list,
                  placeholder='Select Report Type',
                  value='Hourly'
       )] ),
    dcc.Tab(label="Device Analytics tool", id="Device Analytics tool", value="tab-2", children=[
        html.Br(),
        dcc.Dropdown(
            id='device-date-dropdown',
            options=start_date_list,
            placeholder="select Date here",
            multi=True
            ),
        html.Br()]),
        dcc.Tab(label="Service Analytics tool", id="Service Analytics tool", value="tab-3", children=[
        html.Br(),
        dcc.Dropdown(
            id='service-date-dropdown',
            options=start_date_list,
            placeholder="Select Date Here",
            multi=True
            ),
        html.Br()]),
    ]),
    html.Br(),
    dcc.Loading(html.Div(id='visualization-object', children='Graph, Card, Data Table')),
    ])
    
    
    
    return main_layout


def create_card(title,content,color):
    card=dbc.Card(
        dbc.CardBody(
            [
                html.H4(title),
                html.Br(),
                html.Br(),
                html.H2(content),
                html.Br(),
                ]
            ),
            color=color, inverse=True
        )
    return(card)

def count_devices(data):
    
    device_dict={"Polycom":0,
    "Windows":0,
    "iphone":0,
    "Android":0,
    "Mac":0,
    "Yealink":0,
    "Aastra":0,
    "Others":0}
    
    reformed_data=data["UserDeviceType"].dropna().reset_index()
    for var in reformed_data["UserDeviceType"]:
        if re.search("Polycom",var):
            device_dict["Polycom"]+=1
        elif re.search("Yealink",var):
            device_dict["Yealink"]+=1
        elif re.search("Aastra",var):
            device_dict["Aastra"]+=1
            
        elif re.search("Windows",var):
            device_dict["Windows"]+=1
        elif re.search("iphone|ios",var):
            device_dict["iphone"]+=1
        elif re.search("Mac",var):
            device_dict["Mac"]+=1
        elif re.search("Android",var):
            device_dict["Android"]+=1
            
        else:
            device_dict["Others"]+=1
    final_data=pd.DataFrame()
    final_data["Device"]=device_dict.keys()
    final_data["Count"]=device_dict.values()
    return final_data



            
     
                



@app.callback(
    Output('visualization-object', 'children'),
    [
    Input("Tabs","value"),
    Input('start-date-dropdown', 'value'),
    Input('end-date-dropdown', 'value'),
    Input('group-dropdown', 'value'),
    Input('Report-type-dropdown', 'value'),
    Input('device-date-dropdown','value'),
    Input('service-date-dropdown','value')
    ]
    )



def update_app_ui(Tabs,start_date,end_date,group,report_type,device_date,service_date):
    
    print('Data type of start_date value=', str(type(start_date)))
    print('Data of start_value=', str(start_date))
    
    print('Data type of end_date value=', str(type(end_date)))
    print('Data of end_date value=', str(end_date))
    
    print('Data type of group value=', str(type(group)))
    print('data of group value=', str(group))
    
    print('Data type of report_type value=', str(type(report_type)))
    print('Data of report_type value', str(report_type))
    
    print('Data type of device_date value=', str(type(device_date)))
    print('Data of device_date value=', str(device_date))
    
    print('Data type of service_date value=', str(type(service_date)))
    print('Data of service_date value=',str(service_date))
    
    if Tabs=="tab-1":
        call_analytics_data=call_data[(call_data["date"]>=start_date) & (call_data["date"]<=end_date)]
        
        if group==[] or group is None:
              pass
        else:
              call_analytics_data=call_analytics_data[call_analytics_data["Group"].isin(group)]

        graph_data=call_analytics_data
    
        if report_type=="Hourly":
            graph_data=graph_data.groupby("hourly_range")["Call_Direction"].value_counts().reset_index(name="count")
            x="hourly_range"
            content=call_analytics_data["hourly_range"].value_counts().idxmax()
            title="Busiest Hour"
   
        elif report_type=="Daywise":
            graph_data=graph_data.groupby("date")["Call_Direction"].value_counts().reset_index(name="count")
            x="date"
            content=call_analytics_data["date"].value_counts().idxmax()
            title="Busiest Day"
        
   
        else:
            #it should be weekly_range not Weekly_range
            graph_data=graph_data.groupby("weekly_range")["Call_Direction"].value_counts().reset_index(name="count")
            x="weekly_range"
        
        content=call_analytics_data["weekly_range"].value_counts().idxmax()
        title="Busiest Weekday"
        
        figure=px.area(graph_data,
                       x=x,
                       y="count",
                       color="Call_Direction",
                       hover_data=["Call_Direction","count"],
                       template="plotly_dark")
                    
        figure.update_traces(mode="lines+markers")
                   
       
    
    
        total_calls=call_analytics_data["Call_Direction"].count()
        card_1=create_card("Total Calls", total_calls, "success")
    
    
        incoming_calls=call_analytics_data["Call_Direction"][call_analytics_data["Call_Direction"]=="Incoming"].count()
        card_2=create_card("Incoming Calls", incoming_calls, "primary")
    
        outgoing_calls=call_analytics_data["Call_Direction"][call_analytics_data["Call_Direction"]=="Outgoing"].count()
        card_3=create_card("Outgoing Calls", outgoing_calls, "warning")
    
        missed_calls=call_analytics_data["Missed Calls"][call_analytics_data["Missed Calls"]==3].count()
        card_4=create_card("Missed Calls", missed_calls, "danger")
    
    
        max_duration=call_analytics_data["duration"].max()
        card_5=create_card("Max Duration", f'{max_duration}  min', "info")
    
        card_6=create_card(title,content,"primary")
    
    
    
        graphRow0 =dbc.Row([dbc.Col(id='card1', children=[card_1], md=3), dbc.Col(id='card2',children=[card_2], md=3)])
        graphRow1=dbc.Row([dbc.Col(id='card3', children=[card_3], md=3), dbc.Col(id='card4',children=[card_4], md=3)])
        graphRow2=dbc.Row([dbc.Col(id='card5', children=[card_5], md=3), dbc.Col(id='card6',children=[card_6], md=3)])
    
    
        cardDiv=html.Div([graphRow0,html.Br(), graphRow1,html.Br(), graphRow2])
    
        datatable_data=call_analytics_data.groupby(["Group","UserID","UserDeviceType"])["Call_Direction"].value_counts().unstack(fill_value=0).reset_index()
        if call_analytics_data["Missed Calls"][call_analytics_data["Missed Calls"]==19].count()!=0:
            datatable_data["Missed Calls"]=call_analytics_data.groupby(["Group","UserID","UserDeviceType"])["Missed Calls"].value_counts().unstack()[3]
        else:
            datatable_data["Missed Calls"]=0
    
        datatable_data["Total_call_duration"]=call_analytics_data.groupby(["Group","UserID","UserDeviceType"])["duration"].sum().tolist()
    
    
        datatable=dt.DataTable(
            id='table',
            columns=[{"name": i, "id": i} for i in datatable_data.columns],
            data=datatable_data.to_dict('records'),
            page_current=0,
            page_size=5,
            page_action='native',
            style_header={'backgroundColor':'rgb(30,30,30'},
            style_cell={
                'backgroundColor':'rgb(50,50,50)',
                'color':'white'
                }
            )
        
    
   
        return [
            dcc.Graph(figure=figure),
            html.Br(),
            cardDiv,
            html.Br(),
            datatable
            ]
    elif Tabs=="tab-2":
         
        if device_date is None or device_date==[]:
              
              device_analytics_data=count_devices(device_data)
        else:
            device_analytics_data=count_devices(device_data[device_data["DeviceEventDate"].isin(device_date)])
            fig=px.pie(device_analytics_data,names="Device", values="Count", color="Device", hole=.3)
            fig.update_layout(autosize=True,
                              margin=dict(l=0, r=0, t=25, b=20),
                              )
            return dcc.Graph(figure=fig)
        
    elif Tabs=="tab-3":
        if service_date is None or service_date==[]:
            service_analytics_data=service_data["FeatureName"].value_counts().reset_index(name="Count")
        else:
            service_analytics_data=service_data["FeatureName"][service_data["FeatureEventDate"].isin(service_date)].value_counts().reset_index(name="Count")
            fig=px.pie(service_analytics_data,names="index", values="Count", color="index")
            fig.update_layout(autosize=True,
                              margin=dict(l=0, r=0, t=25, b=20),
                              )
            return dcc.Graph(figure=fig)
        
    else:
        return None
            
        
        


@app.callback(
    Output('group-dropdown'  ,  'options'  ),
    [
    Input( 'start-date-dropdown'  ,  'value' ),
    Input( 'end-date-dropdown'  ,  'value' )
    ]
    )



def update_groups(start_date, end_date):
    
   reformed_data=call_data[(call_data["date"]>=start_date) & (call_data["date"]<=end_date)]
   group_list=reformed_data["Group"].unique().tolist()
   group_list=[{"label":m, "value":m}  for m in group_list]
    
   return group_list
        
    
    
    
def main():
    
    
    load_data()
    open_browser()
    
    global app, project_name
    project_name="CDR Analysis with Insights"
    
    app.layout=create_app_ui()
    app.title=project_name
    
    
    app.run_server()
    
    print("This would be executed only after the script is closed")
    app=None
    project_name=None
    
    global call_data, service_data, device_data, start_date_list, end_date_list, report_type_list
    call_data=None
    service_data=None
    device_data=None
    start_date_list=None
    end_date_list=None
    report_type_list=None
    
    
if __name__ == '__main__':
    main()
    
    
  
  
    





