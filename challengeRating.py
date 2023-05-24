from sklearn.ensemble import RandomForestRegressor
import pandas as pd
import json
from tkinter import *




with open('bestiary-bam.json', 'r') as f:
    data = json.load(f)
    
with open('bestiary-cm.json', 'r') as f:
    data2 = json.load(f)
    
with open('bestiary-bgdia.json', 'r') as f:
    data3 = json.load(f)
    
with open('bestiary-cos.json', 'r') as f:
    data4 = json.load(f)
    
with open('bestiary-crcotn.json', 'r') as f:
    data5 = json.load(f)
    
with open('bestiary-ggr.json', 'r') as f:
    data6 = json.load(f)

with open('bestiary-dsotdq.json', 'r') as f:
    data7 = json.load(f)
    
with open('bestiary-mm.json', 'r') as f:
    data8 = json.load(f)

with open('bestiary-mtf.json', 'r') as f:
    data9 = json.load(f)

with open('bestiary-gos.json', 'r') as f:
    data10 = json.load(f)
    
with open('bestiary-oota.json', 'r') as f:
    data11 = json.load(f)
    
with open('bestiary-toa.json', 'r') as f:
    data12 = json.load(f)
    
with open('bestiary-ftd.json', 'r') as f:
    data13= json.load(f)
    
with open('bestiary-pota.json', 'r') as f:
    data14= json.load(f)


def hp_score(data):
    monster_hp_dict = {}
    for monster in data['monster']:
        if 'hp' in monster:
            if 'average' in monster["hp"]:
                hp_average = monster["hp"]["average"]
            else:
                hp_average="N/A"
        else:
            hp_average=0
        monster_hp_dict[monster['name']] = hp_average
    return monster_hp_dict

def speed_score(data):
    scores = {}
    for monster in data['monster']:
        if 'speed' in monster:
            walk_speed_score = 0
            fly_speed_score = 0
            burrow_speed_score = 0
            climb_speed_score = 0
            swim_speed_score = 0

            if 'walk' in monster["speed"]:
                if isinstance(monster["speed"]["walk"], dict) and 'condition' in monster["speed"]["walk"]:
                    walk_speed_score = monster["speed"]["walk"]["number"]
                else:
                    walk_speed_score = monster["speed"]["walk"]
                    
            if 'fly' in monster["speed"]:
                if isinstance(monster["speed"]["fly"], dict) and 'condition' in monster["speed"]["fly"]:
                    fly_speed_score = monster["speed"]["fly"]["number"]
                else:
                    fly_speed_score = monster["speed"]["fly"]
            if 'burrow' in monster["speed"]:
                burrow_speed_score = monster["speed"]["burrow"]
            if 'climb' in monster["speed"]:
                climb_speed_score = monster["speed"]["climb"]
            if 'swim' in monster["speed"]:
                if isinstance(monster["speed"]["swim"], dict) and 'condition' in monster["speed"]["swim"]:
                    swim_speed_score=monster["speed"]["swim"]["number"]
                else:
                    swim_speed_score = monster["speed"]["swim"]
        else:
            walk_speed_score = 0
            fly_speed_score = 0
            burrow_speed_score = 0
            climb_speed_score = 0
            swim_speed_score = 0
            

        scores[monster['name']] = {
            'walk speed': walk_speed_score,
            'fly speed': fly_speed_score,
            'burrow speed': burrow_speed_score,
            'climb speed': climb_speed_score,
            'swim speed': swim_speed_score,
        }

    return scores



def size_score(data):
    scores={}
    size_scores = {'T': 1, 'S': 2, 'M': 3,'L':4,'H':5,'G':6}
    for monster in data['monster']:
        if 'size' in monster:
            size_score=size_scores[monster['size'][0]]
        else:
            size_score=2
        
        scores[monster['name']]=size_score
    return scores


def sense_score(data):
    scores={}
    sense_scores = {'darkvision':1,'blindsight':2,'truesight':4,'tremorsense':3}


    for monster in data['monster']:
    
        if 'senses' in monster:
            if len(monster['senses'])==1:
                new=monster['senses'][0].split()
                sense_score=sense_scores[new[0]]*int(new[1])
            else:
                new=monster['senses'][1].split()
                sense_score=sense_scores[new[0]]*int(new[1])
               
                
        else:
            sense_score=0
        
        scores[monster['name']]=sense_score
        
    return scores


