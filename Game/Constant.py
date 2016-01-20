def blending(color1, color2):
    return tuple(map(sum,zip(color1,color2)))
#basic color
const_black = (0, 0 ,0)
const_white = (255, 255, 255)
const_red = (255, 0, 0)
const_green = (0, 255, 0)
const_blue = (0, 0, 255)
const_yellow = blending(const_red, const_green)
