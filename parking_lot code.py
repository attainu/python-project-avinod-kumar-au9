
import time

import datetime
current_date_time= datetime.datetime.now()

class vehicle_Parking:
    def __init__(self):
        pass

    def creating_parking_slots(self,create_parking_lot):
        
        if create_parking_lot > 0:
            for i in range(1,(create_parking_lot)+1):
                if i not in dicti:
                    dicti['slot_'+str(i)]="a"

            # print(dicti)
            print("Created a parking lot with",create_parking_lot,"slots")

        if create_parking_lot <= 0:
            print("Minimum one slot is required to create parking slot")

    
    def parking_vehicle_at_slots(self,vehicle_for_parking):
        checking_parking_lot_is_full=0

        for i in range(1,(create_parking_lot)+1):
            checking_parking_lot_is_full+=1
            
            checking_given_car_in_parking_lot= 0
            for keys,values in dicti.items():
                if vehicle_for_parking[0] in values:
                    checking_given_car_in_parking_lot+=1
                    break
            

            if checking_given_car_in_parking_lot == 1:
                    print("Car already in parking slot, recheck your entry")
                    break
            
            if checking_given_car_in_parking_lot != 1:
                if dicti["slot_"+str(i)]=="a":
                    
                    dicti["slot_"+str(i)]=vehicle_for_parking
                    print("Allocated slot number:", i,"on",current_date_time.strftime('%d-%m-%Y'),current_date_time.strftime("%H:%M"))
                    # print(dicti)
                    break
            
            if checking_given_car_in_parking_lot!= 1:    
                if checking_parking_lot_is_full==create_parking_lot:
            
                        print("Sorry, parking lot is full")

        
    def Leaving_vehicle_from_parking_lot(self,Leave,create_parking_lot):
        
        if int(Leave) > create_parking_lot:
            print("Slot number",Leave,"is not found")
        if int(Leave) <= create_parking_lot:
            if dicti['slot_'+str(Leave)]=="a":
                print("Slot number",Leave,"is already free")
        if int(Leave) <= create_parking_lot:
            if dicti['slot_'+str(Leave)]!="a":
                dicti['slot_'+str(Leave)]="a"
                print("Slot number",Leave,"is free")


    def getParkingStatus(self,create_parking_lot):
        checking_parking_free_count=0
        for keys,values in dicti.items():
            
            if values == "a":
                checking_parking_free_count+=1

        
        if  checking_parking_free_count==create_parking_lot:
            print("Sorry, parking lot is empty")

        else:
            print("--- Below parking status as on:",current_date_time.strftime('%d-%m-%Y'),current_date_time.strftime("%H:%M"),"---")
            print("Slot No.  Registration No   Colour")
            for keys,values in dicti.items():
                if values != "a":
                    print(keys[5:]," "," "," "," ",values[0]," "," ",values[1])

        
            

    def get_registration_numbers_for_cars_with_colour(self,colour):
        str=""
        for keys,values in dicti.items():
            if colour in values:
                str+=values[0]+", "
        
        print(str[:-2])
        

    def get_slot_numbers_for_cars_with_colour(self,colour):
        str=""
        for keys,values in dicti.items():
            if colour in values:
                str+=keys[5:]+", "
        print(str[:-2])
        


    def get_slot_number_for_registration_number(self,registration_number):
        for keys,values in dicti.items():
            if registration_number in values:
                return (keys[5:])
        else:
            return ("Not found")
    

    def show_line(self,user_input):
        
        
        
        if "create_parking_lot" in user_input:
            
            global create_parking_lot
            create_parking_lot=int(user_input[-1])
            
            parking.creating_parking_slots(create_parking_lot)
        
        
        if "park" in user_input:
            
            vehicle_for_parking= user_input[1]+" "+user_input[2]
            vehicle_for_parking=vehicle_for_parking.split()
            
            parking.parking_vehicle_at_slots(vehicle_for_parking)


        if "leave" in user_input:
            
            Leave = user_input[1]
            parking.Leaving_vehicle_from_parking_lot(Leave,create_parking_lot)

        
        if "status" in user_input:
            parking.getParkingStatus(create_parking_lot)
            

        
        if "registration_numbers_for_cars_with_colour" in user_input:
            colour= user_input[-1]
            parking.get_registration_numbers_for_cars_with_colour(colour)

        
        if "slot_numbers_for_cars_with_colour" in user_input:
            colour=user_input[-1]
            parking.get_slot_numbers_for_cars_with_colour(colour)


        if "slot_number_for_registration_number" in user_input:
            registration_number = user_input[-1]
            parking.get_slot_number_for_registration_number(registration_number)
            print(parking.get_slot_number_for_registration_number(registration_number))

        

