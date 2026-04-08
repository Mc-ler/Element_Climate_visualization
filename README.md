TASK DESCRIPTION

Data&Description&task(data -> analysis -> visualization -> set model -> visualization): 

data_ori["STATION","DATE","EMNT","EMXT"](from NOAA)
  D:There two STATION with its recode time, MAX/MIN temperature.
  I:1.Single STATION with different months or years and predict the next month/years(scikit_learn, neural_network)
    devise a math model with random factor to describe climate change
    2.Differentiate two STATION with  distance(compute by Long. Lat.)
    Info:
    CHM00057127 Lat. 43.5333 Long. 10.313
    CHM00057131 Lat. 12.217  Long. 109.187
    units of temperature: Fahrenheit(transfer to celsius  -->  F = (C * 1.8) + 32)
  Q:How to calculate distance by Long. and Lat. How to address missing values, How to make distance as a factor into math model, How to make time as a factor.

china_SURF_Station["STATION_ID","PROVINCE","STATION_NAME","LONGITUDE","LATITUDE","ALTITUDE"](from NSTI)
  D:There many stations with its location
  I:Different Stations location in interactive_map with its altitude
  Q:How to use map in python, How to make it interacted, How to make altitude bar in map

gsom_sample_csv["STATION"..."TMAX","TMIN"](from NOAA)
  D:There many indexes but just 4 rows in it

tips: D(description), I(ideas), Q(questions)


Daily Log:
  2026-4-7: clear and get data. next step is going to format date used in plot
  2026-4-8: define the explore function but have loop problem to solve. maybe we can let original data into function.