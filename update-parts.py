import sys, os, glob

sys.path.append("/usr/lib/freecad/lib/")
import FreeCAD

cur_dir = os.path.curdir

def main():
    for name in glob.iglob(cur_dir + '/FCStd/*.fcstd'):

        if name == './FCStd/TK0_Assembly.fcstd':
            pass
        else:
            print name
            fcstd2stp(name)

def fcstd2stp(filename):
    doc = FreeCAD.open(filename)
    objects = doc.Objects
    fn = doc.Label

    for ob in objects:
        if ob.InList == [] and ob.OutList.__len__() > 0 :
            ob.Shape.exportStep(cur_dir + '/STEP/'+ fn + '.stp' )

if __name__ == '__main__':
    main()