def skills_score(data):
    scores={}
    for monster in data['monster']:
        physical_skills=0
        knowledge_skills=0
        emotional_skills=0
        survival_skills=0
        detective_skills=0
        performance_skills=0
        stealth_skills=0
        animal_skills=0
    
        if 'skill' in monster:
            if 'arcana' in monster['skill']:
                knowledge_skills+=int(monster['skill']['arcana'][1:])
            if 'stealth' in monster['skill']:
                stealth_skills+=int(monster['skill']['stealth'][1:])
            if 'persuasion' in monster['skill']:
                emotional_skills+=int(monster['skill']['persuasion'][1:])
            if 'intimidation' in monster['skill']:
                emotional_skills+=int(monster['skill']['intimidation'][1:])
            if 'deception' in monster['skill']:
                emotional_skills+=int(monster['skill']['deception'][1:])
            if 'survival' in monster['skill']:
                survival_skills+=int(monster['skill']['survival'][1:])
            if 'animal handling' in monster['skill']:
                animal_skills+=int(monster['skill']['animal handling'][1:])
            if 'nature' in monster['skill']:
                knowledge_skills+=int(monster['skill']['nature'][1:])
            if 'medicine' in monster['skill']:
                knowledge_skills+=int(monster['skill']['medicine'][1:])
            if 'religion' in monster['skill']:
                knowledge_skills+=int(monster['skill']['religion'][1:])
            if 'history' in monster['skill']:
                knowledge_skills+=int(monster['skill']['history'][1:])
            if 'acrobatics' in monster['skill']:
                physical_skills+=int(monster['skill']['acrobatics'][1:])
            if 'athletics' in monster['skill']:
                physical_skills+=int(monster['skill']['athletics'][1:])
            if 'sleight of hand' in monster['skill']:
                stealth_skills+=int(monster['skill']['sleight of hand'][1:])
            if 'perception' in monster['skill']:
                detective_skills+=int(monster['skill']['perception'][1:])
            if 'insight' in monster['skill']:
                detective_skills+=int(monster['skill']['insight'][1:])
            if 'investigation' in monster['skill']:
                detective_skills+=int(monster['skill']['investigation'][1:])
            if 'performance' in monster['skill']:
                performance_skills+=int(monster['skill']['performance'][1:])
                
        scores[monster['name']] = {
            'physical skills': physical_skills,
            'knowledge skills': knowledge_skills,
            'emotional skills': emotional_skills,
            'detective skills': detective_skills,
            'survival skills': survival_skills,
            'performance skills': performance_skills,
            'stealth skills': stealth_skills,
            'animal skills': animal_skills
        }
    
    return scores


def ac_score(data):
    scores={}
    for monster in data['monster']:
        ac_score=0
        if 'ac' in monster:
            if isinstance(monster['ac'][0],dict):
                if 'ac' in monster['ac'][0]:
                    ac_score=monster['ac'][0]['ac']
                else:
                    ac_score="N/A"
            else:
                ac_score=monster['ac'][0]
        
        scores[monster['name']]=ac_score
    
    return scores


def cr_score(data):
    scores={}
    for monster in data['monster']:
        if 'cr' in monster:
            if isinstance(monster["cr"], dict) :
                cr_score=int(monster['cr']['cr'])
                
            else:
                try:
                    cr_score=int(monster['cr'])
                except ValueError:
                    numerator, denominator = monster['cr'].split('/')
                    cr_score = int(numerator) / int(denominator)
        else:
            cr_score="N/A"
        scores[monster['name']]=cr_score
        
    return scores


hp_scores = hp_score(data)
speed_scores = speed_score(data)
size_scores = size_score(data)
sense_scores = sense_score(data)
skills_scores = skills_score(data)
ac_scores=ac_score(data)
cr_scores=cr_score(data)


df = pd.DataFrame({'name': list(hp_scores.keys()),
                   'hp': list(hp_scores.values()),
                   'walk speed': [d.get('walk speed', 0) for d in speed_scores.values()],
                   'fly speed': [d.get('fly speed', 0) for d in speed_scores.values()],
                   'burrow speed': [d.get('burrow speed', 0) for d in speed_scores.values()],
                   'climb speed': [d.get('climb speed', 0) for d in speed_scores.values()],
                   'swim speed': [d.get('swim speed', 0) for d in speed_scores.values()],
                   'size': list(size_scores.values()),
                   'sense': list(sense_scores.values()),
                   'physical skills': [d.get('physical skills', 0) for d in skills_scores.values()],
                   'knowledge skills': [d.get('knowledge skills', 0) for d in skills_scores.values()],
                   'emotional skills': [d.get('emotional skills', 0) for d in skills_scores.values()],
                   'survival skills': [d.get('survival skills', 0) for d in skills_scores.values()],
                   'detective skills': [d.get('detective skills', 0) for d in skills_scores.values()],
                   'performance skills': [d.get('performance skills', 0) for d in skills_scores.values()],
                   'stealth skills': [d.get('stealth skills', 0) for d in skills_scores.values()],
                   'animal skills': [d.get('animal skills', 0) for d in skills_scores.values()],
                   'ac': list(ac_scores.values()),
                   'cr': list(cr_scores.values())
                  })



hp_scores2 = hp_score(data2)
speed_scores2 = speed_score(data2)
size_scores2 = size_score(data2)
sense_scores2 = sense_score(data2)
skills_scores2 = skills_score(data2)
ac_scores2=ac_score(data2)
cr_scores2=cr_score(data2)


hp_scores3 = hp_score(data3)
speed_scores3 = speed_score(data3)
size_scores3 = size_score(data3)
sense_scores3 = sense_score(data3)
skills_scores3 = skills_score(data3)
ac_scores3=ac_score(data3)
cr_scores3=cr_score(data3)

hp_scores4 = hp_score(data4)
speed_scores4 = speed_score(data4)
size_scores4 = size_score(data4)
sense_scores4 = sense_score(data4)
skills_scores4 = skills_score(data4)
ac_scores4=ac_score(data4)
cr_scores4=cr_score(data4)

hp_scores5 = hp_score(data5)
speed_scores5 = speed_score(data5)
size_scores5 = size_score(data5)
sense_scores5 = sense_score(data5)
skills_scores5 = skills_score(data5)
ac_scores5=ac_score(data5)
cr_scores5=cr_score(data5)

