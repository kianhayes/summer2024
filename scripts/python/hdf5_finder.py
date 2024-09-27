import h5py
import yt

data_file = f'/data/khyaes/solvers_test/rt/hllc/data/rt.out2.00008.athdf'
ds = yt.load(data_file)
h5_array = h5py.File('/data/khyaes/solvers_test/rt/hllc/data/rt.out2.00008.athdf')

yt_temp_array = ds.r['gas', 'density'].v
print(yt_temp_array)
for value1 in h5_array['prim']:
    for value2 in value1:
        for value3 in value2:
            for value4 in value3:
                for value5 in value4:
                    if value5 == yt_temp_array[0]:
                        print(value4)

