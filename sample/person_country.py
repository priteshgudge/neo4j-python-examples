from models.person_country import Person,Country


def create_person(person_dict):
    if not person_dict:
        return None
    person = Person.create_or_update(person_dict)
    return person[0]

def create_country(country_dict):
    if not country_dict:
        return None
    country = Country.create_or_update(country_dict)
    return country[0]


def link_person_country(person_obj, country_obj):
    person_obj.country.connect(country_obj)


def check_link(person_obj,country_obj):
    if person_obj.country.is_connected(country_obj):
        return True
    else:
        return False

def find_person_by_name(name):

    #person = Person.nodes.get(name=name) Will  throw error
    person = Person.nodes.get_or_none(name=name)
    return person

def find_person_by_id(id):
    person = Person.nodes.get_or_none(id=id)
    return person

def filter_persons_by_age(age):
    persons = Person.nodes.filter(age__gte=age)
    return persons

def filter_by_name_in_country(country_obj,name):
    person = country_obj.inhabitant.search(name=name)
    return person

def list_all_inhabitants(country):
    inhabs = country.inhabitant.all()
    for inh in inhabs:
        print(inh.id, inh.name, inh.age)




if __name__ == '__main__':
    #pritesh = create_person(dict(name="Pritesh",age=27))
    #pritesh.refresh()
    #print ("Pritesh: ",pritesh.id)
    #ramesh = create_person(dict(name="Ramesh", age=34))
    #ramesh.refresh()
    #print(ramesh.id)
    #india = create_country(dict(code="IN"))
    pritesh = Person.nodes.get_or_none(name="Pritesh")
    ramesh = Person.nodes.get_or_none(name="Ramesh")
    india = Country.nodes.get_or_none(code="IN")

    india.refresh()
    link_person_country(pritesh,india)
    print(check_link(pritesh,india))
    link_person_country(ramesh,india)
    print(check_link(ramesh,india))

    list_all_inhabitants(india)

    print(filter_by_name_in_country(india,"pritesh"))

    india.inhabitant.disconnect(pritesh)

    list_all_inhabitants(india)