import random

#dictionary of anime genre as the keys and list of some anime titles as values
anime = {'Action':['One Piece','Naruto Shippuden','Naruto','JoJo\'s Bizarre Adventure'], 
'Adventure':['Inuyasha','10 Tokyo Warriors','3000 Leagues in Search of Mother','Tweeny Witches: The Adventure'],
 'Comedy':['D-Frag!','Robot Girls Z','Space Dandy','Mr. Osomatsu'], 
 'Drama':['Maroko','A Letter to Momo','	5 Centimeters Per Second','	The Pilot\'s Love Song'],
 'Fantasy':['10 Tokyo Warriors','Angel Beats!','Unbreakable Machine-Doll','Bikini Warriors'], 
 'Sports':['Ace of Diamond','Attack on Tomorrow','Haikyu!!','Hinomaru Sumo']}

#diplaying all the genre that exist in the dict
print("Which type of anime would you like to watch?")
for i in anime.keys():
    print(i,end="        ")
print()
a=1
while a:  #loop to continue if the entered genre doesn't exist or even entered in wrong format
    ans = input()
    if ans in anime.keys():
        print("You can start by watching ",random.choice(anime.get(ans)))   #picks a random value(anime title) from the list in the particular genre requested
        a=0
    else:
        print("\nThis category doesn't exist. Please choose a valid category:\n")
        a=1
input("Press enter to exit ;)")