hp_scores6 = hp_score(data6)
speed_scores6 = speed_score(data6)
size_scores6 = size_score(data6)
sense_scores6 = sense_score(data6)
skills_scores6 = skills_score(data6)
ac_scores6=ac_score(data6)
cr_scores6=cr_score(data6)

hp_scores7 = hp_score(data7)
speed_scores7 = speed_score(data7)
size_scores7 = size_score(data7)
sense_scores7 = sense_score(data7)
skills_scores7 = skills_score(data7)
ac_scores7=ac_score(data7)
cr_scores7=cr_score(data7)

hp_scores8 = hp_score(data8)
speed_scores8 = speed_score(data8)
size_scores8 = size_score(data8)
sense_scores8 = sense_score(data8)
skills_scores8 = skills_score(data8)
ac_scores8=ac_score(data8)
cr_scores8=cr_score(data8)

hp_scores9 = hp_score(data9)
speed_scores9 = speed_score(data9)
size_scores9 = size_score(data9)
sense_scores9 = sense_score(data9)
skills_scores9 = skills_score(data9)
ac_scores9=ac_score(data9)
cr_scores9=cr_score(data9)

hp_scores10 = hp_score(data10)
speed_scores10 = speed_score(data10)
size_scores10 = size_score(data10)
sense_scores10 = sense_score(data10)
skills_scores10 = skills_score(data10)
ac_scores10=ac_score(data10)
cr_scores10=cr_score(data10)

hp_scores11 = hp_score(data11)
speed_scores11 = speed_score(data11)
size_scores11 = size_score(data11)
sense_scores11 = sense_score(data11)
skills_scores11 = skills_score(data11)
ac_scores11=ac_score(data11)
cr_scores11=cr_score(data11)

hp_scores12 = hp_score(data12)
speed_scores12 = speed_score(data12)
size_scores12 = size_score(data12)
sense_scores12 = sense_score(data12)
skills_scores12 = skills_score(data12)
ac_scores12=ac_score(data12)
cr_scores12=cr_score(data12)

hp_scores13 = hp_score(data13)
speed_scores13 = speed_score(data13)
size_scores13 = size_score(data13)
sense_scores13 = sense_score(data13)
skills_scores13 = skills_score(data13)
ac_scores13=ac_score(data13)
cr_scores13=cr_score(data13)

hp_scores14 = hp_score(data14)
speed_scores14 = speed_score(data14)
size_scores14 = size_score(data14)
sense_scores14 = sense_score(data14)
skills_scores14 = skills_score(data14)
ac_scores14=ac_score(data14)
cr_scores14=cr_score(data14)


df2 = pd.DataFrame({'name': list(hp_scores2.keys()),
                   'hp': list(hp_scores2.values()),
                   'walk speed': [d.get('walk speed', 0) for d in speed_scores2.values()],
                   'fly speed': [d.get('fly speed', 0) for d in speed_scores2.values()],
                   'burrow speed': [d.get('burrow speed', 0) for d in speed_scores2.values()],
                   'climb speed': [d.get('climb speed', 0) for d in speed_scores2.values()],
                   'swim speed': [d.get('swim speed', 0) for d in speed_scores2.values()],
                   'size': list(size_scores2.values()),
                   'sense': list(sense_scores2.values()),
                   'physical skills': [d.get('physical skills', 0) for d in skills_scores2.values()],
                   'knowledge skills': [d.get('knowledge skills', 0) for d in skills_scores2.values()],
                   'emotional skills': [d.get('emotional skills', 0) for d in skills_scores2.values()],
                   'survival skills': [d.get('survival skills', 0) for d in skills_scores2.values()],
                   'detective skills': [d.get('detective skills', 0) for d in skills_scores2.values()],
                   'performance skills': [d.get('performance skills', 0) for d in skills_scores2.values()],
                   'stealth skills': [d.get('stealth skills', 0) for d in skills_scores2.values()],
                   'animal skills': [d.get('animal skills', 0) for d in skills_scores2.values()],
                   'ac': list(ac_scores2.values()),
                   'cr': list(cr_scores2.values())
                  })

df3 = pd.DataFrame({'name': list(hp_scores3.keys()),
                   'hp': list(hp_scores3.values()),
                   'walk speed': [d.get('walk speed', 0) for d in speed_scores3.values()],
                   'fly speed': [d.get('fly speed', 0) for d in speed_scores3.values()],
                   'burrow speed': [d.get('burrow speed', 0) for d in speed_scores3.values()],
                   'climb speed': [d.get('climb speed', 0) for d in speed_scores3.values()],
                   'swim speed': [d.get('swim speed', 0) for d in speed_scores3.values()],
                   'size': list(size_scores3.values()),
                   'sense': list(sense_scores3.values()),
                   'physical skills': [d.get('physical skills', 0) for d in skills_scores3.values()],
                   'knowledge skills': [d.get('knowledge skills', 0) for d in skills_scores3.values()],
                   'emotional skills': [d.get('emotional skills', 0) for d in skills_scores3.values()],
                   'survival skills': [d.get('survival skills', 0) for d in skills_scores3.values()],
                   'detective skills': [d.get('detective skills', 0) for d in skills_scores3.values()],
                   'performance skills': [d.get('performance skills', 0) for d in skills_scores3.values()],
                   'stealth skills': [d.get('stealth skills', 0) for d in skills_scores3.values()],
                   'animal skills': [d.get('animal skills', 0) for d in skills_scores3.values()],
                   'ac': list(ac_scores3.values()),
                   'cr': list(cr_scores3.values())
                  })



