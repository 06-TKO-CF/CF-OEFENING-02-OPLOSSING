from PIL import Image, ImageTk, ImageOps

class ImageTKHelper:
    @staticmethod
    def schaal(pad:str=None, grootte=(200,200)):
        try:
            foto = Image.open(pad)
            breedte, hoogte = foto.size
            if breedte / hoogte <= 1:
                breedte = int(grootte[1] * breedte / hoogte)
                hoogte = grootte[1]
            else:
                hoogte = int(hoogte * grootte[0] / breedte)
                breedte = grootte[0]
            foto = foto.resize((breedte, hoogte), resample=Image.BICUBIC)
            return ImageTk.PhotoImage(image=foto)
        except:
            return None
        
    @staticmethod
    def passend(pad:str=None, grootte=(200,200), resampleMode=Image.BICUBIC, rand=0, centreren=(0.5, 0.5)):
        try:
            foto = Image.open(pad)
            foto = ImageOps.fit(image = foto,
                                size = grootte,
                                method = resampleMode,
                                bleed = rand,
                                centering = centreren)
            return ImageTk.PhotoImage(foto)
        except Exception as ex:
            # return None
            print(ex)