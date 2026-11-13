import time
lifts = {
    'bench': '205',
    'squat': '230',
    'deadlift': '330',
    'dl': '330',
}
while True:
    which_lift = input('What Compund lift do you want to know my max of? Options are Bench, Squat, and Deadlift\n').lower().strip()
    if which_lift in lifts:  
        print(f"My {which_lift} is "+lifts[which_lift])
        question = input('do you want to know the others? [Y] or [N]\n').lower().strip()
        if question in ['y']:
            running = True 

        elif question in ['n']:
            print('Good fucking bye than bro')
        else:
            print('TWO OPTIONS and you typed some bullshit')
            question2 = input('u wanna know it or not? [Y] or [N]\n').lower().strip()
            if question2 in ['n']:
                print('cya boi')
                break
            elif question2 in ['y', 'Y']:
                time.sleep(1.5)
                running = True
            else:
                print('u keep typing bullshit ur fuckin outta here broski')
                break             
    else: 
        print("do that shit again bro i gave you options")
        time.sleep(2)