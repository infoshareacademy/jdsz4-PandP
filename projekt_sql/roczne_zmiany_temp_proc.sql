--roczne zmiany temperatur w procentach
--San Francisco
--Palo Alto
--Redwood City
--San Jose
--Mountain

with wsad as
         (
             select distinct ztc.city city,
                             wn.rok rok,
                             avg(wn.min_temperature_c) over (partition by wn.rok)  avg_min_temp_rok,
                             avg(wn.max_temerature_c) over (partition by wn.rok)   avg_max_temp_rok,
                             avg(wn.mean_temperature_c) over (partition by wn.rok) avg_mean_temp_rok
             from weather_norm wn
                      join zip_to_cities ztc on wn.zip_code = ztc.zip_code
             where ztc.city = 'Mountain View'
             group by wn.rok, ztc.city, wn.miesiac, wn.max_temerature_C, wn.mean_temperature_C, wn.min_temperature_C
             order by 2, 3
         )
select
       city,
       rok,
       avg_min_temp_rok,
       (((avg_min_temp_rok - lag(avg_min_temp_rok) over ())/lag(avg_min_temp_rok) over ())*100)::numeric(2) YoY_proc_avg_min_temp_rok,
       avg_max_temp_rok,
       (((avg_max_temp_rok - lag(avg_max_temp_rok) over ())/lag(avg_max_temp_rok) over ())*100)::numeric(2)  YoY_proc_avg_max_temp_rok,
       avg_mean_temp_rok,
       (((avg_mean_temp_rok - lag(avg_mean_temp_rok) over ())/lag(avg_mean_temp_rok) over ())*100)::numeric(2) YoY_proc_mean_min_temp_rok
from wsad