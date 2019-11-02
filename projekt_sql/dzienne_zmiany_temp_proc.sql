--dzienne zmiany temperatur w procentach
--San Francisco
--Palo Alto
--Redwood City
--San Jose
--Mountain View

with wsad as
         (
             select distinct ztc.city city,
                             wn.rok rok,
                             wn.miesiac miesiac,
                             wn.dzien dzien,
                             wn.dzien_tygodnia dzien_tygodnia,
                             avg(wn.min_temperature_c) over (partition by wn.dzien)  avg_min_temp_dzien,
                             avg(wn.max_temerature_c) over (partition by wn.dzien)   avg_max_temp_dzien,
                             avg(wn.mean_temperature_c) over (partition by wn.dzien) avg_mean_temp_dzien
             from weather_norm wn
                      join zip_to_cities ztc on wn.zip_code = ztc.zip_code
             where ztc.city = 'Mountain View'
             group by wn.rok, ztc.city, wn.miesiac, wn.max_temerature_C, wn.mean_temperature_C, wn.min_temperature_C, wn.dzien, wn.dzien_tygodnia
             order by 2, 3
         )
select
       city,
       rok,
       miesiac,
       dzien,
       dzien_tygodnia,
       avg_min_temp_dzien,
       (((avg_min_temp_dzien - lag(avg_min_temp_dzien) over ())/lag(avg_min_temp_dzien) over ())*100)::numeric(2) DoD_proc_avg_min_temp_dzien,
       avg_max_temp_dzien,
       (((avg_max_temp_dzien - lag(avg_max_temp_dzien) over ())/lag(avg_max_temp_dzien) over ())*100)::numeric(2)  DoD_proc_avg_max_temp_dzien,
       avg_mean_temp_dzien,
       (((avg_mean_temp_dzien - lag(avg_mean_temp_dzien) over ())/lag(avg_mean_temp_dzien) over ())*100)::numeric(2) DoD_proc_mean_min_temp_dzien
from wsad
group by 1,2,3,4,5,6,8,10
order by 2,3
