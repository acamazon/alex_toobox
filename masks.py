import numpy as np
def mask_square_in(img, center=None, side = None):
    h, w = len(img), len(img)
    if center is None: # use the middle of the image
        center = (int(w/2), int(h/2))
    if side is None: # use the smallest distance between the center and image walls
        side = min(center[0], center[1], w-center[0], h-center[1])

    mask = np.zeros_like(img)
    mask[int(center[1]-side/2) : int(center[1] + side/2),
         int(center[0]-side/2) : int(center[0] + side/2)] = 1
    
    masked_img = mask * img
    masked_img = masked_img.astype('float')
    masked_img[masked_img == 0] = np.nan
    return masked_img


def mask_square_out(img, center=None, side = None):
    h, w = len(img), len(img)
    if center is None: # use the middle of the image
        center = (int(w/2), int(h/2))
    if side is None: # use the smallest distance between the center and image walls
        side = min(center[0], center[1], w-center[0], h-center[1])

    mask = np.ones_like(img)
    mask[int(center[1]-side/2) : int(center[1] + side/2),
         int(center[0]-side/2) : int(center[0] + side/2)] = 0
    
    masked_img = mask * img
    masked_img = masked_img.astype('float')
    masked_img[masked_img == 0] = np.nan
    return masked_img
    
    
def mask_rectan_in(img, center=None, side_x = None, side_y = None, fill_with = 'nan'):
    h, w = len(img), len(img)
    if center is None: # use the middle of the image
        center = (int(w/2), int(h/2))
    if (side_y is None) &(side_x is None): # use the smallest distance between the center and image walls
        side = min(center[0], center[1], w-center[0], h-center[1])

    mask = np.zeros_like(img)
    mask[int(center[1]-side_y/2) : int(center[1] + side_y/2),
         int(center[0]-side_x/2) : int(center[0] + side_x/2)] = 1
    
    masked_img = mask * img
    masked_img = masked_img.astype('float')
    if fill_with=='nan':
        masked_img[masked_img == 0] = np.nan
    if fill_with!='nan':
        masked_img[masked_img == 0] = fill_with
    return masked_img


def mask_rectan_out(img, center=None, side_x = None, side_y = None):
    h, w = len(img), len(img)
    if center is None: # use the middle of the image
        center = (int(w/2), int(h/2))
    if (side_y is None) &(side_x is None): # use the smallest distance between the center and image walls
        side = min(center[0], center[1], w-center[0], h-center[1])

    mask = np.ones_like(img)
    mask[int(center[1]-side_y/2) : int(center[1] + side_y/2),
         int(center[0]-side_x/2) : int(center[0] + side_x/2)] = 0
    
    masked_img = mask * img
    masked_img = masked_img.astype('float')
    masked_img[masked_img == 0] = np.nan
    return masked_img


    
def mask_circle_in(img, center=None, radius=None):
    h, w = len(img), len(img)
    if center is None: # use the middle of the image
        center = (int(w/2), int(h/2))
    if radius is None: # use the smallest distance between the center and image walls
        radius = min(center[0], center[1], w-center[0], h-center[1])

    Y, X = np.ogrid[:h, :w]
    dist_from_center = np.sqrt((X - center[0])**2 + (Y-center[1])**2)

    mask = dist_from_center <= radius

    masked_img = img.copy()
    masked_img = masked_img.astype('float')
    masked_img[~mask] = np.nan
    
    return masked_img


def mask_circle_out(img, center=None, radius=None):
    h, w = len(img), len(img)
    if center is None: # use the middle of the image
        center = (int(w/2), int(h/2))
    if radius is None: # use the smallest distance between the center and image walls
        radius = min(center[0], center[1], w-center[0], h-center[1])

    Y, X = np.ogrid[:h, :w]
    dist_from_center = np.sqrt((X - center[0])**2 + (Y-center[1])**2)

    mask = dist_from_center >= radius

    masked_img = img.copy()
    masked_img = masked_img.astype('float')
    masked_img[~mask] = np.nan
    
    return masked_img
