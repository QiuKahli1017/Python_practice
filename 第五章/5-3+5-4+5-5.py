alien_color='green'
score=0
if alien_color.lower()=='green':
    score+=5
elif alien_color.lower()=='red':
    score+=4
else:
    score+=3
print(score)
