import pandas as pd
from pandas.io.excel import ExcelWriter
from decimal import *
from math import *
import numpy as np

JoF = {"meters": '20, 40, 60, 80, 100, 120, 140, 160', "meters_corrections": '0, 0, 0, 0, 0, 0, 0, 0' }

StF = [{'station_name': '216', 'station_height': '1.40', 'sighting_points1': '215', 'sighting_points2': '101', 'sighting_points3': '215', 'sighting_points4': '101',
'gorizontal_angle_gradus': '0, 237, 180, 57',  'gorizontal_angle_min': '0.5, 46.0, 1.0, 46.0',
'sighting_points_neighbors': '101', 'sighting_points_neighbors_height': '2.84', 
'vertical_angle_gradus': '0, 0', 'vertical_angle_min': '-40.0, 39.0', 'rail': '118.1, 118.4'}, 

{'station_name': '101', 'station_height': '1.35', 'sighting_points1': '216', 'sighting_points2': '102', 'sighting_points3': '216', 'sighting_points': '102', 
'gorizontal_angle_gradus': '0, 137, 180, 317','gorizontal_angle_min': '0.5, 1.5, 1.0, 1.5', 
'sighting_points_neighbors': '216, 102', 'sighting_points_neighbors_height': '1.82, 2.76', 
'vertical_angle_gradus': '1, -1, 0, 0', 'vertical_angle_min': '35.5, -36.0, 15.0, -15.5', 'rail': '118.4, 118.2, 157.3, 157.5'}, 

{'station_name': '102', 'station_height': '1.33', 'sighting_points1': '101', 'sighting_points2': '225', 'sighting_points3': '101', 'sighting_points4': '225',
'gorizontal_angle_gradus': '0, 225, 180, 45','gorizontal_angle_min': '0.5, 58.5, 1.0, 59.5', 
'sighting_points_neighbors': '101, 225', 'sighting_points_neighbors_height': '1.78, 2.87', 
'vertical_angle_gradus': '0, 0, 0, 0', 'vertical_angle_min': '26.0, -26.5, 51.5, -52.0', 'rail': '157.4, 157.5, 126.8, 127.1'}, 

{'station_name': '225', 'station_height': '1.33', 'sighting_points1': '102', 'sighting_points2': '226', 'sighting_points3': '101', 'sighting_points4': '226',
'gorizontal_angle_gradus': '0, 251, 180, 71','gorizontal_angle_min': '0.5, 46.0, 1.5, 46.0', 
'sighting_points_neighbors': '102', 'sighting_points_neighbors_height': '2.79', 
'vertical_angle_gradus': '0, 0', 'vertical_angle_min': '30.0, -30.5', 'rail': '126.9, 127.2'}]

stf2 = [{'station_name': '216', 'station_height': '1.40', 'sighting_points1': '215', 'sighting_points2': '101', 'sighting_points3': '215', 'sighting_points4': '101', 
'gorizontal_angle_gradus1': '0',  'gorizontal_angle_min1': '0.5',
'gorizontal_angle_gradus2': '237',  'gorizontal_angle_min2': '46.0',
'gorizontal_angle_gradus3': '180',  'gorizontal_angle_min3': '1.0',
'gorizontal_angle_gradus4': '57',  'gorizontal_angle_min4': '46.0',
'sighting_points_neighbors1': '101', 'sighting_points_neighbors_height1': '2.84', 
'vertical_angle_gradus1': '0', 'vertical_angle_min1': '-40.0', 'rail1': '118.1',
'vertical_angle_gradus2': '0', 'vertical_angle_min2': '39.0', 'rail2': '118.4'}, 

{'station_name': '101', 'station_height': '1.35', 'sighting_points1': '216', 'sighting_points2': '102', 'sighting_points3': '216', 'sighting_points4': '102', 
'gorizontal_angle_gradus1': '0','gorizontal_angle_min1': '0.5', 
'gorizontal_angle_gradus2': '137','gorizontal_angle_min2': '1.5',
'gorizontal_angle_gradus3': '180','gorizontal_angle_min3': '1.0',
'gorizontal_angle_gradus4': '317','gorizontal_angle_min4': '1.5',
'sighting_points_neighbors1': '216', 'sighting_points_neighbors_height1': '1.82', 
'sighting_points_neighbors2': '102', 'sighting_points_neighbors_height2': '2.76', 
'vertical_angle_gradus1': '1', 'vertical_angle_min1': '35.5', 'rail1': '118.4',
'vertical_angle_gradus2': '-1', 'vertical_angle_min2': '-36.0', 'rail2': '118.2',
'vertical_angle_gradus3': '0', 'vertical_angle_min3': '15.0', 'rail3': '157.3',
'vertical_angle_gradus4': '0', 'vertical_angle_min4': '-15.5', 'rail4': '157.5'}, 

{'station_name': '102', 'station_height': '1.33', 'sighting_points1': '101', 'sighting_points2': '225', 'sighting_points3': '101', 'sighting_points4': '225', 
'gorizontal_angle_gradus1': '0','gorizontal_angle_min1': '0.5',
'gorizontal_angle_gradus2': '225','gorizontal_angle_min2': '58.5',
'gorizontal_angle_gradus3': '180','gorizontal_angle_min3': '1.0',
'gorizontal_angle_gradus4': '45','gorizontal_angle_min4': '59.5', 
'sighting_points_neighbors1': '101', 'sighting_points_neighbors_height1': '1.78',
'sighting_points_neighbors2': '225', 'sighting_points_neighbors_height2': '2.87', 
'vertical_angle_gradus1': '0', 'vertical_angle_min1': '26.0', 'rail1': '157.4',
'vertical_angle_gradus2': '0', 'vertical_angle_min2': '-26.5', 'rail2': '157.5',
'vertical_angle_gradus3': '0', 'vertical_angle_min3': '51.5', 'rail3': '126.8',
'vertical_angle_gradus4': '0', 'vertical_angle_min4': '-52.0', 'rail4': '127.1'}, 

{'station_name': '225', 'station_height': '1.33', 'sighting_points1': '102', 'sighting_points2': '226', 'sighting_points3': '101', 'sighting_points4': '226', 
'gorizontal_angle_gradus1': '0','gorizontal_angle_min1': '0.5',
'gorizontal_angle_gradus2': '251','gorizontal_angle_min2': '46.0',
'gorizontal_angle_gradus3': '180','gorizontal_angle_min3': '1.5',
'gorizontal_angle_gradus4': '71','gorizontal_angle_min4': '46.0', 
'sighting_points_neighbors1': '102', 'sighting_points_neighbors_height1': '2.79', 
'vertical_angle_gradus1': '0', 'vertical_angle_min1': '30.0', 'rail1': '126.9',
'vertical_angle_gradus2': '0', 'vertical_angle_min2': '-30.5', 'rail2': '127.2'}]

