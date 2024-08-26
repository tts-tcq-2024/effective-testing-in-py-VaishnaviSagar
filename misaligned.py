
def print_color_map():
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            print(f'{i * 5 + j} | {major} | {minor}')
    return len(major_colors) * len(minor_colors)
#To verify the color mapping
expected_color_format = [(0,'White','Slate'),
                         (1,'White','Brown'),
                         (2,'White','Green'),
                         (3,'White','Orange'),
                         (4,'White','Blue'),
                         (5,'Red','Slate'),
                         (6,'Red','Brown'),
                         (7,'Red','Green'),
                         (8,'Red','Orange'),
                         (9,'Red','Blue'),
                         (10,'Black','Slate'),
                         (11,'Black','Brown'),
                         (12,'Black','Green'),
                         (13,'Black','Orange'),
                         (14,'Black','Blue'),
                         (15,'Yellow','Slate'),
                         (16,'Yellow','Brown'),
                         (17,'Yellow','Green'),
                         (18,'Yellow','Orange'),
                         (19,'Yellow','Blue'),
                         (20,'Violet','Slate'),
                         (21,'Violet','Brown'),
                         (22,'Violet','Green'),
                         (23,'Violet','Orange'),
                         (24,'Violet','Blue'),]

#To verify function handles empty color lists 
def print_color_map(major_colors=None, minor_colors=None):
    major_colors = major_colors or ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = minor_colors or ["Blue", "Orange", "Green", "Brown", "Slate"]
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            print(f'{i*5+j} | {major} | {minor}')
    return len(major_colors) * len(minor_colors)
    result = print_color_map([], [])
    assert(result == 0)
    
#To verify function for large inputs
major_colors = ["Color" + str(i) for i in range(100)]
minor_colors = ["Shade" + str(i) for i in range(100)]
result = print_color_map(major_colors, minor_colors)
assert(result == 10000)
                         
 #To verify the function with custom color lists
result = print_color_map(["Cyan", "Magenta"], ["Black", "White"])
expected_custom_color_format = [(0,'Cyan','Black'),
                                (0,'Magenta','Black'),
                                (0,'Cyan','White'),
                                (0,'Magenta','White'),]
assert(result == 4)

assert major_colors== expected_color_format, "Color map does not match expected values"
assert len(major_colors) == 25, "Color map length is incorrect"
print("All checks passed successfully!\n")
