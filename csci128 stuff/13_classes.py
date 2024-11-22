# Roman Rodriguez
# CSCI 128 - Section J
# Assessment 13
# References: Jesse Paulsen
# Time: 30 minutes

class Material:
    def __init__(self, id):
        self.id = id
        self.price = 0
        self.material_type = 'Not Determined'

    def setPrice(self, price):
        self.price = price

    def getPrice(self):
        return self.price

    def setMaterialType(self, material_type):
        self.material_type = material_type

    def getMaterialType(self):
        return self.material_type

    def setID(self, id):
        self.id = id

    def getID(self):
        return self.id


class ConstructionSite:
    def __init__(self, name, city):
        self.name = name
        self.city = city
        self.price = 0
        self.materials = []

    def addMaterial(self, material):
        self.materials.append(material)
        self.calculatePrice()

    def findMaterial(self, id):
        for material in self.materials:
            if material.getID() == id:
                return material
        return -1

    def calculatePrice(self):
        self.price = sum(material.getPrice() for material in self.materials)

    def countMaterials(self):
        wood_count = sum(1 for m in self.materials if m.getMaterialType() == 'WOOD')
        steel_count = sum(1 for m in self.materials if m.getMaterialType() == 'STEEL')
        brick_count = sum(1 for m in self.materials if m.getMaterialType() == 'BRICK')
        return [wood_count, steel_count, brick_count]

    def incorporateSite(self, other_site):
        self.materials.extend(other_site.materials)
        self.calculatePrice() 

    def __str__(self):
        total_materials = len(self.materials)
        return f"{self.name} site in {self.city} has {total_materials} materials, with a value of {self.price}."

if __name__ == "__main__":
    primary_file = input("PRIMARY> ")
    secondary_file = input("SECONDARY> ")

    with open(primary_file, 'r') as file:
        primary_name = file.readline().strip()
        primary_city = file.readline().strip()
        primary_site = ConstructionSite(primary_name, primary_city)
        for line in file:
            parts = line.split()
            material_id = int(parts[0])
            material_type = parts[1]
            material_price = int(parts[2])
            material = Material(material_id)
            material.setMaterialType(material_type)
            material.setPrice(material_price)
            primary_site.addMaterial(material)

    with open(secondary_file, 'r') as file:
        secondary_name = file.readline().strip()
        secondary_city = file.readline().strip()
        secondary_site = ConstructionSite(secondary_name, secondary_city)
        for line in file:
            parts = line.split()
            material_id = int(parts[0])
            material_type = parts[1]
            material_price = int(parts[2])
            material = Material(material_id)
            material.setMaterialType(material_type)
            material.setPrice(material_price)
            secondary_site.addMaterial(material)

    print(f"OUTPUT {primary_site}")
    material_count = primary_site.countMaterials()
    print(f"OUTPUT Wood:{material_count[0]} Steel:{material_count[1]} Brick:{material_count[2]}")

    print(f"OUTPUT {secondary_site}")
    material_count = secondary_site.countMaterials()
    print(f"OUTPUT Wood:{material_count[0]} Steel:{material_count[1]} Brick:{material_count[2]}")

    primary_site.incorporateSite(secondary_site)
    print(f"OUTPUT {primary_site}")