df4 = pd.DataFrame({'name': list(hp_scores4.keys()),
                   'hp': list(hp_scores4.values()),
                   'walk speed': [d.get('walk speed', 0) for d in speed_scores4.values()],
                   'fly speed': [d.get('fly speed', 0) for d in speed_scores4.values()],
                   'burrow speed': [d.get('burrow speed', 0) for d in speed_scores4.values()],
                   'climb speed': [d.get('climb speed', 0) for d in speed_scores4.values()],
                   'swim speed': [d.get('swim speed', 0) for d in speed_scores4.values()],
                   'size': list(size_scores4.values()),
                   'sense': list(sense_scores4.values()),
                   'physical skills': [d.get('physical skills', 0) for d in skills_scores4.values()],
                   'knowledge skills': [d.get('knowledge skills', 0) for d in skills_scores4.values()],
                   'emotional skills': [d.get('emotional skills', 0) for d in skills_scores4.values()],
                   'survival skills': [d.get('survival skills', 0) for d in skills_scores4.values()],
                   'detective skills': [d.get('detective skills', 0) for d in skills_scores4.values()],
                   'performance skills': [d.get('performance skills', 0) for d in skills_scores4.values()],
                   'stealth skills': [d.get('stealth skills', 0) for d in skills_scores4.values()],
                   'animal skills': [d.get('animal skills', 0) for d in skills_scores4.values()],
                   'ac': list(ac_scores4.values()),
                   'cr': list(cr_scores4.values())
                  })


df5 = pd.DataFrame({'name': list(hp_scores5.keys()),
                   'hp': list(hp_scores5.values()),
                   'walk speed': [d.get('walk speed', 0) for d in speed_scores5.values()],
                   'fly speed': [d.get('fly speed', 0) for d in speed_scores5.values()],
                   'burrow speed': [d.get('burrow speed', 0) for d in speed_scores5.values()],
                   'climb speed': [d.get('climb speed', 0) for d in speed_scores5.values()],
                   'swim speed': [d.get('swim speed', 0) for d in speed_scores5.values()],
                   'size': list(size_scores5.values()),
                   'sense': list(sense_scores5.values()),
                   'physical skills': [d.get('physical skills', 0) for d in skills_scores5.values()],
                   'knowledge skills': [d.get('knowledge skills', 0) for d in skills_scores5.values()],
                   'emotional skills': [d.get('emotional skills', 0) for d in skills_scores5.values()],
                   'survival skills': [d.get('survival skills', 0) for d in skills_scores5.values()],
                   'detective skills': [d.get('detective skills', 0) for d in skills_scores5.values()],
                   'performance skills': [d.get('performance skills', 0) for d in skills_scores5.values()],
                   'stealth skills': [d.get('stealth skills', 0) for d in skills_scores5.values()],
                   'animal skills': [d.get('animal skills', 0) for d in skills_scores5.values()],
                   'ac': list(ac_scores5.values()),
                   'cr': list(cr_scores5.values())
                  })

df6 = pd.DataFrame({'name': list(hp_scores6.keys()),
                   'hp': list(hp_scores6.values()),
                   'walk speed': [d.get('walk speed', 0) for d in speed_scores6.values()],
                   'fly speed': [d.get('fly speed', 0) for d in speed_scores6.values()],
                   'burrow speed': [d.get('burrow speed', 0) for d in speed_scores6.values()],
                   'climb speed': [d.get('climb speed', 0) for d in speed_scores6.values()],
                   'swim speed': [d.get('swim speed', 0) for d in speed_scores6.values()],
                   'size': list(size_scores6.values()),
                   'sense': list(sense_scores6.values()),
                   'physical skills': [d.get('physical skills', 0) for d in skills_scores6.values()],
                   'knowledge skills': [d.get('knowledge skills', 0) for d in skills_scores6.values()],
                   'emotional skills': [d.get('emotional skills', 0) for d in skills_scores6.values()],
                   'survival skills': [d.get('survival skills', 0) for d in skills_scores6.values()],
                   'detective skills': [d.get('detective skills', 0) for d in skills_scores6.values()],
                   'performance skills': [d.get('performance skills', 0) for d in skills_scores6.values()],
                   'stealth skills': [d.get('stealth skills', 0) for d in skills_scores6.values()],
                   'animal skills': [d.get('animal skills', 0) for d in skills_scores6.values()],
                   'ac': list(ac_scores6.values()),
                   'cr': list(cr_scores6.values())
                  })

df7 = pd.DataFrame({'name': list(hp_scores7.keys()),
                   'hp': list(hp_scores7.values()),
                   'walk speed': [d.get('walk speed', 0) for d in speed_scores7.values()],
                   'fly speed': [d.get('fly speed', 0) for d in speed_scores7.values()],
                   'burrow speed': [d.get('burrow speed', 0) for d in speed_scores7.values()],
                   'climb speed': [d.get('climb speed', 0) for d in speed_scores7.values()],
                   'swim speed': [d.get('swim speed', 0) for d in speed_scores7.values()],
                   'size': list(size_scores7.values()),
                   'sense': list(sense_scores7.values()),
                   'physical skills': [d.get('physical skills', 0) for d in skills_scores7.values()],
                   'knowledge skills': [d.get('knowledge skills', 0) for d in skills_scores7.values()],
                   'emotional skills': [d.get('emotional skills', 0) for d in skills_scores7.values()],
                   'survival skills': [d.get('survival skills', 0) for d in skills_scores7.values()],
                   'detective skills': [d.get('detective skills', 0) for d in skills_scores7.values()],
                   'performance skills': [d.get('performance skills', 0) for d in skills_scores7.values()],
                   'stealth skills': [d.get('stealth skills', 0) for d in skills_scores7.values()],
                   'animal skills': [d.get('animal skills', 0) for d in skills_scores7.values()],
                   'ac': list(ac_scores7.values()),
                   'cr': list(cr_scores7.values())
                  })

