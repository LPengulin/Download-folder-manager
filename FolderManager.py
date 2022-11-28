import os


class FolderSorter(object):

    # image directory
    # video directory
    # books / pdf files
    # .exe directory
    # .zip directory
    #pass in all of these as a dict

    def __init__(self, directories=None):

        if not directories: 
            self.images = "downloaded_images/"
            self.videos = "downloaded_videos/"
            self.books = "downloaded_books/"
            self.executables = "executables/"
            self.zips = "zips/"

            try:
                os.makedirs(self.images)

            except Exception as e:
                pass

            try:
                os.makedirs(self.videos)

            except Exception as e:
                pass

            try:
                os.makedirs(self.books)

            except Exception as e:
                pass

            try:
                os.makedirs(self.executables)

            except Exception as e:
                pass

            try:    
                os.makedirs(self.zips)

            except Exception as e:
                pass
 

        else:
            self.images = directories.images
            self.books = directories.books
            self.executables = directories.executables
            self.zips = directories.zips

        self.stuff = os.listdir()

    
    def Sort_images(self):
        jpgs = [thing for thing in self.stuff if '.jpg' in thing]
        jpegs = [thing for thing in self.stuff if '.jpeg' in thing]
        pngs = [thing for thing in self.stuff if '.png' in thing]
        gifs = [thing for thing in self.stuff if '.gif' in thing]
        cr2s = [thing for thing in self.stuff if '.cr2' in thing]
        crws = [thing for thing in self.stuff if '.crw' in thing]
        nefs = [thing for thing in self.stuff if '.nef' in thing]
        pefs = [thing for thing in self.stuff if '.pef' in thing]
        webp = [thing for thing in self.stuff if '.webp' in thing]

        all_imgs = jpgs + jpegs + pngs + gifs + cr2s + crws + nefs + pefs + webp

        for thing in all_imgs:
            new_thing = self.images + thing

            try:
                os.rename(thing, new_thing)

            except Exception as e:
                print("exception with", thing, e)

    
                
    def Sort_videos(self):
        mp4s = [thing for thing in self.stuff if '.mp4' in thing]
        wavs = [thing for thing in self.stuff if '.wav' in thing]

        all_videos = mp4s + wavs

        for thing in all_videos:
            new_thing = self.videos + thing

            try:
                os.rename(thing, new_thing)

            except Exception as e:
                print("exception with", thing, e)


                
    def Sort_books(self):
        # only doing pdfs and epubs for now
        pdfs = [thing for thing in self.stuff if '.pdf' in thing]
        epubs = [thing for thing in self.stuff if '.epub' in thing]

        all_books = pdfs + epubs

        for thing in all_books:
            new_thing = self.books + thing

            try:
                os.rename(thing, new_thing)

            except Exception as e:
                print("Exception with", thing, e)

    
    def Sort_executables(self):
        # .exe not ur ex
        exes = [thing for thing in self.stuff if '.exes' in thing]

        all_executables = exes

        for thing in all_executables:
            new_thing = self.executables + thing

            try:
                os.rename(thing, new_thing)

            except Exception as e:
                print("Exception with", thing, e)
    
    
    def Sort_zips(self):
        zips = [thing for thing in self.stuff if '.zip' in thing]
        svn_zips = [thing for thing in self.stuff if '.7z' in thing]


        #not the one in your pants
        all_zips = zips + svn_zips

        for thing in all_zips:
            new_thing = self.zips + thing

            try:
                os.rename(thing, new_thing)

            except Exception as e:
                print("Exception with", thing, e)




if __name__ == '__main__':

    app = FolderSorter()

    app.Sort_images()
    app.Sort_books()
    app.Sort_executables()
    app.Sort_zips()
            
