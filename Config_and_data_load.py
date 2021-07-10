import pandas as pd
import numpy as np
import re



class ConfigDataLoad():


    def __init__(self,date_var,target_var,file_path,category_var):
        self.date_var = date_var
        self.target_var = target_var
        self.file_path = file_path
        self.category_var = category_var
        # self.start_year = start_year
    def call_data_load_preprocessing(self):
        main_df = self.data_load_preprocessing()
        data_list = self.category_div(main_df,self.category_var)
        return main_df,data_list

    def category_div(self,df,categories): #function to divide the main dataframe into all the categories that are present
        df['key']=''
        non_zero_flag=0
        for j in range(0,len(categories)):
            if j==0:
                df['key']=df['key']+df[categories[j]].map(str)
            else:
                df['key']=df['key']+'|'+df[categories[j]].map(str)
        key= df['key'].unique()
        dfs=[]
        #print df[df['key']==key[0]]
        print('started making df_list')
        for i in range(len(key)):

            df_key = df[df['key']==key[i]]
            if(non_zero_flag==1):
                if df_key[target_var].sum()>0:
                    non_zero_index = df_key[target_var].to_numpy().nonzero()[0][0]
                    df_key_non_zero = df_key[non_zero_index:]
                    df_key_non_zero = df_key_non_zero.sort_index()
                    
            else:
                df_key_non_zero = df_key
                df_key_non_zero = df_key_non_zero.sort_index()
            #put the condition year-1-month to year-month
            if (len(df_key_non_zero)>24) & (2020 in df_key_non_zero.Year.unique()) :
                dfs.append(df_key_non_zero)
            # else:
            #     key_skipped.append(df_key)


        #print len(dfs)
        self.dfs = dfs
        return self.dfs

    def data_load_preprocessing(self):

        main_df = pd.read_csv(self.file_path)
        main_df = main_df.loc[main_df['Year']>2016]
        main_df['Used BGR'] = main_df['Used BGR'].astype(str).str.upper()
        # main_df = main_df.loc[main_df['Used BGR'].isin(['SHOWER','DEO FEMALE ROLL-ON','DEO MALE ROLL-ON'])]
        # main_df = main_df.loc[main_df['Depot'].isin(['DEHRADUN', 'INDORE', 'DELHI', 'BHIWANDI'])]
        #input from config
        main_df = main_df.loc[main_df['Used BGR'].isin(['DEO MALE ROLL-ON'])]
        main_df = main_df.loc[main_df['Depot'].isin(['DEHRADUN'])]
        main_df = main_df.loc[main_df['Used_channel']!='NOT to be used']
        time_features_to_add = ['days_in_month']
        main_df[self.date_var] = pd.to_datetime(main_df[self.date_var], format="%d-%m-%Y")
        main_df['Quarter'] = main_df[self.date_var].dt.quarter
        main_df,added_cols = self.add_datepart(main_df,self.date_var,time_features_to_add,drop=False,cyclic=True)
        #main_df.drop(columns=['Month','Week'],inplace=True)
        #main_df['calendar_wom'] = main_df[date_var].apply(week_of_month)
        print(main_df.columns)
        main_df.drop(columns=['Child SPGR','RATE', 'GROSS_AMOUNT', 'SCHEME_AMT',
            'CASH_DISCOUNT', 'STOCKIST_DISCOUNT', 'TAX_AMOUNT', 'NET_AMOUNT',
            'DLP_AMOUNT', 'PNS_VALUE','PGR for File'],inplace=True)
        main_df['promo_type'].fillna('No Promo',inplace=True)
        main_df.fillna(0,inplace=True)

        #main_df[target_var] = main_df[target_var].shift(-prediction_period)
        main_df = pd.concat([main_df,pd.get_dummies(main_df['promo_type'], prefix='Promo')],axis=1)
        main_df = pd.concat([main_df,pd.get_dummies(main_df['Holiday_cat'], prefix='Holiday')],axis=1)
        


        main_df = main_df.drop(columns=['promo_type','Holiday_cat']).dropna()
        # main_df['promo_qty'] = main_df['promo_qty'].str.replace(' -   ','0')
        main_df['promo_qty'] = main_df['promo_qty'].astype(np.float64)
        main_df['promo_qty'].fillna(0,inplace=True)
        main_df = main_df.set_index(self.date_var,drop=True)
        return main_df

    
    
    def add_datepart(self, df, date_col, time_features_to_add, drop=True, cyclic=True):
        
        init_cols = df.columns
        fld = df[date_col]
        if not np.issubdtype(fld.dtype, np.datetime64):
            df[date_col] = fld = pd.to_datetime(fld, infer_datetime_format=True)
        targ_pre = re.sub('[Dd]ate$', '', date_col)
        for n in time_features_to_add:
            print("Adding feature ", targ_pre + n.lower())
            df[targ_pre + n.lower()] = getattr(fld.dt, n.lower())
            if n in ['year', 'dayofyear']:
                df[targ_pre + n.lower()] = df[targ_pre + n.lower()].astype(np.int32)
            else:
                df[targ_pre + n.lower()] = df[targ_pre + n.lower()].astype(np.int8)
        df[targ_pre + 'elapsed'] = fld.astype(np.int64) // 10 ** 9
        if drop: df.drop(date_col, axis=1, inplace=True)
    
        if cyclic:
            print("Adding cyclic features")
            def encode(data, col, max_val):
                data[col + '_sin'] = np.sin(2 * np.pi * data[col] / max_val)
                data[col + '_cos'] = np.cos(2 * np.pi * data[col] / max_val)
                return data
    
            # Convert this feature to its sin and cos components to represent cyclical behavior
            for n in ('Month', 'Quarter', 'Week'):
                print("Adding cyclic features for ", n)
                max_val = max(df.loc[:, n])
                df = encode(df, n, max_val)
        datetime_columns = list(set(df.columns).difference(init_cols))
        return df, datetime_columns

        #tgtdate = tgtdate.to_datetime()

        days_this_month = calendar.mdays[tgtdate.month]
        for i in range(1, days_this_month):
            d = datetime.datetime(tgtdate.year, tgtdate.month, i)
            if d.day - d.weekday() > 0:
                startdate = d
                break
        # now we can use the modulo 7 appraoch
        return (tgtdate - startdate).days //7 + 1



    

