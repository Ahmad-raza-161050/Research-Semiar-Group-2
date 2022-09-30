import re
import emoji
import nltk
import pandas as pd
import snscrape.modules.twitter as sntwitter
import itertools
import nltk

tweets_list1 = []
start = '2020-03-01'
end = '2020-08-15'
account_list= ["ADHPIO","AHRQNews","AllofUsResearch","APHealthScience","ArmyMedicine","ask405d","ATFBoston","AusPublicHealth"
,"AZDHS","BMore_Healthy","CA_OSG","CAgovernor","Cal_HHS","Cal_OES","CAPublicHealth","CDC_DASH","CDC_Genomics","CDCChronic","CDCDiabetes","CDCDirector"
,"CDCemergency","CDCFlu","CDCFound","CDCgov","ChrissyFOX5","ClevelandClinic","CMSGov","covinapd","cspan","danlederman","DCHHS","DHSGOv","distressline"
,"DrJudyMonroe","DrMartinCDC","ExportGov","FamiliesUSA","FDA_MCMi","FDArecalls","fema","FNIH_Org","GaDPH","genome_gov","GovernorGordon","GovHawaii","govkristinoem"
,"GovRicketts","GregAbbott_TX","HamCoHealth","HawaiiDOH","haphtx","HealthCare.gov","HealthGov","HealthNYGov","healthychildren","HealthyOklahoma"
,"HealthySCC","HHS.gov","HHS_ASH","HHSGov","HHSOCR","HHSRegion2","HHSRegion5","HHSRegion6","HHSRegion9","hhsregionone","HHSvaccines","HoustonHealth","HRSAgov"
,"JeffcoPH","KamalaHarris","LADeptHealth","lapublichealth","MDHealthDept","MedicaidGov","MEPublicHealth","MichiganHHS","Mike_Pence","MinorityHealth"
,"MRC_ASPR","NavyMedicine","NCBI","ncdhhs","NICHD_NIH","NICHDPress","NIH","NIH_CommonFund","NIH_ORWH","NIHAging","NIHClinicalCntr"
,"NIHCOVIDTxGuide","NIHDataScience","NIHDirector","NIHprevents","NIMHD","NLMdirector","nycHealthy","OHdeptofhealth","OhioAG","OlGatHHS"
,"PAHumanServices","PHIdotorg","PHLPublicHealth","PJCrowley","precisionfda","publicservice","RealBenCarson","RIHEALTH","RuralED","SAHealth","SaltLakeHealth"
,"SBAgov","ScottSingerUSA","SecAzar","SeemaCMS","ShareAmerica","SLOPublicHealth","Surgeon_General","theNCI","TNDeptofHealth","UCLAHealth","US_FDA","USACEHQ"
,"USAFMedicine","USAGOV","USAID","USAmbCroatia","USAO_RI","usatodayDC","USATODAYhealth","USDOL","USDS","USGSA","USNRL","UtahDHHS","VDHgov","VP","WHAAsstSecty"]

keywords_list=["mask", "N95", "surgicalmasks", "FFP2", "Wear" ,"social","distancing", "hands", "sanitizers", "face shields" , "n95", "masks" 
, "surgical" , "gloves" , "gowns" , "hand" , "hands","sainitizers" , "self", "quarantine", "self-quarantine" ,"homes","isolation", "nighttime" 
, "curfew" , "lock-down", "lock-downs", "lockdowns","lockdown", "stay home" ,"avoid gatherings", "avoid crowds", "no events", "no socializing" 
, "stop socializing", "avoid gathering", "stay safe", "cover" , "nose", "your nose", "mouth", "cover your mouth", "gathering"
, "less people","6ft", "6ft distance", "social distance" , "self isolation" , "protect yourself", "protect your family", "protect people"
, "sanitizers" , "hand sanitizers", "clean", "your hands", "wash" , "wash your hands", "disinfect yourself", "disinfect", "disinfect your hands"
 , "disinfect your surroundings", "covid-19", "Corona virus", "virus", "pandemic", "covid", "spread", "stop corona" , "stop covid"
 , "stop spreading covid", "stop spreading corona", "stop spreading virus","corona"]

for key in keywords_list:
    for acc in account_list:
        for i, tweet in enumerate(sntwitter.TwitterSearchScraper(' {keywords1} from:{account} since:{start_date} until:{end_date}'
        .format( keywords1=key, account= acc, start_date=start, end_date=end)).get_items()):
            if i > 3000:
                break
            tweets_list1.append([tweet.date, tweet.id, tweet.content])
    
tweets_df1 = pd.DataFrame(tweets_list1, columns = ['Datetime', 'Tweet_id', 'Content'])
tweets_df1.to_csv(r'C:\Users\ahmad\Downloads\Research Seminar Data\1st wave\lockdowns\raw\1st_wave-lockdowns.csv')



nltk.download('words')
words = set(nltk.corpus.words.words())

clean_tweets = []
test = []
for tweet in tweets_df1['Content']:
    tweet = re.sub("@[A-Za-z0-9]+","",tweet) #Remove @ sign
    tweet = re.sub(r"(?:\@|http?\://|https?\://|www)\S+", "", tweet)
    tweet = re.sub("#[A-Za-z0-9_]+","", tweet)
    tweet = re.sub("&[A-Za-z0-9_]+","", tweet)
    tweet = re.sub(";[A-Za-z0-9_]+","", tweet)
    tweet = tweet.replace("#", "").replace("_", " ")
    tweet = ''.join(c for c in tweet if c not in emoji.distinct_emoji_list(test))
    ##Here's where all the cleaning takes place
    clean_tweets.append(tweet)
tweets_df1['Content'] = clean_tweets
tweets_df1.to_csv(r'C:\Users\ahmad\Downloads\Research Seminar Data\1st wave\lockdowns\cleaned\1st_wave-lockdowns.csv') #Specify location
data_1 = pd.read_csv(r'C:\Users\ahmad\Downloads\Research Seminar Data\1st wave\lockdowns\cleaned\1st_wave-lockdowns.csv')
data_1.head()

