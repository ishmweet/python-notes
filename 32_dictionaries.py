# A collection of {key:value} pairs ordered and changeable. NO duplicates

capitals = {"USA": "Washington D.C.",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}

#print(dir(capitals))
#print(capitals.get("USA"))  #prints the capital of this country
#capitals.update({"Germany": "Berlin"})  #adds new country and it's capital
#capitals.update({"USA": "Detroit"})  #updates USA's capital to Detroit
#capitals.pop("China")  #removes china
#capitals.popitem()  #removes latest key value
#capitals.clear()
#keys = capitals.keys()  #prints countries
#values = capitals.values()  #prints capitals
#items = capitals.items()  #resembles 2d list of tuples. items = [(), (), ()]

for key, value in capitals.items():
    print(f"{key}: {value}")