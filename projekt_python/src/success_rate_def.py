def success_ratio(data_frame):
    
    success_number = data_frame['state'][data_frame['state']=='successful'].count()
    failed_number = data_frame['state'][data_frame['state']=='failed'].count()
    cancelled_number = data_frame['state'][data_frame['state']=='canceled'].count()
    all_number = success_number + failed_number + cancelled_number
    
    if success_number == 0 and failed_number == 0 and cancelled_number == 0:
        print('Sorry, for this particular setting we haven\'t found any campaign at all!\nYou are sailing some uncharted waters here!')
    elif success_number >= 0 and all_number > 0:
        success_ratio = success_number / all_number
        if data_frame.shape[0] < 10:
            print('The overall success ratio is: ',round(success_ratio,4)*100,'%')
            print('However due to lack of sufficient data this is based on a small number of past campaigns.\nIf you\'d like to check the odds for a bigger sample, please consider changing some of the parameters to either \'not considered\' or \'any\'')
            print('Here are the ones we found similar:')
            print(data_frame) # tutaj coś zmienić, żeby df się ładniej wyświetlało
        elif data_frame.shape[0] < 50:
            print('The overall success ratio is: ',round(success_ratio,4)*100,'%')
            print('However due to lack of sufficient data this is based on a limited number of past campaigns.\nIf you\'d like to check the odds for a bigger sample, please consider changing some of the parameters to either \'not considered\' or \'any\'')
        else:
            print('The success ratio for past campaigns similar to yours is:\n',round(success_ratio,4)*100,'%')
         
    else:
        print('something went really wrong, contact the admin!')
