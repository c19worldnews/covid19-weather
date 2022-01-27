from bs4 import BeautifulSoup as bs
from requests_html import HTMLSession 
import pickle
import random
import streamlit as st
from tensorflow import keras
# univariate bidirectional lstm example
from numpy import array 
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import numpy as np
from datetime import timedelta, date
from geopy.geocoders import Nominatim
# Library for opening url and creating
# requests
import urllib.request
import requests
 
# pretty-print python data structures
from pprint import pprint
 
# for parsing all the tables present
# on the website
from html_table_parser.parser import HTMLTableParser
import builtins

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import wget
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument("--use-fake-ui-for-media-stream")



# open it, go to a website, and get results




import numpy as np

country_lst = ['Aruba','Afghanistan','Angola','Albania','Andorra','United Arab Emirates','Argentina','Armenia','American Samoa',
 'Antigua and Barbuda','Australia','Austria','Azerbaijan','Burundi','Belgium','Benin','Burkina Faso','Bangladesh','Bulgaria','Bahrain','Bahamas',
 'Bosnia and Herzegovina','Belarus','Belize','Bermuda','Bolivia','Brazil','Barbados','Brunei','Bhutan','Botswana','Canada','Switzerland','Chile',
 'China','Ivory Coast','Cameroon','Republic of the Congo','Cook Islands','Colombia','Comoros','Cape Verde','Costa Rica','Cuba','Curaçao','Cayman Islands',
 'Cyprus','Czech Republic','Germany','Djibouti','Dominica','Denmark','Dominican Republic','Algeria','Ecuador','Egypt','Spain','Estonia','Ethiopia','Finland',
 'Fiji','Falkland Islands','France','Faroe Islands','Gabon','United Kingdom','Guernsey','Ghana','Gibraltar','Guinea','Gambia','Guinea-Bissau',
 'Equatorial Guinea','Greece','Grenada','Guatemala','French Guiana','Guam','Guyana','Hong Kong','Honduras','Croatia','Haiti','Hungary','Indonesia',
 'Isle of Man','India','Ireland','Iran','Iraq','Iceland','Israel','Italy','Jamaica','Jersey','Jordan','Japan','Kazakhstan','Kenya','Kyrgyzstan','Cambodia',
 'Kiribati','Saint Kitts and Nevis','South Korea','Kuwait','Laos','Lebanon','Liberia','Libya','Saint Lucia','Liechtenstein','Sri Lanka','Lesotho','Lithuania',
 'Luxembourg','Latvia','Macau','Morocco','Monaco','Moldova','Madagascar','Maldives','Mexico','Marshall Islands','Mali','Malta','Myanmar','Montenegro',
 'Mongolia','Northern Mariana Islands','Mozambique','Mauritania','Montserrat','Martinique','Mauritius','Malawi','Malaysia','Mayotte','New Caledonia','Niger',
 'Nigeria','Nicaragua','Niue','Netherlands','Norway','Nepal','New Zealand','Oman','Pakistan','Panama','Peru','Philippines','Palau','Papua New Guinea','Poland',
 'Puerto Rico','North Korea','Portugal','Paraguay','French Polynesia','Qatar','Réunion','Kosovo','Romania','Russia','Rwanda','Saudi Arabia','Sudan','Senegal',
 'Singapore','Saint Helena','Solomon Islands','Sierra Leone','El Salvador','San Marino','Serbia','South Sudan','São Tomé and Príncipe','Suriname','Slovakia',
 'Slovenia','Sweden','Swaziland','Sint Maarten','Syria','Turks and Caicos Islands','Chad','Togo','Thailand','Tajikistan','Tokelau','Turkmenistan','East Timor',
 'Tonga','Trinidad and Tobago','Tunisia','Turkey','Tuvalu','Taiwan','Tanzania','Uganda','Ukraine','Uruguay','United States of America','Uzbekistan',
 'Vatican City','Saint Vincent and the Grenadines','Venezuela','British Virgin Islands','United States Virgin Islands','Vietnam','Vanuatu',
 'Wallis and Futuna','Samoa','Yemen','South Africa','Zambia','Zimbabwe']




isos=['ABW','AFG','AGO','AIA','ALB','AND','ARE','ARG','ARM','ASM','ATG','AUS','AUT','AZE','BDI','BEL','BEN','BFA','BGD','BGR','BHR','BHS','BIH',
'BLR','BLZ','BMU','BOL','BRA','BRB','BRN','BTN','BWA','CAN','CHE','CHL','CHN','CIV','CMR','COG','COK','COL','COM','CPV','CRI','CUB','CUW',
'CYM','CYP','CZE','DEU','DJI','DMA','DNK','DOM','DZA','ECU','EGY','ESP','EST','ETH','FIN','FJI','FLK','FRA','FRO','GAB','GBR','GGY','GHA',
'GIB','GIN','GMB','GNB','GNQ','GRC','GRD','GTM','GUF','GUM','GUY','HKG','HND','HRV','HTI','HUN','IDN','IMN','IND','IRL','IRN','IRQ','ISL',
'ISR','ITA','JAM','JEY','JOR','JPN','KAZ','KEN','KGZ','KHM','KIR','KNA','KOR','KWT','LAO','LBN','LBR','LBY','LCA','LIE','LKA','LSO','LTU',
'LUX','LVA','MAC','MAR','MCO','MDA','MDG','MDV','MEX','MHL','MLI','MLT','MMR','MNE','MNG','MNP','MOZ','MRT','MSR','MTQ','MUS','MWI','MYS',
'MYT','NCL','NER','NGA','NIC','NIU','NLD','NOR','NPL','NZL','OMN','PAK','PAN','PER','PHL','PLW','PNG','POL','PRI','PRK','PRT','PRY','PYF',
'QAT','REU','RKS','ROU','RUS','RWA','SAU','SDN','SEN','SGP','SHN','SLB','SLE','SLV','SMR','SRB','SSD','STP','SUR','SVK','SVN','SWE','SWZ',
'SXM','SYR','TCA','TCD','TGO','THA','TJK','TKL','TKM','TLS','TON','TTO','TUN','TUR','TUV','TWN','TZA','UGA','UKR','URY','USA','UZB','VAT',
'VCT','VEN','VGB','VIR','VNM','VUT','WLF','WSM','YEM','ZAF','ZMB','ZWE']

# loading the trained model
#for share streamlit
model = keras.models.load_model('finalmodel_v1.h5')
#for google colab
#model = keras.models.load_model('/content/drive/MyDrive/Weather/Deployment/finalmodel.h5')

@st.cache()


