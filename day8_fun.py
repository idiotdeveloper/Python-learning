import math

def paint_cans(height, width, cover):
    cans = (height*width)/cover
    nu = math.ceil(cans)
    print(f"no of cans = {nu}")


test_h = int(input("enter height of the wall :: "))
test_w = int(input("enter width of the wall :: "))
coverage = 5

paint_cans(height=test_h, width=test_w, cover=coverage)