def calculations(JournalForm, StationForm):
    #import pandas as pd
    #from pandas.io.excel import ExcelWriter
    #from decimal import *
    #from math import *
    #import numpy as np
    meters = []
    meters_corrections = []
    if ", " in JournalForm['meters']:
        meters = list(JournalForm['meters'].split(', '))    
        meters[::] = map(int, meters[::])
        meters_corrections = list(JournalForm['meters_corrections'].split(', '))
        meters_corrections[::] = map(int, meters_corrections[::])
    else:
        meters.append(int(JournalForm['meters']))
        meters_corrections.append(int(JournalForm['meters_corrections']))
    #meters_corrections = list(JournalForm['meters_corrections'].split(', '))
    
    if len(meters) > 18:   
        df_length = len(meters)+1
    else:
        df_length = 19    
    df_depth = len(StationForm) * 6 + 7
    nn = np.nan
    df = pd.DataFrame(columns = range(df_length), index = range(df_depth))
    df[0][0] = "Журнал Тахеометрического хода"
    df[0][2] = "Поправки"
    
    str6 = ['№ станции', 'Визир. пункты', 'Л/П', nn,nn,nn,nn, 'Визир. пункты', 'Л/П', 'Отсчеты', nn, 'По рейке', 'МО, угол', nn, 'l,D,S', 'h1,d,h', 'hпр,hобр,hср', nn,nn]
    #print(len(str6))
    for i in range(df.shape[1]):
        df[i][6] = str6[i]
    
    df[17][9] = "ΔD"
    df[18][9] = "Δh"
    df[2][5] = "Горизонтальный круг"
    df[5][5] = "Угол, среднее"
    df[8][5] = "Вертикальный угол"
    df[12][5] = "Вычисления"
    k1 = 0
    
    for i in range(1, len(meters)+1):
        df[i][1] = meters[k1]   
        df[i][2] = meters_corrections[k1]        
        if k1+1 < len(meters):
            k1+=1
            
    for i in range(8, len(df[2])-2, 6):
        df[2][i] = "Л"
        df[2][i+1] = "Л"
        df[2][i+2] = "П"
        df[2][i+3] = "П"
    for i in range(11, len(df[8])-4, 3):
        df[8][i] = "Л"
        df[8][i+1] = "П"
    
    
    station_names = []
    station_heights = []
    sighting_points = []    
    gorizontal_angles_gradus = []
    gorizontal_angles_min = []
    sighting_points_neighbors = []
    sighting_points_neighbors_heights = []
    vertical_angles_gradus = []
    vertical_angles_min = []
    rails = []
    
    #1 вариант
    '''for i in StationForm:
        station_names.append(int(i['station_name']))
        station_heights.append(float(i['station_height']))
        for j in i['sighting_points'].split(', '):
            sighting_points.append(int(j))
        for j in i['gorizontal_angle_gradus'].split(', '):
            gorizontal_angles_gradus.append(int(j))
        for j in i['gorizontal_angle_min'].split(', '):
            gorizontal_angles_min.append(float(j))   
        if ', ' in i['sighting_points_neighbors']:
            for j in i['sighting_points_neighbors'].split(', '):
                sighting_points_neighbors.append(int(j))
        else:
            sighting_points_neighbors.append(int(i['sighting_points_neighbors']))
        if ', ' in i['sighting_points_neighbors_height']:
            for j in i['sighting_points_neighbors_height'].split(', '):
                sighting_points_neighbors_heights.append(float(j))
        else:
            sighting_points_neighbors_heights.append(float(i['sighting_points_neighbors_height']))
        for j in i['vertical_angle_gradus'].split(', '):
            vertical_angles_gradus.append(int(j))
        for j in i['vertical_angle_min'].split(', '):
            vertical_angles_min.append(float(j))
        for j in i['rail'].split(', '):
            rails.append(float(j))'''

    #2 вариант
    count1=0
    for i in StationForm:
        #print(count1)
        if (count1 != 0) and (count1 != (len(StationForm)-1)):
            station_names.append(int(i['station_name']))
            station_heights.append(float(i['station_height']))        
            sighting_points.append(int(i['sighting_points1']))
            sighting_points.append(int(i['sighting_points2']))
            sighting_points.append(int(i['sighting_points3']))
            sighting_points.append(int(i['sighting_points4']))
            gorizontal_angles_gradus.append(int(i['gorizontal_angle_gradus1']))
            gorizontal_angles_gradus.append(int(i['gorizontal_angle_gradus2']))
            gorizontal_angles_gradus.append(int(i['gorizontal_angle_gradus3']))
            gorizontal_angles_gradus.append(int(i['gorizontal_angle_gradus4']))
            gorizontal_angles_min.append(float(i['gorizontal_angle_min1']))
            gorizontal_angles_min.append(float(i['gorizontal_angle_min2']))
            gorizontal_angles_min.append(float(i['gorizontal_angle_min3']))
            gorizontal_angles_min.append(float(i['gorizontal_angle_min4']))
            sighting_points_neighbors.append(int(i['sighting_points_neighbors1']))
            sighting_points_neighbors.append(int(i['sighting_points_neighbors2']))
            sighting_points_neighbors_heights.append(float(i['sighting_points_neighbors_height1']))
            sighting_points_neighbors_heights.append(float(i['sighting_points_neighbors_height2']))
            vertical_angles_gradus.append(int(i['vertical_angle_gradus1']))
            vertical_angles_gradus.append(int(i['vertical_angle_gradus2']))
            vertical_angles_gradus.append(int(i['vertical_angle_gradus3']))
            vertical_angles_gradus.append(int(i['vertical_angle_gradus4']))
            vertical_angles_min.append(float(i['vertical_angle_min1']))
            vertical_angles_min.append(float(i['vertical_angle_min2']))
            vertical_angles_min.append(float(i['vertical_angle_min3']))
            vertical_angles_min.append(float(i['vertical_angle_min4']))
            rails.append(float(i['rail1']))
            rails.append(float(i['rail2']))
            rails.append(float(i['rail3']))
            rails.append(float(i['rail4']))
        
        else:
            station_names.append(int(i['station_name']))
            station_heights.append(float(i['station_height']))        
            sighting_points.append(int(i['sighting_points1']))
            sighting_points.append(int(i['sighting_points2']))
            sighting_points.append(int(i['sighting_points3']))
            sighting_points.append(int(i['sighting_points4']))
            gorizontal_angles_gradus.append(int(i['gorizontal_angle_gradus1']))
            gorizontal_angles_gradus.append(int(i['gorizontal_angle_gradus2']))
            gorizontal_angles_gradus.append(int(i['gorizontal_angle_gradus3']))
            gorizontal_angles_gradus.append(int(i['gorizontal_angle_gradus4']))
            gorizontal_angles_min.append(float(i['gorizontal_angle_min1']))
            gorizontal_angles_min.append(float(i['gorizontal_angle_min2']))
            gorizontal_angles_min.append(float(i['gorizontal_angle_min3']))
            gorizontal_angles_min.append(float(i['gorizontal_angle_min4']))
            sighting_points_neighbors.append(int(i['sighting_points_neighbors1']))
            #sighting_points_neighbors.append(int(i['sighting_points_neighbors2']))
            sighting_points_neighbors_heights.append(float(i['sighting_points_neighbors_height1']))
            #sighting_points_neighbors_heights.append(float(i['sighting_points_neighbors_height2']))
            vertical_angles_gradus.append(int(i['vertical_angle_gradus1']))
            vertical_angles_gradus.append(int(i['vertical_angle_gradus2']))
            #vertical_angles_gradus.append(int(i['vertical_angle_gradus3']))
            #vertical_angles_gradus.append(int(i['vertical_angle_gradus4']))
            vertical_angles_min.append(float(i['vertical_angle_min1']))
            vertical_angles_min.append(float(i['vertical_angle_min2']))
            #vertical_angles_min.append(float(i['vertical_angle_min3']))
            #vertical_angles_min.append(float(i['vertical_angle_min4']))
            rails.append(float(i['rail1']))
            rails.append(float(i['rail2']))
            #rails.append(float(i['rail3']))
            #rails.append(float(i['rail4']))
        count1+=1

    
    k1=0
    for i in range(8, len(df[0])-2, 6):
        df[0][i] = station_names[k1]
        df[0][i+2] = station_heights[k1]
        if k1+1 < len(station_names):
            k1+=1
    k1=0
    for i in range(8, len(df[1])-3, 6):
        df[1][i] = sighting_points[k1]    
        df[1][i+1] = sighting_points[k1+1]
        df[1][i+2] = sighting_points[k1+2]
        df[1][i+3] = sighting_points[k1+3]
        df[3][i] = gorizontal_angles_gradus[k1]
        df[3][i+1] = gorizontal_angles_gradus[k1+1]
        df[3][i+2] = gorizontal_angles_gradus[k1+2]
        df[3][i+3] = gorizontal_angles_gradus[k1+3]
        df[4][i] = gorizontal_angles_min[k1]
        df[4][i+1] = gorizontal_angles_min[k1+1]
        df[4][i+2] = gorizontal_angles_min[k1+2]
        df[4][i+3] = gorizontal_angles_min[k1+3]
    
        if k1+4 < len(sighting_points):
            k1+=4
    k1=0
    k2=0
    for i in range(11, len(df[7])-4, 3):
        df[7][i] = sighting_points_neighbors[k1]
        df[7][i+1] = sighting_points_neighbors_heights[k1]
        df[9][i] = vertical_angles_gradus[k2]
        df[9][i+1] = vertical_angles_gradus[k2+1]
        df[10][i] = vertical_angles_min[k2]
        df[10][i+1] = vertical_angles_min[k2+1]
        df[11][i] = rails[k2]
        df[11][i+1] = rails[k2+1]
        if k1+1 < len(sighting_points_neighbors):
            k1+=1
        if k2+2 < len(vertical_angles_gradus):
            k2+=2



    #mat = [meters, meters_corrections, station_names, station_heights, sighting_points, gorizontal_angles_gradus,
    #gorizontal_angles_min, sighting_points_neighbors, sighting_points_neighbors_heights,
    #vertical_angles_gradus, vertical_angles_min, rails]
    '''print('meters: ', mat[0])
    print('meters_corrections: ', mat[1])
    print('station_names: ', mat[2])
    print('stastion_heights: ', mat[3])
    print('sighting_points: ', mat[4])
    print('gorizontal_angles_gradus: ', mat[5])
    print('gorizontal_angles_min: ', mat[6])
    print('sighting_points_neighbors: ', mat[7])
    print('sighting_points_neighbors_heights: ', mat[8])
    print('vertical_angles_gradus: ', mat[9])
    print('vertical_angles_min: ', mat[10])
    print('rails: ', mat[11])'''
    print(df)
    #return()