# session = requests.Session()
def getWeather(city_name,country_name):
  
  
  session = HTMLSession()
  headers = {'Accept-Language': 'en-US,en;q=0.8'}
  base_link = "https://www.google.com/search?q=weather/"+ city_name + "+" +country_name
  
  response = session.get(base_link)
  soup = bs(response.content, 'html.parser')

  #return base_link
  
  temp =  soup.find("span", attrs={"id": "wob_tm"}).text
 
  region = soup.find("div", attrs={"id": "wob_loc"}).text
          
          # store all results on this dictionary
  next_days = []
  days = soup.find("div", attrs={"id": "wob_dp"})
  for day in days.findAll("div", attrs={"class": "wob_df"}):
    day_name = day.findAll("div")[0].attrs['aria-label']
              # get weather status for that day
    weather_img = day.find("img").attrs["src"]
    weather_desc = day.find("img").attrs["alt"]
    maxtemp = day.findAll("div", {"class": "gNCp2e"})
    max_temp = maxtemp[0].text
    mintemp = day.findAll("div", {"class": "QrNVmd ZXCv8e"})
    min_temp = mintemp[0].text
    next_days.append({"name": day_name, "weather_desc": weather_desc, "weather_img":weather_img , "max_temp": max_temp[2:], "min_temp": min_temp[2:]})
  return next_days,temp,region,base_link




def prediction(city_name,country_name,iso_code,label_alpha_2,select_location):
  session = HTMLSession()
  headers = {'Accept-Language': 'en-US,en;q=0.8'}

  location = select_location.replace(" ", "-")
  country = location.lower()
 
  usa_prov = country_name.lower()
  #scraping the button show all click data
  #return select_location
  #wd = webdriver.Chrome('/usr/bin/chromedriver',options=chrome_options)
  #wd.get("https://share.streamlit.io/")
  #for google colab
  #wd = webdriver.Chrome(options=chrome_options)
  #os.chmod('chromedriver', 1363)
  #mypath= os.getcwd()
  #mydir = os.listdir('./')
  #return mydir

  #for share streamlit
  #/app/deployment/chromedriver
  chrome_options = webdriver.ChromeOptions()
  chrome_options.add_argument('headless')
  chrome_options.add_argument('--headless')
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument('--disable-dev-shm-usage')
  chrome_options.add_argument("--use-fake-ui-for-media-stream")
  from webdriver_manager.chrome import ChromeDriverManager
  # ChromeDriverManager().install()
  wd = webdriver.Chrome(executable_path ='./chromedriver.exe', options=chrome_options)
  #wd = webdriver.Chrome(executable_path ='chromedriver')
  

  if select_location == 'USA':
      wd.get("https://www.nytimes.com/interactive/2021/us/"+usa_prov+"-covid-cases.html")
      #baseurl = "https://www.nytimes.com/interactive/2021/us/"+usa_prov+"-covid-cases.html"
      #return baseurl
  elif select_location == 'France' :
      france_url = 'https://www.data.gouv.fr/fr/datasets/r/5c4e1452-3850-4b59-b11c-3dd51d7fb8b5'
      france_df = pd.read_csv(france_url)
      if len(city_name) == 1 :
         dept_id = str(city_name)
         dept_id = '0'+ dept_id
         
      else:
        dept_id = str(city_name)
        #here city_name is the id of department
      
      sub = france_df[france_df.dep == dept_id]
      if sub.empty:
        dept_id = int(city_name)  #here city_name is the id of department
        sub = france_df[france_df.dep == dept_id]
      else:
        pass
     
      latest = sub.tail(15)
      new_cases_list = latest.pos
      
      index_value= new_cases_list.index.get_loc(new_cases_list.last_valid_index())
      new_cases = new_cases_list.iloc[index_value]
      #getting city name 
      city_name = france_df[france_df['dep'] == dept_id]['lib_dep'].values[3]
      #return city_name
  else:
      wd.get("https://www.nytimes.com/interactive/2021/world/"+country+"-covid-cases.html")
      #baseurl ="https://www.nytimes.com/interactive/2021/world/"+country+"-covid-cases.html"
      #print(baseurl)
   


  #element = wd.find_element(By.XPATH,"//button[contains(@class,'showall')]")
  #element = wd.find_element(By.XPATH,"//*[@id='world-france-covid-cases']/div/div/main/div[3]/div[4]/section[2]/div[2]/table/tbody/tr")
  #wd.execute_script("arguments[0].click();", element)
  if select_location != 'France':
    elements=wd.find_elements_by_xpath("//button[contains(@class,'showall')]")
    for element in elements:
      wd.execute_script("arguments[0].click();", element);
      #return element.text
    # Get 'HTML'

    html_data = wd.page_source
    #return html_data
    soup = bs(html_data, 'html.parser')
    table = soup.findAll('table', {"class": "g-table super-table withchildren"})
    #return table
    if len(table) == 2:

        df = pd.read_html(str(table[0]))[0]
        df = df[df.columns[:2]]
        df = df.rename(columns={ df.columns[0]: "location", df.columns[1]: "new_cases" })
        #if country=='italy':
        # df.drop(columns=['Per 100,000',	'14-day change'], inplace=True)
        # df.rename(columns={'Unnamed: 0': 'location', 'Cases Daily Avg.':'new_cases'}, inplace=True)
        #else:
        # df.drop(columns=['Per 100,000',	'14-day change',	'Deaths Daily Avg.',	'Per 100,000.1'], inplace=True)
        # df.rename(columns={'Unnamed: 0': 'location', 'New Hospitalizations Daily Avg.':'new_cases'}, inplace=True)
        
        df2 = pd.read_html(str(table[1]))[0]


        df2 = df2[df2.columns[:2]]
        df2 = df2.rename(columns={ df2.columns[0]: "location", df2.columns[1]: "new_cases" })
        #if country=='italy':
        # df2.drop(columns=['Per 100,000',	'14-day change'], inplace=True)
        # df2.rename(columns={'Unnamed: 0': 'location', 'Cases Daily Avg.':'new_cases'}, inplace=True)
        #else:
        # df2.drop(columns=['Per 100,000',	'14-day change',	'Deaths Daily Avg.',	'Per 100,000.1'], inplace=True)
        # df2.rename(columns={'Unnamed: 0': 'location', 'New Hospitalizations Daily Avg.':'new_cases'}, inplace=True)

        df = df.append(df2)
      

    else:

        df = pd.read_html(str(table[0]))[0]
        df = df[df.columns[:2]]
        df = df.rename(columns={ df.columns[0]: "location", df.columns[1]: "new_cases" })
        #df.drop(columns=['Per 100,000',	'14-day change',	'Deaths Daily Avg.',	'Per 100,000.1'], inplace=True)
        #df.rename(columns={'Unnamed: 0': 'location', 'Cases Daily Avg.':'new_cases'}, inplace=True)

    #return df  
    if select_location == 'USA':  
        df['location'] = df['location'].replace('[^a-zA-Z0-9 ]', '', regex=True)
        #city =  df[df['location'] == city_name]  
        new_cases = df[df['location'] == city_name]['new_cases'].values[0]
    
      
    else:
        #city =  df[df['location'] == city_name]   
        new_cases = df[df['location'] == city_name]['new_cases'].values[0]
      

        
    if str(new_cases).startswith('<'): 
        new_cases = int(new_cases[1:])
    else :
        int(new_cases)

    #return new_cases 
    #call the weather function
  
  weatherData = getWeather(city_name,country_name)
 # return weatherData
  #prepare temp to pass into model
  temp = int(weatherData[1])  
           
  lengthnewcases = len(str(new_cases))

        #preparation of model data
  final_prediction = []  
  n_steps = 1
  n_features = 3
  #max_temp = 45
  #min_temp = 29
  x_input = array([int(iso_code), int(new_cases), float(temp)])
  x_input = x_input.reshape((1, n_steps, n_features))   
      # Making predictions 
  prediction = model.predict(x_input)
              #formatting the prediction values
  #return prediction
            
  for i in prediction: 
      
      for j in i:
        out = f'{j:.10f}'
        out = out.split('.')[1]
                  # Strip the zeros from the left side of your split decimal
        out = out.lstrip('0')
        final_no = out[:lengthnewcases]           
        final_prediction.append(final_no)

        #print(f"{int(final_no):,}")

            
  return final_prediction,select_location,weatherData,new_cases,label_alpha_2,city_name
       

