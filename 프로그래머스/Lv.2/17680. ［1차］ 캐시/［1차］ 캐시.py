from collections import defaultdict

def lowerString(string):
    return string.lower()

def isCache(city, caches):
    if city in caches:
        return True
    return False

def solution(cacheSize, cities):
    answer = 0
    global caches
    caches = defaultdict()
    
    if len(cities) == 0:
        return 0
    
    if cacheSize == 0:
        answer = len(cities) * 5
        return answer
    
    for number, city in enumerate(cities):
        lowerCity = lowerString(city)
        if isCache(lowerCity, caches):
            answer += 1
            del caches[lowerCity]
            caches[lowerCity] = number
        else:
            answer += 5
            if len(caches) == cacheSize:
                min_city = min(caches, key=caches.get)
                del caches[min_city]
                caches[lowerCity] = number
            elif len(caches) < cacheSize:
                caches[lowerCity] = number
                
    return answer