#calculations(JoF, stf2)
    

    
    #path = 'C:/Users/Илья/Documents/'
    #filename = 'Тахеометрическая съемка_2Т30П.xls'
    #df = pd.read_excel(f"{path}{filename}", header=None)
    #код для динамической таблицы поправок







    for j in range(1, df.shape[1]): 
        value = df.at[1, j] 
        if type(value) == type(np.nan):
            index_1_table = j
            break
    df1 = df.iloc[1:3, 1:index_1_table]
    df1_numpy = df1.to_numpy()
    df2 = df.iloc[8:df.shape[0], 0:df.shape[1]]

    # функция для округления до 0,1
    def f_round(array, index = 1):
        for i in range(len(array)):
            znak = 0
            if array[i] > 0:
                znak = 1
            else:
                znak = -1
            
            t = abs(array[i])    
            t_index = t * 10 ** index
            t_index_int = int(t_index)
            
            if t_index - t_index_int < 0.5:
                array[i] = znak * t_index_int / 10 ** index
            else:
                t_index_int += 1
                array[i] = znak * t_index_int / 10 ** index
        return array
    def f_round0(num, index = 1):
        znak = 0
        if num > 0:
            znak = 1
        else:
            znak = -1
            
        t = abs(num)    
        t_index = t * 10 ** index
        t_index_int = int(t_index)
            
        if t_index - t_index_int < 0.5:
            num = znak * t_index_int / 10 ** index
        else:
            t_index_int += 1
            num = znak * t_index_int / 10 ** index  
        return num

    # считаю горитольные и средние углы
    df_new1 = list(df2.loc[:,3])
    df_new2 = list(df2.loc[:,4])
    array_gor_angle_gr = []
    array_gor_angle_min = []
    array_gor_angle_gr_mean = []
    array_gor_angle_min_mean = []


    for i in range(3, len(df_new1), 6):
        mn1 = df_new2[i - 2] - df_new2[i - 3]
        gr1 = int(df_new1[i - 2] - df_new1[i - 3])
        
        if mn1 < 0:
            mn1 += 60
            gr1 -= 1
            array_gor_angle_min.append(mn1)
        else:
            array_gor_angle_min.append(mn1)
        
        if gr1 < 0:
            gr1 += 360
            array_gor_angle_gr.append(gr1)
        else:
            array_gor_angle_gr.append(gr1)
        
        mn2 = df_new2[i] - df_new2[i - 1]
        gr2 = int(df_new1[i] - df_new1[i - 1])
    
        if mn2 < 0:
            mn2 += 60
            gr2 -= 1
            array_gor_angle_min.append(mn2)
        else:
            array_gor_angle_min.append(mn2)
            
        if gr2 < 0:
            gr2 += 360
            array_gor_angle_gr.append(gr2)
        else:
            array_gor_angle_gr.append(gr2)
            
        array_gor_angle_gr_mean.append(int((gr1 + gr2) / 2))
        array_gor_angle_min_mean.append((mn1 + mn2) / 2)

    f_round(array_gor_angle_min_mean)

    # df_new1 и df_new2 массивы с градусами и минутами вертикальных углов 
    # array_ver_angle_min - перевожу угол в градусы
    df_new1 = list(df2.loc[:,9])
    df_new2 = list(df2.loc[:,10])

    array_ver_angle_min = []

    for i in range(3, len(df_new1) - 3, 3):
        if df_new1[i] > 0:
            array_ver_angle_min.append(df_new1[i] * 60 + df_new2[i])
        if df_new1[i] < 0:
            array_ver_angle_min.append(df_new1[i] * 60 - abs(df_new2[i]))
        if df_new1[i] == 0:
            array_ver_angle_min.append(df_new2[i])
        
        if df_new1[i + 1] > 0:
            array_ver_angle_min.append(df_new1[i + 1] * 60 + df_new2[i + 1])
        if df_new1[i + 1] < 0:
            array_ver_angle_min.append(df_new1[i + 1] * 60 - abs(df_new2[i + 1]))
        if df_new1[i + 1] == 0:
            array_ver_angle_min.append(df_new2[i + 1])
        
    # считаю mo и v (в минутах) для 2т30п
    array_angle_gr_mo_2t30 = []
    array_angle_min_mo_2t30 = []
    array_angle_gr_v_2t30 = []
    array_angle_min_v_2t30 = []

    array_angle_mo_2t30 = []
    array_angle_v_2t30 = []
    for i in range(0, len(array_ver_angle_min), 2):
        mo = (array_ver_angle_min[i] + array_ver_angle_min[i + 1]) / 2
        v = (array_ver_angle_min[i] - array_ver_angle_min[i + 1]) / 2
        array_angle_mo_2t30.append(mo)
        array_angle_v_2t30.append(v)

    f_round(array_angle_mo_2t30)
    f_round(array_angle_v_2t30)

    # перехожу от минут к градусам и минутам для mo и v
    for i in range(len(array_angle_mo_2t30)):
        if array_angle_mo_2t30[i] < 60 and array_angle_mo_2t30[i] > -60:
            array_angle_gr_mo_2t30.append(0)
            array_angle_min_mo_2t30.append(array_angle_mo_2t30[i])
        elif array_angle_mo_2t30[i] >= 60:
            array_angle_gr_mo_2t30.append(int(array_angle_mo_2t30[i] // 60))
            array_angle_min_mo_2t30.append(array_angle_mo_2t30[i] % 60)
        else:
            array_angle_gr_mo_2t30.append(int(abs(array_angle_mo_2t30[i]) // 60) * (-1))
            array_angle_min_mo_2t30.append(abs(array_angle_mo_2t30[i]) % 60)
            
        if array_angle_v_2t30[i] < 60 and array_angle_v_2t30[i] > -60:
            array_angle_gr_v_2t30.append(0)
            array_angle_min_v_2t30.append(array_angle_v_2t30[i])
        elif array_angle_v_2t30[i] >= 60:
            array_angle_gr_v_2t30.append(int(array_angle_v_2t30[i] // 60))
            array_angle_min_v_2t30.append(array_angle_v_2t30[i] % 60)
        else:
            array_angle_gr_v_2t30.append(int(abs(array_angle_v_2t30[i]) // 60) * (-1))
            array_angle_min_v_2t30.append(abs(array_angle_v_2t30[i]) % 60)

    # array_angle_gr_mo_2t30 array_angle_min_mo_2t30 array_angle_gr_v_2t30 array_angle_min_v_2t30 
    # в этих массивах храняться данные которые нужно загрузить в M и N столбцы excel

    #считаю значение d (столбец Q в excel)
    df_station_data = list(df2.loc[:,0])
    df_station = []
    for i in range(2, len(df_station_data) - 1, 6):
        df_station.append(df_station_data[i])

    df_vizpoint_data = list(df2.loc[:,7])
    df_vizpoint = []
    for i in range(4, len(df_vizpoint_data) - 2, 3):
        df_vizpoint.append(df_vizpoint_data[i])

    dl = []
    dl.append(df_station[0] - df_vizpoint[0])

    for i in range(1, len(df_station) - 1):
        dl.append(df_station[i] - df_vizpoint[2 * i - 1])
        dl.append(df_station[i] - df_vizpoint[2 * i])
    dl.append(df_station[-1] - df_vizpoint[-1])
    f_round(dl, 2)

    # переходим от вертикальных углов в минутах к радианам
    array_angle_v_gr_2t30 = [i / 60 for i in array_angle_v_2t30]
    array_angle_v_rad_2t30 = [radians(i) for i in array_angle_v_gr_2t30]
    array_angle_v_rad_cos_2t30 = [cos(i) for i in array_angle_v_rad_2t30]
    array_angle_v_tan_2t30 = [tan(i) for i in array_angle_v_rad_2t30]
    # код для столбца P
    I = []
    D = []
    S = []
    h1 = []
    h = []
    h_pr = []
    h_obr = []
    h_mean = []
    reika = list(df2.loc[:,11])
    q = 0
    for a in range(3, len(reika) - 3, 3):
        i = (reika[a] + reika[a + 1]) / 2
        i01 = f_round0(i)
        I.append(i01)
        
        for j in range(len(df1_numpy[0])): 
            value = df1_numpy[0, j]
            if i >= value:   # исправлено, раньше было: if value >= i:
                popravka = df1_numpy[1, j]
                break
        d = i01 + popravka    
        D.append(d)
        
        s = d * array_angle_v_rad_cos_2t30[q] * array_angle_v_rad_cos_2t30[q]
        s01 = f_round0(s)
        S.append(s01)
        
        #считаю h1
        h1_el = s01 * array_angle_v_tan_2t30[q]
        h1_el01 = f_round0(h1_el, 2)
        h1.append(h1_el01)
        
        #считаю h 
        h_el = dl[q] + h1_el01
        h_el0 = f_round0(h_el, 2)
        h.append(h_el0)
        
        if a % 2 != 0:
            h_pr.append(h_el0)
        if a % 6 == 0:
            h_obr.append(h_el0)
        
        if len(h_pr) == len(h_obr):
            if h_pr[-1] > 0:
                h_mean_el = (abs(h_pr[-1]) + abs(h_obr[-1])) / 2
            else:
                h_mean_el = (-1) * (abs(h_pr[-1]) + abs(h_obr[-1])) / 2
            
            h_mean.append(f_round0(h_mean_el, 2))
        
        q += 1

    S_column = []
    T_column = []
    U_column = []

    for i in range(0, len(D), 2):
        S_column_el = abs(D[i] - D[i + 1])
        S_column.append(f_round0(S_column_el))

        T_column_el = (D[i] + D[i + 1]) / 2
        T_column.append(f_round0(T_column_el, 2))

        U_column_el = S_column[-1] / T_column[-1]
        if U_column_el != 0:
            U_column.append(1)
            U_column.append(int(1 / U_column_el))
        else:
            U_column.append(U_column_el)


    V_column = []
    for i in range(len(h_obr)):
        V_column_el = round(abs(h_pr[i] + h_obr[i])*100)
        V_column.append(V_column_el)

    print(U_column)

    #tacheometry = pd.read_excel("Тахеометрическая съемка_2Т30П.xls", sheet_name="Тахеометрия",header=None)
    tacheometry = pd.read_excel(f"{path}{filename}", sheet_name="Тахеометрия",header=None)

    index_table = [4]
    for i in range(4, tacheometry.shape[0]):
        if type(tacheometry.at[i, 0]) == type(np.nan):
            index_table.append(i - 2)
            index_table.append(i + 5)
    index_table.append(tacheometry.shape[0] - 2)


    index_table0 =[]
    for l in range(0, len(index_table), 2):
        index_table0.append(index_table[l])

    #index_table0.append(index_table)
    #index_table1 = sum(index_table0, [])

    tacheometry_df = []
    #2 <-> len(index_table)
    for i in range(0, 1, 2):
        tacheometry_df = tacheometry.loc[index_table[i]:index_table[i + 1], 0:17]
        gor_limb_gr = list(tacheometry_df.loc[:,1])
        gor_limb_min = list(tacheometry_df.loc[:,2])
        gor_limb_rad = []
        for j in range(len(gor_limb_gr)):
            gor_limb_rad.append(radians(gor_limb_gr[j] + gor_limb_min[j]/60))
        
        ver_limb_gr = list(tacheometry_df.loc[:,4])
        ver_limb_min = list(tacheometry_df.loc[:,5])
        

        tacheometry_df0 = tacheometry.iloc[index_table0[i] - 4:index_table0[i] - 2, 0:17]
        tacheometry_df0_np = tacheometry_df0.to_numpy()
        
        KL = [tacheometry_df0_np[0, 8], tacheometry_df0_np[0, 10]]
        KP = [tacheometry_df0_np[1, 8], tacheometry_df0_np[1, 10]]
        if KL[0] == 0 and KP[0] == 0:
            KL_min = KL[1]
            KP_min = KP[1]
        else:
            KL_min = KL[0] + KL[1] * KL[0] / abs(KL[0])
            KP_min = KP[0] + KP[1] * KP[0] / abs(KP[0])
        
        tach_MO_min = f_round0((KL_min + KP_min) / 2)

        tach_MO_gr = (abs(tach_MO_min) // 60) * tach_MO_min / abs(tach_MO_min)
        tach_MO_minn = (abs(tach_MO_min) % 60) * tach_MO_min / abs(tach_MO_min)

        tach_i = tacheometry_df0_np[1,1]
        
        tach_I = list(tacheometry_df.loc[:,10])
        
        tach_V = list(tacheometry_df.loc[:,13])
        
        tach_H = tacheometry_df0_np[1,16]
        print(tach_H)
        tach_v = []
        tach_v_gr = []
        tach_v_min = []
        tach_D = []
        tach_S = []
        tach_h = []
        tach_H_array = []
        for j in range(len(ver_limb_gr)):
        
            if ver_limb_gr[j] == 0:
                ver = ver_limb_min[j]
            else:
                ver = ver_limb_gr[j] * 60 + ver_limb_min[j]# * ver_limb_gr[j] / abs(ver_limb_gr[j])
            v_el = ver - tach_MO_min
            tach_v.append(v_el)
            
            tach_v_gr_el = (abs(v_el) // 60) * v_el / abs(v_el)
            tach_v_gr.append(tach_v_gr_el)
            tach_v_min_el = (abs(v_el) % 60) * v_el / abs(v_el)
            tach_v_min.append(tach_v_min_el)

            for k in range(len(df1_numpy[0])): 
                value = df1_numpy[0, k]
                if value >= tach_I[j]:
                    tach_popravka = df1_numpy[1, k]
                    break
            tach_d_el = tach_I[j] + tach_popravka   
            tach_D.append(tach_d_el)

            tach_v_el_rad_cos = cos(radians(v_el / 60))
            tach_v_el_rad_tan = tan(radians(v_el / 60))
            tach_s_el = tach_d_el * tach_v_el_rad_cos * tach_v_el_rad_cos
            tach_S.append(tach_s_el)

            tach_h_el = tach_s_el * tach_v_el_rad_tan + tach_i - tach_V[j]
            tach_h.append(tach_h_el)

            tach_H_el = tach_H + tach_h_el
            tach_H_array.append(tach_H_el)


    def truncpart(n, k=1):
        return(trunc(n*10**k)/10**k)

    last_dir_angle_gr = 354
    last_dir_angle_min = 25.9
    last_alpha = radians(last_dir_angle_gr + (last_dir_angle_min/60))
    array_dir_angle_gr = [221]                                                                          #Дир угол в гр с входными значениями
    array_dir_angle_min = [55.3]                                                                        #Дир угол в мин с входными значениями
    array_alpha = []                                                                                    #alpha
    array_alpha.append(radians(array_dir_angle_gr[0] + (array_dir_angle_min[0]/60)))
    #H
    array_h = [222.06]
    last_h = 218.83

    array_x = [4523.7]
    array_y = [2917.3]
    last_x = 4485.0
    last_y = 2545.1

    array_betta = []                                                                                    #betta
    for i in range(len(array_gor_angle_gr_mean)):
        array_betta.append(radians(array_gor_angle_gr_mean[i] + (array_gor_angle_min_mean[i]/60))) 
    #Cумм практ 
    sump_betta = sum(array_betta)                                                                       #Сумма практ столбца betta
    sump_gor_angle_gr_mean = trunc(degrees(sump_betta))                                                 #Сумм практ угла поворота в градусах
    sump_gor_angle_min_mean = (degrees(sump_betta)-sump_gor_angle_gr_mean)*60                           #Сумм практ угла поворота в минутах
    #Сумм теор
    sumt_betta = last_alpha - array_alpha[0] + pi*4                                                     #Сумма теор столбца betta
    sumt_gor_angle_gr_mean = trunc(degrees(sumt_betta))                                                 #Сумм теор угла поворота в градусах
    sumt_gor_angle_min_mean = (degrees(sumt_betta)-sumt_gor_angle_gr_mean)*60                           #Сумм теор угла поворота в минутах
    #fb1
    fb1_gor_angle_min_mean = sump_gor_angle_min_mean - sumt_gor_angle_min_mean

    array_gor_angle_min_popravka = []
    for i in range(len(array_gor_angle_min_mean)):
        array_gor_angle_min_popravka.append(truncpart(-fb1_gor_angle_min_mean/len(array_gor_angle_min_mean)))
    for i in range(len(array_gor_angle_min_mean)):
        if int(sum(array_gor_angle_min_popravka)*10) != int(-fb1_gor_angle_min_mean*10):
            array_gor_angle_min_popravka[i] += 0.1
    print(fb1_gor_angle_min_mean,'\n',array_gor_angle_min_popravka)
    array_gor_angle_unknown = []                                                                        #безымянный столбец G в таблице
    for i in range(len(array_betta)): 
        array_gor_angle_unknown.append(radians(array_gor_angle_min_popravka[i]/60) + array_betta[i])
        #print(array_gor_angle_unknown)

    array_gor_angle_gr_new = []                                                                         #Расчёт угла поворота исправ в градусах
    for i in range(len(array_gor_angle_unknown)):
        array_gor_angle_gr_new.append(trunc(degrees(array_gor_angle_unknown[i])))

    array_gor_angle_min_new = []                                                                        #Расчёт угла поворота исправ в минутах
    for i in range(len(array_gor_angle_unknown)):
        array_gor_angle_min_new.append(round((degrees(array_gor_angle_unknown[i]) - array_gor_angle_gr_new[i])*60, 1))

    ########################################################array_dir_angle_gr = [221]                                                                          #Дир угол в гр с входными значениями
    ########################################################array_dir_angle_min = [55.3]                                                                        #Дир угол в мин с входными значениями
    ########################################################
    ########################################################array_alpha = []                                                                                    #alpha
    ########################################################array_alpha.append(radians(array_dir_angle_gr[0] + (array_dir_angle_min[0]/60)))
    for i in range(len(array_gor_angle_unknown)):
        array_alpha.append(array_gor_angle_unknown[i]+array_alpha[i]-pi)

    for i in range(len(array_alpha)-1):                                                                 #Расчёт дир уг в градусах
        array_dir_angle_gr.append(trunc(degrees(array_alpha[i+1]))) 

    for i in range(len(array_alpha)-1):                                                                 #Расчёт дир уг в минутах
        array_dir_angle_min.append(round((degrees(array_alpha[i+1]) - array_dir_angle_gr[i+1])*60, 1))

    ########################################################last_dir_angle_gr = 354
    ########################################################last_dir_angle_min = 25.9
    ########################################################last_alpha = radians(last_dir_angle_gr + (last_dir_angle_min/60))

    #Cумм практ
    ########################################################sump_betta = sum(array_betta)                                                                       #Сумма практ столбца betta
    ########################################################sump_gor_angle_gr_mean = trunc(degrees(sump_betta))                                                 #Сумм практ угла поворота в градусах
    ########################################################sump_gor_angle_min_mean = (degrees(sump_betta)-sump_gor_angle_gr_mean)*60                           #Сумм практ угла поворота в минутах
    sump_gor_angle_unknown = sum(array_gor_angle_unknown)                                               #Сумм практ безымянного столбца G
    sump_gor_angle_gr_new = trunc(degrees(sump_gor_angle_unknown))                                      #Сумм практ исправленного угла поворота в градусах
    sump_gor_angle_min_new = (degrees(sump_gor_angle_unknown)-sump_gor_angle_gr_new)*60                 #Сумм практ исправленного угла поворота в минутах

    #вывод сумм для проверки
    #print(f'{sump_gor_angle_gr_mean} {sump_gor_angle_min_mean} {sump_betta}\n {sump_gor_angle_gr_new} {sump_gor_angle_min_new} {sump_gor_angle_unknown} ')

    #Cумм теор
    ########################################################sumt_betta = last_alpha - array_alpha[0] + pi*4                                                     #Сумма теор столбца betta
    ########################################################sumt_gor_angle_gr_mean = trunc(degrees(sumt_betta))                                                 #Сумм теор угла поворота в градусах
    ########################################################sumt_gor_angle_min_mean = (degrees(sumt_betta)-sumt_gor_angle_gr_mean)*60                           #Сумм теор угла поворота в минутах


    #fb величина
    ########################################################fb1_gor_angle_min_mean = sump_gor_angle_min_mean - sumt_gor_angle_min_mean
    fb2_gor_angle_min_mean = sum(array_gor_angle_min_popravka)
    fb1_betta = radians(fb1_gor_angle_min_mean/60)
    fb2_betta = radians(fb2_gor_angle_min_mean/60)



    #S и сумма S
    array_s = []
    for i in range(0, len(S), 2):
        array_s.append(round((S[i]+S[i+1])/2 , 1))
    sum_s = sum(array_s)

    #dx и dy
    array_dx = []
    array_dy = []
    for i in range(len(array_s)):
        array_dx.append(round(array_s[i]*cos(array_alpha[i+1]) ,1)) 
        array_dy.append(round(array_s[i]*sin(array_alpha[i+1]) ,1))
    #print(f'{array_dx}\n{array_dy}')

    #сумма практическая и теоретическая dx и dy
    sump_dx = sum(array_dx)
    sump_dy = sum(array_dy)
    sumt_dx= last_x - array_x[0]
    sumt_dy= last_y - array_y[0]
    #print(f'{sump_dx} {sump_dy}\n{sumt_dx} {sumt_dy}')

    #fx и fy и fs и fs/sum_s и 1/N
    fx_dx = sump_dx - sumt_dx
    fy_dy = sump_dy - sumt_dy 
    fs_s = sqrt(fx_dx**2+fy_dy**2)
    fs_div_sum_s = fs_s / sum_s
    one_div_n = 1 / fs_div_sum_s
    #print(f'{fx_dx}  {fy_dy}  {fs_s}  {fs_div_sum_s} {one_div_n}')

    #поправка dx и dy
    array_dx_popravka = []
    array_dy_popravka = []
    for i in range(len(array_s)):
        array_dx_popravka.append(-fx_dx*array_s[i]/sum_s)
        array_dy_popravka.append(-fy_dy*array_s[i]/sum_s)
    sum_dx_popravka = sum(array_dx_popravka)
    sum_dy_popravka = sum(array_dy_popravka)
    #print(f'{array_dx_popravka}\n{array_dy_popravka}\n{sum_dx_popravka} {sum_dy_popravka}')

    #dx и dy исправленные
    array_dx_new = []
    array_dy_new = []
    for i in range(len(array_dx)):
        array_dx_new.append(array_dx[i]+array_dx_popravka[i])
        array_dy_new.append(array_dy[i]+array_dy_popravka[i])

    #сумма практическая dx и dy исправленные
    sump_dx_new = sum(array_dx_new) 
    sump_dy_new = sum(array_dy_new) 

    #расчёт всех x и y
    for i in range(len(array_dx_new)):
        array_x.append(round(array_dx_new[i]+array_x[i] ,3)) 
        array_y.append(round(array_dy_new[i]+array_y[i] ,3)) 
    #print(f'{array_x}\n{array_y}')

    #допуски
    dopusk_с20 = 1 * sqrt(4)
    dopusk_o18 = sum_s/(400*sqrt(3))
    dopusk_o20 = sum_s/dopusk_o18
    #print(f'{dopusk_с20} {dopusk_o18} {dopusk_o20}')


    #h среднее и суммы
    sump_h_mean = sum(h_mean)
    sumt_h_mean = last_h - array_h[0]
    #print(f'{h_mean} {sump_h_mean} {sumt_h_mean}')

    #fh и fh доп
    fh = sump_h_mean - sumt_h_mean
    fh1_dop = (sum_s*0.04)/sqrt(3)
    fh2_dop = fh1_dop / 100
    #print(f'{fh} {fh1_dop} {fh2_dop}')

    #V I и h испр
    array_v_i = []
    array_h_new = []
    for i in range(len(array_s)):
        array_v_i.append(-fh*array_s[i]/sum_s)
        array_h_new.append(h_mean[i] + array_v_i[i])
    sum_v_i = sum(array_v_i)
    sum_h_new = sum(array_h_new)
    v_i_t19 = -fh
    v_i_t19_div_sum_s = v_i_t19 / sum_s
    print(v_i_t19,'\n', v_i_t19_div_sum_s )

    #заполнение H 
    for i in range(len(array_h_new)):
        array_h.append(array_h[i]+array_h_new[i])    



    #ВЫВОД ДАННЫХ В ТАБЛИЦУ
    #так как в основной таблице наны, их я и использовал при заполнении
    #print(array_gor_angle_gr)
    #print(array_gor_angle_min)
    #print(array_gor_angle_gr_mean)
    #print(array_gor_angle_min_mean)
    #print('__________')
    #print(array_angle_gr_mo_2t30)
    #print(array_angle_min_mo_2t30)
    #print(array_angle_gr_v_2t30) 
    #print(array_angle_min_v_2t30) 
    #print('__________')
    #print(I)
    #print(D)
    #print(S)
    #print('___')
    #print(h1)
    #print(dl)
    #print(h)
    #print('___')
    #print(h_pr)
    #print(h_obr)
    #print(h_mean)
    p_ = 'C:/Users/Илья/Desktop/'
    f_ = 'konets_2_lista.xlsx'
    #print(U_column)
    def tabl1(db, db2, ar1_5, ar2_5, ar1_6, ar2_6, ar1_12, ar2_12, ar1_13,
    ar2_13, ar1_15, ar2_15, ar3_15, ar1_16, ar2_16, ar3_16,ar1_17, ar2_17, 
    ar3_17, ar1_20, d_h):#, path1, filename1):    
        
        from pandas.io.excel import ExcelWriter
        import numpy as np
        lsttodf12 = [np.nan for x in db2[12]]
        lsttodf13 = [np.nan for x in db2[13]]
        lsttodf5 = [np.nan for x in db2[5]]
        lsttodf6 = [np.nan for x in db2[6]]
        lsttodf15 = [np.nan for x in db2[15]]
        lsttodf16 = [np.nan for x in db2[16]]
        lsttodf17 = [np.nan for x in db2[17]]
        lsttodf20 = [np.nan for x in db2[20]]
        lsttodf20[1] = "ΔD"
        k0 = 0
        k1 = 0
        k2 = 0
        for j in range(2, len(lsttodf5)-1, 6):        
            lsttodf5[j] = ar2_5[k0]
            lsttodf6[j] = ar2_6[k0]
            lsttodf5[j-1] = ar1_5[k1]
            lsttodf6[j-1] = ar1_6[k1]
            lsttodf5[j+1] = ar1_5[k1+1]
            lsttodf6[j+1] = ar1_6[k1+1]
            
            if (k0+1) <= len(ar2_5)-1:    
                k0+=1
            if (k1+2) <= len(ar1_5)-1:
                k1+=2
                
        for i in range(3, len(lsttodf12)-3, 3):         #len(lsttodf12)-3  раньше было:  len(lsttodf12)-1
            lsttodf12[i] = ar1_12[k2]
            lsttodf12[i+1] = ar2_12[k2]
            lsttodf13[i] = ar1_13[k2]
            lsttodf13[i+1] = ar2_13[k2]
            if k2+1 <= len(ar1_12)-1:
                k2+=1    
        k0 = 0
        k1 = 0
        #k2 = 0
        for i in range(2, len(lsttodf15)-3, 3):        #len(lsttodf15)-3  раньше было:  len(lsttodf15)-2
            lsttodf15[i] = ar1_15[k0]
            lsttodf15[i+1] = ar2_15[k0]
            lsttodf15[i+2] = ar3_15[k0]
            lsttodf16[i] = ar1_16[k0]
            lsttodf16[i+1] = ar2_16[k0]
            lsttodf16[i+2] = ar3_16[k0]
            if (i%2 == 0):    
                lsttodf17[i] = ar1_17[k1]
                lsttodf17[i+1] = ar2_17[k1]
                lsttodf17[i+2] = ar3_17[k1]
                if k1+1 < len(ar1_17):
                    k1+=1
                
            if k0+1 < len(ar1_15):
                k0+=1         
        k0 = 2
        for i in range(len(ar1_20)):       
            if ar1_20[i] == 0:
                lsttodf20[k0] = ar1_20[i]
            if ar1_20[i] == 1:
                lsttodf20[k0] = ar1_20[i]
                lsttodf20[k0+1] = ar1_20[i+1]
            if k0+6 < len(lsttodf20)-3:        # раньше было: if k0+6 < len(lsttodf20)-2:
                k0+=6       
        db2[5] = lsttodf5
        db2[6] = lsttodf6
        db2[12] = lsttodf12
        db2[13] = lsttodf13
        db2[15-1] = lsttodf15
        db2[16-1] = lsttodf16 
        db2[17-1] = lsttodf17 
        db2[20-3] = lsttodf20
        db.iloc[8:db.shape[0], 0:db.shape[1]] = db2   
        #dbp = db.drop([14, 18, 19], axis=1)    
        k0=0
        for i in range(11, len(db[18])-7, 6):
            db[18][i] = d_h[k0]
            if k0+1 < len(d_h):
                k0+=1
            
        return(db)    # раньше было: return(dbp)

    kolvostan = (len(df2[0]) - int(df2.isna().sum()[0]))//2
    stoLperar = [sump_dx,sumt_dx,fx_dx,fs_s,fs_div_sum_s,one_div_n,sum_dx_popravka]
    stoMperar = [sump_dy,sumt_dy,fy_dy,np.nan,np.nan,np.nan,sum_dy_popravka]
    stoOperar = [sump_dy_new,np.nan,np.nan,dopusk_o18,np.nan,dopusk_o20,np.nan]
    stoTperar = [sump_h_mean,sumt_h_mean,fh,fh1_dop,v_i_t19,v_i_t19_div_sum_s,np.nan]
    n_stantsiy = list()
    for i in df2[0]:
        if (type(i) == type(5)):
            n_stantsiy.append(i)



    def tabl2(kolvost, n_stants, stoBar, stoB1p, stoB2p, stoCar1, stoCar2, stoC1p, stoC2p,
    stoC3p, stoC4p, stoC5p, stoHar, stoHp, stoIar, stoI1p, stoI2p, stoKar, stoLar1, stoLar2,
    stoLperar, stoMar1, stoMar2, stoMperar, stoNar, stoNp, stoOar, stoOperar, stoPar, stoPp,
    stoQar, stoQp, stoSar, stoSp, stoTar, stoTperar, stoUar, stoUp1, stoUp2, stoVar, stoVp,
    stoWar, stoWp):
        longdf_and_ar = (6 + kolvost*2 + 7)
        df = pd.DataFrame(columns = range(18), index = range(longdf_and_ar))    
        slova1sto = ['Сумма практ', 'Сумма теор', 'f b', np.nan, 'допуск']
        slova5sto = ['[практич]=','[теор]=','fx, fy=','fs=','fs/[s]=','1/N=','[vi]=']
        slova13sto = ['теор=','fh=','fh доп=','[vi]=','[vi]/[s]=']
        slovazag3str = [np.nan, 'угол поворота', np.nan, 'дирекционный угол', np.nan,
        'S', 'dX', 'dY', 'dX', 'dY', 'X', 'Y']#, np.nan,np.nan,np.nan,np.nan,np.nan,np.nan]
        slovazag4str = [np.nan, 'гр', 'мин', 'гр', 'мин', np.nan,np.nan,np.nan,
        'исправл','исправл', np.nan,np.nan, '№','S(m)','h cp','V I','h испр','H']
        #Названия таблиц + некоторые слова:
        df[0][0] = 'Ведомость вычисления координат точек хода'
        df[12][0] = 'Ведомость увязки превышений тахеометрического хода'
        df[12][len(df[0])-7] = 'Суммы'
        df[3][len(df[0])-4] = '[S] ='
        df[8][len(df[8])-2] = 'допуск'
        df[8][len(df[8])-4] = 'допуск'
        # 0 столбец:
        k1=6
        for i in range(len(n_stants)):
            df[0][k1] = n_stants[i]
            df[12][k1] = n_stants[i]
            #временно тут стобцы 10 и 11 и W:
            df[10][k1] = stoPar[i]
            df[11][k1] = stoQar[i]
            df[17][k1] = stoWar[i]
                    
            if k1+2 <= len(df[0]):
                k1+=2    
        #1+2 столбцы массивы:
        k1=6    
        for i in range(len(stoBar)):
            df[1][k1] = stoBar[i]
            df[2][k1] = stoCar1[i]
            df[2][k1-1] = stoCar2[i]
            if k1+2 <= len(df[0]):
                k1+=2
        # 1 столбец переменные:
        df[1][len(df[1])-6] = stoB1p
        df[1][len(df[1])-5] = stoB2p
        # 2 столбец переменные:
        df[2][len(df[1])-6] = stoC1p
        df[2][len(df[1])-5] = stoC2p
        df[2][len(df[1])-4] = stoC3p
        df[2][len(df[1])-3] = stoC4p
        df[2][len(df[1])-2] = stoC5p    
        #3+4 столбцы массивы:
        k1=5
        for i in range(len(stoHar)):       
            df[3][k1] = stoHar[i]
            df[4][k1] = stoIar[i]
            if k1+2 <= len(df[3]):
                k1+=2
        #3+4+8+10+11 cтолбцы переменные:
        df[3][len(df[3])-7] = stoHp
        df[4][len(df[4])-7] = stoI1p
        df[4][len(df[4])-4] = stoI2p
        df[8][len(df[8])-7] = stoNp
        df[10][len(df[10])-8] = stoPp
        df[11][len(df[11])-8] = stoQp
        #столбец S+U+V+W переменная:
        df[13][len(df[13])-7] = stoSp
        df[15][len(df[15])-7] = stoUp1
        df[15][len(df[15])-4] = stoUp2
        df[16][len(df[16])-7] = stoVp
        df[17][len(df[17])-8] = stoWp
        #5+6+7+8+9+S+T+U+V столбцы массивы:
        k1=7
        for i in range(len(stoKar)):
            df[5][k1] = stoKar[i]
            df[6][k1] = stoLar1[i]
            df[6][k1-1] = stoLar2[i]
            df[7][k1] = stoMar1[i]
            df[7][k1-1] = stoMar2[i]
            df[8][k1] = stoNar[i]
            df[9][k1] = stoOar[i]
            df[13][k1] = stoSar[i]
            df[14][k1] = stoTar[i]
            df[15][k1] = stoUar[i]
            df[16][k1] = stoVar[i]
            if k1+2 <= len(df[5]):
                k1+=2
        #сразу напишем все 'заголовки':
        k1=0
        for i in range(len(df[0])-6, len(df[0])-1):
            df[0][i] = slova1sto[k1]
            if k1+1 < len(slova1sto):
                k1+=1    
        for i in range(len(slovazag3str)):
            df[i][3] = slovazag3str[i]
        for i in range(len(slovazag4str)):
            df[i][4] = slovazag4str[i]
        k1=0
        for i in range(len(df[5])-7, len(df[5])):
            df[5][i] = slova5sto[k1]
            df[6][i] = stoLperar[k1]  #6 столбец переменные
            df[7][i] = stoMperar[k1]  #7 столбец переменные
            df[9][i] = stoOperar[k1]  #9 столбец переменные
            df[14][i] = stoTperar[k1] #14 столбец переменные
            if k1+1 < len(slova5sto):
                k1+=1
        k1=0
        for i in range(len(df[13])-6, len(df[13])-1):
            df[13][i] = slova13sto[k1]
            if k1+1 < len(slova13sto):
                k1+=1
        
        return(df)


    def vivodexl(path1, filename1, db1, db2='', db3=''):
        with ExcelWriter(f"{path1}{filename1}", mode="w") as writer:
            db1.to_excel(writer, sheet_name='ход', index=None, header=None)
            #if db2 != '' and db2 != '':    
            db2.to_excel(writer, sheet_name='Ведомость ур-я', index=None, header=None)
                #db3.to_excel(writer, sheet_name='Тахеометрия', index=None, header=None)
        #print(db1)
        #print(db2)
        #print(db3)


    sheet1 = tabl1(df, df2, array_gor_angle_gr, array_gor_angle_gr_mean, array_gor_angle_min,
    array_gor_angle_min_mean, array_angle_gr_mo_2t30, array_angle_gr_v_2t30, array_angle_min_mo_2t30,
    array_angle_min_v_2t30, I, D, S, h1, dl, h, h_pr, h_obr, h_mean, U_column, V_column)   #, p_, f_ )

    sheet2 = tabl2(kolvostan, n_stantsiy, array_gor_angle_gr_mean, sump_gor_angle_gr_mean,
    sumt_gor_angle_gr_mean, array_gor_angle_min_mean, array_gor_angle_min_popravka, 
    sump_gor_angle_min_mean, sumt_gor_angle_min_mean, fb1_gor_angle_min_mean, fb2_gor_angle_min_mean,
    dopusk_с20, array_dir_angle_gr, last_dir_angle_gr, array_dir_angle_min, last_dir_angle_min,
    sum_s, array_s, array_dx, array_dx_popravka, stoLperar, array_dy, array_dy_popravka,
    stoMperar, array_dx_new, sump_dx_new, array_dy_new, stoOperar, array_x, last_x, array_y, last_y,
    array_s, sum_s, h_mean, stoTperar, array_v_i, sum_v_i, fh2_dop, array_h_new,
    sum_h_new, array_h, last_h)

    
    #tabl2(kolvostan, n_stantsiy, array_gor_angle_gr_mean, sump_gor_angle_gr_mean,
    #sumt_gor_angle_gr_mean, array_gor_angle_min_mean, array_gor_angle_min_popravka, 
    #sump_gor_angle_min_mean, sumt_gor_angle_min_mean, fb1_gor_angle_min_mean, fb2_gor_angle_min_mean,
    #dopusk_с20, array_dir_angle_gr, last_dir_angle_gr, array_dir_angle_min, last_dir_angle_min,
    #sum_s, array_s, array_dx, array_dx_popravka, stoLperar, array_dy, array_dy_popravka,
    #stoMperar)

    #vivodexl(p_, f_, sheet1, sheet2)
    
    #return(sheet1, sheet2)
    return(sheet1, sheet2)