df8 = pd.DataFrame({'name': list(hp_scores8.keys()),
                   'hp': list(hp_scores8.values()),
                   'walk speed': [d.get('walk speed', 0) for d in speed_scores8.values()],
                   'fly speed': [d.get('fly speed', 0) for d in speed_scores8.values()],
                   'burrow speed': [d.get('burrow speed', 0) for d in speed_scores8.values()],
                   'climb speed': [d.get('climb speed', 0) for d in speed_scores8.values()],
                   'swim speed': [d.get('swim speed', 0) for d in speed_scores8.values()],
                   'size': list(size_scores8.values()),
                   'sense': list(sense_scores8.values()),
                   'physical skills': [d.get('physical skills', 0) for d in skills_scores8.values()],
                   'knowledge skills': [d.get('knowledge skills', 0) for d in skills_scores8.values()],
                   'emotional skills': [d.get('emotional skills', 0) for d in skills_scores8.values()],
                   'survival skills': [d.get('survival skills', 0) for d in skills_scores8.values()],
                   'detective skills': [d.get('detective skills', 0) for d in skills_scores8.values()],
                   'performance skills': [d.get('performance skills', 0) for d in skills_scores8.values()],
                   'stealth skills': [d.get('stealth skills', 0) for d in skills_scores8.values()],
                   'animal skills': [d.get('animal skills', 0) for d in skills_scores8.values()],
                   'ac': list(ac_scores8.values()),
                   'cr': list(cr_scores8.values())
                  })

df9 = pd.DataFrame({'name': list(hp_scores9.keys()),
                   'hp': list(hp_scores9.values()),
                   'walk speed': [d.get('walk speed', 0) for d in speed_scores9.values()],
                   'fly speed': [d.get('fly speed', 0) for d in speed_scores9.values()],
                   'burrow speed': [d.get('burrow speed', 0) for d in speed_scores9.values()],
                   'climb speed': [d.get('climb speed', 0) for d in speed_scores9.values()],
                   'swim speed': [d.get('swim speed', 0) for d in speed_scores9.values()],
                   'size': list(size_scores9.values()),
                   'sense': list(sense_scores9.values()),
                   'physical skills': [d.get('physical skills', 0) for d in skills_scores9.values()],
                   'knowledge skills': [d.get('knowledge skills', 0) for d in skills_scores9.values()],
                   'emotional skills': [d.get('emotional skills', 0) for d in skills_scores9.values()],
                   'survival skills': [d.get('survival skills', 0) for d in skills_scores9.values()],
                   'detective skills': [d.get('detective skills', 0) for d in skills_scores9.values()],
                   'performance skills': [d.get('performance skills', 0) for d in skills_scores9.values()],
                   'stealth skills': [d.get('stealth skills', 0) for d in skills_scores9.values()],
                   'animal skills': [d.get('animal skills', 0) for d in skills_scores9.values()],
                   'ac': list(ac_scores9.values()),
                   'cr': list(cr_scores9.values())
                  })

df10 = pd.DataFrame({'name': list(hp_scores10.keys()),
                   'hp': list(hp_scores10.values()),
                   'walk speed': [d.get('walk speed', 0) for d in speed_scores10.values()],
                   'fly speed': [d.get('fly speed', 0) for d in speed_scores10.values()],
                   'burrow speed': [d.get('burrow speed', 0) for d in speed_scores10.values()],
                   'climb speed': [d.get('climb speed', 0) for d in speed_scores10.values()],
                   'swim speed': [d.get('swim speed', 0) for d in speed_scores10.values()],
                   'size': list(size_scores10.values()),
                   'sense': list(sense_scores10.values()),
                   'physical skills': [d.get('physical skills', 0) for d in skills_scores10.values()],
                   'knowledge skills': [d.get('knowledge skills', 0) for d in skills_scores10.values()],
                   'emotional skills': [d.get('emotional skills', 0) for d in skills_scores10.values()],
                   'survival skills': [d.get('survival skills', 0) for d in skills_scores10.values()],
                   'detective skills': [d.get('detective skills', 0) for d in skills_scores10.values()],
                   'performance skills': [d.get('performance skills', 0) for d in skills_scores10.values()],
                   'stealth skills': [d.get('stealth skills', 0) for d in skills_scores10.values()],
                   'animal skills': [d.get('animal skills', 0) for d in skills_scores10.values()],
                   'ac': list(ac_scores10.values()),
                   'cr': list(cr_scores10.values())
                  })


