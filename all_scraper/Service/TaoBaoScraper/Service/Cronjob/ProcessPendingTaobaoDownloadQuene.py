# -*-coding:utf-8*-
from get_downloadquene import get_TaoBao_download_Quene
from Service.Service_TaobaoQuene import Service_TaobaoQuene



class Service_Cronjob_ProcessPendingTaobaoDownloadQuene():

    def __init__(self):
        pass


    def start(self):
        try:
            #从downloadquene中取出数据库中数据
            type_list=get_TaoBao_download_Quene()
            downloadQuenes=type_list
        except Exception as err:
            print err
        if(downloadQuenes):
            queneService=Service_TaobaoQuene()
            for downloadQuene in downloadQuenes:
                # print (downloadQuene[3])
                queneService.processPendingTaobaoDownloadQuene(downloadQuene)
        else:
            print ("no downloadquenes")