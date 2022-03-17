import random
fortunes = ["1. Good things come to those who wait.",
            "2. Patience is a virtue.",
            "3. The early bird gets the worm.",
            "4. A wise man once said, everything in its own time and place.",
            "5. Fortune cookies rarely share fortunes."]

the_number = random.randint(0, 4)

print ("Your Fourtune is: ", fortunes[the_number])