df11 = pd.DataFrame({'name': list(hp_scores11.keys()),
                   'hp': list(hp_scores11.values()),
                   'walk speed': [d.get('walk speed', 0) for d in speed_scores11.values()],
                   'fly speed': [d.get('fly speed', 0) for d in speed_scores11.values()],
                   'burrow speed': [d.get('burrow speed', 0) for d in speed_scores11.values()],
                   'climb speed': [d.get('climb speed', 0) for d in speed_scores11.values()],
                   'swim speed': [d.get('swim speed', 0) for d in speed_scores11.values()],
                   'size': list(size_scores11.values()),
                   'sense': list(sense_scores11.values()),
                   'physical skills': [d.get('physical skills', 0) for d in skills_scores11.values()],
                   'knowledge skills': [d.get('knowledge skills', 0) for d in skills_scores11.values()],
                   'emotional skills': [d.get('emotional skills', 0) for d in skills_scores11.values()],
                   'survival skills': [d.get('survival skills', 0) for d in skills_scores11.values()],
                   'detective skills': [d.get('detective skills', 0) for d in skills_scores11.values()],
                   'performance skills': [d.get('performance skills', 0) for d in skills_scores11.values()],
                   'stealth skills': [d.get('stealth skills', 0) for d in skills_scores11.values()],
                   'animal skills': [d.get('animal skills', 0) for d in skills_scores11.values()],
                   'ac': list(ac_scores11.values()),
                   'cr': list(cr_scores11.values())
                  })


df12 = pd.DataFrame({'name': list(hp_scores12.keys()),
                   'hp': list(hp_scores12.values()),
                   'walk speed': [d.get('walk speed', 0) for d in speed_scores12.values()],
                   'fly speed': [d.get('fly speed', 0) for d in speed_scores12.values()],
                   'burrow speed': [d.get('burrow speed', 0) for d in speed_scores12.values()],
                   'climb speed': [d.get('climb speed', 0) for d in speed_scores12.values()],
                   'swim speed': [d.get('swim speed', 0) for d in speed_scores12.values()],
                   'size': list(size_scores12.values()),
                   'sense': list(sense_scores12.values()),
                   'physical skills': [d.get('physical skills', 0) for d in skills_scores12.values()],
                   'knowledge skills': [d.get('knowledge skills', 0) for d in skills_scores12.values()],
                   'emotional skills': [d.get('emotional skills', 0) for d in skills_scores12.values()],
                   'survival skills': [d.get('survival skills', 0) for d in skills_scores12.values()],
                   'detective skills': [d.get('detective skills', 0) for d in skills_scores12.values()],
                   'performance skills': [d.get('performance skills', 0) for d in skills_scores12.values()],
                   'stealth skills': [d.get('stealth skills', 0) for d in skills_scores12.values()],
                   'animal skills': [d.get('animal skills', 0) for d in skills_scores12.values()],
                   'ac': list(ac_scores12.values()),
                   'cr': list(cr_scores12.values())
                  })

df13 = pd.DataFrame({'name': list(hp_scores13.keys()),
                   'hp': list(hp_scores13.values()),
                   'walk speed': [d.get('walk speed', 0) for d in speed_scores13.values()],
                   'fly speed': [d.get('fly speed', 0) for d in speed_scores13.values()],
                   'burrow speed': [d.get('burrow speed', 0) for d in speed_scores13.values()],
                   'climb speed': [d.get('climb speed', 0) for d in speed_scores13.values()],
                   'swim speed': [d.get('swim speed', 0) for d in speed_scores13.values()],
                   'size': list(size_scores13.values()),
                   'sense': list(sense_scores13.values()),
                   'physical skills': [d.get('physical skills', 0) for d in skills_scores13.values()],
                   'knowledge skills': [d.get('knowledge skills', 0) for d in skills_scores13.values()],
                   'emotional skills': [d.get('emotional skills', 0) for d in skills_scores13.values()],
                   'survival skills': [d.get('survival skills', 0) for d in skills_scores13.values()],
                   'detective skills': [d.get('detective skills', 0) for d in skills_scores13.values()],
                   'performance skills': [d.get('performance skills', 0) for d in skills_scores13.values()],
                   'stealth skills': [d.get('stealth skills', 0) for d in skills_scores13.values()],
                   'animal skills': [d.get('animal skills', 0) for d in skills_scores13.values()],
                   'ac': list(ac_scores13.values()),
                   'cr': list(cr_scores13.values())
                  })

df14 = pd.DataFrame({'name': list(hp_scores14.keys()),
                   'hp': list(hp_scores14.values()),
                   'walk speed': [d.get('walk speed', 0) for d in speed_scores14.values()],
                   'fly speed': [d.get('fly speed', 0) for d in speed_scores14.values()],
                   'burrow speed': [d.get('burrow speed', 0) for d in speed_scores14.values()],
                   'climb speed': [d.get('climb speed', 0) for d in speed_scores14.values()],
                   'swim speed': [d.get('swim speed', 0) for d in speed_scores14.values()],
                   'size': list(size_scores14.values()),
                   'sense': list(sense_scores14.values()),
                   'physical skills': [d.get('physical skills', 0) for d in skills_scores14.values()],
                   'knowledge skills': [d.get('knowledge skills', 0) for d in skills_scores14.values()],
                   'emotional skills': [d.get('emotional skills', 0) for d in skills_scores14.values()],
                   'survival skills': [d.get('survival skills', 0) for d in skills_scores14.values()],
                   'detective skills': [d.get('detective skills', 0) for d in skills_scores14.values()],
                   'performance skills': [d.get('performance skills', 0) for d in skills_scores14.values()],
                   'stealth skills': [d.get('stealth skills', 0) for d in skills_scores14.values()],
                   'animal skills': [d.get('animal skills', 0) for d in skills_scores14.values()],
                   'ac': list(ac_scores14.values()),
                   'cr': list(cr_scores14.values())
                  })


