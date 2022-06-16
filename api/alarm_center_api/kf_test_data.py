"""
author :admin
Date : 2021/12/07
Description :
"""
from utilss.time_utils import TimeUtils

fn_ua_message = {
    "staId": "PARK172_EMS01",
    "data": [{"metric": "METE_CO1381D04_Ua",
              # "2021-10-13 15:39:00"
              "time": TimeUtils.get_current_timestamp(), "value": "120.0"}],
    "domain": "EMS",
    "allPoints": 1,
    "version": "0.0.1"}

fn_STspringusto_message = {
    "staId": "PARK172_EMS01",
    "data": [{"metric": "METE_CO1381D05_STspringusto",
              # "2021-10-13 15:39:00"
              "time": TimeUtils.get_current_timestamp(), "value": "1"}],
    "domain": "EMS",
    "allPoints": 1,
    "version": "0.0.1"}

fn_STspringusto_message01 = {
    "staId": "PARK172_EMS01",
    "data": [{"metric": "BK_BK01_STspringusto",
              # "2021-10-13 15:39:00"
              "time": TimeUtils.get_current_timestamp(), "value": "1"}],
    "domain": "EMS",
    "allPoints": 1,
    "version": "0.0.1"}

fn_stbk_message = {
    "staId": "PARK172_EMS01",
    "data": [{"metric": "BK_BK01_STbk",
              # "2021-10-13 15:39:00"
              "time": TimeUtils.get_current_timestamp(), "value": "1.0"}],
    "domain": "EMS",
    "allPoints": 1,
    "version": "0.0.1"}

fn_posbkcls_message = {
    "staId": "PARK172_EMS01",
    "data": [{"metric": "BK_BK01_POSbkCls",
              # "2021-10-13 15:39:00"
              "time": TimeUtils.get_current_timestamp(), "value": "0.0"}],
    "domain": "EMS",
    "allPoints": 1,
    "version": "0.0.1"}

fn_ALMsmoke_message = {
    "staId": "PARK172_EMS01",
    "data": [{"metric": "SA_SA01_ALMsmoke",
              # "2021-10-13 15:39:00"
              "time": TimeUtils.get_current_timestamp(), "value": "1"}],
    "domain": "EMS",
    "allPoints": 1,
    "version": "0.0.1"}

fn_AbnmPAdischrg_message = {
    "staId": "PARK172_EMS01",
    "data": [{"metric": "ACOP_ACOP07_AbnmPAdischrg",
              # "2021-10-13 15:39:00"
              "time": TimeUtils.get_current_timestamp(), "value": "0"}],
    "domain": "EMS",
    "allPoints": 1,
    "version": "0.0.1"}

fn_FwaterInt_message = {
    "staId": "PARK172_EMS01",
    "data": [{"metric": "CM_CM01_FwaterInt",
              # "2021-10-13 15:39:00"
              "time": TimeUtils.get_current_timestamp(),
              "value": "0.0075"}],
    "domain": "EMS",
    "allPoints": 1,
    "version": "0.0.1"}
