# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 21:23:04 2021

@author: eeuma
"""

import pandas as pd

df1 = pd.read_csv("CSV Data/YouTube_ThumbMedia/YouTube_ThumbMedia_M_20210201_claim_raw_v1-1.csv")
df2 = pd.read_csv("Premium/YouTube_Thumb_Media_Music/YouTube_Thumb_Media_Music_M_20210201_20210228_red_label_rawdata_video_v1-1.csv")
df3 = pd.read_csv("Superchat/YouTube_Thumb_Media_monetized_M_20210201_claim_raw_v1-1.csv")


Main = pd.concat([df1, df2,df3])
partnerCsv = Main.loc[Main['Content Type'] == "Partner-provided"]
assetID=partnerCsv.sort_values(by=['Asset ID'])
