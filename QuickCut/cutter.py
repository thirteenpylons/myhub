"""
This module compiles the cutsheet

Author: Christian M. Fulton
Date: 29.Oct.2021
"""
import time
import os
import json
import itertools
from datetime import datetime
from urllib.request import urlopen
from openpyxl import load_workbook as LW

from messages import Message
from helpers import FromDict


def cut(**kwargs):
    """
    Builds cutsheet

    Parameter kwargs: takes the dict(data) from the account
    Precondition: kwargs must be a non empty dict
    """

    # store dict -> const
    CDATA = FromDict(kwargs)

    # conf file data...
    job_log = 'jobs.txt'
    template = 'template.xlsx'
    # following my personal naming conventions..
    dirname = f'{CDATA.NAME}@{CDATA.ADDRESS}'
    loc = f'./{dirname}/Cut_Sheet_{CDATA.NAME}_{CDATA.ENG}.xslx'

    # Keeping a log of the jobs that I do
    logged_data = f'{CDATA.NAME} {CDATA.ENG} {datetime.now()}\n'

    try:
        os.mkdir(dirname)
    except FileExistsError:
        print(Message.dir_exists_err(dirname))

    try:
        with open(job_log, 'a') as txt_file:
            txt_file.write(logged_data)
        print(Message.write_data_com(logged_data, job_log))
    except:
        print(Message.write_data_err(NAME, job_log))
    
    if os.path.isfile(loc):
        print(Message.dir_exists_err(loc))
        loc = loc[:-5] + '_NEW.xslx'
    
    try:
        doc = LW(filename=template)
        WS = doc.active

        WS['D6'] = CDATA.ENG
        WS['D22'] = CDATA.CID
        WS['D8'] = CDATA.WO
        WS['B10'] = CDATA.ACCOUNT
        WS['B6'] = CDATA.NAME
        WS['B7'] = CDATA.ADDRESS
        WS['B9'] = CDATA.CONTACT
        WS['D11'] = CDATA.PM
        WS['D12'] = CDATA.SDM
        WS['B23'] = CDATA.CIRCUIT_TYPE
        WS['D19'] = CDATA.UNI
        WS['D20'] = CDATA.DUPLEX
        WS['D21'] = CDATA.SPEED + CDATA.SPEED_UNIT
        WS['D24'] = CDATA.HANDOFF
        WS['G9'] = CDATA.A_OPTIC

        doc.save(loc)
        print(Message.write_file_com(loc, dirname))
    except:
        print(Message.write_data_err(dirname,loc))