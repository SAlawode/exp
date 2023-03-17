# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 20:25:56 2023

@author: user
"""

import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **all_item):
        #self.kwargs = kwargs
        self.contents=[]
        for key,value in all_item.items():
            for itr in range(value):
                self.contents.append(key)
    def __str__(self):
        s = ""
        for i in self.contents:
            s += i
            s += " "
        return s
    
    def draw(self, amount):
        drawn = []
        if amount >= len(self.contents):
            return self.contents
        else:
            for i in range(amount):
                item = self.contents.pop(random.randrange(len(self.contents)))
                drawn.append(item)  
        return drawn
    
    def get_contents(self, *kwargs):
        contents = []
        for i in self.kwargs:
            for k in range(self.kwargs[i]):
                contents.append(i)
        return contents



def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    #print(expected)
    m = 0
    #drawn = hat.draw(num_balls_drawn)
    for i in range(num_experiments-1):
        #print(hat)
        hat1 = copy.deepcopy(hat)
        drawn = hat1.draw(num_balls_drawn)
        drawn_dict = {}
        '''for elem in drawn:
            drawn_dict[elem] = drawn_dict.get(elem, 0) + 1
        for elem in expected_balls:
            if elem not in drawn_dict or expected_balls[elem] < drawn_dict[elem]:
                break
            #print(expected, drawn)
            else:
                m += 1'''
        for key, value in expected_balls.items():
            if drawn.count(key) < value:
                break
            else:
                m +=1
            
    return m/num_experiments
    
        

                
s = "good=3"
t = "verygood=2"
#print(contents)

hat = Hat(blue=3,red=2,green=6)
probability = experiment(hat=hat,
                         expected_balls={"blue":2,"green":1},
                         num_balls_drawn=4,
                         num_experiments=1000)

print(probability)

for i in range(3):
    print(i)