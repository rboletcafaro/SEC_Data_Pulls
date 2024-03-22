#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 17:04:04 2024

@author: robcafaro
"""
from backports.zoneinfo import ZoneInfo
from ffiec_data_connect import methods, credentials, ffiec_connection
        
creds = credentials.WebserviceCredentials(username="rboletcafaro", password="nick4vuNH4rEaIVJXGxp")

conn = ffiec_connection.FFIECConnection()

reporting_periods = methods.collect_reporting_periods(
            session=conn,
            creds=creds,
            output_type="list",
            date_output_format="string_original"
        )