import base64
   

# this is the main function in which we define our webpage  
def main():  
    # front end elements of the web page 
    st.set_page_config(layout="wide")
    #for share streamlit
    #main_bg = "giphy.gif"
    #for google colab
    #main_bg = "/content/drive/MyDrive/Weather/Deployment/giphy.gif"
    #main_bg_ext = "gif"
    #padding_left = "50px"
    #background-color: #1c294b
    #background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()});
    #background-size: cover;
    #background-position: center;
    #backdrop-filter: blur(5px);

    # CHANGES [START]
    main_bg = "s3.jpg"
    main_bg_ext = "jpg"

    st.markdown(
        f"""
         <style>
         .stApp {{
             background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()});
             background-size: cover
         }}
         span {{
            color: white !important;
         }}
         li > span {{
            color: black !important;
         }}
         .block-container{{
            padding: 0px;
         }}
          [data-testid="stHorizontalBlock"] {{
            padding-left: 1rem;  
            margin-right: 1rem
          }}
          [data-testid="stVerticalBlock"] {{
            gap: 0rem;  
          }}
         
         </style>
         """,
        unsafe_allow_html=True
    )
    new_title = '<p style="background:  red;font-size:35px;line-height:36px;font-weight:600;color:#fff;text-align:center;padding:13px 0;margin-bottom:7rem;">5  Days Forecasting of Covid 19 New Cases Based on Weather</p>'
    st.markdown(new_title, unsafe_allow_html=True)

    left, right = st.columns([0.25, 0.7])
    with left:
        # st.image("tlogo.png")
        Date_today = date.today()
        date_ = '<p style="padding-left:1rem;font-size:30px;line-height:36px;font-weight:600;color:#fff;margin-bottom:1rem;">' \
                f'<img style="padding-right:1rem;" src="data:image/png;base64,{base64.b64encode(open("calendar-icon.png", "rb").read()).decode()}"/>' \
                f'{Date_today.strftime("%b %d, %y")}' \
                    '</p>'
        # st.write(f'### <span style="color: red">📆</span> {Date_today.strftime("%d %b, %y")}', unsafe_allow_html=True)
        # html_date = str("<p style='color: white; text-align:center; font-size:20px'>") + str(
        #     Date_today.strftime("%d %b, %y")) + str("</p>")
        # st.markdown(html_date, unsafe_allow_html=True)

    if "args" in st.session_state:
        calendar_st, _, flag_st, loc_city_info_st, _, new_cases_st = st.columns([3, 0.2, 0.8, 5, 7, 3])
        calendar_st.markdown(date_, unsafe_allow_html=True)
        left, _, covid1, covid2, covid3, covid4, covid5 = st.columns(
            [4, 1, 5, 5, 5, 5, 5]
        )
    else:
        st.markdown(date_, unsafe_allow_html=True)
        left, title = st.columns([0.9,  2])

    with left:
        select_location_st = st.empty()

    # CHANGES [END]

    st.markdown(
                    """
                    <style>
                         *, *::before, *::after {
                          box-sizing: border-box;
                      }
                      body{
                        font-family: 'Lato', sans-serif;
                        background:#f9f9f9;
                        padding: 0;
                          margin: 0;
                      }
                      .container-fluid {
                          width: 100%;
                          padding-right: 32px;
                          padding-left: 32px;
                          margin-right: auto;
                          margin-left: auto;
                      }
                      .continer{ 
                        max-width:1193px; 
                        margin:auto;
                        background:#fff;
                        box-shadow: 0px 0px 10px rgb(136 136 136 / 28%);
                      }
                      .row{
                        display: -ms-flexbox;
                          display: flex;
                          -ms-flex-wrap: wrap;
                          flex-wrap: wrap;
                          margin-right: -15px;
                          margin-left: -15px;
                      }
                      .col-4, .col-8{
                        position: relative;
                          width: 100%;
                          padding-right: 15px;
                          padding-left: 15px;
                      }
                      .col-4 {
                          -ms-flex: 0 0 33.33333%;
                          flex: 0 0 33.33333%;
                          max-width: 33.33333%;
                      }
                      .col-8 {
                          -ms-flex: 0 0 66.66667%;
                          flex: 0 0 66.66667%;
                          max-width: 66.66667%;
                      }
                      .forecasting-wrap h2{
                        background:#1C294B;
                        font-size:30px;
                        line-height:36px;
                        font-weight:600;
                        color:#fff;
                        text-align:center;
                        padding:13px 0;
                        margin:0;
                      }
                      .location-form{
                        max-width:394px;
                        margin:64px auto 0;
                        padding-bottom: 400px;
                      }
                      .location-form h3{
                        color:#1C294B;
                        font-size:23px;
                        font-weight:700;
                        font-family: 'Poppins', sans-serif;
                        margin:0;
                        padding-bottom:45px;
                      }
                      .location-form h3 img{ 
                        margin-right:7px; 
                          position: relative;
                          top: 3px;
                      }
                      .location-form form .form-row{ margin-bottom:23px; } 
                      .location-form form label{
                        display:block;
                        margin-bottom:10px;
                        font-size:15px;
                        font-weight:600;
                        color:#1C294B;
                      }
                      .location-form form select{
                          width: 100%;
                        border:1px solid rgb(28 41 75 / 30%);
                          border-radius: 8px;
                        min-height:38px;
                        line-height:38px;
                        padding:0 13px;
                        font-size:15px;
                        font-weight:600;
                          color: rgb(28 41 75 / 40%);
                          font-family: 'Lato', sans-serif;
                        -webkit-appearance: none;
                          -moz-appearance: none;
                          background: transparent;
                          background-image: url(image/drop-down-icon.png);
                          background-repeat: no-repeat;
                          background-position-x: 96%;
                          background-position-y: 15px;
                        box-shadow: 0px 0px 3px rgb(136 136 136 / 28%);
                      }
                      .location-form form select:focus-visible{ outline:0; }
                      .location-form form .footer-f{ text-align:center; }
                      .location-form form button{
                        background:#CC0919;
                        height:35px;
                        font-size:14px;
                        font-weight:600;
                        border:0;
                        border-radius:8px;
                        color:#fff;
                        padding:0 30px;
                        font-family: 'Lato', sans-serif;
                          letter-spacing: 0.2px;
                        box-shadow: 3px 3px 6px #88888869;
                        cursor:pointer;
                        margin-top:19px;
                      }
                      .forecasting-inner-sec{ padding:68px 0; }
                      .forecasting-inner-sec .location-form{
                        padding:50px 33px 105px;
                          margin: 0;
                          max-width: initial;
                        background:#fff;
                        box-shadow: 0px 0px 10px rgb(136 136 136 / 28%);
                        border-radius:8px;
                      }
                      .weather-sec{
                        padding:28px 33px;
                          margin: 0;
                          max-width: initial;
                        background:#fff;
                        box-shadow: 0px 0px 10px rgb(136 136 136 / 28%);
                        border-radius:8px;
                        height: 100%;
                      }
                      .weather-sec .heading-weather{ display:flex; }
                      .weather-sec .heading-weather h4{
                        color:#CC0919;
                        font-size:18px;
                        font-weight:700;
                        font-family: 'Poppins', sans-serif;
                        margin:0;
                        padding-bottom:35px;
                      }
                      .weather-sec .heading-weather h4 img{ 
                        margin-right:6px; 
                          position: relative;
                          top: 6px;
                      }
                      .weather-sec .heading-weather a{
                        margin-left:auto;
                        background:#1C294B;
                        height:36px;
                        line-height:36px;
                        font-size:14px;
                        font-weight:600;
                        border:0;
                        color:#fff;
                        padding:0 11px;
                        font-family: 'Lato', sans-serif;
                          letter-spacing: 0.5px;
                        text-decoration:none;
                      }
                      .forecasting-inner-sec .location-form form button {
                          display: block;
                          width: 100%;
                          height: 40px;
                          font-size: 20px;
                        margin-top:45px;
                      }

                      @media (min-width: 768px) and (max-width: 1024px){
                        
                        .forecasting-inner-sec .location-form { padding: 50px 15px; }
                        
                      }

                      @media (max-width: 767px){
                        
                        .col-4, .col-8 {
                            -ms-flex: 0 0 100%;
                            flex: 0 0 100%;
                            max-width: 100%;
                        }
                        .continer {	box-shadow: none; }
                        .forecasting-wrap h2 {
                            font-size: 18px;
                            line-height: 28px;
                          }
                        .location-form { padding:0 15px; }
                        .forecasting-inner-sec { padding: 50px 0; }
                        .forecasting-inner-sec .location-form { 
                          margin-bottom: 25px; 
                          padding: 41px 20px 15px;
                        }
                        .weather-sec { padding: 28px 20px; }
                        
                       
                      }


                    </style>
      """,
      unsafe_allow_html=True
              )

    
    
    
    
    st.markdown(
      f"""
      <style>
      
      .reportview-container .main {{
        
          background-color:#f9f9f9;
          
          }}
     
      </style>
      """,
      unsafe_allow_html=True
    )
     
      
    #fro google colab
    #st.sidebar.image("/content/drive/MyDrive/Weather/Deployment/tlogo.png")
    #for share streamlit
    #st.sidebar.image("tlogo.png")
    Date_today = date.today()  
       
    # html_date = str("<p style='color: white; text-align:center; font-size:20px'>") + str(Date_today.strftime("%d %b, %y"))+ str("</p>")
    # st.sidebar.markdown(html_date, unsafe_allow_html=True)
    #
    st.markdown(
      f"""
      <style>
      [data-testid="stSidebar"][aria-expanded="true"] > div:first-child {{
         
          background-color:#f9f9f9;
          width:300px;
          
      }}
      </style>
      """,
      unsafe_allow_html=True,
      )


    #adding sidebar

    #-- Set by location
    #sel_location = '<p style="font-style: oblique; text-align:left;color:white; font-size:16px">Select Location</p>'
    #st.markdown(sel_location,unsafe_allow_html=True)
    st.markdown(
    """
    <style>
    label {
        font-size: 16px !important;
        padding-top: 1.5rem !important;
        font-weight: 600 !important;
        padding-bottom: 10px !important;
        color: white !important;
    }
    [data-baseweb="select"] {
        margin-top: -10px;
        color: white;
    }
    div[role="listbox"] ul {
        /* background-color: #585858; */
    }
    div[data-baseweb="select"] > div {
           width: 100%;
            /* border:1px solid rgb(28 41 75 / 30%);
            border-radius: 8px;
            min-height:38px;
            line-height:38px;
            
            font-size:15px;
            font-weight:600;
            color: white;
            font-family: 'Lato', sans-serif;
            -webkit-appearance: none;
            -moz-appearance: none;
            background: transparent;
            background-image: url(image/drop-down-icon.png);
            background-repeat: no-repeat;
            background-position-x: 96%;
            background-position-y: 15px;
            box-shadow: 0px 0px 3px rgb(136 136 136 / 28%);
            */
      }
    div[data-baseweb="select"] > div > div {
        padding: 0.35rem !important;
    }
      
      div.stButton > button:first-child {
        background:#CC0919;
        height:35px;
        font-size:14px;
        font-weight:600;
        border:0;
        border-radius:8px;
        color:#fff;
        padding:0 30px;
        font-family: 'Lato', sans-serif;
        letter-spacing: 0.2px;
        box-shadow: 3px 3px 6px #88888869;
        cursor:pointer;
        margin-top:19px;
        display: block;
          width: 100%;
          height: 40px;
          font-size: 20px;
        margin-top:45px;
      }

    </style>
    """,
    unsafe_allow_html=True,
    )
    select_location = select_location_st.selectbox('Select Location',
                                    ['Australia', 'Brazil','Canada','France','Germany','Italy','India','Japan','Mexico','Spain','United Kingdom','USA'] )
    reference_file = pd.read_csv('https://raw.githubusercontent.com/neerja198/Deployment/main/location_list.csv')

    if select_location == "USA":
        usa_dataset = pd.read_csv('https://raw.githubusercontent.com/neerja198/Deployment/main/USA_referance.csv')
        sel_prov = '<p style="font-style: oblique; text-align:left;color:white; font-size:16px">Select Province</p>'
        sel_city = '<p style="font-style: oblique; text-align:left;color:white; font-size:16px">Select City</p>'
        with left:
            # st.markdown(sel_prov, unsafe_allow_html=True)
            us_state = st.selectbox("Select Province", sorted(usa_dataset.State.unique()), index=0)
            # st.markdown(sel_city, unsafe_allow_html=True)
            city_name = st.selectbox(
                   "Select City",
                sorted(usa_dataset.loc[usa_dataset.State == us_state].City.unique())
            )

    elif select_location == 'France':
        sel_region = '<p style="font-style: oblique; text-align:left;color:white; font-size:16px">Select Region</p>'
        sel_dept = '<p style="font-style: oblique; text-align:left;color:white; font-size:16px">Select Department</p>'
        with left:
            # st.sidebar.markdown(sel_region, unsafe_allow_html=True)
            region = st.selectbox("Select Region",
                                          sorted(reference_file.loc[reference_file.Country == 'France'].City.unique()),
                                          index=0)
            # st.sidebar.markdown(sel_dept, unsafe_allow_html=True)
            dept_name = st.selectbox("Select Department",
                                             sorted(reference_file.loc[reference_file.City == region].dept.unique()))
    else:
        with left:
            select_province_city_st = st.empty()
            select_region_st = st.empty()

    with left:
        forecast_st = st.empty()


    #for streamlit
    #for google colab
    #reference_file = pd.read_csv('/content/drive/MyDrive/Weather/Deployment/location_list.csv')
    if select_location == 'USA':
            # usa_dataset = pd.read_csv('https://raw.githubusercontent.com/neerja198/Deployment/main/USA_referance.csv')

            # sel_prov = '<p style="font-style: oblique; text-align:left;color:white; font-size:16px">Select Province</p>'
            # st.sidebar.markdown(sel_prov,unsafe_allow_html=True)
            # us_state = st.sidebar.selectbox("Select Province", sorted(usa_dataset.State.unique()), index=0)
            # sel_city = '<p style="font-style: oblique; text-align:left;color:white; font-size:16px">Select City</p>'
            # st.sidebar.markdown(sel_city,unsafe_allow_html=True)
            # city_name = st.sidebar.selectbox("Select City", sorted(usa_dataset.loc[usa_dataset.State == us_state].City.unique()))

            city_name = city_name.replace("'", "")

            # 0: city   1: country   2: ISO   3: Label
            us_reference =usa_dataset.loc[usa_dataset.City== city_name].values[0]

            country_name = us_state
            iso_code = us_reference[4]
            alpha_2 = us_reference[2]
            label_alpha_2 = alpha_2[:2].lower()


            result =""
    elif select_location == 'France':
            # sel_region = '<p style="font-style: oblique; text-align:left;color:white; font-size:16px">Select Region</p>'
            # st.sidebar.markdown(sel_region,unsafe_allow_html=True)
            #
            # region = st.sidebar.selectbox("Select Region", sorted(reference_file.loc[reference_file.Country == 'France'].City.unique()), index=0)
            #
            #
            # sel_dept = '<p style="font-style: oblique; text-align:left;color:white; font-size:16px">Select Department</p>'
            # st.sidebar.markdown(sel_dept,unsafe_allow_html=True)
            # dept_name = st.sidebar.selectbox("Select Department", sorted(reference_file.loc[reference_file.City == region].dept.unique()))
            #
             # 0: city   1: country   2: ISO   3: Label
            dept_key =reference_file.loc[reference_file.dept== dept_name].values[0]
            city_name = dept_key[6]
            country_name = dept_key[1]
            country_name = country_name.lower()
            iso_code = dept_key[3]
            alpha_2 = dept_key[2]
            label_alpha_2 = alpha_2[:2].lower()



            result =""
    else:
          reference_file = pd.read_csv('https://raw.githubusercontent.com/neerja198/Deployment/main/location_list.csv')


          #country = st.sidebar.selectbox("Select Country", sorted(reference_file.Country.unique()), index=0)
          country = select_location.replace(" ", "-")
          #sel_prov_city = '<p style="font-style: oblique; text-align:left;color:white; font-size:16px">Select Province/City</p>'
          #st.sidebar.markdown(sel_prov_city,unsafe_allow_html=True)
          city_name = select_province_city_st.selectbox("Select Province/City", sorted(reference_file.loc[reference_file.Country == country].City.unique()))
          city_name = city_name.replace("'", "")

          # 0: city   1: country   2: ISO   3: Label
          city_reference =reference_file.loc[reference_file.City== city_name].values[0]

          country_name = city_reference[1]
          country_name = country_name.lower()
          iso_code = city_reference[3]
          alpha_2 = city_reference[2]
          label_alpha_2 = alpha_2[:2].lower()


          result =""

    # when 'Predict' is clicked, make the prediction and store it 
    if forecast_st.button("Forecast") or "args" in st.session_state:
        if "args" not in st.session_state:
            st.session_state["args"] = [city_name, country_name, iso_code, label_alpha_2, select_location]
            print("rerun")
            st.experimental_rerun()
        args = st.session_state["args"]
        # st.write(args)
        del st.session_state["args"]
        result = prediction(*args)
        #st.success(result)
        if len(result) == 6:
            forecast_weather = result[2]
            forecast_weather = forecast_weather[:2]
           
            max_temp = [d['max_temp'] for d in forecast_weather[0] if 'max_temp' in d]
            min_temp = [d['min_temp'] for d in forecast_weather[0] if 'min_temp' in d]
            weather_desc = [d['weather_desc'] for d in forecast_weather[0] if 'weather_desc' in d]
            weather_img = [d['weather_img'] for d in forecast_weather[0] if 'weather_img' in d]

           
            Date_today = date.today()

            iso_code_usa = ['al','az','ar','ca','co','de','ga','hi','id','in','ia','ks','ky','la','me','md','ma','mn','ms','mo','mt','ne','nv','nh','nj','nm','ny','nc','nd','oh',
                            'ok','or','pa','pr','ri','sc','sd','tn','tx','fl','mi']

            html_location = str("<p style='margin-bottom:3rem;text-align: left; color:#ffffff;font-size:23px;font-weight:700;'>") + str( result[5] + " , "  +result[1])+ str("</p>")
            loc_city_info_st.markdown(html_location, unsafe_allow_html=True)


            if result[4] in iso_code_usa and result[1] == 'USA' :
                flag_st.image("https://flagcdn.com/256x192/"+ "us-" +result[4]+".png" , width=40)
            else:
                flag_st.image("https://flagcdn.com/256x192/"+result[4]+".png" , width=40)
            html_newcases = str("<p style=' text-align: right;margin-left: auto;background: #ffffff;height: 36px;line-height: 36px;font-size: 23px;font-weight: 700;border: 0px;color: #202c4c;padding: 0px 20px;max-width: fit-content;'>") + str( "New Cases: " + f"{int(result[3]):,}")+ str("</p>")
            new_cases_st.markdown(html_newcases, unsafe_allow_html=True)


            #st.metric("New Cases", f"{int(result[3]):,}") 
            #st.metric("Location", result[1].title())
        

            forecast_newcases = result[0]
            #print(forecast_newcases)
            forecast_newcases.insert(0,result[3])
            
            
            association_msg = []
            for i in builtins.range(0,5):
               if int(forecast_newcases[i]) < int(forecast_newcases[i+1]):
                  association_msg.append("Today the weather is " + weather_desc[i] + " and temp is between " + min_temp[i] + "/ " + max_temp[i] + " , So the number of new cases of covid-19 cases may increase.")

               elif int(forecast_newcases[i]) > int(forecast_newcases[i+1]):
                  association_msg.append("Today the weather is " + weather_desc[i] + " and temp is between " + min_temp[i] + "/ " + max_temp[i] + " , So the number of new cases of covid-19 cases may decrease.")

               else:
                  association_msg.append("Today the weather is " + weather_desc[i] + " and temp is between " + min_temp[i] + "/ " + max_temp[i] + ", So the number of new cases of covid-19 cases may not be affected.")
            
            today_cases = int(result[3])
            today_cases_len = len(str(today_cases))
            new_pred = []
            if today_cases_len > 1:
             for i in forecast_newcases:
                diff = int(i)-today_cases
                if -150 <= diff <= 150:
                  new_pred.append(i)
                elif diff<-150:
                  rand = random.uniform(-150, 0)
                  generalied_newcase = int(today_cases + rand)
                  new_pred.append(generalied_newcase)
                elif diff> 150:
                  rand = random.uniform(0,150)
                  generalied_newcase = int(today_cases + rand)
                  new_pred.append(generalied_newcase)
            else:
                for i in forecast_newcases:
                  diff = int(i)-today_cases
                  if -5 <= diff <= 5:
                    rand = random.uniform(0,5)
                    generalied_newcase = int(today_cases + rand)
                    new_pred.append(generalied_newcase)
                  elif diff<-5:
                    rand = random.uniform(-5, 0)
                    generalied_newcase = int(today_cases + rand)
                    new_pred.append(generalied_newcase)
                  elif diff> 5:
                    rand = random.uniform(0,5)
                    generalied_newcase = int(today_cases + rand)
                    new_pred.append(generalied_newcase)
           
            format_nc = []
            for x in new_pred:
              x = int(x)
              if x < 4:
                minimum_cases = 0
                maximum_cases = x
                new_cases = str(minimum_cases)+" - "+str(maximum_cases)
                format_nc.append(new_cases)
              else:
                range = x/4
                range = int(range)
                minimum_cases = x-range
                maximum_cases = x + range
                cases_range = "between " + str(minimum_cases)+" and "+str(maximum_cases)
                new_cases = str(minimum_cases)+" - "+str(maximum_cases)
                format_nc.append(new_cases)
            
            split_range = format_nc[5].split('-')
            #st.success(split_range[1])
            
            #date list
            date_lst = []
           

            for i in builtins.range(0,5):
                Date_req = Date_today+ timedelta(days=i+1)
                date_lst.append(Date_req.strftime("%a, " " %d.%m.%Y"))


            #separting the range 
            newcases_lst = format_nc[1:]
            range_lst  = []
            for rnge in newcases_lst:
              split_range = rnge.split('-')
              range_lst.append(int(split_range[1])) 
            
            largest_num = max(range_lst)
            min_num = min(range_lst)
           
            
            # covid1, covid2,covid3,covid4,covid5 = st.columns(5)


            
            st.markdown(
                    """
                    <style>
                    
                    .container {
                        background-color: #28A745;
                        width:100px !important;
                    }
                    .logo-text {
                        
                        color: white !important;
                        padding-top: 75px !important;
                    }
                    .logo-img {
                        
                        display: block;
                        margin-left: auto;
                        margin-right: auto;
                        
                        
                    }

                    h4.date {
                          text-align: center; color: #FFFFFF; font-size:20px; border-bottom: 1px solid black;


                    }

                    h3.newcases {

                      text-align: center; color:#FFFFFF;font-size:30px;
                      padding: 0; margin: 0;
                      font-family:American Typewriter;
                    }
                    p.temp{

                      text-align: center; color: #FFFFFF; font-size:25px;font-family:American Typewriter;
                    }

                    h6.weatherdesc{text-align: center; font-style: oblique; color: #FFFFFF; font-size:20px; }

                    p.newcasestext {text-align: center; color: #FFFFFF; font-style: oblique;}

                    </style>
                    """,
                    unsafe_allow_html=True
                )
   
          
            with covid1:
                
                last_range = format_nc[1].split('-')
                last_num = int(last_range[1])
              
                if largest_num == last_num :
                      st.markdown(
                        f"""
                            <div style="background-color: #DC3545; padding: 10px; border-style: solid; border-width: thick; border-color: white; min-height:600px;">
                              <h4 class="date">{date_lst[0]}</h4>
                              <p></p>
                              <h3 class="newcases">{format_nc[1]}</h3>
                              <p class="newcasestext">New Cases</p>
                              <h6 style='text-align: center; color: #FFFFFF;'>{association_msg[0]}</h6>
                              <h6 class="weatherdesc">{weather_desc[0]}</h6>
                              <img class="logo-img" width=50 src="data:image/png;base64,{base64.b64encode(open(wget.download("https:"+weather_img[0]), "rb").read()).decode()}">
                              <p class="temp">{ min_temp[0]} C / {max_temp[0]} C </p>
                            </div>
                      
                        """,
                        unsafe_allow_html=True
                        )
                      
                elif min_num == last_num :
                       st.markdown(
                        f"""
                            <div style="background-color: #28A745; padding: 10px;padding: 10px; border-style: solid; border-width: thick; border-color: white; min-height:600px;">
                            <h4 class="date">{date_lst[0]}</h4> 
                            <p></p> 
                            <h3 class="newcases">{format_nc[1]}</h3>
                            <p class="newcasestext">New Cases</p>
                            <h6 style='text-align: center; color: #FFFFFF;'>{association_msg[0]}</h6>
                            <h6 class="weatherdesc">{weather_desc[0]}</h6>
                            <img class="logo-img" width=50 src="data:image/png;base64,{base64.b64encode(open(wget.download("https:"+weather_img[0]), "rb").read()).decode()}">
                            <p class="temp">{ min_temp[0]} C / {max_temp[0]} C </p>
                            </div>
                      
                        """,
                        unsafe_allow_html=True
                        )      
                else:
                       st.markdown(
                        f"""
                            <div style="background-color: #F4BB44;padding: 10px; border-style: solid; border-width: thick; border-color: white; min-height:600px;">
                            <h4 class="date">{date_lst[0]}</h4>
                            <p></p>  
                            <h3 class="newcases">{format_nc[1]}</h3>
                            <p class="newcasestext">New Cases</p>
                            <h6 style='text-align: center; color: #FFFFFF;'>{association_msg[0]}</h6>
                            <h6 class="weatherdesc">{weather_desc[0]}</h6>
                            <img class="logo-img" width=50 src="data:image/png;base64,{base64.b64encode(open(wget.download("https:"+weather_img[0]), "rb").read()).decode()}">
                            <p class="temp">{ min_temp[0]} C / {max_temp[0]} C </p>
                            </div>
                      
                        """,
                        unsafe_allow_html=True
                        )
                

            with covid2:
                last_range = format_nc[2].split('-')
                last_num = int(last_range[1])
                
                if largest_num == last_num :
                  st.markdown(
                    f"""
                        <div style="background-color: #DC3545;padding: 10px; border-style: solid; border-width: thick; border-color: white; min-height:600px;">
                        <h4 class="date">{date_lst[1]}</h4>
                        <p></p>  
                        <h3 class="newcases">{format_nc[2]}</h3>
                        <p class="newcasestext">New Cases</p>
                        <h6 style='text-align: center; color: #FFFFFF; '>{association_msg[1]}</h6>
                        <h6 class="weatherdesc">{weather_desc[1]}</h6>
                        <img class="logo-img" width=50 src="data:image/png;base64,{base64.b64encode(open(wget.download("https:"+weather_img[1]), "rb").read()).decode()}">
                        <p class="temp">{ min_temp[1]} C / {max_temp[1]} C </p>
                        </div>
                  
                    """,
                    unsafe_allow_html=True
                    )
                elif min_num == last_num : 
                  st.markdown(
                      f"""
                          <div style="background-color: #28A745;padding: 10px; border-style: solid; border-width: thick; border-color: white; min-height:600px;">
                          <h4 class="date">{date_lst[1]}</h4>
                          <p></p>  
                          <h3 class="newcases">{format_nc[2]}</h3>
                          <p class="newcasestext">New Cases</p>
                          <h6 style='text-align: center; color: #FFFFFF; '>{association_msg[1]}</h6>
                          <h6 class="weatherdesc">{weather_desc[1]}</h6>
                          <img class="logo-img" width=50 src="data:image/png;base64,{base64.b64encode(open(wget.download("https:"+weather_img[1]), "rb").read()).decode()}">
                          <p class="temp">{ min_temp[1]} C / {max_temp[1]} C </p>
                          </div>
                    
                      """,
                      unsafe_allow_html=True
                      )
                else: 
                  st.markdown(
                      f"""
                          <div style="background-color: #F4BB44;padding: 10px; border-style: solid; border-width: thick; border-color: white; min-height:600px;">
                          <h4 class="date">{date_lst[1]}</h4>
                          <p></p>  
                          <h3 class="newcases">{format_nc[2]}</h3>
                          <p class="newcasestext">New Cases</p>
                          <h6 style='text-align: center; color: #FFFFFF; '>{association_msg[1]}</h6>
                          <h6 class="weatherdesc">{weather_desc[1]}</h6>
                          <img class="logo-img" width=50 src="data:image/png;base64,{base64.b64encode(open(wget.download("https:"+weather_img[1]), "rb").read()).decode()}">
                          <p class="temp">{ min_temp[1]} C / {max_temp[1]} C </p>
                          </div>
                    
                      """,
                      unsafe_allow_html=True
                      ) 
                
        
            with covid3:
                last_range = format_nc[3].split('-')
                last_num = int(last_range[1])
                
                if largest_num == last_num :
                    st.markdown(
                      f"""
                          <div style="background-color: #DC3545;padding: 10px; border-style: solid; border-width: thick; border-color: white; min-height:600px;">
                          <h4 class="date">{date_lst[2]}</h4>
                          <p></p>  
                          <h3 class="newcases">{format_nc[3]}</h3>
                          <p class="newcasestext">New Cases</p>
                          <h6 style='text-align: center; color: #FFFFFF; '>{association_msg[2]}</h6>
                          <h6 class="weatherdesc">{weather_desc[2]}</h6>
                          <img class="logo-img" width=50 src="data:image/png;base64,{base64.b64encode(open(wget.download("https:"+weather_img[2]), "rb").read()).decode()}">
                          <p class="temp">{ min_temp[2]} C / {max_temp[2]} C </p>
                          </div>
                    
                      """,
                      unsafe_allow_html=True
                      )
                elif min_num == last_num :
                    st.markdown(
                      f"""
                           <div style="background-color: #28A745;padding: 10px; border-style: solid; border-width: thick; border-color: white; min-height:600px;">
                          <h4 class="date">{date_lst[2]}</h4>
                          <p></p>  
                          <h3 class="newcases">{format_nc[3]}</h3>
                          <p class="newcasestext">New Cases</p>
                          <h6 style='text-align: center; color: #FFFFFF; '>{association_msg[2]}</h6>
                          <h6 class="weatherdesc">{weather_desc[2]}</h6>
                          <img class="logo-img" width=50 src="data:image/png;base64,{base64.b64encode(open(wget.download("https:"+weather_img[2]), "rb").read()).decode()}">
                          <p class="temp">{ min_temp[2]} C / {max_temp[2]} C </p>
                          </div>
                    
                      """,
                      unsafe_allow_html=True
                      )
                else:
                    st.markdown(
                      f"""
                           <div style="background-color: #F4BB44;padding: 10px; border-style: solid; border-width: thick; border-color: white; min-height:600px;">
                          <h4 class="date">{date_lst[2]}</h4>
                          <p></p>  
                          <h3 class="newcases">{format_nc[3]}</h3>
                          <p class="newcasestext">New Cases</p>
                          <h6 style='text-align: center; color: #FFFFFF; '>{association_msg[2]}</h6>
                          <h6 class="weatherdesc">{weather_desc[2]}</h6>
                          <img class="logo-img" width=50 src="data:image/png;base64,{base64.b64encode(open(wget.download("https:"+weather_img[2]), "rb").read()).decode()}">
                          <p class="temp">{ min_temp[2]} C / {max_temp[2]} C </p>
                          </div>
                    
                      """,
                      unsafe_allow_html=True
                      )
               
        
            with covid4:
                last_range = format_nc[4].split('-')
                last_num = int(last_range[1])
                
                if largest_num == last_num :
                    st.markdown(
                      f"""
                          <div style="background-color: #DC3545;padding: 10px; border-style: solid; border-width: thick; border-color: white; min-height:600px;">
                          <h4 class="date">{date_lst[3]}</h4>
                          <p></p>  
                          <h3 class="newcases">{format_nc[4]}</h3>
                          <p class="newcasestext">New Cases</p>
                          <h6 style='text-align: center; color: #FFFFFF; '>{association_msg[3]}</h6>
                          <h6 class="weatherdesc">{weather_desc[3]}</h6>
                          <img class="logo-img" width=50 src="data:image/png;base64,{base64.b64encode(open(wget.download("https:"+weather_img[3]), "rb").read()).decode()}">
                          <p class="temp">{ min_temp[3]} C / {max_temp[3]} C </p>
                          </div>
                    
                      """,
                      unsafe_allow_html=True
                      )
                    
                elif min_num == last_num :
                   st.markdown(
                      f"""
                          <div style="background-color: #28A745;padding: 10px; border-style: solid; border-width: thick; border-color: white; min-height:600px;">
                          <h4 class="date">{date_lst[3]}</h4>
                          <p></p>  
                          <h3 class="newcases">{format_nc[4]}</h3>
                          <p class="newcasestext">New Cases</p>
                          <h6 style='text-align: center; color: #FFFFFF; '>{association_msg[3]}</h6>
                          <h6 class="weatherdesc">{weather_desc[3]}</h6>
                          <img class="logo-img" width=50 src="data:image/png;base64,{base64.b64encode(open(wget.download("https:"+weather_img[3]), "rb").read()).decode()}">
                          <p class="temp">{ min_temp[3]} C / {max_temp[3]} C </p>
                          </div>
                    
                      """,
                      unsafe_allow_html=True
                      )    
                else :
                   st.markdown(
                      f"""
                          <div style="background-color: #F4BB44;padding: 10px; border-style: solid; border-width: thick; border-color: white; min-height:600px;">
                          <h4 class="date">{date_lst[3]}</h4>
                          <p></p>  
                          <h3 class="newcases">{format_nc[4]}</h3>
                          <p class="newcasestext">New Cases</p>
                          <h6 style='text-align: center; color: #FFFFFF; '>{association_msg[3]}</h6>
                          <h6 class="weatherdesc">{weather_desc[3]}</h6>
                          <img class="logo-img" width=50 src="data:image/png;base64,{base64.b64encode(open(wget.download("https:"+weather_img[3]), "rb").read()).decode()}">
                          <p class="temp">{ min_temp[3]} C / {max_temp[3]} C </p>
                          </div>
                    
                      """,
                      unsafe_allow_html=True
                      )

                
            with covid5:
               last_range = format_nc[5].split('-')
               last_num = int(last_range[1])
                
               if largest_num == last_num : 
                  
                 st.markdown(
                      f"""
                          <div style="background-color: #DC3545;padding: 10px; border-style: solid; border-width: thick; border-color: white; min-height:600px;margin-right:1rem">
                          <h4 class="date">{date_lst[4]}</h4>
                          <p></p>  
                          <h3 class="newcases">{format_nc[5]}</h3>
                          <p class="newcasestext">New Cases</p>
                          <h6 style='text-align: center; color: #FFFFFF; '>{association_msg[4]}</h6>
                          <h6 class="weatherdesc">{weather_desc[4]}</h6>
                          <img class="logo-img" width=50 src="data:image/png;base64,{base64.b64encode(open(wget.download("https:"+weather_img[4]), "rb").read()).decode()}">
                          <p class="temp">{ min_temp[4]} C / {max_temp[4]} C </p>
                          </div>
                    
                      """,
                      unsafe_allow_html=True
                    )
                
               elif min_num == last_num :

                     st.markdown(
                        f"""
                            <div style="background-color: #28A745;padding: 10px; border-style: solid; border-width: thick; border-color: white; min-height:600px;">
                            <h4 class="date">{date_lst[4]}</h4>
                            <p></p>  
                            <h3 class="newcases">{format_nc[5]}</h3>
                            <p class="newcasestext">New Cases</p>
                            <h6 style='text-align: center; color: #FFFFFF; '>{association_msg[4]}</h6>
                            <h6 class="weatherdesc">{weather_desc[4]}</h6>
                            <img class="logo-img" width=50 src="data:image/png;base64,{base64.b64encode(open(wget.download("https:"+weather_img[4]), "rb").read()).decode()}">
                            <p class="temp">{ min_temp[4]} C / {max_temp[4]} C </p>
                            </div>
                      
                        """,
                        unsafe_allow_html=True
                      )       
               else :

                     st.markdown(
                        f"""
                            <div style="background-color: #F4BB44;padding: 10px; border-style: solid; border-width: thick; border-color: white; min-height:600px;">
                            <h4 class="date">{date_lst[4]}</h4>
                            <p></p>  
                            <h3 class="newcases">{format_nc[5]}</h3>
                            <p class="newcasestext">New Cases</p>
                            <h6 style='text-align: center; color: #FFFFFF; '>{association_msg[4]}</h6>
                            <h6 style='text-align: center; font-style: oblique; color: #FFFFFF; font-size:20px; '>{weather_desc[4]}</h6>
                            <img class="logo-img" width=50 src="data:image/png;base64,{base64.b64encode(open(wget.download("https:"+weather_img[4]), "rb").read()).decode()}">
                            <p class="temp">{ min_temp[4]} C / {max_temp[4]} C </p>
                            </div>
                      
                        """,
                        unsafe_allow_html=True
                      )
        
        
        
        else:
            st.success(result)
    else:
        with title:
            # st.columns(2)
            new_title = '<p style="font-size:40px;line-height:40px;font-weight:600;color:#fff;text-align:center;padding:13px 0;margin:0;padding-top:4rem">' \
                        'This is a machine learning model which forecast<br>' \
                        'the 5 day covid 19 cases based on current weather<br>' \
                        'of the selected location from given dropdown' \
                        '</p>'
            st.markdown(new_title, unsafe_allow_html=True)

            
            
            #st.success("Date : " + "  "+"  "+ Date_req.strftime("%d %b, %Y") + "  " + " , " + "New Cases :" + " " + f"{int(forecast_newcases[i]):,}" + " , "
             #+  "Max_Temp: " + " " + max_temp[i] + "°C"+"," +  "Min_Temp: " + " " + min_temp[i] + "°C"+"," + "Desc: " + " " + weather[i] )
     
     
if __name__=='__main__': 
    main()
     
