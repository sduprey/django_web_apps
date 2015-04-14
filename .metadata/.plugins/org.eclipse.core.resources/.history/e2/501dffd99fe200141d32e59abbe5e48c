'''
Created on 14 Apr 2015

@author: sduprey
'''
import psycopg2
class Datacollector(object):
    my_conn=None
    @staticmethod
    def get_pictures(my_sku):
        if Datacollector.my_conn is None:
            conn_string = "host='localhost' dbname='KRITERDB' user='postgres' password='mogette'"
            print "Connecting to database\n    ->%s" % (conn_string)
            Datacollector.my_conn=psycopg2.connect(conn_string) 
        cursor = Datacollector.my_conn.cursor()       
        print "Dealing with :"+my_sku
        my_cds_request = "select sku1, sku2, sku3, sku4, sku5, sku6 from CATALOG where sku=(%s)"
        cursor.execute(my_cds_request,(my_sku,)); 
        cds_datas = cursor.fetchall()
        cds_similar_skus = cds_datas[0];
        my_cds_pictures=[]
        for sim_sku in cds_similar_skus:
            my_image_request = "select lien_image from CATALOG where sku=(%s)"
            cursor.execute(my_image_request,(sim_sku,)); 
            pictures = cursor.fetchall()
            print 
            my_cds_pictures.append(pictures[0][0])
        
        
        my_kriter_request = "select krit_sku1, krit_sku2, krit_sku3, krit_sku4, krit_sku5, krit_sku6 from CATALOG where sku=(%s)"
        cursor.execute(my_kriter_request,(my_sku,)); 
        kriter_datas = cursor.fetchall()
        kriter_similar_skus = kriter_datas[0];
        my_kriter_pictures=[]
        for sim_sku in kriter_similar_skus:
            my_image_request = "select lien_image from CATALOG where sku=(%s)"
            cursor.execute(my_image_request,(sim_sku,)); 
            pictures = cursor.fetchall()
            print 
            my_kriter_pictures.append(pictures[0][0])
        
        return my_cds_pictures,my_kriter_pictures
    
    
    
    
    
    