def main():
    
    global dicti
    dicti=dict()
    print("\n")
    print("---- Welcome to the automated parking lot system ----")
    
    print("\n")
    time.sleep(2)
    print("System Initializing...")
    time.sleep(1)
    print("\n")
    
    while True:
        user_input=input("Choose your choice - interactive or file ?: ").lower()
        
        if "interactive" in user_input:
            break
        if "file" in user_input:
            break
        if "exit" in user_input:
            print("Thank you for mingling with Me!")
            break
        if "interactive" not in user_input or "file" not in user_input:
            print("Human error!, Choose a right choice")
            print("\n")
    
    print("\n")
    if "interactive" in user_input:
        
        while True:
            print("----------------------------")
            user_input=input("What can i do for you ?: ")
            user_input=user_input.split()
            if "".join(user_input)=="exit":
                print("\n")
                print("Thank you for mingling with Me!")
                print("\n")
                break

            if "create_parking_lot" not in user_input:
                if "park" not in user_input:
                    if "leave" not in user_input:
                        
                        if "status" not in user_input:
                            if "registration_numbers_for_cars_with_colour" not in user_input:
                                if "slot_numbers_for_cars_with_colour" not in user_input:
                                    if "slot_number_for_registration_number" not in user_input:
                                        print("PLease enter a valid command")
                                        continue  
            
            
            if "create_parking_lot" in user_input:
                if len(user_input) < 2 or len(user_input) > 2:
                    print("PLease enter a valid command")
                    continue
            
            if "park" in user_input:
                if len(dicti)==0 :
                    print("Parking lot is not created, please create it")
                    continue
                if len(user_input) < 3 or len(user_input) > 3:
                    print("PLease enter a valid command")
                    continue 
            if "leave" in user_input:
                if len(dicti)==0 :
                    print("Parking lot is not created, please create it")
                    continue
                if len(user_input) < 2 or len(user_input) > 2:
                    print("PLease enter a valid command")
                    continue
            if "status" in user_input:
                if len(dicti)==0 :
                    print("Parking lot is not created, please create it")
                    continue
                if len(user_input) > 1:
                    print("PLease enter a valid command")
                    continue
            if "registration_numbers_for_cars_with_colour" in user_input:
                if len(dicti)==0 :
                    print("Parking lot is not created, please create it")
                    continue
                if len(user_input) < 2 or len(user_input) > 2:
                    print("PLease enter a valid command")
                    continue
            if "slot_numbers_for_cars_with_colour" in user_input:
                if len(dicti)==0 :
                    print("Parking lot is not created, please create it")
                    continue
                if len(user_input) < 2 or len(user_input) > 2:
                    print("PLease enter a valid command")
                    continue
            if "slot_number_for_registration_number" in user_input:
                if len(dicti)==0 :
                    print("Parking lot is not created, please create it")
                    continue
                if len(user_input) < 2 or len(user_input) > 2:
                    print("PLease enter a valid command")
                    continue
            
                                      
            parking.show_line(user_input)
            
            

    if "file" in user_input:
   
        with open("D:\Vinod\practise/1.txt","r") as f:
            for line in f:
                user_input=line
                user_input=user_input.split()
                if "create_parking_lot" not in user_input:
                    if "park" not in user_input:
                        if "leave" not in user_input:
                            
                            if "status" not in user_input:
                                if "registration_numbers_for_cars_with_colour" not in user_input:
                                    if "slot_numbers_for_cars_with_colour" not in user_input:
                                        if "slot_number_for_registration_number" not in user_input:
                                            print("PLease enter a valid command")
                                            continue  
                
                
                
                if "create_parking_lot" in user_input:
                    if len(user_input) < 2 or len(user_input) > 2:
                        print("PLease enter a valid command")
                        continue
                
                if "park" in user_input:
                    if len(dicti)==0 :
                        print("Parking lot is not created, please create it")
                        continue
                    if len(user_input) < 3 or len(user_input) > 3:
                        print("PLease enter a valid command")
                        continue 
                if "leave" in user_input:
                    if len(dicti)==0 :
                        print("Parking lot is not created, please create it")
                        continue
                    if len(user_input) < 2 or len(user_input) > 2:
                        print("PLease enter a valid command")
                        continue
                if "status" in user_input:
                    if len(dicti)==0 :
                        print("Parking lot is not created, please create it")
                        continue
                    if len(user_input) > 1:
                        print("PLease enter a valid command")
                        continue
                if "registration_numbers_for_cars_with_colour" in user_input:
                    if len(dicti)==0 :
                        print("Parking lot is not created, please create it")
                        continue
                    if len(user_input) < 2 or len(user_input) > 2:
                        print("PLease enter a valid command")
                        continue
                if "slot_numbers_for_cars_with_colour" in user_input:
                    if len(dicti)==0 :
                        print("Parking lot is not created, please create it")
                        continue
                    if len(user_input) < 2 or len(user_input) > 2:
                        print("PLease enter a valid command")
                        continue
                if "slot_number_for_registration_number" in user_input:
                    if len(dicti)==0 :
                        print("Parking lot is not created, please create it")
                        continue
                    if len(user_input) < 2 or len(user_input) > 2:
                        print("PLease enter a valid command")
                        continue


                parking.show_line(user_input)
            print("\n")
            print("Thank you for mingling with Me!")
            print("\n")



if __name__ == "__main__":
    
    
    parking= vehicle_Parking()
    main()

