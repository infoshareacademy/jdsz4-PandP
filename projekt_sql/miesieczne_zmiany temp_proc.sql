--miesieczne zmiany temperatur w procentach
--San Francisco
--Palo Alto
--Redwood City
--San Jose
--Mountain

with wsad as
         (
             select  distinct ztc.city city,
                             wn.rok rok,
                             wn.miesiac miesiac,
                             avg(wn.min_temperature_c) over (partition by wn.miesiac)  avg_min_temp_month,
                             avg(wn.max_temerature_c) over (partition by wn.miesiac)   avg_max_temp_month,
                             avg(wn.mean_temperature_c) over (partition by wn.miesiac) avg_mean_temp_month
             from weather_norm wn
                      join zip_to_cities ztc on wn.zip_code = ztc.zip_code
             where ztc.city = 'Mountain View'
             group by wn.rok, ztc.city, wn.miesiac, wn.max_temerature_C, wn.mean_temperature_C, wn.min_temperature_C
             order by 2, 3
         )
select
       city,
       rok,
       miesiac,
       avg_min_temp_month,
       (((avg_min_temp_month - lag(avg_min_temp_month) over ())/lag(avg_min_temp_month) over ())*100)::numeric(2) MoM_proc_avg_min_temp_month,
       avg_max_temp_month,
       (((avg_max_temp_month - lag(avg_max_temp_month) over ())/lag(avg_max_temp_month) over ())*100)::numeric(2)  MoM_proc_avg_max_temp_month,
       avg_mean_temp_month,
       (((avg_mean_temp_month - lag(avg_mean_temp_month) over ())/lag(avg_mean_temp_month) over ())*100)::numeric(2) MoM_proc_mean_min_temp_month
from wsad
group by 1,2,3,4,6,8
order by 2,3