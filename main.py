print('formula a. workdone = force * distance ...(w.d=fd)')
print('formula b. acceleration = velocity / time ...(a=v/t)')
print('formula c. voltage = current * time ...(v=it)')
print('formula d. velocity = displacement / time ...(v=d/t)')
print('formula e. force = mass * acceleration ...(f=ma)')
selected_formula = input('\nchoose the formula you will want to use\n enter a formula between a-e:')
if selected_formula == 'a':
    force = float(input('enter the force:'))
    distance = float(input('enter the distance:'))
    print('workdone = ' +str(force * distance) + 'J')
elif selected_formula == 'b':
    velocity = float(input('enter the velocity:'))
    time = float(input('enter the time:'))
    print('acceleration = ' +str(velocity / time) + 'm/s2')
elif selected_formula == 'c':
    current = float(input('enter the current:'))
    time = float(input('enter the time:'))
    print('voltage = ' +str(current * time) + 'V')
elif selected_formula == 'd':
    displacement = float(input('enter the displacement:'))
    time = float(input('enter the time:'))
    print('velocity = ' +str(displacement / time) + 'm/s')
elif selected_formula == 'e':
    mass = float(input('enter the mass:'))
    acceleration = float(input('enter the acceleration:'))
    print('force = ' +str(mass * acceleration) + 'N')
else:
    print('invalid formula...')