combined_df = pd.concat([df,df2,df3,df4,df5,df6,df7,df8,df9,df10,df11,df12,df13,df14], ignore_index=True)



combined_df = combined_df[combined_df['cr'] != 'N/A']
combined_df=combined_df[combined_df['hp'] != 'N/A']
combined_df=combined_df[combined_df['ac'] != 'N/A']

x=combined_df.loc[:, 'hp':'ac']
y=combined_df['cr']

rf = RandomForestRegressor()
rf.fit(x.values, y)

def predict():
    hp_score=float(hp_var.get())
    walk_score=float(walk_var.get())
    fly_score=float(fly_var.get())
    swim_score=float(swim_var.get())
    burrow_score=float(burrow_var.get())
    climb_score=float(climb_var.get())
    size_scores = {'tiny': 1, 'small': 2, 'medium': 3,'large':4,'huge':5,'gargantuan':6}
    size_score=size_scores[size_var.get()]
    sense_types={'darkvision':1,'blindsight':2,'truesight':4,'tremorsense':3,'none':0}
    sense_score=sense_types[sensetype_var.get()]*float(senserange_var.get())
    ac_score=float(armor_var.get())
    physical_score=float(acrobatics_var.get())+float(athletics_var.get())
    knowledge_score=float(arcana_var.get())+float(nature_var.get())+float(medicine_var.get())+float(religion_var.get())+float(history_var.get())
    emotional_score=float(persuasion_var.get())+float(intimidation_var.get())+float(deception_var.get())
    survival_score=float(survival_var.get())
    detective_score=float(perception_var.get())+float(insight_var.get())+float(investigation_var.get())
    stealth_score=float(stealth_var.get())+float(sleight_var.get())
    performance_score=float(performance_var.get())
    animal_score=float(animal_var.get())

    all_scores=[hp_score,walk_score,fly_score,burrow_score,climb_score,swim_score,size_score,
                sense_score,physical_score,knowledge_score,emotional_score,survival_score,detective_score,performance_score,stealth_score,animal_score,
                ac_score]


    predicted_value = round(rf.predict([all_scores])[0], 2)




    predicted_var.set(predicted_value)
                

def clear_all():
    hp_entry.delete(0, END)
    walk_entry.delete(0, END)
    swim_entry.delete(0, END)
    burrow_entry.delete(0, END)
    fly_entry.delete(0, END)
    climb_entry.delete(0, END)
    sensetype_entry.delete(0, END)
    senserange_entry.delete(0, END)
    size_entry.delete(0, END)
    armor_entry.delete(0, END)
    arcana_entry.delete(0, END)
    stealth_entry.delete(0, END)
    persuasion_entry.delete(0, END)
    intimidation_entry.delete(0, END)
    deception_entry.delete(0, END)
    survival_entry.delete(0, END)
    animal_entry.delete(0, END)
    nature_entry.delete(0, END)
    medicine_entry.delete(0, END)
    religion_entry.delete(0, END)
    history_entry.delete(0, END)
    acrobatics_entry.delete(0, END)
    athletics_entry.delete(0, END)
    sleight_entry.delete(0, END)
    perception_entry.delete(0, END)
    insight_entry.delete(0, END)
    investigation_entry.delete(0, END)
    performance_entry.delete(0, END)
    predicted_entry.delete(0,END)

    

    
    

window = Tk()
 
window.title("Challenge Rating Predictor")
window.geometry('500x350')


hit_points= Label(window, text = "Hit Points").grid(row = 0,column = 0)
walk_speed=Label(window, text = "Walk Speed").grid(row = 0,column = 1)
fly_speed=Label(window, text = "Fly Speed").grid(row = 0,column = 2)
swim_speed=Label(window, text = "Swim Speed").grid(row = 0,column = 3)
burrow_speed=Label(window, text = "Burrow Speed").grid(row = 0,column = 4)
climb_speed=Label(window, text = "Climb Speed").grid(row = 0,column = 5)
size=Label(window, text = "Size").grid(row = 2,column = 0)
sense_type=Label(window, text = "Sense Type").grid(row = 2,column = 1)
sense_range=Label(window, text = "Sense Range").grid(row = 2,column = 2)
armor_class=Label(window, text = "Armor Class").grid(row = 2,column = 3)
arcana=Label(window, text = "Arcana").grid(row = 2,column = 4)
stealth=Label(window, text = "Stealth").grid(row = 2,column = 5)
persuasion=Label(window, text = "Persuasion").grid(row = 4,column = 0)
intimidation=Label(window, text = "Intimidation").grid(row = 4,column = 1)
deception=Label(window, text = "Deception").grid(row = 4,column = 2)
survival=Label(window, text = "Survival").grid(row = 4,column = 3)
animal_handling=Label(window, text = "Animal Handling").grid(row = 4,column = 4)
nature=Label(window, text = "Nature").grid(row = 4,column = 5)
medicine=Label(window, text = "Medicine").grid(row = 6,column = 0)
religion=Label(window, text = "Religion").grid(row = 6,column = 1)
history=Label(window, text = "History").grid(row = 6,column = 2)
acrobatics=Label(window, text = "Acrobatics").grid(row = 6,column = 3)
athletics=Label(window, text = "Athletics").grid(row = 6,column = 4)
sleight_of_hand=Label(window, text = "Sleight of Hand").grid(row = 6,column = 5)
perception=Label(window, text = "Perception").grid(row = 8,column = 0)
insight=Label(window, text = "Insight").grid(row = 8,column = 1)
investigation=Label(window, text = "Investigation").grid(row = 8,column = 2)
performance=Label(window, text = "Performance").grid(row = 8,column = 3)

