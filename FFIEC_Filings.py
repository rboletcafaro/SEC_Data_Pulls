#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 17:04:04 2024

@author: robcafaro
"""

#from backports.zoneinfo import ZoneInfo
from ffiec_data_connect import methods, credentials, ffiec_connection
import pandas as pd
        
creds = credentials.WebserviceCredentials(username="rboletcafaro", password="nick4vuNH4rEaIVJXGxp")

conn = ffiec_connection.FFIECConnection()

reporting_periods = methods.collect_reporting_periods(session=conn,creds=creds,output_type="list",date_output_format="string_original")
reporting_periods


# Collect List Of Filers For A Particular Period
filers = methods.collect_filers_on_reporting_period(session=conn,creds=creds,reporting_period="6/30/2022",output_type="pandas")




last_filing_date_time = methods.collect_filers_submission_date_time(session=conn,creds=creds,since_date="6/30/2022",reporting_period="6/30/2022",)

tmp_data = methods.collect_data(session=conn,creds=creds, reporting_period="6/30/2022", rssd_id='480228', series = "call", output_type = 'pandas')

time_series = methods.collect_data(session=conn,creds=creds,rssd_id="37",reporting_period="6/30/2022",series="call")



