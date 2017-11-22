import 
from multiprocessing import Pool

def processSQL(param):
    sqlPath = os.path.join(path, 'Sqlite3.db')
    with sqlite3.connect(sqlPath) as conn:
        data = analysis.generate()

    return (success,name,data)


def processHDF(param):
    hdfPath = os.path.join(mc, 'Alldata.h5')
    with h5py.File(hdfPath) as hdf:
        data = table.create(hdf)
        data['mc'] = mc
        
    return (success,name,data)


def multi(params):
    pool = Pool()
    processed = pool.map(process, parameters)
    
    return 
    
def standard(params):
    