hp_var=StringVar()
walk_var=StringVar()
fly_var=StringVar()
swim_var=StringVar()
burrow_var=StringVar()
climb_var=StringVar()
size_var=StringVar()
sensetype_var=StringVar()
senserange_var=StringVar()
armor_var=StringVar()
arcana_var=StringVar()
stealth_var=StringVar()
persuasion_var=StringVar()
intimidation_var=StringVar()
deception_var=StringVar()
survival_var=StringVar()
animal_var=StringVar()
nature_var=StringVar()
medicine_var=StringVar()
religion_var=StringVar()
history_var=StringVar()
acrobatics_var=StringVar()
athletics_var=StringVar()
sleight_var=StringVar()
perception_var=StringVar()
insight_var=StringVar()
investigation_var=StringVar()
performance_var=StringVar()
predicted_var=StringVar()

hp_entry=Entry(window,textvariable=hp_var,width=10)
hp_entry.grid(row = 1,column = 0)
walk_entry=Entry(window,textvariable=walk_var,width=10)
walk_entry.grid(row = 1,column = 1)
fly_entry=Entry(window,textvariable=fly_var,width=10)
fly_entry.grid(row = 1,column = 2)
swim_entry=Entry(window,textvariable=swim_var,width=10)
swim_entry.grid(row = 1,column = 3)
burrow_entry=Entry(window,textvariable=burrow_var,width=10)
burrow_entry.grid(row = 1,column = 4)
climb_entry=Entry(window,textvariable=climb_var,width=10)
climb_entry.grid(row = 1,column = 5)
size_entry=Entry(window,textvariable=size_var,width=10)
size_entry.grid(row = 3,column = 0)
sensetype_entry=Entry(window,textvariable=sensetype_var,width=10)
sensetype_entry.grid(row = 3,column = 1)
senserange_entry=Entry(window,textvariable=senserange_var,width=10)
senserange_entry.grid(row = 3,column = 2)
armor_entry=Entry(window,textvariable=armor_var,width=10)
armor_entry.grid(row = 3,column = 3)
arcana_entry=Entry(window,textvariable=arcana_var,width=10)
arcana_entry.grid(row = 3,column = 4)
stealth_entry=Entry(window,textvariable=stealth_var,width=10)
stealth_entry.grid(row = 3,column = 5)
persuasion_entry=Entry(window,textvariable=persuasion_var,width=10)
persuasion_entry.grid(row = 5,column = 0)
intimidation_entry=Entry(window,textvariable=intimidation_var,width=10)
intimidation_entry.grid(row = 5,column = 1)
deception_entry=Entry(window,textvariable=deception_var,width=10)
deception_entry.grid(row = 5,column = 2)
survival_entry=Entry(window,textvariable=survival_var,width=10)
survival_entry.grid(row = 5,column = 3)
animal_entry=Entry(window,textvariable=animal_var,width=10)
animal_entry.grid(row = 5,column = 4)
nature_entry=Entry(window,textvariable=nature_var,width=10)
nature_entry.grid(row = 5,column = 5)
medicine_entry=Entry(window,textvariable=medicine_var,width=10)
medicine_entry.grid(row = 7,column = 0)
religion_entry=Entry(window,textvariable=religion_var,width=10)
religion_entry.grid(row = 7,column = 1)
history_entry=Entry(window,textvariable=history_var,width=10)
history_entry.grid(row = 7,column = 2)
acrobatics_entry=Entry(window,textvariable=acrobatics_var,width=10)
acrobatics_entry.grid(row = 7,column = 3)
athletics_entry=Entry(window,textvariable=athletics_var,width=10)
athletics_entry.grid(row = 7,column = 4)
sleight_entry=Entry(window,textvariable=sleight_var,width=10)
sleight_entry.grid(row = 7,column = 5)
perception_entry=Entry(window,textvariable=perception_var,width=10)
perception_entry.grid(row = 9,column = 0)
insight_entry=Entry(window,textvariable=insight_var,width=10)
insight_entry.grid(row = 9,column = 1)
investigation_entry=Entry(window,textvariable=investigation_var,width=10)
investigation_entry.grid(row = 9,column = 2)
performance_entry=Entry(window,textvariable=performance_var,width=10)
performance_entry.grid(row = 9,column = 3)
randLabel1=Label(window, text = "").grid(row = 10,column = 0)
predict=Button(window,text='Predict',command=predict).grid(row=11,column=2)
randLabel2=Label(window, text = "").grid(row = 12,column = 0)



challenge_rating=Label(window, text ="Challenge Rating: ").grid(row = 13,column = 1)


predicted_entry=Entry(window,textvariable=predicted_var,width=10)
predicted_entry.grid(row=13,column=2)
randLabel3=Label(window, text = "").grid(row = 14,column = 0)
clear_button=Button(window,text='Clear All',command=clear_all).grid(row=15,column=2)



 
window.mainloop()
